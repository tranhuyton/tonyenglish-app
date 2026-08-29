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
  
  // Test browser
  const [studentCourses, setStudentCourses] = useState<any[]>([]);
  const [allFoldersForAssign, setAllFoldersForAssign] = useState<any[]>([]);
  const [allTestsForAssign, setAllTestsForAssign] = useState<any[]>([]);
  const [testBrowserCourseId, setTestBrowserCourseId] = useState<string | null>(null);
  const [selectedTestIds, setSelectedTestIds] = useState<Set<string>>(new Set());

  const [showAssignModal, setShowAssignModal] = useState(false);
  const [isAssigning, setIsAssigning] = useState(false);

  const [showCreateUserModal, setShowCreateUserModal] = useState(false);
  const [isCreatingUser, setIsCreatingUser] = useState(false);
  const [newUserRole, setNewUserRole] = useState('student');

  const [editingUser, setEditingUser] = useState<any>(null);
  const [isUpdatingUser, setIsUpdatingUser] = useState(false);

  // ðŸš€ KHO Äá»€ THI Äá»‚ Má»ž TÃNH NÄ‚NG XEM Láº I BÃ€I
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
      console.error("Lá»—i táº£i há»c viÃªn:", err.message);
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
  };

  const fetchStudentCoursesAndTests = async (userId: string) => {
    // Get enrolled courses
    const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', userId);
    const courseIds = enrolls?.map(e => e.course_id) || [];
    if (courseIds.length === 0) { setStudentCourses([]); return; }
    
    const { data: coursesData } = await supabase.from('courses').select('id, title, type').in('id', courseIds);
    setStudentCourses(coursesData || []);
    
    // Get all folders + tests for these courses
    const { data: folders } = await supabase.from('folders').select('id, course_id, parent_id, title, display_order').in('course_id', courseIds).order('display_order');
    setAllFoldersForAssign(folders || []);
    
    const { data: tests } = await supabase.from('tests').select('id, title, test_type, folder_id, course_id').in('course_id', courseIds).eq('is_published', true).order('order_index');
    setAllTestsForAssign(tests || []);
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
      return {
        user_id: selectedStudent.id,
        due_date: assignSelectedDate,
        title: tpl?.title || '',
        description: tpl?.description || '',
        task_type: 'manual',
        created_by: session?.user?.id || null
      };
    });
    await supabase.from('assignments').insert(tasks);
    setSelectedTemplates(new Set());
    setShowTaskPicker(false);
    setTaskPickerMode('choose');
    setIsAddingAssignment(false);
    fetchAssignments(selectedStudent.id);
  };

  const handleAddTestTasks = async () => {
    if (!selectedStudent || selectedTestIds.size === 0) return;
    setIsAddingAssignment(true);
    const { data: { session } } = await supabase.auth.getSession();
    const tasks = Array.from(selectedTestIds).map(testId => {
      const test = allTestsForAssign.find(t => t.id === testId);
      return {
        user_id: selectedStudent.id,
        due_date: assignSelectedDate,
        title: test?.title || '',
        task_type: 'test',
        test_id: testId,
        created_by: session?.user?.id || null
      };
    });
    await supabase.from('assignments').insert(tasks);
    setSelectedTestIds(new Set());
    setTestBrowserCourseId(null);
    setShowTaskPicker(false);
    setTaskPickerMode('choose');
    setIsAddingAssignment(false);
    fetchAssignments(selectedStudent.id);
  };

  const handleApproveAssignment = async (id: string) => {
    await supabase.from('assignments').update({ admin_approved: true, is_completed: true, updated_at: new Date().toISOString() }).eq('id', id);
    if (selectedStudent) fetchAssignments(selectedStudent.id);
  };

  const handleDeleteAssignment = async (id: string) => {
    if (!window.confirm('XÃ³a cÃ´ng viá»‡c nÃ y?')) return;
    await supabase.from('assignments').delete().eq('id', id);
    if (selectedStudent) fetchAssignments(selectedStudent.id);
  };

  // Toggle folder selection (select/deselect all tests in folder)
  const toggleFolderSelection = (folderId: string) => {
    const testsInFolder = allTestsForAssign.filter(t => t.folder_id === folderId);
    const allSelected = testsInFolder.every(t => selectedTestIds.has(t.id));
    const newSet = new Set(selectedTestIds);
    testsInFolder.forEach(t => allSelected ? newSet.delete(t.id) : newSet.add(t.id));
    // Also handle sub-folders
    const subFolders = allFoldersForAssign.filter(f => f.parent_id === folderId);
    subFolders.forEach(sf => {
      const subTests = allTestsForAssign.filter(t => t.folder_id === sf.id);
      subTests.forEach(t => allSelected ? newSet.delete(t.id) : newSet.add(t.id));
    });
    setSelectedTestIds(newSet);
  };

  // Calendar days for admin mini calendar
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

  // Group assignments by date for calendar dots
  const assignDateStatus: Record<string, 'blue' | 'green' | 'red'> = {};
  const today = new Date().toISOString().split('T')[0];
  const byDate: Record<string, any[]> = {};
  studentAssignments.forEach(a => { if (!byDate[a.due_date]) byDate[a.due_date] = []; byDate[a.due_date].push(a); });
  Object.entries(byDate).forEach(([date, tasks]) => {
    const allDone = tasks.every(t => t.is_completed);
    assignDateStatus[date] = allDone ? 'green' : date < today ? 'red' : 'blue';
  });
  
  const tasksForSelectedDate = studentAssignments.filter(a => a.due_date === assignSelectedDate);

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

      // ðŸš€ FETCH NHáº¬T KÃ HOáº T Äá»˜NG
      const { data: actData } = await supabase.from('activity_logs').select('*').eq('user_id', student.id).order('created_at', { ascending: false });
      setStudentActivities(actData || []);
      
    } catch (err: any) {
      console.error("Lá»—i táº£i chi tiáº¿t:", err.message);
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

      alert(`âœ… ÄÃ£ táº¡o tÃ i khoáº£n ${newUserRole === 'admin' ? 'Quáº£n trá»‹ viÃªn' : 'Há»c viÃªn'} thÃ nh cÃ´ng!`);
      setShowCreateUserModal(false);
      setNewUserRole('student');
      fetchStudents(); 
    } catch (err: any) {
      alert("âŒ Lá»—i táº¡o tÃ i khoáº£n: " + err.message);
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
      
      alert("âœ… ÄÃ£ cáº­p nháº­t thÃ´ng tin thÃ nh cÃ´ng!");
      
      if (selectedStudent && selectedStudent.id === editingUser.id) {
         setSelectedStudent({ ...selectedStudent, full_name: fullName, role: role, phone: phone });
      }
      
      setEditingUser(null);
      fetchStudents();
    } catch (err: any) {
      alert("âŒ Lá»—i cáº­p nháº­t: " + err.message);
    } finally {
      setIsUpdatingUser(false);
    }
  };

  const handleDeleteUser = async (id: string, name: string) => {
    if (!window.confirm(`Anh cÃ³ cháº¯c cháº¯n muá»‘n xÃ³a VÄ¨NH VIá»„N tÃ i khoáº£n cá»§a ${name || 'há»c viÃªn nÃ y'} khÃ´ng? ToÃ n bá»™ lá»‹ch sá»­ lÃ m bÃ i sáº½ bá»‹ máº¥t!\n\nðŸ’¡ Gá»£i Ã½: NÃªn dÃ¹ng nÃºt "Táº¡m dá»«ng" thay vÃ¬ xÃ³a Ä‘á»ƒ giá»¯ láº¡i lá»‹ch sá»­.`)) return;

    try {
      const { error } = await supabase.rpc('delete_admin_user', { target_user_id: id });
      if (error) throw error;
      alert("ðŸ—‘ï¸ ÄÃ£ xÃ³a tÃ i khoáº£n thÃ nh cÃ´ng!");
      fetchStudents(); 
    } catch (err: any) {
      alert("âŒ Lá»—i xÃ³a tÃ i khoáº£n: " + err.message);
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
        if (error.code === '23505') throw new Error("Há»c viÃªn nÃ y Ä‘Ã£ Ä‘Æ°á»£c gÃ¡n khÃ³a há»c nÃ y rá»“i!");
        throw error;
      }
      
      setStudentEnrollments([data[0], ...studentEnrollments]);
      setShowAssignModal(false);
      alert("âœ… ÄÃ£ gÃ¡n khÃ³a há»c thÃ nh cÃ´ng!");
    } catch (err: any) {
      alert("âŒ Lá»—i: " + err.message);
    } finally {
      setIsAssigning(false);
    }
  };

  const handleRemoveCourse = async (enrollmentId: string) => {
    if (!window.confirm("XÃ³a quyá»n truy cáº­p khÃ³a há»c nÃ y cá»§a há»c viÃªn?")) return;
    try {
      await supabase.from('enrollments').delete().eq('id', enrollmentId);
      setStudentEnrollments(studentEnrollments.filter(e => e.id !== enrollmentId));
    } catch (err: any) {
      alert("Lá»—i khi xÃ³a: " + err.message);
    }
  };

  // ðŸš€ HÃ€M Má»ž BÃ€I THI CHI TIáº¾T Tá»ª ADMIN
  const handleReviewTest = async (h: any) => {
    const testId = h.details?.test_id || h.test_id;
    
    // TÃ¬m test ID tá»« cache nháº¹ (chá»‰ Ä‘á»ƒ láº¥y test_type náº¿u cáº§n)
    let cachedTest = allTests.find(t => String(t.id) === String(testId));
    if (!cachedTest) cachedTest = allTests.find(t => t.title?.trim() === h.test_title?.trim());
    
    // LuÃ´n fetch Ä‘áº§y Ä‘á»§ dá»¯ liá»‡u tá»« DB (bao gá»“m json_config, insert_pdf_url...)
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
        // ðŸ”’ LÆ°u context Ä‘á»ƒ khi quay láº¡i admin sáº½ tá»± má»Ÿ Ä‘Ãºng profile há»c viÃªn + tab lá»‹ch sá»­
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
        alert("Äá» thi nÃ y khÃ´ng cÃ²n tá»“n táº¡i trÃªn há»‡ thá»‘ng.");
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
    const action = isCurrentlyActive ? 'Táº M Dá»ªNG' : 'KÃCH HOáº T Láº I';
    
    if (!window.confirm(`${action} tÃ i khoáº£n cá»§a ${student.full_name || student.email}?${isCurrentlyActive ? '\n\nHá»c viÃªn sáº½ khÃ´ng thá»ƒ Ä‘Äƒng nháº­p cho Ä‘áº¿n khi Ä‘Æ°á»£c kÃ­ch hoáº¡t láº¡i. ToÃ n bá»™ lá»‹ch sá»­ Ä‘Æ°á»£c giá»¯ nguyÃªn.' : ''}`)) return;
    
    try {
      const { error } = await supabase.from('profiles').update({ status: newStatus }).eq('id', student.id);
      if (error) throw error;
      
      alert(`âœ… ÄÃ£ ${action.toLowerCase()} tÃ i khoáº£n thÃ nh cÃ´ng!`);
      
      // Update local state
      setStudents(prev => prev.map(s => s.id === student.id ? { ...s, status: newStatus } : s));
      if (selectedStudent?.id === student.id) {
        setSelectedStudent({ ...selectedStudent, status: newStatus });
      }
    } catch (err: any) {
      alert('âŒ Lá»—i: ' + err.message);
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
  // VIEW CHI TIáº¾T Há»ŒC VIÃŠN
  // ==========================================
  if (selectedStudent) {
    const totalTests = studentHistory.length;
    const avgScore = totalTests > 0 ? (studentHistory.reduce((acc, curr) => acc + (curr.score || 0), 0) / totalTests).toFixed(1) : 0;
    const totalTime = studentHistory.reduce((acc, curr) => acc + Math.round((curr.time_spent || 0) / 60), 0);

    return (
      <>
        <div className="animate-in slide-in-from-right-4 duration-300">
          <button onClick={() => setSelectedStudent(null)} className="mb-6 flex items-center gap-2 text-slate-500 hover:text-[#0a5482] font-bold transition-colors bg-white px-4 py-2 rounded-lg border border-slate-200 shadow-sm w-fit">
            <span>â†</span> Quay láº¡i danh sÃ¡ch
          </button>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative overflow-hidden">
              <span className={`absolute top-0 w-full py-1 text-[10px] font-black uppercase tracking-widest text-white ${selectedStudent.role === 'admin' ? 'bg-red-500' : 'bg-emerald-500'}`}>
                {selectedStudent.role === 'admin' ? 'Quáº£n trá»‹ viÃªn' : 'Há»c viÃªn'}
              </span>
              <div className="w-20 h-20 rounded-full bg-[#0a5482] text-white flex items-center justify-center font-black text-3xl mb-4 shadow-inner mt-4">
                {selectedStudent.full_name ? selectedStudent.full_name.trim().split(/\s+/).pop()?.charAt(0).toUpperCase() : (selectedStudent.email ? selectedStudent.email.charAt(0).toUpperCase() : 'U')}
              </div>
              
              <h2 className="text-xl font-black text-slate-800 mb-1 flex items-center justify-center gap-2">
                 {selectedStudent.full_name || <span className="text-orange-500 italic text-lg">[ChÆ°a cáº­p nháº­t TÃªn]</span>}
                 <button onClick={() => setEditingUser(selectedStudent)} className="text-sm bg-slate-100 hover:bg-[#0a5482] hover:text-white text-slate-400 p-1.5 rounded-md transition-colors" title="Sá»­a thÃ´ng tin">âœï¸</button>
              </h2>
              
              <p className="text-slate-500 font-medium text-[14px] mb-1">{selectedStudent.email}</p>
              {selectedStudent.phone && <p className="text-slate-500 font-bold text-[13px] mb-4 bg-slate-50 px-3 py-1 rounded-full border border-slate-100">ðŸ“ž {selectedStudent.phone}</p>}
              
              <div className="w-full border-t border-slate-100 pt-4 flex justify-between text-[13px] mt-auto">
                <span className="text-slate-500 font-medium">NgÃ y tham gia:</span>
                <span className="font-bold text-slate-700">{formatDate(selectedStudent.created_at).split(' ')[0]}</span>
              </div>
            </div>

            <div className="lg:col-span-2 grid grid-cols-3 gap-4">
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-emerald-500 text-lg">ðŸ“</span> Tá»•ng bÃ i lÃ m</div>
                <div className="text-4xl font-black text-slate-800">{totalTests}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-blue-500 text-lg">ðŸ“Š</span> Äiá»ƒm trung bÃ¬nh</div>
                <div className="text-4xl font-black text-slate-800">{avgScore}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-amber-500 text-lg">â±ï¸</span> Tá»•ng giá» há»c</div>
                <div className="text-4xl font-black text-slate-800">{Math.round(totalTime/60)} <span className="text-base text-slate-400 font-medium">giá»</span></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col min-h-[400px]">
            <div className="bg-slate-50 px-2 pt-2 border-b border-slate-200 flex gap-2 overflow-x-auto custom-scrollbar">
              <button onClick={() => setActiveDetailTab('courses')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'courses' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>ðŸ“š KhÃ³a há»c</button>
              <button onClick={() => setActiveDetailTab('history')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'history' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>ðŸ“Š Lá»‹ch sá»­ Äiá»ƒm</button>
              <button onClick={() => setActiveDetailTab('activity')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'activity' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>ðŸ‘€ Nháº­t kÃ½ Truy cáº­p</button>
              <button onClick={() => setActiveDetailTab('assignments')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'assignments' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>ðŸ“… Lá»‹ch bÃ¡o bÃ i</button>
            </div>
            
            <div className="p-6 flex-1 bg-white">
              {isLoadingDetails ? (
                <div className="py-20 text-center text-slate-400 font-bold">â³ Äang táº£i dá»¯ liá»‡u...</div>
              ) : activeDetailTab === 'courses' ? (
                <div>
                  <div className="flex justify-between items-center mb-6">
                    <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest">Danh sÃ¡ch khÃ³a há»c Ä‘Æ°á»£c phÃ©p truy cáº­p</h3>
                    <button onClick={() => setShowAssignModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white px-5 py-2.5 rounded-lg font-bold text-xs shadow-sm transition">+ GÃN KHÃ“A Há»ŒC</button>
                  </div>
                  
                  {studentEnrollments.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Há»c viÃªn nÃ y chÆ°a Ä‘Æ°á»£c gÃ¡n khÃ³a há»c nÃ o.</div>
                  ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                      {studentEnrollments.map(e => (
                        <div key={e.id} className="border border-slate-200 p-5 rounded-xl bg-slate-50 flex flex-col relative group">
                          <span className="bg-blue-100 text-blue-700 font-black uppercase text-[10px] px-2 py-1 rounded w-fit mb-3">{e.courses?.type || 'KhÃ³a há»c'}</span>
                          <h4 className="font-bold text-slate-800 text-[15px] mb-2">{e.courses?.title || 'KhÃ³a há»c Ä‘Ã£ xÃ³a'}</h4>
                          <p className="text-[12px] text-slate-500 font-medium">GÃ¡n ngÃ y: {formatDate(e.enrolled_at).split(' ')[0]}</p>
                          <button onClick={() => handleRemoveCourse(e.id)} className="absolute top-4 right-4 text-red-400 hover:text-red-600 font-bold text-xs opacity-0 group-hover:opacity-100 transition-opacity">Gá»¡ bá» âœ–</button>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

              ) : activeDetailTab === 'history' ? (
                <div>
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-6">Lá»‹ch sá»­ ná»™p bÃ i ({studentHistory.length} bÃ i)</h3>
                  {studentHistory.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Há»c viÃªn nÃ y chÆ°a ná»™p bÃ i thi nÃ o.</div>
                  ) : (
                    <div className="border border-slate-200 rounded-xl overflow-hidden">
                      <table className="w-full text-left border-collapse">
                        <thead className="bg-[#f8fafc] text-[11px] font-black uppercase tracking-wider text-slate-500 border-b border-slate-200">
                          <tr>
                            <th className="px-5 py-3">TÃªn bÃ i thi</th>
                            <th className="px-5 py-3 text-center">Dáº¡ng</th>
                            <th className="px-5 py-3 text-center">Äiá»ƒm</th>
                            <th className="px-5 py-3 text-center">NgÃ y ná»™p</th>
                            <th className="px-5 py-3 text-right">Thao tÃ¡c</th>
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
                                    ðŸ‘ï¸ Xem bÃ i lÃ m
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
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-8">Nháº­t kÃ½ truy cáº­p & hÃ nh vi</h3>
                  {studentActivities.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">ChÆ°a cÃ³ hoáº¡t Ä‘á»™ng nÃ o Ä‘Æ°á»£c ghi nháº­n.</div>
                  ) : (
                    <div className="space-y-6 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-200 before:to-transparent">
                      {studentActivities.map((act) => (
                         <div key={act.id} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div className="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#0a5482] text-white font-bold shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow-sm z-10 text-[14px]">
                               {act.action_type === 'login' ? 'ðŸ”‘' : act.action_type === 'finish_test' ? 'ðŸ“' : act.action_type === 'call_tutor' ? 'ðŸ“ž' : 'ðŸ“–'}
                            </div>
                            <div className="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-[#2bd6eb] transition-colors">
                               <div className="flex justify-between items-start mb-2">
                                  <h4 className="font-black text-[#0a5482] text-[13px] md:text-[15px] uppercase tracking-tight">
                                     {act.action_type === 'login' && 'ÄÄƒng nháº­p há»‡ thá»‘ng'}
                                     {act.action_type === 'finish_test' && 'Ná»™p bÃ i kiá»ƒm tra'}
                                     {act.action_type === 'call_tutor' && 'Há»i Ä‘Ã¡p AI / Voice'}
                                     {act.action_type === 'finish_lecture' && 'HoÃ n thÃ nh bÃ i giáº£ng'}
                                  </h4>
                                  <span className="text-[11px] font-bold text-slate-400 whitespace-nowrap ml-2 bg-slate-50 px-2 py-1 rounded border border-slate-100">{formatDate(act.created_at)}</span>
                               </div>
                               <p className="text-[13px] text-slate-600 font-medium leading-relaxed">
                                  {act.action_type === 'login' && 'Há»c sinh Ä‘Äƒng nháº­p thÃ nh cÃ´ng vÃ o LMS.'}
                                  {act.action_type === 'finish_test' && `ÄÃ£ ná»™p bÃ i: "${act.details?.test_title || 'IELTS'}" vá»›i sá»‘ Ä‘iá»ƒm: ${act.details?.score || 0}`}
                                  {act.action_type === 'call_tutor' && `Thá»i lÆ°á»£ng Ä‘Ã m thoáº¡i / há»i AI: ${act.details?.duration || 0} giÃ¢y.`}
                                  {act.action_type === 'finish_lecture' && `Há»c xong bÃ i giáº£ng: "${act.details?.lecture_title || 'Lecture'}"`}
                               </p>
                            </div>
                         </div>
                      ))}
                    </div>
                  )}
                </div>
              ) : activeDetailTab === 'assignments' ? (
                <div className="space-y-5">
                  {/* ========== MINI CALENDAR ========== */}
                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                    <div className="flex items-center justify-between px-5 py-3 border-b border-slate-100">
                      <button onClick={() => setAssignCalMonth(new Date(assignCalMonth.getFullYear(), assignCalMonth.getMonth() - 1))} className="w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500">â†</button>
                      <h4 className="font-black text-sm text-[#0a5482] capitalize">{assignCalMonth.toLocaleDateString('vi-VN', { month: 'long', year: 'numeric' })}</h4>
                      <button onClick={() => setAssignCalMonth(new Date(assignCalMonth.getFullYear(), assignCalMonth.getMonth() + 1))} className="w-8 h-8 rounded-full hover:bg-slate-100 flex items-center justify-center text-slate-500">â†’</button>
                    </div>
                    <div className="grid grid-cols-7 px-3 pt-2 pb-1">
                      {['CN','T2','T3','T4','T5','T6','T7'].map(d => <div key={d} className="text-center text-[10px] font-bold text-slate-400 uppercase">{d}</div>)}
                    </div>
                    <div className="grid grid-cols-7 px-3 pb-3 gap-0.5">
                      {assignCalDays.map((day, i) => {
                        const status = assignDateStatus[day.date];
                        const isSelected = assignSelectedDate === day.date;
                        return (
                          <button key={i} onClick={() => setAssignSelectedDate(day.date)}
                            className={`relative aspect-square rounded-lg flex flex-col items-center justify-center text-[12px] font-semibold transition-all
                              ${!day.isCurrentMonth ? 'text-slate-300' : 'text-slate-700'}
                              ${day.isToday ? 'ring-1 ring-[#0ea5e9]' : ''}
                              ${isSelected ? 'bg-[#0a5482] text-white scale-105 shadow' : 'hover:bg-slate-50'}
                            `}>
                            <span>{day.day}</span>
                            {status && !isSelected && <span className={`absolute bottom-0.5 w-1.5 h-1.5 rounded-full ${status === 'green' ? 'bg-emerald-500' : status === 'red' ? 'bg-red-500' : 'bg-[#0ea5e9]'}`}></span>}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* ========== TASKS FOR SELECTED DATE ========== */}
                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                    <div className="px-5 py-3 border-b border-slate-100 bg-slate-50 flex items-center justify-between">
                      <h4 className="font-black text-sm text-slate-700">
                        ðŸ“‹ {new Date(assignSelectedDate + 'T00:00:00').toLocaleDateString('vi-VN', { weekday: 'long', day: 'numeric', month: 'long' })}
                        <span className="text-slate-400 font-normal ml-2">({tasksForSelectedDate.length} viá»‡c)</span>
                      </h4>
                      <button onClick={() => { setShowTaskPicker(true); setTaskPickerMode('choose'); }} className="bg-[#0a5482] text-white px-4 py-1.5 rounded-lg text-[12px] font-bold hover:bg-[#083d5e] transition-all">+ Giao viá»‡c</button>
                    </div>
                    {tasksForSelectedDate.length === 0 ? (
                      <div className="p-8 text-center text-slate-400 text-[13px]">ChÆ°a giao viá»‡c cho ngÃ y nÃ y.</div>
                    ) : (
                      <div className="divide-y divide-slate-100">
                        {tasksForSelectedDate.map((a: any) => (
                          <div key={a.id} className="px-5 py-3 flex items-center gap-4 hover:bg-slate-50">
                            <div className={`w-3 h-3 rounded-full shrink-0 ${a.is_completed ? 'bg-emerald-500' : a.student_completed ? 'bg-amber-400' : a.due_date < today ? 'bg-red-500' : 'bg-[#0ea5e9]'}`}></div>
                            <div className="flex-1 min-w-0">
                              <p className="text-[13px] font-bold text-slate-800 truncate">{a.title}</p>
                              <p className="text-[11px] text-slate-400">{a.task_type === 'test' ? 'ðŸ“ BÃ i táº­p' : 'ðŸ“‹ Thá»§ cÃ´ng'}{a.description ? ` Â· ${a.description}` : ''}</p>
                            </div>
                            <div className="flex items-center gap-2 shrink-0">
                              {a.is_completed && <span className="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">âœ… HoÃ n thÃ nh</span>}
                              {a.student_completed && !a.is_completed && a.task_type === 'manual' && (
                                <button onClick={() => handleApproveAssignment(a.id)} className="text-[10px] font-bold bg-amber-100 text-amber-700 px-3 py-1 rounded-full hover:bg-amber-200 transition-colors">â³ Duyá»‡t</button>
                              )}
                              {!a.is_completed && !a.student_completed && <span className="text-[10px] font-bold text-slate-400">Chá»</span>}
                              <button onClick={() => handleDeleteAssignment(a.id)} className="text-slate-300 hover:text-red-500 transition-colors text-[14px]">ðŸ—‘</button>
                            </div>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>

                  {/* ========== TASK PICKER MODAL ========== */}
                  {showTaskPicker && (
                    <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4" onClick={() => { setShowTaskPicker(false); setTaskPickerMode('choose'); }}>
                      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[80vh] flex flex-col" onClick={e => e.stopPropagation()}>
                        {/* Header */}
                        <div className="px-6 py-4 border-b border-slate-200 flex items-center justify-between shrink-0">
                          <div className="flex items-center gap-3">
                            {taskPickerMode !== 'choose' && (
                              <button onClick={() => { setTaskPickerMode(testBrowserCourseId ? 'test' : 'choose'); setTestBrowserCourseId(null); }} className="text-slate-400 hover:text-slate-700 text-lg">â†</button>
                            )}
                            <h3 className="font-black text-[#0a5482]">
                              {taskPickerMode === 'choose' ? '+ Giao viá»‡c' : taskPickerMode === 'manual' ? 'ðŸ“‹ Chá»n viá»‡c thá»§ cÃ´ng' : testBrowserCourseId ? 'ðŸ“ Chá»n bÃ i táº­p' : 'ðŸ“š Chá»n khÃ³a há»c'}
                            </h3>
                          </div>
                          <button onClick={() => { setShowTaskPicker(false); setTaskPickerMode('choose'); }} className="text-slate-400 hover:text-red-500 text-xl font-bold">âœ•</button>
                        </div>

                        {/* Body */}
                        <div className="flex-1 overflow-y-auto p-6">
                          {/* MODE: CHOOSE */}
                          {taskPickerMode === 'choose' && (
                            <div className="space-y-3">
                              <p className="text-[13px] text-slate-500 mb-4">Giao cho ngÃ y <b>{new Date(assignSelectedDate + 'T00:00:00').toLocaleDateString('vi-VN')}</b></p>
                              <button onClick={() => setTaskPickerMode('manual')} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-4 text-left">
                                <span className="text-3xl">ðŸ“‹</span>
                                <div><p className="font-bold text-slate-800 text-[14px]">Viá»‡c thá»§ cÃ´ng</p><p className="text-[12px] text-slate-400">Chá»n tá»« danh má»¥c Ä‘Ã£ táº¡o sáºµn</p></div>
                              </button>
                              <button onClick={() => setTaskPickerMode('test')} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-4 text-left">
                                <span className="text-3xl">ðŸ“</span>
                                <div><p className="font-bold text-slate-800 text-[14px]">BÃ i táº­p trong há»‡ thá»‘ng</p><p className="text-[12px] text-slate-400">Duyá»‡t khÃ³a há»c â†’ folder â†’ chá»n Ä‘á»</p></div>
                              </button>
                            </div>
                          )}

                          {/* MODE: MANUAL TEMPLATES */}
                          {taskPickerMode === 'manual' && (
                            <div className="space-y-2">
                              {manualTemplates.length === 0 ? (
                                <div className="p-8 text-center text-slate-400 text-[13px]">
                                  <p className="text-4xl mb-3">ðŸ“­</p>
                                  <p className="font-bold">ChÆ°a cÃ³ danh má»¥c viá»‡c thá»§ cÃ´ng</p>
                                  <p className="text-[12px] mt-1">VÃ o KhÃ³a há»c & Lá»›p â†’ tab Danh má»¥c viá»‡c thá»§ cÃ´ng Ä‘á»ƒ táº¡o.</p>
                                </div>
                              ) : manualTemplates.map(tpl => (
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
                          )}

                          {/* MODE: TEST â€” Course List */}
                          {taskPickerMode === 'test' && !testBrowserCourseId && (
                            <div className="space-y-2">
                              {studentCourses.length === 0 ? (
                                <div className="p-8 text-center text-slate-400 text-[13px]">Há»c sinh chÆ°a Ä‘Æ°á»£c gÃ¡n khÃ³a há»c nÃ o.</div>
                              ) : studentCourses.map(c => (
                                <button key={c.id} onClick={() => setTestBrowserCourseId(c.id)} className="w-full p-4 bg-slate-50 border border-slate-200 rounded-xl hover:bg-sky-50 hover:border-[#0ea5e9] transition-all flex items-center gap-3 text-left">
                                  <span className="text-xl">ðŸ“š</span>
                                  <p className="font-bold text-slate-800 text-[13px]">{c.title}</p>
                                  <span className="ml-auto text-slate-400">â†’</span>
                                </button>
                              ))}
                            </div>
                          )}

                          {/* MODE: TEST â€” Folder/Test Browser */}
                          {taskPickerMode === 'test' && testBrowserCourseId && (() => {
                            const courseFolders = allFoldersForAssign.filter(f => f.course_id === testBrowserCourseId && !f.parent_id);
                            const courseTests = allTestsForAssign.filter(t => t.course_id === testBrowserCourseId);
                            const rootTests = courseTests.filter(t => !t.folder_id);
                            return (
                              <div className="space-y-1">
                                {courseFolders.map(folder => {
                                  const folderTests = courseTests.filter(t => t.folder_id === folder.id);
                                  const subFolders = allFoldersForAssign.filter(f => f.parent_id === folder.id);
                                  const allFolderTestIds = [...folderTests.map(t => t.id), ...subFolders.flatMap(sf => courseTests.filter(t => t.folder_id === sf.id).map(t => t.id))];
                                  const allChecked = allFolderTestIds.length > 0 && allFolderTestIds.every(id => selectedTestIds.has(id));
                                  const someChecked = allFolderTestIds.some(id => selectedTestIds.has(id));
                                  return (
                                    <div key={folder.id}>
                                      <label className={`flex items-center gap-3 p-2.5 rounded-xl cursor-pointer transition-all ${someChecked ? 'bg-sky-50' : 'hover:bg-slate-50'}`}>
                                        <input type="checkbox" checked={allChecked} ref={el => { if (el) el.indeterminate = someChecked && !allChecked; }} onChange={() => toggleFolderSelection(folder.id)} className="w-4 h-4 rounded accent-[#0a5482]" />
                                        <span className="text-[14px]">ðŸ“</span>
                                        <p className="font-bold text-[13px] text-slate-700">{folder.title}</p>
                                        <span className="ml-auto text-[11px] text-slate-400">{allFolderTestIds.length} Ä‘á»</span>
                                      </label>
                                      <div className="ml-8 space-y-0.5">
                                        {subFolders.map(sf => {
                                          const sfTests = courseTests.filter(t => t.folder_id === sf.id);
                                          return (
                                            <div key={sf.id}>
                                              <label className="flex items-center gap-3 p-2 rounded-lg cursor-pointer hover:bg-slate-50">
                                                <input type="checkbox" checked={sfTests.length > 0 && sfTests.every(t => selectedTestIds.has(t.id))} onChange={() => toggleFolderSelection(sf.id)} className="w-3.5 h-3.5 rounded accent-[#0a5482]" />
                                                <span className="text-[13px]">ðŸ“‚</span>
                                                <p className="text-[12px] font-semibold text-slate-600">{sf.title}</p>
                                              </label>
                                              <div className="ml-7 space-y-0.5">
                                                {sfTests.map(t => (
                                                  <label key={t.id} className="flex items-center gap-3 p-1.5 rounded-lg cursor-pointer hover:bg-slate-50">
                                                    <input type="checkbox" checked={selectedTestIds.has(t.id)} onChange={() => { const s = new Set(selectedTestIds); s.has(t.id) ? s.delete(t.id) : s.add(t.id); setSelectedTestIds(s); }} className="w-3.5 h-3.5 rounded accent-[#0a5482]" />
                                                    <p className="text-[12px] text-slate-600 truncate">{t.title}</p>
                                                  </label>
                                                ))}
                                              </div>
                                            </div>
                                          );
                                        })}
                                        {folderTests.map(t => (
                                          <label key={t.id} className="flex items-center gap-3 p-2 rounded-lg cursor-pointer hover:bg-slate-50">
                                            <input type="checkbox" checked={selectedTestIds.has(t.id)} onChange={() => { const s = new Set(selectedTestIds); s.has(t.id) ? s.delete(t.id) : s.add(t.id); setSelectedTestIds(s); }} className="w-3.5 h-3.5 rounded accent-[#0a5482]" />
                                            <p className="text-[12px] text-slate-600 truncate">{t.title}</p>
                                          </label>
                                        ))}
                                      </div>
                                    </div>
                                  );
                                })}
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

                        {/* Footer */}
                        {taskPickerMode === 'manual' && selectedTemplates.size > 0 && (
                          <div className="px-6 py-3 border-t border-slate-200 shrink-0">
                            <button onClick={handleAddManualTasks} disabled={isAddingAssignment} className="w-full bg-[#0a5482] text-white py-2.5 rounded-xl text-[13px] font-bold hover:bg-[#083d5e] disabled:opacity-50 transition-all">
                              {isAddingAssignment ? 'â³ Äang giao...' : `Giao ${selectedTemplates.size} viá»‡c thá»§ cÃ´ng`}
                            </button>
                          </div>
                        )}
                        {taskPickerMode === 'test' && testBrowserCourseId && selectedTestIds.size > 0 && (
                          <div className="px-6 py-3 border-t border-slate-200 shrink-0">
                            <button onClick={handleAddTestTasks} disabled={isAddingAssignment} className="w-full bg-[#0a5482] text-white py-2.5 rounded-xl text-[13px] font-bold hover:bg-[#083d5e] disabled:opacity-50 transition-all">
                              {isAddingAssignment ? 'â³ Äang giao...' : `Giao ${selectedTestIds.size} bÃ i táº­p`}
                            </button>
                          </div>
                        )}
                      </div>
                    </div>
                  )}
                </div>
              ) : null}


            </div>
          </div>
        </div>

        {/* MODAL EDIT TÃ€I KHOáº¢N KHI ÄANG XEM CHI TIáº¾T */}
        {editingUser && (
          <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
            <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sá»­a ThÃ´ng Tin</h2>
              
              <div className="space-y-4 mb-8">
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Há» vÃ  tÃªn</label>
                  <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Tráº§n Huy TÃ´n" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>
                
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Sá»‘ Ä‘iá»‡n thoáº¡i</label>
                  <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email Ä‘Äƒng nháº­p</label>
                  <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                  <p className="text-[10px] text-slate-400 mt-1 italic">* KhÃ´ng thá»ƒ sá»­a email tá»« Admin Panel.</p>
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">PhÃ¢n quyá»n</label>
                  <div className="grid grid-cols-2 gap-3 mt-2">
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                      ðŸ‘¨â€ðŸŽ“ Há»c viÃªn
                    </label>
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                      ðŸ‘‘ Quáº£n trá»‹
                    </label>
                  </div>
                </div>
              </div>

              <div className="flex gap-4">
                <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Há»§y</button>
                <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                  {isUpdatingUser ? 'ÄANG LÆ¯U...' : 'LÆ¯U THAY Äá»”I'}
                </button>
              </div>
            </form>
          </div>
        )}

        {/* MODAL GÃN KHÃ“A Há»ŒC */}
        {showAssignModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <form onSubmit={handleAssignCourse} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4">GÃ¡n KhÃ³a Há»c</h2>
              <div className="space-y-4 mb-8">
                <label className="text-[13px] font-bold text-slate-500 uppercase">Chá»n khÃ³a há»c</label>
                <select name="courseId" required defaultValue="" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] font-medium bg-slate-50">
                  <option value="" disabled>-- Chá»n khÃ³a há»c --</option>
                  {availableCourses.length === 0 ? (
                     <option value="" disabled>Há»c viÃªn Ä‘Ã£ gÃ¡n táº¥t cáº£ khÃ³a há»c</option>
                  ) : (
                     availableCourses.map(c => <option key={c.id} value={c.id}>[{c.type}] {c.title}</option>)
                  )}
                </select>
              </div>
              <div className="flex gap-4">
                <button type="button" onClick={() => setShowAssignModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Há»§y</button>
                <button type="submit" disabled={isAssigning} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition disabled:opacity-50">GÃN NGAY</button>
              </div>
            </form>
          </div>
        )}
      </>
    );
  }

  // ==========================================
  // VIEW DANH SÃCH Há»ŒC VIÃŠN Tá»”NG
  // ==========================================
  return (
    <>
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden animate-in fade-in duration-300 flex flex-col h-[calc(100vh-120px)]">
        <div className="bg-slate-50 px-6 py-5 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-4 shrink-0">
          <div className="flex items-center gap-4">
            <h2 className="font-black text-xl text-[#0a5482]">Quáº£n lÃ½ TÃ i Khoáº£n</h2>
            <div className="flex bg-white border border-slate-200 rounded-lg overflow-hidden shadow-sm">
              <button onClick={() => { setStatusFilter('active'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors ${statusFilter === 'active' ? 'bg-emerald-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Äang há»c ({students.filter(s => s.status !== 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('inactive'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'inactive' ? 'bg-slate-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Táº¡m dá»«ng ({students.filter(s => s.status === 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('all'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'all' ? 'bg-[#0a5482] text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Táº¥t cáº£
              </button>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <div className="relative w-full sm:w-72">
              <input 
                type="text" 
                placeholder="TÃ¬m kiáº¿m theo email, tÃªn, SÄT..." 
                defaultValue={searchQuery}
                onChange={(e) => {
                  clearTimeout(studentSearchTimer);
                  studentSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350);
                }} 
                className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 font-medium text-[13px] outline-none focus:border-[#0a5482] focus:ring-1 focus:ring-[#0a5482] bg-white transition-all shadow-sm" 
              />
              <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">ðŸ”</span>
            </div>
            <button onClick={() => setShowCreateUserModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-6 py-2.5 rounded-xl transition shadow-md text-sm whitespace-nowrap">+ Táº¡o TÃ i Khoáº£n</button>
          </div>
        </div>

        <div className="flex-1 flex flex-col overflow-hidden">
          {isLoading ? (
            <div className="p-16 text-center text-slate-500 font-bold text-lg flex items-center justify-center gap-3"><span className="animate-spin text-2xl">â³</span> Äang táº£i dá»¯ liá»‡u...</div>
          ) : filteredStudents.length === 0 ? (
            <div className="p-16 text-center text-slate-400 font-medium text-lg border-t border-slate-100">KhÃ´ng tÃ¬m tháº¥y tÃ i khoáº£n nÃ o.</div>
          ) : (
            <>
              <div className="flex-1 overflow-y-auto custom-scrollbar">
                <table className="w-full text-left border-collapse min-w-[900px]">
                  <thead className="sticky top-0 bg-white shadow-[0_1px_2px_rgba(0,0,0,0.05)] z-10">
                    <tr className="text-[11px] font-black uppercase tracking-wider text-slate-400">
                      <th className="px-6 py-4 text-center w-16">STT</th>
                      <th className="px-6 py-4">TÃ i Khoáº£n (Email)</th>
                      <th className="px-6 py-4">Sá»‘ Äiá»‡n Thoáº¡i</th>
                      <th className="px-6 py-4">Há» vÃ  TÃªn</th>
                      <th className="px-6 py-4">Tráº¡ng thÃ¡i</th>
                      <th className="px-6 py-4 text-center">NgÃ y táº¡o</th>
                      <th className="px-6 py-4 text-right">HÃ nh Ä‘á»™ng</th>
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
                             {student.full_name || '[ChÆ°a cáº­p nháº­t]'}
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex flex-col gap-1">
                            <span className={`px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-wider border w-fit ${student.role === 'admin' ? 'bg-red-50 text-red-600 border-red-200' : 'bg-emerald-50 text-emerald-600 border-emerald-200'}`}>{student.role || 'Student'}</span>
                            {student.status === 'inactive' && <span className="px-2 py-0.5 rounded text-[9px] font-bold uppercase bg-slate-100 text-slate-500 border border-slate-200 w-fit">â¸ Táº¡m dá»«ng</span>}
                          </div>
                        </td>
                        <td className="px-6 py-4 text-slate-600 font-medium text-[13px] text-center">
                          {formatDate(student.created_at).split(' ')[0]}
                        </td>
                        <td className="px-6 py-4 text-right flex items-center justify-end gap-1.5">
                          <button onClick={() => handleSelectStudent(student)} className="text-[#0a5482] font-bold text-[12px] bg-white hover:bg-[#0a5482] hover:text-white px-4 py-2 rounded-lg transition-all border border-slate-200 shadow-sm uppercase tracking-wider">
                            Cáº¥u hÃ¬nh & Tiáº¿n Ä‘á»™
                          </button>
                          
                          <button onClick={() => setEditingUser(student)} className="text-blue-500 hover:text-blue-600 hover:bg-blue-50 p-2 rounded-lg transition-colors border border-transparent hover:border-blue-200" title="Sá»­a thÃ´ng tin">
                            âœï¸
                          </button>

                          <button onClick={() => handleToggleStatus(student)} className={`p-2 rounded-lg transition-colors border border-transparent ${student.status === 'inactive' ? 'text-emerald-500 hover:text-emerald-600 hover:bg-emerald-50 hover:border-emerald-200' : 'text-amber-500 hover:text-amber-600 hover:bg-amber-50 hover:border-amber-200'}`} title={student.status === 'inactive' ? 'KÃ­ch hoáº¡t láº¡i' : 'Táº¡m dá»«ng'}>
                            {student.status === 'inactive' ? 'â–¶ï¸' : 'â¸ï¸'}
                          </button>
    
                          <button onClick={() => handleDeleteUser(student.id, student.full_name)} className="text-slate-400 hover:text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors border border-transparent hover:border-red-200" title="XÃ³a vÄ©nh viá»…n">
                            ðŸ—‘ï¸
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
                      â† Trang trÆ°á»›c
                   </button>
                   <span className="text-[13px] font-black text-slate-500">
                      Trang {currentPage} <span className="font-medium text-slate-400">/ {totalPages}</span>
                   </span>
                   <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => p + 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                      Trang sau â†’
                   </button>
                </div>
              )}
            </>
          )}
        </div>
      </div>

      {/* MODAL Táº O TÃ€I KHOáº¢N Má»šI */}
      {showCreateUserModal && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleCreateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Táº¡o TÃ i Khoáº£n Má»›i</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Há» vÃ  tÃªn</label>
                <input name="fullName" required type="text" defaultValue="" autoComplete="off" placeholder="Nguyá»…n VÄƒn A" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Sá»‘ Ä‘iá»‡n thoáº¡i</label>
                <input name="phone" type="text" defaultValue="" autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email Ä‘Äƒng nháº­p</label>
                <input name="email" required type="email" defaultValue="" autoComplete="off" placeholder="email@tonyenglish.vn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Máº­t kháº©u</label>
                <input name="password" required type="password" minLength={6} defaultValue="123456" autoComplete="off" placeholder="Ãt nháº¥t 6 kÃ½ tá»±" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold text-[#0a5482]" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">PhÃ¢n quyá»n</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'student' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" checked={newUserRole === 'student'} onChange={() => setNewUserRole('student')} className="hidden" />
                    ðŸ‘¨â€ðŸŽ“ Há»c viÃªn
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" checked={newUserRole === 'admin'} onChange={() => setNewUserRole('admin')} className="hidden" />
                    ðŸ‘‘ Quáº£n trá»‹ viÃªn
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setShowCreateUserModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Há»§y</button>
              <button type="submit" disabled={isCreatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isCreatingUser ? 'ÄANG Táº O...' : 'Táº O TÃ€I KHOáº¢N'}
              </button>
            </div>
          </form>
        </div>
      )}
      
      {/* MODAL EDIT TÃ€I KHOáº¢N NGOÃ€I DANH SÃCH Tá»”NG */}
      {editingUser && !selectedStudent && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sá»­a ThÃ´ng Tin</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Há» vÃ  tÃªn</label>
                <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Tráº§n Huy TÃ´n" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Sá»‘ Ä‘iá»‡n thoáº¡i</label>
                <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email Ä‘Äƒng nháº­p</label>
                <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                <p className="text-[10px] text-slate-400 mt-1 italic">* KhÃ´ng thá»ƒ sá»­a email tá»« Admin Panel.</p>
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">PhÃ¢n quyá»n</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                    ðŸ‘¨â€ðŸŽ“ Há»c viÃªn
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                    ðŸ‘‘ Quáº£n trá»‹
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Há»§y</button>
              <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isUpdatingUser ? 'ÄANG LÆ¯U...' : 'LÆ¯U THAY Äá»”I'}
              </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
}