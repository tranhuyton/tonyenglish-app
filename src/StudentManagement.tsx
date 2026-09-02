import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';
import { createClient } from '@supabase/supabase-js';

const authSupabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
  { auth: { persistSession: false } }
);

let studentSearchTimer: any;

export default function StudentManagement({ onStartTest, autoSelectUserId, autoTab, onAutoSelectDone }: { onStartTest?: any, autoSelectUserId?: string | null, autoTab?: 'courses' | 'history' | 'activity' | 'assignments' | null, onAutoSelectDone?: () => void }) {
  const [students, setStudents] = useState<any[]>([]);
  const [courses, setCourses] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState<'active' | 'inactive' | 'all'>('active');
  
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 20;
  
  const [selectedStudent, setSelectedStudent] = useState<any>(null);
  const [studentHistory, setStudentHistory] = useState<any[]>([]);
  const [studentEnrollments, setStudentEnrollments] = useState<any[]>([]);
  const [isLoadingDetails, setIsLoadingDetails] = useState(false);
  const [activeDetailTab, setActiveDetailTab] = useState<'courses' | 'history' | 'activity' | 'assignments'>('courses');
  const [studentActivities, setStudentActivities] = useState<any[]>([]);

  const [studentAssignments, setStudentAssignments] = useState<any[]>([]);
  const [assignCalMonth, setAssignCalMonth] = useState(new Date());
  const [assignSelectedDate, setAssignSelectedDate] = useState<string>(new Date().toISOString().split('T')[0]);
  const [isAddingAssignment, setIsAddingAssignment] = useState(false);
  
  // Task picker modal
  const [showTaskPicker, setShowTaskPicker] = useState(false);
  const [taskPickerMode, setTaskPickerMode] = useState<'choose' | 'manual' | 'test'>('choose');
  const [manualTemplates, setManualTemplates] = useState<any[]>([]);
  const [selectedTemplates, setSelectedTemplates] = useState<Set<string>>(new Set());
  const [courseTaskLinks, setCourseTaskLinks] = useState<any[]>([]);
  const [manualBrowserCourseId, setManualBrowserCourseId] = useState<string | null>(null);
  
  // Test browser
  const [studentCourses, setStudentCourses] = useState<any[]>([]);
  const [allFoldersForAssign, setAllFoldersForAssign] = useState<any[]>([]);
  const [allTestsForAssign, setAllTestsForAssign] = useState<any[]>([]);
  const [testBrowserCourseId, setTestBrowserCourseId] = useState<string | null>(null);
  const [selectedTestIds, setSelectedTestIds] = useState<Set<string>>(new Set());

  const [showAssignModal, setShowAssignModal] = useState(false);
  const [isAssigning, setIsAssigning] = useState(false);

  // Auto-distribute
  const [showAutoDistribute, setShowAutoDistribute] = useState(false);
  const [autoDistCourseId, setAutoDistCourseId] = useState<string | null>(null);
  const [autoDistDayPlans, setAutoDistDayPlans] = useState<any[]>([]);
  const [autoDistTasks, setAutoDistTasks] = useState<any[]>([]);
  const [autoDistSelectedDays, setAutoDistSelectedDays] = useState<Set<string>>(new Set());
  const [autoDistStartDate, setAutoDistStartDate] = useState<string>(new Date().toISOString().split('T')[0]);
  const [isAutoDistributing, setIsAutoDistributing] = useState(false);

  const [showBoardAssign, setShowBoardAssign] = useState(false);
  const [boardAssignCourseId, setBoardAssignCourseId] = useState<string | null>(null);
  const [boardAssignColumns, setBoardAssignColumns] = useState<any[]>([]);
  const [boardAssignCards, setBoardAssignCards] = useState<any[]>([]);
  const [boardAssignItems, setBoardAssignItems] = useState<any[]>([]);
  const [isBoardAssigning, setIsBoardAssigning] = useState(false);

  const [showCreateUserModal, setShowCreateUserModal] = useState(false);
  const [isCreatingUser, setIsCreatingUser] = useState(false);
  const [newUserRole, setNewUserRole] = useState('student');

  const [editingUser, setEditingUser] = useState<any>(null);
  const [isUpdatingUser, setIsUpdatingUser] = useState(false);

  // 🚀 KHO ĐỀ THI ĐỂ MỞ TÍNH NĂNG XEM LẠI BÀI
  const [allTests, setAllTests] = useState<any[]>([]);

  useEffect(() => {
    fetchStudents();
    fetchCourses();
    supabase.from('tests').select('id, title, test_type, course_id, skill').then(({data}) => setAllTests(data || []));
  }, []);

  useEffect(() => {
    setCurrentPage(1);
  }, [searchQuery]);

  // Auto-select student from notification click
  useEffect(() => {
    if (autoSelectUserId && students.length > 0) {
      const target = students.find(s => s.id === autoSelectUserId);
      if (target) {
        handleSelectStudent(target);
        if (autoTab) {
          // Delay slightly to ensure state is set after handleSelectStudent
          setTimeout(() => setActiveDetailTab(autoTab), 100);
        }
      }
      onAutoSelectDone?.();
    }
  }, [autoSelectUserId, students]);

  const fetchStudents = async () => {
    setIsLoading(true);
    try {
      const { data, error } = await supabase.from('profiles').select('*').order('created_at', { ascending: false });
      if (error) throw error;
      setStudents(data || []);
    } catch (err: any) {
      console.error("Lỗi tải học viên:", err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchCourses = async () => {
    const { data } = await supabase.from('courses').select('id, title, type').order('created_at', { ascending: false });
    setCourses(data || []);
  };

  const fetchAssignments = async (userId: string) => {
    const { data } = await supabase.from('assignments').select('*').eq('user_id', userId).order('due_date', { ascending: true });
    setStudentAssignments(data || []);
  };

  const fetchManualTemplates = async () => {
    const { data } = await supabase.from('manual_task_templates').select('*').order('title');
    setManualTemplates(data || []);
    const { data: links } = await supabase.from('course_task_templates').select('*');
    setCourseTaskLinks(links || []);
  };

  const fetchStudentCoursesAndTests = async (userId: string) => {
    const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', userId);
    const courseIds = enrolls?.map(e => e.course_id) || [];
    if (courseIds.length === 0) { setStudentCourses([]); return; }
    const { data: coursesData } = await supabase.from('courses').select('id, title, type').in('id', courseIds);
    setStudentCourses(coursesData || []);
    
    // Fetch folders per course to bypass Supabase server-side max_rows=1000
    const folderResults = await Promise.all(courseIds.map(cid =>
      supabase.from('folders').select('id, course_id, parent_id, title, display_order').eq('course_id', cid).order('display_order').limit(1000)
    ));
    const allFolders = folderResults.flatMap(r => r.data || []);
    setAllFoldersForAssign(allFolders);
    
    // Fetch tests per course (each course < 1000 tests, so no truncation)
    const testResults = await Promise.all(courseIds.map(cid =>
      supabase.from('tests').select('id, title, test_type, folder_id, course_id').eq('course_id', cid).order('order_index').limit(1000)
    ));
    const allTests = testResults.flatMap(r => r.data || []);
    
    setAllTestsForAssign(allTests);
  };

  useEffect(() => {
    if (activeDetailTab === 'assignments' && selectedStudent) {
      fetchAssignments(selectedStudent.id);
      fetchManualTemplates();
      fetchStudentCoursesAndTests(selectedStudent.id);
    }
  }, [activeDetailTab, selectedStudent]);

  const handleAddManualTasks = async () => {
    if (!selectedStudent || selectedTemplates.size === 0) return;
    setIsAddingAssignment(true);
    const { data: { session } } = await supabase.auth.getSession();
    const tasks = Array.from(selectedTemplates).map(tplId => {
      const tpl = manualTemplates.find(t => t.id === tplId);
      return { user_id: selectedStudent.id, due_date: assignSelectedDate, title: tpl?.title || '', description: tpl?.description || '', task_type: 'manual', created_by: session?.user?.id || null };
    });
    await supabase.from('assignments').insert(tasks);
    setSelectedTemplates(new Set());
    setShowTaskPicker(false);
    setTaskPickerMode('choose');
    setManualBrowserCourseId(null);
    setIsAddingAssignment(false);
    fetchAssignments(selectedStudent.id);
  };

  const handleAddTestTasks = async () => {
    if (!selectedStudent || selectedTestIds.size === 0) return;
    setIsAddingAssignment(true);
    const { data: { session } } = await supabase.auth.getSession();
    const tasks = Array.from(selectedTestIds).map(testId => {
      const test = allTestsForAssign.find(t => t.id === testId);
      return { user_id: selectedStudent.id, due_date: assignSelectedDate, title: test?.title || '', task_type: 'test', test_id: testId, created_by: session?.user?.id || null };
    });
    await supabase.from('assignments').insert(tasks);
    setSelectedTestIds(new Set());
    setTestBrowserCourseId(null);
    setShowTaskPicker(false);
    setTaskPickerMode('choose');
    setIsAddingAssignment(false);
    fetchAssignments(selectedStudent.id);
  };

  useEffect(() => {
    if (autoDistCourseId) {
      const fetchDayPlans = async () => {
        const { data: plans } = await supabase.from('course_day_plans').select('*').eq('course_id', autoDistCourseId).order('day_number', { ascending: true });
        if (plans && plans.length > 0) {
          setAutoDistDayPlans(plans);
          const planIds = plans.map((p: any) => p.id);
          const { data: tasks } = await supabase.from('day_plan_tasks').select('*').in('day_plan_id', planIds).order('order_index', { ascending: true });
          setAutoDistTasks(tasks || []);
          setAutoDistSelectedDays(new Set(planIds));
        } else {
          setAutoDistDayPlans([]);
          setAutoDistTasks([]);
          setAutoDistSelectedDays(new Set());
        }
      };
      fetchDayPlans();
    } else {
      setAutoDistDayPlans([]);
      setAutoDistTasks([]);
      setAutoDistSelectedDays(new Set());
    }
  }, [autoDistCourseId]);

  useEffect(() => {
    if (!boardAssignCourseId) {
      setBoardAssignColumns([]);
      setBoardAssignCards([]);
      setBoardAssignItems([]);
      return;
    }
    const fetchBoard = async () => {
      const { data: cols } = await supabase.from('board_columns').select('*').eq('course_id', boardAssignCourseId).order('order_index', { ascending: true });
      setBoardAssignColumns(cols || []);

      if (cols && cols.length > 0) {
        const colIds = cols.map(c => c.id);
        const { data: cards } = await supabase.from('board_cards').select('*').in('column_id', colIds).order('order_index', { ascending: true });
        setBoardAssignCards(cards || []);

        if (cards && cards.length > 0) {
          const cardIds = cards.map(c => c.id);
          const { data: items } = await supabase.from('board_card_items').select('*').in('card_id', cardIds).order('order_index', { ascending: true });
          setBoardAssignItems(items || []);
        } else {
          setBoardAssignItems([]);
        }
      } else {
        setBoardAssignCards([]);
        setBoardAssignItems([]);
      }
    };
    fetchBoard();
  }, [boardAssignCourseId]);

  const handleBoardAssignSubmit = async () => {
    if (!selectedStudent || !boardAssignCourseId) return;
    setIsBoardAssigning(true);
    
    try {
      const inserts = [];
      for (const col of boardAssignColumns) {
        const colCards = boardAssignCards.filter(c => c.column_id === col.id);
        for (const card of colCards) {
          const cardItems = boardAssignItems.filter(i => i.card_id === card.id);
          for (const item of cardItems) {
            inserts.push({
              user_id: selectedStudent.id,
              title: item.title,
              description: item.description,
              task_type: item.task_type,
              test_id: item.test_id,
              category: col.title,
              card_title: card.title,
              card_order: card.order_index,
              due_date: null
            });
          }
        }
      }
      
      if (inserts.length > 0) {
        const { error } = await supabase.from('assignments').insert(inserts);
        if (error) throw error;
        
        // Refresh assignments
        const { data: updatedAssignments } = await supabase.from('assignments').select('*').eq('user_id', selectedStudent.id);
        if (updatedAssignments) setStudentAssignments(updatedAssignments);
      }
      
      setShowBoardAssign(false);
      setBoardAssignCourseId(null);
      alert('Đã giao thành công!');
    } catch (err: any) {
      console.error(err);
      alert('Lỗi: ' + err.message);
    } finally {
      setIsBoardAssigning(false);
    }
  };

  const handleAutoDistribute = async () => {
    if (!selectedStudent || !autoDistCourseId || autoDistSelectedDays.size === 0) return;
    setIsAutoDistributing(true);
    const { data: { session } } = await supabase.auth.getSession();
    
    // Sort selected days
    const selectedPlans = autoDistDayPlans.filter(p => autoDistSelectedDays.has(p.id)).sort((a, b) => a.day_number - b.day_number);
    
    let currentDate = new Date(autoDistStartDate);
    const newAssignments: any[] = [];
    
    for (const plan of selectedPlans) {
      const planTasks = autoDistTasks.filter(t => t.day_plan_id === plan.id).sort((a, b) => a.order_index - b.order_index);
      const dueDate = currentDate.toISOString().split('T')[0];
      
      for (const task of planTasks) {
        newAssignments.push({
          user_id: selectedStudent.id,
          due_date: dueDate,
          title: task.title,
          description: task.description || '',
          task_type: task.task_type,
          test_id: task.test_id,
          created_by: session?.user?.id || null
        });
      }
      
      currentDate.setDate(currentDate.getDate() + (plan.duration_days || 1));
    }
    
    if (newAssignments.length > 0) {
      // Dedup: delete old manual assignments with same title for this user
      const manualTitles = [...new Set(newAssignments.filter(a => a.task_type === 'manual').map(a => a.title))];
      for (const t of manualTitles) {
        await supabase.from('assignments').delete().eq('user_id', selectedStudent.id).eq('title', t).eq('task_type', 'manual');
      }
      await supabase.from('assignments').insert(newAssignments);
    }
    
    setShowAutoDistribute(false);
    setAutoDistCourseId(null);
    setIsAutoDistributing(false);
    fetchAssignments(selectedStudent.id);
  };


  const handleApproveAssignment = async (id: string) => {
    await supabase.from('assignments').update({ admin_approved: true, is_completed: true, updated_at: new Date().toISOString() }).eq('id', id);
    if (selectedStudent) fetchAssignments(selectedStudent.id);
  };

  const handleDeleteAssignment = async (id: string) => {
    if (!window.confirm('Xóa công việc này?')) return;
    await supabase.from('assignments').delete().eq('id', id);
    if (selectedStudent) fetchAssignments(selectedStudent.id);
  };

  const handleReorderAssignment = async (taskId: string, direction: 'up' | 'down') => {
    const tasks = studentAssignments.filter(a => a.due_date === assignSelectedDate).sort((a, b) => (a.order_index || 0) - (b.order_index || 0));
    const idx = tasks.findIndex(t => t.id === taskId);
    const swapIdx = direction === 'up' ? idx - 1 : idx + 1;
    if (swapIdx < 0 || swapIdx >= tasks.length) return;
    const a = tasks[idx], b = tasks[swapIdx];
    const aOrder = a.order_index ?? idx;
    const bOrder = b.order_index ?? swapIdx;
    await Promise.all([
      supabase.from('assignments').update({ order_index: bOrder }).eq('id', a.id),
      supabase.from('assignments').update({ order_index: aOrder }).eq('id', b.id),
    ]);
    if (selectedStudent) fetchAssignments(selectedStudent.id);
  };

  const toggleFolderSelection = (folderId: string) => {
    const testsInFolder = allTestsForAssign.filter(t => t.folder_id === folderId);
    const allSelected = testsInFolder.every(t => selectedTestIds.has(t.id));
    const newSet = new Set(selectedTestIds);
    testsInFolder.forEach(t => allSelected ? newSet.delete(t.id) : newSet.add(t.id));
    const subFolders = allFoldersForAssign.filter(f => f.parent_id === folderId);
    subFolders.forEach(sf => {
      const subTests = allTestsForAssign.filter(t => t.folder_id === sf.id);
      subTests.forEach(t => allSelected ? newSet.delete(t.id) : newSet.add(t.id));
    });
    setSelectedTestIds(newSet);
  };

  const assignCalDays = (() => {
    const year = assignCalMonth.getFullYear();
    const month = assignCalMonth.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startPad = firstDay.getDay();
    const days: { date: string; day: number; isCurrentMonth: boolean; isToday: boolean }[] = [];
    const prevMonth = new Date(year, month, 0);
    for (let i = startPad - 1; i >= 0; i--) {
      const d = prevMonth.getDate() - i;
      days.push({ date: `${year}-${String(month).padStart(2, '0')}-${String(d).padStart(2, '0')}`, day: d, isCurrentMonth: false, isToday: false });
    }
    const today = new Date().toISOString().split('T')[0];
    for (let d = 1; d <= lastDay.getDate(); d++) {
      const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
      days.push({ date: dateStr, day: d, isCurrentMonth: true, isToday: dateStr === today });
    }
    const remaining = 42 - days.length;
    for (let d = 1; d <= remaining; d++) {
      const nm = month + 2;
      days.push({ date: `${nm > 12 ? year + 1 : year}-${String(nm > 12 ? 1 : nm).padStart(2, '0')}-${String(d).padStart(2, '0')}`, day: d, isCurrentMonth: false, isToday: false });
    }
    return days;
  })();

  const assignDateStatus: Record<string, 'blue' | 'green' | 'red'> = {};
  const today = new Date().toISOString().split('T')[0];
  const byDate: Record<string, any[]> = {};
  studentAssignments.forEach(a => { if (!byDate[a.due_date]) byDate[a.due_date] = []; byDate[a.due_date].push(a); });
  Object.entries(byDate).forEach(([date, tasks]) => {
    const allDone = tasks.every(t => t.is_completed);
    assignDateStatus[date] = allDone ? 'green' : date < today ? 'red' : 'blue';
  });
  const tasksForSelectedDate = studentAssignments.filter(a => a.due_date === assignSelectedDate).sort((a, b) => (a.order_index || 0) - (b.order_index || 0));

  const handleSelectStudent = async (student: any) => {
    setSelectedStudent(student);
    setEditingUser(null);
    setIsLoadingDetails(true);
    setActiveDetailTab('courses');
    
    try {
      const { data: enrollData } = await supabase.from('enrollments').select('*, courses(title, type)').eq('user_id', student.id).order('enrolled_at', { ascending: false });
      setStudentEnrollments(enrollData || []);

      const { data: historyData } = await supabase.from('test_results').select('*').eq('user_id', student.id).order('created_at', { ascending: false });
      setStudentHistory(historyData || []);

      // 🚀 FETCH NHẬT KÝ HOẠT ĐỘNG
      const { data: actData } = await supabase.from('activity_logs').select('*').eq('user_id', student.id).order('created_at', { ascending: false });
      setStudentActivities(actData || []);
      
    } catch (err: any) {
      console.error("Lỗi tải chi tiết:", err.message);
    } finally {
      setIsLoadingDetails(false);
    }
  };

  const handleCreateUser = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsCreatingUser(true);
    
    const formData = new FormData(e.currentTarget);
    const fullName = formData.get('fullName') as string;
    const email = formData.get('email') as string;
    const password = formData.get('password') as string;
    const phone = formData.get('phone') as string;
    
    try {
      const { data, error } = await authSupabase.auth.signUp({
        email: email,
        password: password,
        options: { data: { full_name: fullName, role: newUserRole } }
      });

      if (error) throw error;
      await new Promise(resolve => setTimeout(resolve, 1500));

      if (data.user) {
        await supabase.rpc('update_user_profile', {
            target_user_id: data.user.id,
            new_full_name: fullName,
            new_role: newUserRole,
            new_phone: phone 
        });
      }

      alert(`✅ Đã tạo tài khoản ${newUserRole === 'admin' ? 'Quản trị viên' : 'Học viên'} thành công!`);
      setShowCreateUserModal(false);
      setNewUserRole('student');
      fetchStudents(); 
    } catch (err: any) {
      alert("❌ Lỗi tạo tài khoản: " + err.message);
    } finally {
      setIsCreatingUser(false);
    }
  };

  const handleUpdateUser = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsUpdatingUser(true);
    const formData = new FormData(e.currentTarget);
    const fullName = formData.get('fullName') as string;
    const role = formData.get('role') as string;
    const phone = formData.get('phone') as string;

    try {
      const { error } = await supabase.rpc('update_user_profile', {
          target_user_id: editingUser.id,
          new_full_name: fullName,
          new_role: role,
          new_phone: phone
      });
      
      if (error) throw error;
      
      alert("✅ Đã cập nhật thông tin thành công!");
      
      if (selectedStudent && selectedStudent.id === editingUser.id) {
         setSelectedStudent({ ...selectedStudent, full_name: fullName, role: role, phone: phone });
      }
      
      setEditingUser(null);
      fetchStudents();
    } catch (err: any) {
      alert("❌ Lỗi cập nhật: " + err.message);
    } finally {
      setIsUpdatingUser(false);
    }
  };

  const handleDeleteUser = async (id: string, name: string) => {
    if (!window.confirm(`Anh có chắc chắn muốn xóa VĨNH VIỄN tài khoản của ${name || 'học viên này'} không? Toàn bộ lịch sử làm bài sẽ bị mất!\n\n💡 Gợi ý: Nên dùng nút "Tạm dừng" thay vì xóa để giữ lại lịch sử.`)) return;

    try {
      const { error } = await supabase.rpc('delete_admin_user', { target_user_id: id });
      if (error) throw error;
      alert("🗑️ Đã xóa tài khoản thành công!");
      fetchStudents(); 
    } catch (err: any) {
      alert("❌ Lỗi xóa tài khoản: " + err.message);
    }
  };

  const handleAssignCourse = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const courseId = formData.get('courseId') as string;
    
    if (!courseId || !selectedStudent) return;
    setIsAssigning(true);
    
    try {
      const { data, error } = await supabase.from('enrollments').insert([{
        user_id: selectedStudent.id,
        course_id: courseId,
        status: 'active'
      }]).select('*, courses(title, type)');

      if (error) {
        if (error.code === '23505') throw new Error("Học viên này đã được gán khóa học này rồi!");
        throw error;
      }
      
      setStudentEnrollments([data[0], ...studentEnrollments]);
      setShowAssignModal(false);
      alert("✅ Đã gán khóa học thành công!");
    } catch (err: any) {
      alert("❌ Lỗi: " + err.message);
    } finally {
      setIsAssigning(false);
    }
  };

  const handleRemoveCourse = async (enrollmentId: string) => {
    if (!window.confirm("Xóa quyền truy cập khóa học này của học viên?")) return;
    try {
      await supabase.from('enrollments').delete().eq('id', enrollmentId);
      setStudentEnrollments(studentEnrollments.filter(e => e.id !== enrollmentId));
    } catch (err: any) {
      alert("Lỗi khi xóa: " + err.message);
    }
  };

  // 🚀 HÀM MỞ BÀI THI CHI TIẾT TỪ ADMIN
  const handleReviewTest = async (h: any) => {
    const testId = h.details?.test_id || h.test_id;
    
    // Tìm test ID từ cache nhẹ (chỉ để lấy test_type nếu cần)
    let cachedTest = allTests.find(t => String(t.id) === String(testId));
    if (!cachedTest) cachedTest = allTests.find(t => t.title?.trim() === h.test_title?.trim());
    
    // Luôn fetch đầy đủ dữ liệu từ DB (bao gồm json_config, insert_pdf_url...)
    let foundTest: any = null;
    if (testId) {
        const { data } = await supabase.from('tests').select('*').eq('id', testId).single();
        if (data) foundTest = data;
    }
    if (!foundTest && h.test_title) {
        const { data } = await supabase.from('tests').select('*').eq('title', h.test_title.trim()).limit(1);
        if (data && data.length > 0) foundTest = data[0];
    }
    
    if (foundTest && onStartTest) {
        const type = String(foundTest.test_type || '').toLowerCase();
        let targetMode = 'standard';
        if (type.includes('split-standard')) targetMode = 'split-standard';
        else if (type.includes('splitscreen') && type.includes('standard')) targetMode = 'standard-splitscreen';
        else if (type.includes('standard-reading')) targetMode = 'standard-reading';
        else if (type.includes('case-study') || type.includes('business')) targetMode = 'case-study';
        else if (type.includes('igcse') && type.includes('direct')) targetMode = 'igcse-direct';
        else if (type.includes('igcse') || type.includes('science')) targetMode = 'igcse';
        else if (type === 'ielts-writing') targetMode = 'ielts-writing';
        else if (type === 'ielts-speaking') targetMode = 'ielts-speaking';
        else if (type.includes('ielts')) targetMode = 'computer';
        
        sessionStorage.setItem('lms_current_view', 'admin'); 
        // 🔒 Lưu context để khi quay lại admin sẽ tự mở đúng profile học viên + tab lịch sử
        sessionStorage.setItem('admin_return_student_id', selectedStudent?.id || '');
        sessionStorage.setItem('admin_return_tab', 'history');
        
        onStartTest(targetMode, { 
            ...foundTest, 
            history_id: h.id, 
            isReview: true,
            past_answers: h.details?.userAnswers || h.details?.answers || {},
            past_score: h.score,
            past_total: h.total_score,
            past_band: h.details?.bandScore || '0.0',
            aiFeedback: h.details?.aiFeedback || null
        });
    } else {
        alert("Đề thi này không còn tồn tại trên hệ thống.");
    }
  };

  const formatDate = (isoString: string) => {
    if (!isoString) return '';
    const d = new Date(isoString);
    return `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth() + 1).toString().padStart(2, '0')}/${d.getFullYear()} ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
  };

  // Toggle student status (active <-> inactive)
  const handleToggleStatus = async (student: any) => {
    const isCurrentlyActive = student.status !== 'inactive';
    const newStatus = isCurrentlyActive ? 'inactive' : 'active';
    const action = isCurrentlyActive ? 'TẠM DỪNG' : 'KÍCH HOẠT LẠI';
    
    if (!window.confirm(`${action} tài khoản của ${student.full_name || student.email}?${isCurrentlyActive ? '\n\nHọc viên sẽ không thể đăng nhập cho đến khi được kích hoạt lại. Toàn bộ lịch sử được giữ nguyên.' : ''}`)) return;
    
    try {
      const { error } = await supabase.from('profiles').update({ status: newStatus }).eq('id', student.id);
      if (error) throw error;
      
      alert(`✅ Đã ${action.toLowerCase()} tài khoản thành công!`);
      
      // Update local state
      setStudents(prev => prev.map(s => s.id === student.id ? { ...s, status: newStatus } : s));
      if (selectedStudent?.id === student.id) {
        setSelectedStudent({ ...selectedStudent, status: newStatus });
      }
    } catch (err: any) {
      alert('❌ Lỗi: ' + err.message);
    }
  };

  const filteredStudents = students.filter(s => {
    // Status filter
    if (statusFilter === 'active' && s.status === 'inactive') return false;
    if (statusFilter === 'inactive' && s.status !== 'inactive') return false;
    
    // Search filter
    if (!searchQuery) return true;
    return (
      (s.email && s.email.toLowerCase().includes(searchQuery.toLowerCase())) ||
      (s.full_name && s.full_name.toLowerCase().includes(searchQuery.toLowerCase())) ||
      (s.phone && s.phone.includes(searchQuery))
    );
  });

  const totalPages = Math.ceil(filteredStudents.length / itemsPerPage);
  const paginatedStudents = filteredStudents.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  const availableCourses = courses.filter(c => !studentEnrollments.some(e => e.course_id === c.id));

  // ==========================================
  // VIEW CHI TIẾT HỌC VIÊN
  // ==========================================
  if (selectedStudent) {
    const totalTests = studentHistory.length;
    const avgScore = totalTests > 0 ? (studentHistory.reduce((acc, curr) => acc + (curr.score || 0), 0) / totalTests).toFixed(1) : 0;
    const totalTime = studentHistory.reduce((acc, curr) => acc + Math.round((curr.time_spent || 0) / 60), 0);

    return (
      <>
        <div className="animate-in slide-in-from-right-4 duration-300">
          <button onClick={() => setSelectedStudent(null)} className="mb-6 flex items-center gap-2 text-slate-500 hover:text-[#0a5482] font-bold transition-colors bg-white px-4 py-2 rounded-lg border border-slate-200 shadow-sm w-fit">
            <span>←</span> Quay lại danh sách
          </button>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative overflow-hidden">
              <span className={`absolute top-0 w-full py-1 text-[10px] font-black uppercase tracking-widest text-white ${selectedStudent.role === 'admin' ? 'bg-red-500' : 'bg-emerald-500'}`}>
                {selectedStudent.role === 'admin' ? 'Quản trị viên' : 'Học viên'}
              </span>
              <div className="w-20 h-20 rounded-full bg-[#0a5482] text-white flex items-center justify-center font-black text-3xl mb-4 shadow-inner mt-4">
                {selectedStudent.full_name ? selectedStudent.full_name.trim().split(/\s+/).pop()?.charAt(0).toUpperCase() : (selectedStudent.email ? selectedStudent.email.charAt(0).toUpperCase() : 'U')}
              </div>
              
              <h2 className="text-xl font-black text-slate-800 mb-1 flex items-center justify-center gap-2">
                 {selectedStudent.full_name || <span className="text-orange-500 italic text-lg">[Chưa cập nhật Tên]</span>}
                 <button onClick={() => setEditingUser(selectedStudent)} className="text-sm bg-slate-100 hover:bg-[#0a5482] hover:text-white text-slate-400 p-1.5 rounded-md transition-colors" title="Sửa thông tin">✏️</button>
              </h2>
              
              <p className="text-slate-500 font-medium text-[14px] mb-1">{selectedStudent.email}</p>
              {selectedStudent.phone && <p className="text-slate-500 font-bold text-[13px] mb-4 bg-slate-50 px-3 py-1 rounded-full border border-slate-100">📞 {selectedStudent.phone}</p>}
              
              <div className="w-full border-t border-slate-100 pt-4 flex justify-between text-[13px] mt-auto">
                <span className="text-slate-500 font-medium">Ngày tham gia:</span>
                <span className="font-bold text-slate-700">{formatDate(selectedStudent.created_at).split(' ')[0]}</span>
              </div>
            </div>

            <div className="lg:col-span-2 grid grid-cols-3 gap-4">
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-emerald-500 text-lg">📝</span> Tổng bài làm</div>
                <div className="text-4xl font-black text-slate-800">{totalTests}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-blue-500 text-lg">📊</span> Điểm trung bình</div>
                <div className="text-4xl font-black text-slate-800">{avgScore}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-amber-500 text-lg">⏱️</span> Tổng giờ học</div>
                <div className="text-4xl font-black text-slate-800">{Math.round(totalTime/60)} <span className="text-base text-slate-400 font-medium">giờ</span></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col min-h-[400px]">
            <div className="bg-slate-50 px-2 pt-2 border-b border-slate-200 flex gap-2 overflow-x-auto custom-scrollbar">
              <button onClick={() => setActiveDetailTab('courses')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'courses' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📚 Khóa học</button>
              <button onClick={() => setActiveDetailTab('history')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'history' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📊 Lịch sử Điểm</button>
              <button onClick={() => setActiveDetailTab('activity')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'activity' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>👀 Nhật ký Truy cập</button>
              <button onClick={() => setActiveDetailTab('assignments')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'assignments' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📅 Lịch báo bài</button>
            </div>
            
            <div className="p-6 flex-1 bg-white">
              {isLoadingDetails ? (
                <div className="py-20 text-center text-slate-400 font-bold">⏳ Đang tải dữ liệu...</div>
              ) : activeDetailTab === 'courses' ? (
                <div>
                  <div className="flex justify-between items-center mb-6">
                    <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest">Danh sách khóa học được phép truy cập</h3>
                    <button onClick={() => setShowAssignModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white px-5 py-2.5 rounded-lg font-bold text-xs shadow-sm transition">+ GÁN KHÓA HỌC</button>
                  </div>
                  
                  {studentEnrollments.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Học viên này chưa được gán khóa học nào.</div>
                  ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                      {studentEnrollments.map(e => (
                        <div key={e.id} className="border border-slate-200 p-5 rounded-xl bg-slate-50 flex flex-col relative group">
                          <span className="bg-blue-100 text-blue-700 font-black uppercase text-[10px] px-2 py-1 rounded w-fit mb-3">{e.courses?.type || 'Khóa học'}</span>
                          <h4 className="font-bold text-slate-800 text-[15px] mb-2">{e.courses?.title || 'Khóa học đã xóa'}</h4>
                          <p className="text-[12px] text-slate-500 font-medium">Gán ngày: {formatDate(e.enrolled_at).split(' ')[0]}</p>
                          <button onClick={() => handleRemoveCourse(e.id)} className="absolute top-4 right-4 text-red-400 hover:text-red-600 font-bold text-xs opacity-0 group-hover:opacity-100 transition-opacity">Gỡ bỏ ✖</button>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

              ) : activeDetailTab === 'history' ? (
                <div>
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-6">Lịch sử nộp bài ({studentHistory.length} bài)</h3>
                  {studentHistory.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Học viên này chưa nộp bài thi nào.</div>
                  ) : (
                    <div className="border border-slate-200 rounded-xl overflow-hidden">
                      <table className="w-full text-left border-collapse">
                        <thead className="bg-[#f8fafc] text-[11px] font-black uppercase tracking-wider text-slate-500 border-b border-slate-200">
                          <tr>
                            <th className="px-5 py-3">Tên bài thi</th>
                            <th className="px-5 py-3 text-center">Dạng</th>
                            <th className="px-5 py-3 text-center">Điểm</th>
                            <th className="px-5 py-3 text-center">Ngày nộp</th>
                            <th className="px-5 py-3 text-right">Thao tác</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100">
                          {studentHistory.map(h => (
                            <tr key={h.id} className="hover:bg-slate-50 transition-colors">
                              <td className="px-5 py-3 font-bold text-[13px] text-slate-800">{h.test_title}</td>
                              <td className="px-5 py-3 text-center"><span className="bg-slate-100 text-slate-600 px-2 py-1 rounded text-[10px] font-bold border border-slate-200">{h.test_type}</span></td>
                              <td className="px-5 py-3 text-center font-black text-[14px] text-emerald-600">{h.score} / {h.total_score}</td>
                              <td className="px-5 py-3 text-center text-slate-500 text-[12px]">{formatDate(h.created_at)}</td>
                              <td className="px-5 py-3 text-right">
                                 <button onClick={() => handleReviewTest(h)} className="text-[#0a5482] bg-blue-50 hover:bg-blue-100 border border-blue-200 shadow-sm px-4 py-2 rounded-lg font-bold transition-colors text-[11px] uppercase tracking-wide">
                                    👁️ Xem bài làm
                                 </button>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}
                </div>

              ) : activeDetailTab === 'activity' ? (
                <div className="animate-in fade-in pb-10">
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-8">Nhật ký truy cập & hành vi</h3>
                  {studentActivities.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Chưa có hoạt động nào được ghi nhận.</div>
                  ) : (
                    <div className="space-y-6 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-200 before:to-transparent">
                      {studentActivities.map((act) => (
                         <div key={act.id} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div className="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#0a5482] text-white font-bold shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow-sm z-10 text-[14px]">
                               {act.action_type === 'login' ? '🔑' : act.action_type === 'finish_test' ? '📝' : act.action_type === 'call_tutor' ? '📞' : '📖'}
                            </div>
                            <div className="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-[#2bd6eb] transition-colors">
                               <div className="flex justify-between items-start mb-2">
                                  <h4 className="font-black text-[#0a5482] text-[13px] md:text-[15px] uppercase tracking-tight">
                                     {act.action_type === 'login' && 'Đăng nhập hệ thống'}
                                     {act.action_type === 'finish_test' && 'Nộp bài kiểm tra'}
                                     {act.action_type === 'call_tutor' && 'Hỏi đáp AI / Voice'}
                                     {act.action_type === 'finish_lecture' && 'Hoàn thành bài giảng'}
                                  </h4>
                                  <span className="text-[11px] font-bold text-slate-400 whitespace-nowrap ml-2 bg-slate-50 px-2 py-1 rounded border border-slate-100">{formatDate(act.created_at)}</span>
                               </div>
                               <p className="text-[13px] text-slate-600 font-medium leading-relaxed">
                                  {act.action_type === 'login' && 'Học sinh đăng nhập thành công vào LMS.'}
                                  {act.action_type === 'finish_test' && `Đã nộp bài: "${act.details?.test_title || 'IELTS'}" với số điểm: ${act.details?.score || 0}`}
                                  {act.action_type === 'call_tutor' && `Thời lượng đàm thoại / hỏi AI: ${act.details?.duration || 0} giây.`}
                                  {act.action_type === 'finish_lecture' && `Học xong bài giảng: "${act.details?.lecture_title || 'Lecture'}"`}
                               </p>
                            </div>
                         </div>
                      ))}
                    </div>
                  )}
                </div>
              ) : activeDetailTab === 'assignments' ? (
                <>
                <div className="flex gap-5 items-start">
                  {/* LEFT: MINI CALENDAR */}
                  <div className="w-[320px] shrink-0">
                    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                      <div className="flex items-center justify-between px-4 py-2.5 border-b border-slate-100">
                        <button onClick={() => setAssignCalMonth(new Date(assignCalMonth.getFullYear(), assignCalMonth.getMonth() - 1))} className="w-7 h-7 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500">←</button>
                        <h4 className="font-black text-[13px] text-[#0a5482] capitalize">{assignCalMonth.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' })}</h4>
                        <button onClick={() => setAssignCalMonth(new Date(assignCalMonth.getFullYear(), assignCalMonth.getMonth() + 1))} className="w-7 h-7 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500">→</button>
                      </div>
                      <div className="grid grid-cols-7 px-2 pt-2 pb-1">
                        {['CN','T2','T3','T4','T5','T6','T7'].map(d => <div key={d} className="text-center text-[9px] font-bold text-slate-400 uppercase">{d}</div>)}
                      </div>
                      <div className="grid grid-cols-7 px-2 pb-2 gap-0.5">
                        {assignCalDays.map((day, i) => {
                          const status = assignDateStatus[day.date];
                          const isSelected = assignSelectedDate === day.date;
                          return (
                            <button key={i} onClick={() => setAssignSelectedDate(day.date)}
                              className={`aspect-square rounded-lg flex items-center justify-center text-[11px] font-semibold transition-all
                                ${!day.isCurrentMonth ? 'text-slate-300' : 'text-slate-700'}
                                ${day.isToday && !isSelected ? 'ring-1 ring-[#0ea5e9]' : ''}
                                ${isSelected ? 'bg-[#0a5482] text-white scale-105 shadow' :
                                  status === 'green' ? 'bg-emerald-100 text-emerald-800' :
                                  status === 'red' ? 'bg-red-100 text-red-700' :
                                  status === 'blue' ? 'bg-sky-100 text-sky-800' :
                                  'hover:bg-slate-50'}
                              `}>
                              {day.day}
                            </button>
                          );
                        })}
                      </div>
                      {/* LEGEND */}
                      <div className="flex items-center justify-center gap-4 px-3 pb-2.5 text-[9px] text-slate-400">
                        <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-sky-100 border border-sky-300"></span> Chưa xong</span>
                        <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-emerald-100 border border-emerald-300"></span> Xong</span>
                        <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded bg-red-100 border border-red-300"></span> Quá hạn</span>
                      </div>
                    </div>
                  </div>

                  {/* RIGHT: TASKS FOR SELECTED DATE */}
                  <div className="flex-1 min-w-0">
                    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                      <div className="px-5 py-3 border-b border-slate-100 bg-slate-50 flex items-center justify-between">
                        <h4 className="font-black text-sm text-slate-700">
                          📋 {new Date(assignSelectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'long' })}
                          <span className="text-slate-400 font-normal ml-2">({tasksForSelectedDate.length} việc)</span>
                        </h4>
                        <div className="flex items-center gap-2">
                          <button onClick={() => setShowBoardAssign(true)} className="bg-violet-600 text-white px-4 py-1.5 rounded-lg text-[12px] font-bold hover:bg-violet-700 transition-all">📋 Giao Board</button>
                          <button onClick={() => setShowAutoDistribute(true)} className="bg-emerald-600 text-white px-4 py-1.5 rounded-lg text-[12px] font-bold hover:bg-emerald-700 transition-all">+ Tự động phân bổ</button>
                          <button onClick={() => { setShowTaskPicker(true); setTaskPickerMode('choose'); }} className="bg-[#0a5482] text-white px-4 py-1.5 rounded-lg text-[12px] font-bold hover:bg-[#083d5e] transition-all">+ Giao việc</button>
                        </div>

                      </div>
                      {tasksForSelectedDate.length === 0 ? (
                        <div className="p-8 text-center text-slate-400 text-[13px]">Chưa giao việc cho ngày này.</div>
                      ) : (
                        <div className="divide-y divide-slate-100 max-h-[500px] overflow-y-auto">
                          {tasksForSelectedDate.map((a: any, idx: number) => (
                            <div key={a.id} className="px-5 py-3 flex items-center gap-3 hover:bg-slate-50">
                              {/* REORDER ARROWS */}
                              <div className="flex flex-col gap-0.5 shrink-0">
                                <button onClick={() => handleReorderAssignment(a.id, 'up')} disabled={idx === 0}
                                  className={`w-5 h-5 rounded flex items-center justify-center text-[10px] transition-colors ${idx === 0 ? 'text-slate-200 cursor-default' : 'text-slate-400 hover:bg-slate-200 hover:text-slate-700'}`}>▲</button>
                                <button onClick={() => handleReorderAssignment(a.id, 'down')} disabled={idx === tasksForSelectedDate.length - 1}
                                  className={`w-5 h-5 rounded flex items-center justify-center text-[10px] transition-colors ${idx === tasksForSelectedDate.length - 1 ? 'text-slate-200 cursor-default' : 'text-slate-400 hover:bg-slate-200 hover:text-slate-700'}`}>▼</button>
                              </div>
                              {/* STATUS DOT */}
                              <div className={`w-3 h-3 rounded-full shrink-0 ${a.is_completed ? 'bg-emerald-500' : a.student_completed ? 'bg-amber-400' : a.due_date < today ? 'bg-red-500' : 'bg-[#0ea5e9]'}`}></div>
                              {/* CONTENT */}
                              <div className="flex-1 min-w-0">
                                <p className="text-[13px] font-bold text-slate-800 truncate">{a.title}</p>
                                <p className="text-[11px] text-slate-400">{a.task_type === 'test' ? '📝 Bài tập' : '📋 Thủ công'}{a.description ? ` · ${a.description}` : ''}</p>
                              </div>
                              {/* ACTIONS */}
                              <div className="flex items-center gap-2 shrink-0">
                                {a.is_completed && <span className="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">✅ Hoàn thành</span>}
                                {a.student_completed && !a.is_completed && a.task_type === 'manual' && (
                                  <button onClick={() => handleApproveAssignment(a.id)} className="text-[10px] font-bold bg-amber-100 text-amber-700 px-3 py-1 rounded-full hover:bg-amber-200 transition-colors">⏳ Duyệt</button>
                                )}
                                {!a.is_completed && !a.student_completed && <span className="text-[10px] font-bold text-slate-400">Chờ</span>}
                                <button onClick={() => handleDeleteAssignment(a.id)} className="text-slate-300 hover:text-red-500 transition-colors text-[14px]">🗑</button>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {/* TASK PICKER MODAL */}
                {showTaskPicker && (
                    <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4" onClick={() => { setShowTaskPicker(false); setTaskPickerMode('choose'); }}>
                      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[80vh] flex flex-col" onClick={e => e.stopPropagation()}>
                        <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between shrink-0">
                          <div className="flex items-center gap-3">
                            {taskPickerMode !== 'choose' && (
                              <button onClick={() => { 
                                if (taskPickerMode === 'manual' && manualBrowserCourseId) { setManualBrowserCourseId(null); }
                                else if (taskPickerMode === 'test' && testBrowserCourseId) { setTestBrowserCourseId(null); }
                                else { setTaskPickerMode('choose'); setTestBrowserCourseId(null); setManualBrowserCourseId(null); }
                              }} className="text-slate-400 hover:text-slate-700 text-lg">←</button>
                            )}
                            <h3 className="font-black text-[#0a5482]">
                              {taskPickerMode === 'choose' ? '+ Giao việc' : taskPickerMode === 'manual' ? (manualBrowserCourseId ? '📋 Chọn việc thủ công' : '📚 Chọn khóa học') : testBrowserCourseId ? '📝 Chọn bài tập' : '📚 Chọn khóa học'}
                            </h3>
                          </div>
                          <button onClick={() => { setShowTaskPicker(false); setTaskPickerMode('choose'); setManualBrowserCourseId(null); }} className="text-slate-400 hover:text-red-500 text-xl font-bold">✕</button>
                        </div>
                        <div className="flex-1 overflow-y-auto p-6">
                          {taskPickerMode === 'choose' && (
                            <div className="space-y-3">
                              <p className="text-[13px] text-slate-500 mb-4">Giao cho ngày <b>{new Date(assignSelectedDate + 'T00:00:00').toLocaleDateString('vi-VN')}</b></p>
                              <button onClick={() => setTaskPickerMode('manual')} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-4 text-left">
                                <span className="text-3xl">📋</span>
                                <div><p className="font-bold text-slate-800 text-[14px]">Việc thủ công</p><p className="text-[12px] text-slate-400">Chọn từ danh mục đã tạo sẵn</p></div>
                              </button>
                              <button onClick={() => setTaskPickerMode('test')} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-4 text-left">
                                <span className="text-3xl">📝</span>
                                <div><p className="font-bold text-slate-800 text-[14px]">Bài tập trong hệ thống</p><p className="text-[12px] text-slate-400">Duyệt khóa học → folder → chọn đề</p></div>
                              </button>
                            </div>
                          )}
                          {taskPickerMode === 'manual' && !manualBrowserCourseId && (
                            <div className="space-y-2">
                              {studentCourses.length === 0 ? (
                                <div className="p-8 text-center text-slate-400 text-[13px]">Học sinh chưa được gán khóa học nào.</div>
                              ) : studentCourses.map(c => {
                                const templateCount = courseTaskLinks.filter(l => l.course_id === c.id).length;
                                return (
                                <button key={c.id} onClick={() => { setManualBrowserCourseId(c.id); setSelectedTemplates(new Set()); }} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-3 text-left">
                                  <span className="text-xl">📚</span>
                                  <div className="flex-1">
                                    <p className="font-bold text-slate-800 text-[13px]">{c.title}</p>
                                    <p className="text-[11px] text-slate-400">{templateCount} việc thủ công</p>
                                  </div>
                                  <span className="ml-auto text-slate-400">→</span>
                                </button>
                                );
                              })}
                            </div>
                          )}
                          {taskPickerMode === 'manual' && manualBrowserCourseId && (() => {
                            const linkedTemplateIds = courseTaskLinks.filter(l => l.course_id === manualBrowserCourseId).map(l => l.template_id);
                            const courseTemplates = manualTemplates.filter(t => linkedTemplateIds.includes(t.id));
                            return (
                            <div className="space-y-2">
                              {courseTemplates.length === 0 ? (
                                <div className="p-8 text-center text-slate-400 text-[13px]">
                                  <p className="text-4xl mb-3">📭</p>
                                  <p className="font-bold">Khóa học này chưa có việc thủ công</p>
                                  <p className="text-[12px] mt-1">Vào Khóa học & Lớp → Danh mục Việc thủ công → 📚 để gán.</p>
                                </div>
                              ) : courseTemplates.map(tpl => (
                                <label key={tpl.id} className={`flex items-center gap-3 p-3 rounded-xl border cursor-pointer transition-all ${selectedTemplates.has(tpl.id) ? 'bg-sky-50 border-[#0ea5e9]' : 'border-slate-200 hover:bg-slate-50'}`}>
                                  <input type="checkbox" checked={selectedTemplates.has(tpl.id)} onChange={() => {
                                    const s = new Set(selectedTemplates);
                                    s.has(tpl.id) ? s.delete(tpl.id) : s.add(tpl.id);
                                    setSelectedTemplates(s);
                                  }} className="w-4 h-4 rounded accent-[#0a5482]" />
                                  <div className="flex-1 min-w-0">
                                    <p className="text-[13px] font-bold text-slate-800">{tpl.title}</p>
                                    {tpl.description && <p className="text-[11px] text-slate-400 truncate">{tpl.description}</p>}
                                  </div>
                                </label>
                              ))}
                            </div>
                            );
                          })()}
                          {taskPickerMode === 'test' && !testBrowserCourseId && (
                            <div className="space-y-2">
                              {studentCourses.length === 0 ? (
                                <div className="p-8 text-center text-slate-400 text-[13px]">Học sinh chưa được gán khóa học nào.</div>
                              ) : studentCourses.map(c => (
                                <button key={c.id} onClick={() => setTestBrowserCourseId(c.id)} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-3 text-left">
                                  <span className="text-xl">📚</span>
                                  <p className="font-bold text-slate-800 text-[13px]">{c.title}</p>
                                  <span className="ml-auto text-slate-400">→</span>
                                </button>
                              ))}
                            </div>
                          )}
                          {taskPickerMode === 'test' && testBrowserCourseId && (() => {
                            const courseFolders = allFoldersForAssign.filter(f => f.course_id === testBrowserCourseId && !f.parent_id);
                            const allCourseFolderIds = new Set(allFoldersForAssign.filter(f => f.course_id === testBrowserCourseId).map(f => f.id));
                            const courseTests = allTestsForAssign.filter(t => t.course_id === testBrowserCourseId || (t.folder_id && allCourseFolderIds.has(t.folder_id)));
                            const rootTests = courseTests.filter(t => !t.folder_id);
                            
                            // Recursive: collect ALL test IDs under a folder (any depth)
                            const getAllTestIdsUnder = (folderId: string): string[] => {
                              const direct = courseTests.filter(t => t.folder_id === folderId).map(t => t.id);
                              const children = allFoldersForAssign.filter(f => f.parent_id === folderId);
                              const nested = children.flatMap(c => getAllTestIdsUnder(c.id));
                              return [...direct, ...nested];
                            };

                            // Recursive render component
                            const renderFolder = (folder: any, depth: number) => {
                              const allTestIds = getAllTestIdsUnder(folder.id);
                              const folderTests = courseTests.filter(t => t.folder_id === folder.id);
                              const childFolders = allFoldersForAssign.filter(f => f.parent_id === folder.id);
                              const allChecked = allTestIds.length > 0 && allTestIds.every(id => selectedTestIds.has(id));
                              const someChecked = allTestIds.some(id => selectedTestIds.has(id));
                              return (
                                <div key={folder.id}>
                                  <label className={`flex items-center gap-3 p-2.5 rounded-xl cursor-pointer transition-all ${someChecked ? 'bg-sky-50' : 'hover:bg-slate-50'}`} style={{ paddingLeft: `${depth * 20 + 10}px` }}>
                                    <input type="checkbox" checked={allChecked} ref={el => { if (el) el.indeterminate = someChecked && !allChecked; }} onChange={() => {
                                      const newSet = new Set(selectedTestIds);
                                      allTestIds.forEach(id => allChecked ? newSet.delete(id) : newSet.add(id));
                                      setSelectedTestIds(newSet);
                                    }} className="w-4 h-4 rounded accent-[#0a5482]" />
                                    <span className="text-[14px]">{depth === 0 ? '📁' : '📂'}</span>
                                    <p className={`font-bold text-slate-700 ${depth === 0 ? 'text-[13px]' : 'text-[12px]'}`}>{folder.title}</p>
                                    <span className="ml-auto text-[11px] text-slate-400">{allTestIds.length} đề</span>
                                  </label>
                                  <div>
                                    {childFolders.map(cf => renderFolder(cf, depth + 1))}
                                    {folderTests.map(t => (
                                      <label key={t.id} className="flex items-center gap-3 p-1.5 rounded-lg cursor-pointer hover:bg-slate-50" style={{ paddingLeft: `${(depth + 1) * 20 + 10}px` }}>
                                        <input type="checkbox" checked={selectedTestIds.has(t.id)} onChange={() => { const s = new Set(selectedTestIds); s.has(t.id) ? s.delete(t.id) : s.add(t.id); setSelectedTestIds(s); }} className="w-3.5 h-3.5 rounded accent-[#0a5482]" />
                                        <p className="text-[12px] text-slate-600 truncate">{t.title}</p>
                                      </label>
                                    ))}
                                  </div>
                                </div>
                              );
                            };

                            return (
                              <div className="space-y-1">
                                {courseFolders.map(folder => renderFolder(folder, 0))}
                                {rootTests.map(t => (
                                  <label key={t.id} className="flex items-center gap-3 p-2.5 rounded-xl cursor-pointer hover:bg-slate-50">
                                    <input type="checkbox" checked={selectedTestIds.has(t.id)} onChange={() => { const s = new Set(selectedTestIds); s.has(t.id) ? s.delete(t.id) : s.add(t.id); setSelectedTestIds(s); }} className="w-4 h-4 rounded accent-[#0a5482]" />
                                    <p className="text-[13px] text-slate-700">{t.title}</p>
                                  </label>
                                ))}
                              </div>
                            );
                          })()}
                        </div>
                        {taskPickerMode === 'manual' && selectedTemplates.size > 0 && (
                          <div className="px-6 py-3 border-t border-slate-200 shrink-0">
                            <button onClick={handleAddManualTasks} disabled={isAddingAssignment} className="w-full bg-[#0a5482] text-white py-2.5 rounded-xl text-[13px] font-bold hover:bg-[#083d5e] disabled:opacity-50 transition-all">
                              {isAddingAssignment ? '⏳ Đang giao...' : `Giao ${selectedTemplates.size} việc thủ công`}
                            </button>
                          </div>
                        )}
                        {taskPickerMode === 'test' && testBrowserCourseId && selectedTestIds.size > 0 && (
                          <div className="px-6 py-3 border-t border-slate-200 shrink-0">
                            <button onClick={handleAddTestTasks} disabled={isAddingAssignment} className="w-full bg-[#0a5482] text-white py-2.5 rounded-xl text-[13px] font-bold hover:bg-[#083d5e] disabled:opacity-50 transition-all">
                              {isAddingAssignment ? '⏳ Đang giao...' : `Giao ${selectedTestIds.size} bài tập`}
                            </button>
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </>
              ) : null}

              {/* AUTO DISTRIBUTE MODAL */}
              {showAutoDistribute && (
                <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4" onClick={() => setShowAutoDistribute(false)}>
                  <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[80vh] flex flex-col" onClick={e => e.stopPropagation()}>
                    <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between shrink-0">
                      <div className="flex items-center gap-3">
                        {autoDistCourseId && (
                          <button onClick={() => setAutoDistCourseId(null)} className="text-slate-400 hover:text-slate-700 text-lg">←</button>
                        )}
                        <h3 className="font-black text-emerald-600">
                          {autoDistCourseId ? '🗓️ Cấu hình phân bổ' : '📚 Chọn khóa học để phân bổ'}
                        </h3>
                      </div>
                      <button onClick={() => setShowAutoDistribute(false)} className="text-slate-400 hover:text-red-500 text-xl font-bold">✕</button>
                    </div>

                    <div className="flex-1 overflow-y-auto p-6">
                      {!autoDistCourseId ? (
                        <div className="space-y-2">
                          {studentCourses.length === 0 ? (
                            <div className="p-8 text-center text-slate-400 text-[13px]">Học sinh chưa được gán khóa học nào.</div>
                          ) : studentCourses.map(c => (
                            <button key={c.id} onClick={() => setAutoDistCourseId(c.id)} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-emerald-50 hover:border-emerald-400 transition-all flex items-center gap-3 text-left">
                              <span className="text-xl">📚</span>
                              <p className="font-bold text-slate-800 text-[13px]">{c.title}</p>
                              <span className="ml-auto text-slate-400">→</span>
                            </button>
                          ))}
                        </div>
                      ) : (
                        <div className="space-y-6">
                          <div>
                            <label className="text-[13px] font-bold text-slate-700 block mb-2">Ngày bắt đầu:</label>
                            <input type="date" value={autoDistStartDate} onChange={(e) => setAutoDistStartDate(e.target.value)} className="w-full border border-slate-300 rounded-lg px-3 py-2 text-[14px] outline-none focus:border-emerald-500" />
                          </div>
                          
                          <div>
                            <h4 className="text-[13px] font-bold text-slate-700 mb-3 border-b pb-2">Chọn các Day để giao</h4>
                            {autoDistDayPlans.length === 0 ? (
                              <p className="text-[13px] text-slate-400 text-center py-4">Khóa học này chưa được thiết lập Course Plan.</p>
                            ) : (
                              <div className="space-y-2 max-h-60 overflow-y-auto pr-2 custom-scrollbar">
                                {autoDistDayPlans.map(plan => {
                                  const tasksCount = autoDistTasks.filter(t => t.day_plan_id === plan.id).length;
                                  return (
                                    <label key={plan.id} className={`flex items-center gap-3 p-3 rounded-xl border cursor-pointer transition-all ${autoDistSelectedDays.has(plan.id) ? 'bg-emerald-50 border-emerald-400' : 'border-slate-200 hover:bg-slate-50'}`}>
                                      <input type="checkbox" checked={autoDistSelectedDays.has(plan.id)} onChange={() => {
                                        const s = new Set(autoDistSelectedDays);
                                        s.has(plan.id) ? s.delete(plan.id) : s.add(plan.id);
                                        setAutoDistSelectedDays(s);
                                      }} className="w-4 h-4 rounded accent-emerald-600" />
                                      <div className="flex-1 min-w-0">
                                        <p className="text-[13px] font-bold text-slate-800">Day {plan.day_number}: {plan.title}</p>
                                        <div className="flex items-center gap-2 mt-1">
                                          <span className="bg-slate-200 text-slate-600 text-[10px] px-1.5 py-0.5 rounded font-semibold">{plan.duration_days} ngày</span>
                                          <span className="text-[11px] text-slate-400">{tasksCount} việc</span>
                                        </div>
                                      </div>
                                    </label>
                                  );
                                })}
                              </div>
                            )}
                          </div>

                          {autoDistSelectedDays.size > 0 && (
                            <div>
                              <h4 className="text-[13px] font-bold text-slate-700 mb-2">Xem trước lịch (Dự kiến):</h4>
                              <div className="bg-slate-50 border border-slate-200 rounded-lg p-3 space-y-2 max-h-40 overflow-y-auto text-[12px]">
                                {(() => {
                                  let current = new Date(autoDistStartDate);
                                  const selectedPlans = autoDistDayPlans.filter(p => autoDistSelectedDays.has(p.id)).sort((a, b) => a.day_number - b.day_number);
                                  return selectedPlans.map(plan => {
                                    const startStr = current.toLocaleDateString('vi-VN');
                                    let endStr = '';
                                    if (plan.duration_days > 1) {
                                      const end = new Date(current);
                                      end.setDate(end.getDate() + plan.duration_days - 1);
                                      endStr = ` → ${end.toLocaleDateString('vi-VN')}`;
                                    }
                                    const tCount = autoDistTasks.filter(t => t.day_plan_id === plan.id).length;
                                    
                                    const previewText = `Day ${plan.day_number} (${plan.duration_days} ngày): ${startStr}${endStr}`;
                                    
                                    current.setDate(current.getDate() + plan.duration_days);
                                    
                                    return (
                                      <div key={plan.id} className="flex justify-between border-b border-slate-100 last:border-0 pb-1 last:pb-0">
                                        <span className="font-semibold text-slate-600">{previewText}</span>
                                        <span className="text-slate-400">[{tCount} việc]</span>
                                      </div>
                                    );
                                  });
                                })()}
                              </div>
                            </div>
                          )}
                        </div>
                      )}
                    </div>

                    {autoDistCourseId && autoDistSelectedDays.size > 0 && (
                      <div className="px-6 py-3 border-t border-slate-200 shrink-0">
                        <button onClick={handleAutoDistribute} disabled={isAutoDistributing} className="w-full bg-emerald-600 text-white py-2.5 rounded-xl text-[13px] font-bold hover:bg-emerald-700 disabled:opacity-50 transition-all">
                          {isAutoDistributing ? '⏳ Đang phân bổ...' : `Xác nhận phân bổ`}
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {showBoardAssign && (
                <div className="fixed inset-0 bg-slate-900/60 flex items-center justify-center z-[100] p-4 backdrop-blur-sm">
                  <div className="bg-white rounded-2xl shadow-xl w-full max-w-2xl max-h-[90vh] flex flex-col overflow-hidden animate-in zoom-in-95 duration-200">
                    <div className="px-6 py-4 border-b border-slate-100 flex justify-between items-center bg-slate-50">
                      <h3 className="font-black text-[15px] text-slate-800 flex items-center gap-2">
                        <span className="text-xl">📋</span> {!boardAssignCourseId ? 'Chọn khóa học để Giao Board' : 'Xác nhận Giao Board'}
                      </h3>
                      <button onClick={() => { setShowBoardAssign(false); setBoardAssignCourseId(null); setBoardAssignColumns([]); setBoardAssignCards([]); setBoardAssignItems([]); }} className="text-slate-400 hover:text-red-500 text-xl font-bold">✕</button>
                    </div>

                    <div className="flex-1 overflow-y-auto p-6">
                      {!boardAssignCourseId ? (
                        <div className="space-y-2">
                          {studentCourses.length === 0 ? (
                            <div className="p-8 text-center text-slate-400 text-[13px]">Học sinh chưa được gán khóa học nào.</div>
                          ) : studentCourses.map(c => (
                            <button key={c.id} onClick={() => setBoardAssignCourseId(c.id)} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-violet-50 hover:border-violet-400 transition-all flex items-center gap-3 text-left">
                              <span className="text-xl">📚</span>
                              <p className="font-bold text-slate-800 text-[13px]">{c.title}</p>
                              <span className="ml-auto text-slate-400">→</span>
                            </button>
                          ))}
                        </div>
                      ) : (
                        <div className="space-y-6">
                          <p className="text-[13px] text-slate-600 font-medium">Bản xem trước dữ liệu Board từ khóa học:</p>
                          
                          {boardAssignColumns.length === 0 ? (
                            <div className="p-4 bg-slate-50 border border-slate-200 rounded-lg text-center text-slate-500 text-[13px]">
                              Khóa học này chưa có dữ liệu Board.
                            </div>
                          ) : (
                            <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 space-y-4 max-h-[300px] overflow-y-auto">
                              <div className="flex items-center gap-2 mb-2">
                                <span className="px-2 py-1 bg-violet-100 text-violet-700 rounded-md font-bold text-[12px]">Tổng cộng: {boardAssignItems.length} mục</span>
                              </div>
                              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                                {boardAssignColumns.map(col => {
                                  const colCards = boardAssignCards.filter(c => c.column_id === col.id);
                                  const cardIds = colCards.map(c => c.id);
                                  const colItems = boardAssignItems.filter(i => cardIds.includes(i.card_id));
                                  return (
                                    <div key={col.id} className="bg-white border border-slate-200 rounded-md p-3">
                                      <h4 className="font-bold text-[13px] text-slate-800 mb-1">{col.title}</h4>
                                      <p className="text-[12px] text-slate-500">{colCards.length} thẻ / {colItems.length} mục việc</p>
                                    </div>
                                  )
                                })}
                              </div>
                            </div>
                          )}

                          <div className="bg-amber-50 border border-amber-200 p-3 rounded-lg flex items-start gap-2">
                            <span className="text-amber-500 mt-0.5">⚠️</span>
                            <p className="text-[12px] text-amber-700">Lưu ý: Tất cả các mục việc trong Board sẽ được giao cho học sinh dưới dạng bài tập không có ngày hạn.</p>
                          </div>
                        </div>
                      )}
                    </div>
                    
                    {boardAssignCourseId && (
                      <div className="p-4 border-t border-slate-100 bg-slate-50 flex justify-end gap-2">
                        <button onClick={() => setBoardAssignCourseId(null)} className="px-4 py-2 text-slate-500 hover:text-slate-800 font-semibold text-[13px] hover:bg-slate-200 rounded-lg transition-all" disabled={isBoardAssigning}>Quay lại</button>
                        <button 
                          onClick={handleBoardAssignSubmit}
                          disabled={isBoardAssigning || boardAssignColumns.length === 0}
                          className="px-6 py-2 bg-violet-600 text-white font-bold rounded-lg text-[13px] hover:bg-violet-700 transition-all disabled:opacity-50 flex items-center gap-2"
                        >
                          {isBoardAssigning ? 'Đang giao...' : 'Xác nhận Giao Board'}
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              )}

            </div>
          </div>
        </div>

        {/* MODAL EDIT TÀI KHOẢN KHI ĐANG XEM CHI TIẾT */}
        {editingUser && (
          <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
            <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sửa Thông Tin</h2>
              
              <div className="space-y-4 mb-8">
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                  <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Trần Huy Tôn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>
                
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                  <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                  <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                  <p className="text-[10px] text-slate-400 mt-1 italic">* Không thể sửa email từ Admin Panel.</p>
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                  <div className="grid grid-cols-2 gap-3 mt-2">
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                      👨‍🎓 Học viên
                    </label>
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                      👑 Quản trị
                    </label>
                  </div>
                </div>
              </div>

              <div className="flex gap-4">
                <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                  {isUpdatingUser ? 'ĐANG LƯU...' : 'LƯU THAY ĐỔI'}
                </button>
              </div>
            </form>
          </div>
        )}

        {/* MODAL GÁN KHÓA HỌC */}
        {showAssignModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <form onSubmit={handleAssignCourse} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4">Gán Khóa Học</h2>
              <div className="space-y-4 mb-8">
                <label className="text-[13px] font-bold text-slate-500 uppercase">Chọn khóa học</label>
                <select name="courseId" required defaultValue="" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] font-medium bg-slate-50">
                  <option value="" disabled>-- Chọn khóa học --</option>
                  {availableCourses.length === 0 ? (
                     <option value="" disabled>Học viên đã gán tất cả khóa học</option>
                  ) : (
                     availableCourses.map(c => <option key={c.id} value={c.id}>[{c.type}] {c.title}</option>)
                  )}
                </select>
              </div>
              <div className="flex gap-4">
                <button type="button" onClick={() => setShowAssignModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" disabled={isAssigning} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition disabled:opacity-50">GÁN NGAY</button>
              </div>
            </form>
          </div>
        )}
      </>
    );
  }

  // ==========================================
  // VIEW DANH SÁCH HỌC VIÊN TỔNG
  // ==========================================
  return (
    <>
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden animate-in fade-in duration-300 flex flex-col h-[calc(100vh-120px)]">
        <div className="bg-slate-50 px-6 py-5 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-4 shrink-0">
          <div className="flex items-center gap-4">
            <h2 className="font-black text-xl text-[#0a5482]">Quản lý Tài Khoản</h2>
            <div className="flex bg-white border border-slate-200 rounded-lg overflow-hidden shadow-sm">
              <button onClick={() => { setStatusFilter('active'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors ${statusFilter === 'active' ? 'bg-emerald-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Đang học ({students.filter(s => s.status !== 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('inactive'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'inactive' ? 'bg-slate-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Tạm dừng ({students.filter(s => s.status === 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('all'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'all' ? 'bg-[#0a5482] text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Tất cả
              </button>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <div className="relative w-full sm:w-72">
              <input 
                type="text" 
                placeholder="Tìm kiếm theo email, tên, SĐT..." 
                defaultValue={searchQuery}
                onChange={(e) => {
                  clearTimeout(studentSearchTimer);
                  studentSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350);
                }} 
                className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 font-medium text-[13px] outline-none focus:border-[#0a5482] focus:ring-1 focus:ring-[#0a5482] bg-white transition-all shadow-sm" 
              />
              <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">🔍</span>
            </div>
            <button onClick={() => setShowCreateUserModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-6 py-2.5 rounded-xl transition shadow-md text-sm whitespace-nowrap">+ Tạo Tài Khoản</button>
          </div>
        </div>

        <div className="flex-1 flex flex-col overflow-hidden">
          {isLoading ? (
            <div className="p-16 text-center text-slate-500 font-bold text-lg flex items-center justify-center gap-3"><span className="animate-spin text-2xl">⏳</span> Đang tải dữ liệu...</div>
          ) : filteredStudents.length === 0 ? (
            <div className="p-16 text-center text-slate-400 font-medium text-lg border-t border-slate-100">Không tìm thấy tài khoản nào.</div>
          ) : (
            <>
              <div className="flex-1 overflow-y-auto custom-scrollbar">
                <table className="w-full text-left border-collapse min-w-[900px]">
                  <thead className="sticky top-0 bg-white shadow-[0_1px_2px_rgba(0,0,0,0.05)] z-10">
                    <tr className="text-[11px] font-black uppercase tracking-wider text-slate-400">
                      <th className="px-6 py-4 text-center w-16">STT</th>
                      <th className="px-6 py-4">Tài Khoản (Email)</th>
                      <th className="px-6 py-4">Số Điện Thoại</th>
                      <th className="px-6 py-4">Họ và Tên</th>
                      <th className="px-6 py-4">Trạng thái</th>
                      <th className="px-6 py-4 text-center">Ngày tạo</th>
                      <th className="px-6 py-4 text-right">Hành động</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {paginatedStudents.map((student, index) => (
                      <tr key={student.id} className={`hover:bg-blue-50/50 transition-colors group ${student.status === 'inactive' ? 'opacity-60' : ''}`}>
                        <td className="px-6 py-4 text-center font-bold text-slate-400 text-[13px]">
                          {(currentPage - 1) * itemsPerPage + index + 1}
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex items-center gap-3">
                            <div className={`w-10 h-10 rounded-full text-white flex items-center justify-center font-bold text-sm shrink-0 shadow-inner ${student.status === 'inactive' ? 'bg-slate-400' : student.role === 'admin' ? 'bg-red-500' : 'bg-[#0a5482]'}`}>
                              {student.full_name ? student.full_name.trim().split(/\s+/).pop()?.charAt(0).toUpperCase() : (student.email ? student.email.charAt(0).toUpperCase() : 'U')}
                            </div>
                            <div className="text-[13px] font-bold text-slate-700">{student.email}</div>
                          </div>
                        </td>
                        <td className="px-6 py-4">
                           <div className="font-bold text-[13px] text-slate-600">
                              {student.phone || '--'}
                           </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className={`font-bold text-[14px] ${student.full_name ? 'text-[#0a5482]' : 'text-orange-500 italic'}`}>
                             {student.full_name || '[Chưa cập nhật]'}
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex flex-col gap-1">
                            <span className={`px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-wider border w-fit ${student.role === 'admin' ? 'bg-red-50 text-red-600 border-red-200' : 'bg-emerald-50 text-emerald-600 border-emerald-200'}`}>{student.role || 'Student'}</span>
                            {student.status === 'inactive' && <span className="px-2 py-0.5 rounded text-[9px] font-bold uppercase bg-slate-100 text-slate-500 border border-slate-200 w-fit">⏸ Tạm dừng</span>}
                          </div>
                        </td>
                        <td className="px-6 py-4 text-slate-600 font-medium text-[13px] text-center">
                          {formatDate(student.created_at).split(' ')[0]}
                        </td>
                        <td className="px-6 py-4 text-right flex items-center justify-end gap-1.5">
                          <button onClick={() => handleSelectStudent(student)} className="text-[#0a5482] font-bold text-[12px] bg-white hover:bg-[#0a5482] hover:text-white px-4 py-2 rounded-lg transition-all border border-slate-200 shadow-sm uppercase tracking-wider">
                            Cấu hình & Tiến độ
                          </button>
                          
                          <button onClick={() => setEditingUser(student)} className="text-blue-500 hover:text-blue-600 hover:bg-blue-50 p-2 rounded-lg transition-colors border border-transparent hover:border-blue-200" title="Sửa thông tin">
                            ✏️
                          </button>

                          <button onClick={() => handleToggleStatus(student)} className={`p-2 rounded-lg transition-colors border border-transparent ${student.status === 'inactive' ? 'text-emerald-500 hover:text-emerald-600 hover:bg-emerald-50 hover:border-emerald-200' : 'text-amber-500 hover:text-amber-600 hover:bg-amber-50 hover:border-amber-200'}`} title={student.status === 'inactive' ? 'Kích hoạt lại' : 'Tạm dừng'}>
                            {student.status === 'inactive' ? '▶️' : '⏸️'}
                          </button>
    
                          <button onClick={() => handleDeleteUser(student.id, student.full_name)} className="text-slate-400 hover:text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors border border-transparent hover:border-red-200" title="Xóa vĩnh viễn">
                            🗑️
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
  
              {totalPages > 1 && (
                <div className="p-4 border-t border-slate-200 bg-slate-50 flex justify-center items-center gap-4 shrink-0">
                   <button disabled={currentPage === 1} onClick={() => setCurrentPage(p => p - 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                      ← Trang trước
                   </button>
                   <span className="text-[13px] font-black text-slate-500">
                      Trang {currentPage} <span className="font-medium text-slate-400">/ {totalPages}</span>
                   </span>
                   <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => p + 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                      Trang sau →
                   </button>
                </div>
              )}
            </>
          )}
        </div>
      </div>

      {/* MODAL TẠO TÀI KHOẢN MỚI */}
      {showCreateUserModal && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleCreateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Tạo Tài Khoản Mới</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                <input name="fullName" required type="text" defaultValue="" autoComplete="off" placeholder="Nguyễn Văn A" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                <input name="phone" type="text" defaultValue="" autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                <input name="email" required type="email" defaultValue="" autoComplete="off" placeholder="email@tonyenglish.vn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Mật khẩu</label>
                <input name="password" required type="password" minLength={6} defaultValue="123456" autoComplete="off" placeholder="Ít nhất 6 ký tự" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold text-[#0a5482]" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'student' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" checked={newUserRole === 'student'} onChange={() => setNewUserRole('student')} className="hidden" />
                    👨‍🎓 Học viên
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" checked={newUserRole === 'admin'} onChange={() => setNewUserRole('admin')} className="hidden" />
                    👑 Quản trị viên
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setShowCreateUserModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
              <button type="submit" disabled={isCreatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isCreatingUser ? 'ĐANG TẠO...' : 'TẠO TÀI KHOẢN'}
              </button>
            </div>
          </form>
        </div>
      )}
      
      {/* MODAL EDIT TÀI KHOẢN NGOÀI DANH SÁCH TỔNG */}
      {editingUser && !selectedStudent && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sửa Thông Tin</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Trần Huy Tôn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                <p className="text-[10px] text-slate-400 mt-1 italic">* Không thể sửa email từ Admin Panel.</p>
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                    👨‍🎓 Học viên
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                    👑 Quản trị
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
              <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isUpdatingUser ? 'ĐANG LƯU...' : 'LƯU THAY ĐỔI'}
              </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
}