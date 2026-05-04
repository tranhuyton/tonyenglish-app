import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import TestEditorModal from './TestEditorModal';
import CaseStudyEditorModal from './CaseStudyEditorModal'; 
import StudentManagement from './StudentManagement'; 
import LectureEditorModal from './LectureEditorModal';
import './tailwind.css';

let adminSearchTimer: any;

export default function AdminPanel({ onNavigate }: { onNavigate?: (view: string) => void }) {
  const [activeTab, setActiveTab] = useState('courses'); 
  const [showCreateDropdown, setShowCreateDropdown] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  // --- DATABASE STATES ---
  const [courses, setCourses] = useState<any[]>([]);
  const [folders, setFolders] = useState<any[]>([]);
  const [allFolders, setAllFolders] = useState<any[]>([]); 
  const [libraryTests, setLibraryTests] = useState<any[]>([]); 
  const [assignedTests, setAssignedTests] = useState<any[]>([]); 
  const [selectedCourse, setSelectedCourse] = useState<any>(null);
  const [isLoadingCourses, setIsLoadingCourses] = useState(true);

  // --- LECTURE & CLASS SYSTEM STATES ---
  const [globalLectures, setGlobalLectures] = useState<any[]>([]); 
  const [courseViewMode, setCourseViewMode] = useState<'tests' | 'modules' | 'classes'>('classes'); 
  const [filterLectureCourse, setFilterLectureCourse] = useState('all'); 
  
  const [lectureModules, setLectureModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  
  const [classes, setClasses] = useState<any[]>([]);
  const [selectedClass, setSelectedClass] = useState<any>(null);
  const [classModules, setClassModules] = useState<any[]>([]); 
  
  const [courseStudentsList, setCourseStudentsList] = useState<any[]>([]); 
  const [classStudentsList, setClassStudentsList] = useState<any[]>([]); 
  const [showAssignStudentModal, setShowAssignStudentModal] = useState(false); 
  
  // Modals
  const [showModuleModal, setShowModuleModal] = useState(false);
  const [showClassModal, setShowClassModal] = useState(false);
  const [showAssignClassModuleModal, setShowAssignClassModuleModal] = useState(false);
  const [editingLecture, setEditingLecture] = useState<any>(null);
  const [showAssignLectureModal, setShowAssignLectureModal] = useState<{show: boolean, moduleId: string | null}>({show: false, moduleId: null});

  // --- UI STATES & EDITING STATES ---
  const [currentFolderId, setCurrentFolderId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterCourse, setFilterCourse] = useState('all');
  const [selectedTests, setSelectedTests] = useState<string[]>([]);
  const [editingTest, setEditingTest] = useState<any>(null);
  const [showCreateCourseModal, setShowCreateCourseModal] = useState(false);
  const [showFolderModal, setShowFolderModal] = useState(false);
  const [showAssignModal, setShowAssignModal] = useState(false);
  
  // States lưu giữ việc đang Edit nội tuyến
  const [editingCourseId, setEditingCourseId] = useState<string | null>(null);
  const [editingClassId, setEditingClassId] = useState<string | null>(null);
  const [editingModuleId, setEditingModuleId] = useState<string | null>(null);
  const [editingFolderId, setEditingFolderId] = useState<string | null>(null);

  useEffect(() => {
    fetchCourses();
    fetchLibraryTests();
    fetchAllFolders(); 
    fetchGlobalLectures();
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) setShowCreateDropdown(false);
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const formatDateTime = (iso: string) => {
    if (!iso) return '';
    const d = new Date(iso);
    return `${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')} - ${d.getDate().toString().padStart(2, '0')}/${(d.getMonth()+1).toString().padStart(2, '0')}/${d.getFullYear()}`;
  }

  const fetchCourses = async () => {
    setIsLoadingCourses(true); 
    const { data } = await supabase.from('courses').select('*').order('order_index', { ascending: true }).order('created_at', { ascending: false });
    setCourses(data || []);
    setIsLoadingCourses(false); 
  };

  const fetchLibraryTests = async () => {
    const { data } = await supabase.from('tests').select('*').order('order_index', { ascending: true }).order('created_at', { ascending: false });
    setLibraryTests(data || []);
  };

  const fetchAllFolders = async () => {
    const { data } = await supabase.from('folders').select('*').order('display_order', { ascending: true });
    setAllFolders(data || []);
  };

  const fetchGlobalLectures = async () => {
    const { data } = await supabase.from('lectures').select('*, courses(title)').order('order_index', { ascending: true }).order('created_at', { ascending: false });
    setGlobalLectures(data || []);
  };

  const fetchCourseDetailsData = async (courseId: string) => {
    const { data: mods } = await supabase.from('lecture_modules').select('*').eq('course_id', courseId).order('order_index', { ascending: true });
    setLectureModules(mods || []);
    if (mods && mods.length > 0) {
      const { data: lecs } = await supabase.from('lectures').select('*').in('module_id', mods.map(m => m.id)).order('order_index', { ascending: true });
      setLectures(lecs || []);
    } else setLectures([]);

    const { data: cls } = await supabase.from('classes').select('*').eq('course_id', courseId).order('created_at', { ascending: false });
    setClasses(cls || []);
    
    const { data: flds } = await supabase.from('folders').select('*').eq('course_id', courseId).order('display_order', { ascending: true });
    setFolders(flds || []);
    const { data: ast } = await supabase.from('tests').select('*').eq('course_id', courseId).order('order_index', { ascending: true });
    setAssignedTests(ast || []);

    const { data: enrolls } = await supabase.from('enrollments').select('user_id').eq('course_id', courseId);
    if (enrolls && enrolls.length > 0) {
       const userIds = enrolls.map(e => e.user_id);
       const { data: profiles } = await supabase.from('profiles').select('id, full_name, email').in('id', userIds);
       if (profiles) setCourseStudentsList(profiles.map(p => ({ user_id: p.id, full_name: p.full_name, email: p.email })));
    } else setCourseStudentsList([]);
  };

  const fetchClassDetails = async (classId: string) => {
    const { data: modData } = await supabase.from('class_modules').select('module_id').eq('class_id', classId);
    if (modData) setClassModules(modData.map(d => d.module_id));

    const { data: stuData } = await supabase.from('class_students').select('user_id').eq('class_id', classId);
    if (stuData && stuData.length > 0) {
       const userIds = stuData.map(e => e.user_id);
       const { data: profiles } = await supabase.from('profiles').select('id, full_name, email').in('id', userIds);
       if (profiles) setClassStudentsList(profiles.map(p => ({ user_id: p.id, full_name: p.full_name, email: p.email })));
    } else setClassStudentsList([]);
  };

  // --- ORDERING HANDLERS ---
  const handleUpdateCourseOrder = async (id: string, newOrder: number) => {
    await supabase.from('courses').update({ order_index: newOrder }).eq('id', id); fetchCourses();
  };
  const handleUpdateModuleOrder = async (id: string, newOrder: number) => {
    await supabase.from('lecture_modules').update({ order_index: newOrder }).eq('id', id); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };
  const handleUpdateLectureOrder = async (id: string, newOrder: number) => {
    await supabase.from('lectures').update({ order_index: newOrder }).eq('id', id); fetchGlobalLectures(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };
  const handleUpdateTestOrder = async (id: string, newOrder: number) => {
    await supabase.from('tests').update({ order_index: newOrder }).eq('id', id); fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };
  // CHỨC NĂNG MỚI: CẬP NHẬT THỨ TỰ THƯ MỤC
  const handleUpdateFolderOrder = async (id: string, newOrder: number) => {
    await supabase.from('folders').update({ display_order: newOrder }).eq('id', id); fetchAllFolders(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };
  const handleToggleLectureStatus = async (id: string, currentStatus: boolean) => {
    await supabase.from('lectures').update({ is_published: !currentStatus }).eq('id', id); fetchGlobalLectures(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  // --- EVENT HANDLERS HỌC SINH ---
  const handleAssignStudentToClass = async (userId: string) => {
     if (!selectedClass) return;
     await supabase.from('class_students').insert([{ class_id: selectedClass.id, user_id: userId }]); fetchClassDetails(selectedClass.id);
  };
  const handleUnassignStudentFromClass = async (userId: string) => {
     if (!selectedClass) return;
     if (window.confirm("Gỡ học sinh này khỏi lớp?")) {
        await supabase.from('class_students').delete().match({ class_id: selectedClass.id, user_id: userId }); fetchClassDetails(selectedClass.id);
     }
  };

  // --- EVENT HANDLERS KHÓA HỌC ---
  const handleCreateCourse = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const title = new FormData(e.currentTarget).get('title') as string;
    const type = new FormData(e.currentTarget).get('type') as string;
    const { data, error } = await supabase.from('courses').insert([{ title, type, order_index: courses.length + 1 }]).select();
    if (!error && data) { fetchCourses(); setShowCreateCourseModal(false); }
  };
  const handleUpdateCourseName = async (courseId: string, newTitle: string) => {
    if (!newTitle.trim()) { setEditingCourseId(null); return; }
    await supabase.from('courses').update({ title: newTitle }).eq('id', courseId); fetchCourses(); setEditingCourseId(null);
  };
  const handleDeleteCourse = async () => {
    if (window.confirm("Xác nhận xóa khóa học? Mọi dữ liệu (lớp, học phần, đề thi) bên trong sẽ bị xóa.") && selectedCourse) {
      await supabase.from('courses').delete().eq('id', selectedCourse.id); fetchCourses(); setActiveTab('courses');
    }
  };

  // --- EVENT HANDLERS HỌC PHẦN (MODULE) ---
  const handleUpdateModuleName = async (moduleId: string, newTitle: string) => {
    if (!newTitle.trim()) { setEditingModuleId(null); return; }
    await supabase.from('lecture_modules').update({ title: newTitle }).eq('id', moduleId);
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    setEditingModuleId(null);
  };
  const handleCreateLectureModule = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); if (!selectedCourse) return;
    const title = (new FormData(e.currentTarget).get('title') as string);
    const { data } = await supabase.from('lecture_modules').insert([{ course_id: selectedCourse.id, title, order_index: lectureModules.length + 1 }]).select();
    if (data) { fetchCourseDetailsData(selectedCourse.id); setShowModuleModal(false); }
  };
  const handleDeleteLectureModule = async (id: string) => {
    if (window.confirm("Xóa học phần này? Các bài giảng bên trong sẽ tự động trả về Kho tổng.")) {
      await supabase.from('lecture_modules').delete().eq('id', id); fetchCourseDetailsData(selectedCourse.id); fetchGlobalLectures();
    }
  };
  const handleAssignLecture = async (lectureId: string, moduleId: string) => {
    await supabase.from('lectures').update({ module_id: moduleId }).eq('id', lectureId);
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); fetchGlobalLectures(); setShowAssignLectureModal({show: false, moduleId: null});
  };
  const handleUnassignLecture = async (lectureId: string) => {
    if (window.confirm("Gỡ bài giảng này về Kho Tổng?")) {
      await supabase.from('lectures').update({ module_id: null }).eq('id', lectureId);
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); fetchGlobalLectures();
    }
  };
  const handlePermanentDeleteLecture = async (id: string) => {
    if (window.confirm("XÓA VĨNH VIỄN bài giảng khỏi hệ thống? Sẽ không thể khôi phục!")) {
      await supabase.from('lectures').delete().eq('id', id); fetchGlobalLectures(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    }
  };
  const handleDuplicateLecture = async (lectureData: any) => {
    const { data: newLecture, error: lecErr } = await supabase.from('lectures').insert([{ 
       title: lectureData.title + ' (Bản sao)', course_id: lectureData.course_id, module_id: null, order_index: globalLectures.length + 1 
    }]).select().single();
    if (lecErr) return alert("Lỗi nhân bản bài giảng!");
    const { data: pages } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureData.id);
    if (pages && pages.length > 0) {
       const newPages = pages.map(p => ({ lecture_id: newLecture.id, page_number: p.page_number, content_html: p.content_html }));
       await supabase.from('lecture_pages').insert(newPages);
    }
    fetchGlobalLectures(); alert("✅ Đã nhân bản bài giảng thành công! Bản sao đã được lưu vào Kho.");
  };

  // --- EVENT HANDLERS LỚP HỌC (CLASS) ---
  const handleUpdateClassName = async (classId: string, newName: string) => {
    if (!newName.trim()) { setEditingClassId(null); return; }
    await supabase.from('classes').update({ name: newName }).eq('id', classId);
    setClasses(classes.map(c => c.id === classId ? { ...c, name: newName } : c));
    if (selectedClass?.id === classId) setSelectedClass({ ...selectedClass, name: newName });
    setEditingClassId(null);
  };
  const handleCreateClass = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); if (!selectedCourse) return;
    const name = (new FormData(e.currentTarget).get('name') as string);
    const { data } = await supabase.from('classes').insert([{ course_id: selectedCourse.id, name }]).select();
    if (data) { setClasses([data[0], ...classes]); setShowClassModal(false); }
  };
  const handleDeleteClass = async (id: string) => {
    if (window.confirm("Xóa lớp học này? (Dữ liệu học viên trong lớp sẽ bị ảnh hưởng)")) {
      await supabase.from('classes').delete().eq('id', id); setClasses(classes.filter(c => c.id !== id)); if (selectedClass?.id === id) setSelectedClass(null);
    }
  };
  const handleAssignModuleToClass = async (moduleId: string) => {
    if (!selectedClass) return;
    await supabase.from('class_modules').insert([{ class_id: selectedClass.id, module_id: moduleId }]); fetchClassDetails(selectedClass.id);
  };
  const handleUnassignModuleFromClass = async (moduleId: string) => {
    if (!selectedClass) return;
    await supabase.from('class_modules').delete().match({ class_id: selectedClass.id, module_id: moduleId }); fetchClassDetails(selectedClass.id);
  };

  // --- EVENT HANDLERS ĐỀ THI VÀ THƯ MỤC ---
  const handleInitiateTest = (mode: 'manual' | 'import' | 'case-study') => {
    setShowCreateDropdown(false);
    setEditingTest({ id: 'new', title: '', folder_id: '', test_type: mode === 'case-study' ? 'Case-Study' : 'IELTS-Listening', content_json: null, mode });
  };
  
  const handleSaveTestContent = async (testId: string, finalData: any) => {
    let parsedJsonConfig = null;
    if (finalData.basicInfo?.skill === 'Case-Study' && finalData.json_config_string) {
      try { parsedJsonConfig = JSON.parse(finalData.json_config_string); } catch(e) { return alert("⚠️ Lỗi cú pháp JSON."); }
    }

    const assignedCourseId = finalData.basicInfo?.courseId === 'all' ? null : finalData.basicInfo.courseId;

    const payload: any = { 
       title: finalData.basicInfo?.title || 'Untitled Test', 
       test_type: finalData.basicInfo?.skill || 'IELTS-Listening', 
       content_json: finalData, 
       json_config: parsedJsonConfig, 
       folder_id: finalData.folder_id || null, 
       course_id: assignedCourseId, 
       is_published: true, 
       insert_pdf_url: finalData.basicInfo?.insert_pdf_url || null 
    };
    
    if (testId === 'new') {
       payload.order_index = libraryTests.length + 1;
       await supabase.from('tests').insert([payload]);
    } else {
       await supabase.from('tests').update(payload).eq('id', testId);
    }
    
    setEditingTest(null); fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleUpdateFolderName = async (folderId: string, newTitle: string) => {
    if (!newTitle.trim()) { setEditingFolderId(null); return; }
    await supabase.from('folders').update({ title: newTitle }).eq('id', folderId);
    setFolders(folders.map(f => f.id === folderId ? { ...f, title: newTitle } : f));
    fetchAllFolders();
    setEditingFolderId(null);
  };

  const handleCreateFolder = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); if (!selectedCourse) return;
    const title = new FormData(e.currentTarget).get('title') as string;
    const { data } = await supabase.from('folders').insert([{ course_id: selectedCourse.id, title: title, parent_id: currentFolderId, display_order: folders.length + 1 }]).select();
    if (data) { setFolders([...folders, data[0]]); fetchAllFolders(); setShowFolderModal(false); }
  };
  
  const handleDeleteFolder = async (id: string) => {
    if (window.confirm("Xóa thư mục này? Các đề thi bên trong sẽ TỰ ĐỘNG CHUYỂN VỀ Kho đề của Khóa học.")) {
      await supabase.from('folders').delete().eq('id', id); setFolders(folders.filter(f => f.id !== id && f.parent_id !== id)); fetchAllFolders();
      fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    }
  };

  const handleAssignTest = async (testId: string) => {
    if (!currentFolderId) return;
    await supabase.from('tests').update({ folder_id: currentFolderId }).eq('id', testId);
    fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); setShowAssignModal(false);
  };
  const handleUnassignTest = async (testId: string) => {
    if (window.confirm("Gỡ đề thi khỏi thư mục này? Đề sẽ trở về Kho Tổng.")) {
      await supabase.from('tests').update({ folder_id: null }).eq('id', testId);
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); fetchLibraryTests();
    }
  };
  const handleDeleteTest = async (id: string) => {
    if (window.confirm("Xóa vĩnh viễn đề thi khỏi kho?")) { await supabase.from('tests').delete().eq('id', id); fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);}
  };
  const handleToggleTestVisibility = async (test: any) => {
    const newStatus = !test.is_published;
    await supabase.from('tests').update({ is_published: newStatus }).eq('id', test.id);
    setLibraryTests(libraryTests.map(t => t.id === test.id ? { ...t, is_published: newStatus } : t));
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };
  const handleBulkVisibility = async (status: boolean) => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi!");
    await supabase.from('tests').update({ is_published: status }).in('id', selectedTests);
    fetchLibraryTests(); setSelectedTests([]); 
  };
  const handleBulkDelete = async () => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi!");
    if (window.confirm(`Xác nhận xóa vĩnh viễn ${selectedTests.length} đề thi đã chọn?`)) {
      await supabase.from('tests').delete().in('id', selectedTests); fetchLibraryTests(); setSelectedTests([]);
    }
  };
  const handleSelectAll = (e: React.ChangeEvent<HTMLInputElement>, filteredList: any[]) => {
    if (e.target.checked) setSelectedTests(filteredList.map(t => t.id)); else setSelectedTests([]);
  };
  const handleSelectOne = (id: string) => {
    if (selectedTests.includes(id)) setSelectedTests(selectedTests.filter(t => t !== id)); else setSelectedTests([...selectedTests, id]);
  };

  const handleViewCourseDetail = (course: any) => {
    setSelectedCourse(course); setCurrentFolderId(null); setSelectedClass(null); setCourseViewMode('classes');
    fetchCourseDetailsData(course.id); setActiveTab('course-detail');
  };

  const getCourseNameForTest = (courseId: string | null) => {
     if (!courseId) return '-- Dùng chung --';
     return courses.find(c => c.id === courseId)?.title || '-- Trống --';
  }

  const breadcrumbs = []; let curr = folders.find(f => f.id === currentFolderId);
  while (curr) { breadcrumbs.unshift(curr); curr = folders.find(f => f.id === curr.parent_id); }
  const currentSubFolders = useMemo(() => folders.filter(f => currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')).sort((a,b) => (a.display_order||0) - (b.display_order||0)), [folders, currentFolderId]);
  
  const currentTests = useMemo(() => assignedTests.filter(t => t.folder_id === currentFolderId), [assignedTests, currentFolderId]);

  const filteredLibraryTests = useMemo(() => libraryTests.filter(test => {
      const matchesSearch = test.title.toLowerCase().includes(searchQuery.toLowerCase());
      if (filterCourse === 'all') return matchesSearch;
      return matchesSearch && test.course_id === filterCourse;
  }), [libraryTests, searchQuery, filterCourse]);

  const filteredGlobalLectures = useMemo(() => globalLectures.filter(lec => {
      const matchesSearch = lec.title.toLowerCase().includes(searchQuery.toLowerCase());
      if (filterLectureCourse === 'all') return matchesSearch;
      return matchesSearch && lec.course_id === filterLectureCourse;
  }), [globalLectures, searchQuery, filterLectureCourse]);

  return (
    <div className="min-h-screen bg-[#f8fafc] flex font-sans text-slate-800">
      
      {/* SIDEBAR BỎ QUẢN LÝ TÀI LIỆU */}
      <aside className="w-64 bg-[#1e293b] text-slate-300 flex flex-col shrink-0 sticky top-0 h-screen z-50 shadow-xl">
        <div className="h-20 flex items-center gap-3 px-6 bg-[#0f172a] border-b border-slate-800 cursor-pointer" onClick={() => onNavigate?.('home')}>
          <div className="font-black text-xl tracking-tight text-white uppercase mt-1">TONY<span className="text-[#2bd6eb]">ADMIN</span></div>
        </div>
        <div className="p-4 space-y-1">
          <p className="text-[10px] font-black uppercase text-slate-500 tracking-widest ml-3 mb-2 mt-4">Hệ thống LMS</p>
          <button onClick={() => {setActiveTab('courses'); setSelectedCourse(null);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'courses' || activeTab === 'course-detail' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📁 Khóa học & Lớp</button>
          <button onClick={() => setActiveTab('library')} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'library' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📚 Kho Đề thi</button>
          <button onClick={() => setActiveTab('lectures-library')} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'lectures-library' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📖 Kho Bài giảng</button>
          <button onClick={() => setActiveTab('students')} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'students' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>👨‍🎓 Quản lý học viên</button>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="flex-1 flex flex-col min-w-0 relative">
        <header className="h-20 bg-white border-b border-slate-200 px-8 flex items-center justify-between sticky top-0 z-40 shadow-sm">
          <h1 className="text-xl font-black text-slate-800 uppercase tracking-tight">
            {activeTab === 'courses' ? 'Danh sách Khóa học' : activeTab === 'course-detail' ? 'Chi tiết Khóa học' : activeTab === 'lectures-library' ? 'Kho Bài Giảng Chung' : activeTab === 'library' ? 'Kho lưu trữ đề thi' : 'Quản lý Học viên'}
          </h1>
          <div className="flex items-center gap-4">
            {activeTab === 'courses' && <button onClick={() => setShowCreateCourseModal(true)} className="bg-[#0a5482] text-white font-black px-6 py-2.5 rounded-xl shadow-lg text-sm transition hover:bg-[#084266]">+ THÊM KHÓA HỌC</button>}
            {activeTab === 'lectures-library' && <button onClick={() => setEditingLecture({ id: 'new', title: '', course_id: null })} className="bg-[#00a651] text-white font-black px-6 py-2.5 rounded-xl shadow-md text-sm transition hover:bg-[#008f45]">+ TẠO BÀI GIẢNG MỚI</button>}
            {activeTab === 'library' && (
              <div className="relative shrink-0" ref={dropdownRef}>
                <button onClick={() => setShowCreateDropdown(!showCreateDropdown)} className="bg-[#2bd6eb] text-white font-black px-6 py-2.5 rounded-xl shadow-md flex items-center gap-2 text-sm transition hover:bg-[#1bc1d6]">+ TẠO ĐỀ MỚI <span className={`text-[10px] transition-transform ${showCreateDropdown ? 'rotate-180' : ''}`}>▼</span></button>
                {showCreateDropdown && (
                  <div className="absolute right-0 mt-2 w-64 bg-white border border-slate-200 rounded-2xl shadow-2xl z-50 py-2 animate-in fade-in zoom-in-95">
                    <button onClick={() => handleInitiateTest('manual')} className="w-full text-left px-5 py-3 hover:bg-slate-50 font-bold text-[13px] border-b border-slate-100">✍️ Tạo thủ công (Standard)</button>
                    <button onClick={() => handleInitiateTest('case-study')} className="w-full text-left px-5 py-3 hover:bg-blue-50 font-bold text-[13px] text-[#0a5482] border-b border-slate-100">📄 Tạo đề Case Study</button>
                    <button onClick={() => handleInitiateTest('import')} className="w-full text-left px-5 py-3 hover:bg-slate-50 font-bold text-[13px]">📥 Import Excel/CSV</button>
                  </div>
                )}
              </div>
            )}
          </div>
        </header>

        <div className="flex-1 p-8 overflow-y-auto">
          {activeTab === 'courses' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {isLoadingCourses ? ( <div className="text-slate-400">Đang tải...</div> ) : (
                courses.map(course => (
                  <div key={course.id} className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm hover:shadow-xl transition-all group flex flex-col h-48 relative">
                    <div className="flex justify-between items-start">
                       <span className="px-2.5 py-1 rounded-md text-[10px] font-black uppercase bg-blue-100 text-blue-700">{course.type}</span>
                       <div className="flex items-center gap-3">
                         <button onClick={(e) => { e.stopPropagation(); setEditingCourseId(course.id); }} className="opacity-0 group-hover:opacity-100 text-slate-400 hover:text-[#0a5482] transition-opacity">✏️</button>
                         <div className="flex items-center gap-1 bg-slate-50 px-2 py-1 rounded border border-slate-200" onClick={e => e.stopPropagation()}>
                           <span className="text-[10px] font-bold text-slate-400">Thứ tự:</span>
                           <input type="number" defaultValue={course.order_index || 0} onBlur={e => handleUpdateCourseOrder(course.id, parseInt(e.target.value) || 0)} className="w-8 text-center text-xs font-bold outline-none bg-transparent" />
                         </div>
                       </div>
                    </div>
                    <div className="flex-1 mt-4 mb-2">
                       {editingCourseId === course.id ? (
                         <form onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateCourseName(course.id, new FormData(e.currentTarget).get('title') as string); }}>
                            <input name="title" autoFocus defaultValue={course.title} className="w-full border border-slate-300 rounded-lg px-3 py-1.5 font-black text-[15px] outline-none mb-2 focus:border-[#0a5482]" />
                            <div className="flex gap-2"><button type="submit" className="text-xs font-bold text-white bg-emerald-500 px-3 py-1 rounded">Lưu</button><button type="button" onClick={() => setEditingCourseId(null)} className="text-xs font-bold bg-slate-100 px-3 py-1 rounded border border-slate-200">Hủy</button></div>
                         </form>
                       ) : ( <h3 className="font-black text-lg text-slate-800 line-clamp-2">{course.title}</h3> )}
                    </div>
                    <button onClick={() => handleViewCourseDetail(course)} className="w-full bg-[#f8fafc] group-hover:bg-[#2bd6eb] group-hover:text-white text-slate-600 border border-slate-200 font-bold py-2.5 rounded-xl transition shadow-sm text-sm">Quản lý Lớp & Nội dung ➜</button>
                  </div>
                ))
              )}
            </div>
          )}

          {activeTab === 'course-detail' && selectedCourse && (
            <div className="space-y-6">
              <div className="flex justify-between items-center bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
                <div className="flex items-center gap-2 text-sm font-bold text-slate-500">
                  <button onClick={() => setActiveTab('courses')} className="hover:text-[#2bd6eb] transition-colors">Khóa học</button> <span className="text-slate-300">/</span> <span className="text-slate-800 font-black">{selectedCourse.title}</span>
                </div>
                <button onClick={handleDeleteCourse} className="text-red-500 hover:bg-red-50 px-4 py-2 rounded-lg font-bold text-xs border border-red-100 transition">🗑️ Xóa Khóa học</button>
              </div>

              <div className="flex gap-6 border-b border-slate-200 px-2">
                 <button onClick={() => setCourseViewMode('classes')} className={`pb-3 font-black text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'classes' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>👨‍🏫 QUẢN LÝ LỚP HỌC</button>
                 <button onClick={() => setCourseViewMode('modules')} className={`pb-3 font-black text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'modules' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>📚 CẤU TRÚC HỌC PHẦN (GIÁO TRÌNH)</button>
                 <button onClick={() => setCourseViewMode('tests')} className={`pb-3 font-black text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'tests' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>📁 KHO ĐỀ THI</button>
              </div>

              {courseViewMode === 'classes' && (
                <div className="flex gap-6 h-[600px] animate-in fade-in">
                   <div className="w-1/3 bg-white rounded-3xl border border-slate-200 shadow-sm flex flex-col overflow-hidden">
                      <div className="p-5 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                         <h3 className="font-black text-slate-700 uppercase text-xs tracking-widest">Danh sách Lớp</h3>
                         <button onClick={() => setShowClassModal(true)} className="bg-[#0a5482] hover:bg-[#084266] transition text-white px-4 py-1.5 rounded-lg text-xs font-bold">+ THÊM LỚP</button>
                      </div>
                      <div className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar">
                         {classes.length === 0 ? <p className="text-sm text-slate-400 text-center mt-4 italic">Chưa có lớp nào</p> : (
                            classes.map(cls => (
                               <div key={cls.id} onClick={() => { setSelectedClass(cls); fetchClassDetails(cls.id); }} className={`p-4 border rounded-xl cursor-pointer transition-all flex justify-between items-center group ${selectedClass?.id === cls.id ? 'bg-blue-50 border-blue-400' : 'bg-white border-slate-200 hover:border-[#2bd6eb]'}`}>
                                  <div className="flex-1 mr-2">
                                     {editingClassId === cls.id ? (
                                        <form onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateClassName(cls.id, new FormData(e.currentTarget).get('name') as string); }}>
                                           <input name="name" autoFocus defaultValue={cls.name} className="w-full border border-slate-300 rounded px-2 py-1 font-black text-sm outline-none mb-1 focus:border-[#0a5482]" />
                                           <div className="flex gap-2"><button type="submit" className="text-[10px] font-bold text-white bg-emerald-500 px-2 py-0.5 rounded">Lưu</button><button type="button" onClick={() => setEditingClassId(null)} className="text-[10px] font-bold bg-slate-200 px-2 py-0.5 rounded text-slate-600">Hủy</button></div>
                                        </form>
                                     ) : ( <p className={`font-black text-sm ${selectedClass?.id === cls.id ? 'text-blue-800' : 'text-slate-700'}`}>{cls.name}</p> )}
                                  </div>
                                  <div className="flex items-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                     <button onClick={(e) => { e.stopPropagation(); setEditingClassId(cls.id); }} className="text-blue-400 hover:text-blue-600 text-xs font-bold transition-colors bg-white p-1 rounded border border-blue-200">✏️</button>
                                     <button onClick={(e) => { e.stopPropagation(); handleDeleteClass(cls.id); }} className="text-red-400 hover:text-red-600 text-xs font-bold transition-colors bg-white p-1 rounded border border-red-200">✕</button>
                                  </div>
                               </div>
                            ))
                         )}
                      </div>
                   </div>

                   <div className="flex-1 bg-white rounded-3xl border border-slate-200 shadow-sm flex flex-col overflow-hidden">
                      {!selectedClass ? (
                         <div className="flex-1 flex items-center justify-center text-slate-400 font-medium border-2 border-dashed border-slate-100 m-8 rounded-2xl">👈 Bấm chọn một lớp học bên trái để xem và gán dữ liệu</div>
                      ) : (
                         <div className="flex-1 flex flex-col overflow-hidden animate-in fade-in">
                            <div className="p-6 bg-blue-50/50 border-b border-blue-100"><h2 className="text-lg font-black text-[#0a5482] uppercase tracking-wide">LỚP: {selectedClass.name}</h2></div>
                            <div className="flex-1 flex overflow-hidden">
                               <div className="w-1/2 border-r border-slate-200 flex flex-col">
                                  <div className="p-4 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                                     <h3 className="font-bold text-sm text-slate-700">Học phần của lớp</h3>
                                     <button onClick={() => setShowAssignClassModuleModal(true)} className="text-xs bg-emerald-500 hover:bg-emerald-600 transition text-white font-bold px-3 py-1.5 rounded-lg shadow-sm">+ Gán Học phần</button>
                                  </div>
                                  <div className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar">
                                     {lectureModules.filter(m => classModules.includes(m.id)).length === 0 ? <p className="text-xs text-slate-400 italic text-center mt-4">Lớp này chưa được mở học phần nào.</p> : (
                                        lectureModules.filter(m => classModules.includes(m.id)).map(m => (
                                           <div key={m.id} className="p-3 bg-white border border-slate-200 rounded-lg flex justify-between items-center shadow-sm hover:border-slate-300 transition">
                                              <span className="font-bold text-sm text-slate-700">{m.title}</span>
                                              <button onClick={() => handleUnassignModuleFromClass(m.id)} className="text-red-500 text-xs font-bold hover:underline transition">Gỡ</button>
                                           </div>
                                        ))
                                     )}
                                  </div>
                               </div>
                               <div className="w-1/2 flex flex-col bg-[#f8fafc]">
                                  <div className="p-4 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                                     <h3 className="font-bold text-sm text-slate-700">Học sinh trong lớp</h3>
                                     <button onClick={() => setShowAssignStudentModal(true)} className="text-xs bg-blue-500 hover:bg-blue-600 transition text-white font-bold px-3 py-1.5 rounded-lg shadow-sm">+ Thêm Học sinh</button>
                                  </div>
                                  <div className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar">
                                     {classStudentsList.length === 0 ? <p className="text-xs text-slate-400 italic text-center mt-4">Lớp chưa có học sinh nào.</p> : (
                                        classStudentsList.map(st => (
                                           <div key={st.user_id} className="p-3 bg-white border border-slate-200 rounded-lg flex justify-between items-center shadow-sm">
                                              <div><p className="font-bold text-sm text-slate-700">{st.full_name || 'Học viên'}</p><p className="text-[10px] text-slate-400">{st.email}</p></div>
                                              <button onClick={() => handleUnassignStudentFromClass(st.user_id)} className="text-red-500 text-xs font-bold hover:underline">Gỡ</button>
                                           </div>
                                        ))
                                     )}
                                  </div>
                               </div>
                            </div>
                         </div>
                      )}
                   </div>
                </div>
              )}

              {courseViewMode === 'modules' && (
                <div className="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm animate-in fade-in">
                  <div className="p-6 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                    <p className="font-black text-slate-600 text-xs uppercase tracking-widest">Giáo trình gốc của Khóa học</p>
                    <button onClick={() => setShowModuleModal(true)} className="bg-[#0a5482] hover:bg-[#084266] transition text-white px-6 py-2.5 rounded-xl font-black text-xs">+ THÊM HỌC PHẦN</button>
                  </div>
                  <div className="p-8">
                     {lectureModules.length === 0 ? <div className="text-center py-12 border-2 border-dashed border-slate-200 rounded-2xl text-slate-400 font-medium">Khóa học này chưa có Học phần nào. Hãy tạo Học phần đầu tiên.</div> : (
                        lectureModules.map(mod => {
                           const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                           return (
                             <div key={mod.id} className="border border-slate-200 rounded-2xl overflow-hidden shadow-sm mb-6 group/mod">
                                <div className="bg-slate-50 px-6 py-4 border-b border-slate-200 flex justify-between items-center">
                                   <div className="flex items-center gap-4 flex-1 mr-4">
                                      {editingModuleId === mod.id ? (
                                         <form className="flex-1 flex gap-2" onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateModuleName(mod.id, new FormData(e.currentTarget).get('title') as string); }}>
                                            <input name="title" autoFocus defaultValue={mod.title} className="flex-1 border border-slate-300 rounded-lg px-3 py-1 font-black text-[15px] outline-none focus:border-[#0a5482]" />
                                            <button type="submit" className="text-xs font-bold text-white bg-emerald-500 px-3 py-1 rounded">Lưu</button>
                                            <button type="button" onClick={() => setEditingModuleId(null)} className="text-xs font-bold bg-slate-100 px-3 py-1 rounded border border-slate-200 text-slate-600">Hủy</button>
                                         </form>
                                      ) : (
                                        <>
                                           <div className="flex items-center gap-3">
                                              <h3 className="font-black text-slate-800 text-[16px] flex items-center gap-2">📑 {mod.title}</h3>
                                              <button onClick={() => setEditingModuleId(mod.id)} className="text-blue-500 hover:text-blue-700 transition-colors text-[11px] font-bold bg-blue-50 hover:bg-blue-100 px-2 py-1 rounded border border-blue-200 shadow-sm flex items-center gap-1">✏️ Sửa tên</button>
                                           </div>
                                           <div className="flex items-center gap-1 bg-white px-2 py-1 rounded border border-slate-200"><span className="text-[10px] font-bold text-slate-400 uppercase">Thứ tự:</span><input type="number" defaultValue={mod.order_index || 0} onBlur={e => handleUpdateModuleOrder(mod.id, parseInt(e.target.value) || 0)} className="w-10 text-center text-xs font-bold outline-none" /></div>
                                        </>
                                     )}
                                   </div>
                                   <div className="flex gap-2">
                                      <button onClick={() => setShowAssignLectureModal({show: true, moduleId: mod.id})} className="bg-white border border-slate-300 text-blue-600 px-4 py-1.5 rounded-lg text-xs font-bold hover:border-blue-400 transition">+ Nhặt Bài Giảng Từ Kho</button>
                                      <button onClick={() => setEditingLecture({ id: 'new', title: '', course_id: selectedCourse.id, module_id: mod.id })} className="bg-[#00a651] hover:bg-[#008f45] transition text-white px-4 py-1.5 rounded-lg text-xs font-bold">+ Tạo Mới</button>
                                      <button onClick={() => handleDeleteLectureModule(mod.id)} className="bg-white border border-slate-300 text-red-500 hover:bg-red-50 hover:border-red-300 px-3 py-1.5 rounded-lg text-xs transition">✖</button>
                                   </div>
                                </div>
                                <div className="p-4 bg-white">
                                   {moduleLectures.length === 0 ? <p className="text-sm text-slate-400 italic px-4 py-2">Chưa có bài giảng nào trong học phần này.</p> : (
                                      moduleLectures.map((lec) => (
                                         <div key={lec.id} className="flex justify-between items-center p-3 hover:bg-blue-50 rounded-lg group border border-transparent hover:border-blue-100 transition-colors">
                                            <div className="flex items-center gap-3">
                                               <input type="number" defaultValue={lec.order_index || 0} onBlur={e => handleUpdateLectureOrder(lec.id, parseInt(e.target.value) || 0)} className="w-10 h-6 text-center text-[11px] font-bold border border-slate-200 rounded outline-none focus:border-[#2bd6eb]" title="Thứ tự hiển thị" />
                                               <span className="font-semibold text-slate-700 text-sm">{lec.title}</span>
                                            </div>
                                            <div className="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                               <button onClick={() => handleUnassignLecture(lec.id)} className="text-orange-500 font-bold text-xs bg-white border border-orange-200 px-3 py-1 rounded hover:bg-orange-50 transition">Gỡ (Đưa về Kho)</button>
                                               <button onClick={() => setEditingLecture(lec)} className="text-blue-600 font-bold text-xs bg-white border border-blue-200 px-3 py-1 rounded hover:bg-blue-50 transition">✏️ Sửa</button>
                                            </div>
                                         </div>
                                      ))
                                   )}
                                </div>
                             </div>
                           )
                        })
                     )}
                  </div>
                </div>
              )}

              {/* VIEW: QUẢN LÝ ĐỀ THI TRONG ADMIN (CHỈ CÓ THỨ TỰ, KHÔNG CÓ UPLOAD ẢNH) */}
              {courseViewMode === 'tests' && (
                <div className="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm animate-in fade-in">
                  <div className="p-6 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                    <div className="flex items-center gap-2">
                       {currentFolderId && <button onClick={() => setCurrentFolderId(null)} className="text-slate-400 hover:text-black font-bold mr-2 transition">← Trở về</button>}
                       <p className="font-black text-slate-500 text-xs uppercase tracking-widest">{currentFolderId ? `Danh mục con của: ${breadcrumbs[breadcrumbs.length-1]?.title}` : 'Thư mục gốc đề thi'}</p>
                    </div>
                    <button onClick={() => setShowFolderModal(true)} className="bg-[#00a651] hover:bg-[#008f45] transition text-white px-6 py-2.5 rounded-xl font-black text-xs shadow-md">+ THÊM THƯ MỤC</button>
                  </div>
                  <div className="p-8">
                    {currentSubFolders.length > 0 && (
                      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                        {currentSubFolders.map(sf => (
                          <div key={sf.id} className="relative group h-full">
                            
                            {/* Ô NHẬP ĐỔI THỨ TỰ THƯ MỤC */}
                            <div className="absolute top-2 left-2 bg-white/90 backdrop-blur-sm px-2 py-0.5 rounded border border-slate-200 flex items-center gap-1 z-10 opacity-0 group-hover:opacity-100 transition-opacity">
                               <span className="text-[10px] font-bold text-slate-400">TT:</span>
                               <input type="number" defaultValue={sf.display_order || 0} onBlur={e => handleUpdateFolderOrder(sf.id, parseInt(e.target.value) || 0)} className="w-8 text-center text-xs font-bold outline-none bg-transparent" title="Thứ tự hiển thị" />
                            </div>

                            {editingFolderId === sf.id ? (
                               <div className="bg-white border-2 border-[#2bd6eb] p-4 rounded-2xl shadow-sm h-full flex flex-col justify-center items-center" onClick={e => e.stopPropagation()}>
                                  <form className="w-full flex flex-col items-center" onSubmit={(e) => { e.preventDefault(); handleUpdateFolderName(sf.id, new FormData(e.currentTarget).get('title') as string); }}>
                                     <input name="title" autoFocus defaultValue={sf.title} className="w-full border border-slate-300 rounded px-2 py-1.5 text-sm font-bold outline-none mb-2 text-center focus:border-[#0a5482]" />
                                     <div className="flex gap-2">
                                        <button type="submit" className="text-xs font-bold text-white bg-emerald-500 px-3 py-1 rounded shadow-sm">Lưu</button>
                                        <button type="button" onClick={() => setEditingFolderId(null)} className="text-xs font-bold bg-slate-100 px-3 py-1 rounded border border-slate-200 text-slate-600">Hủy</button>
                                     </div>
                                  </form>
                               </div>
                            ) : (
                               <div onClick={() => setCurrentFolderId(sf.id)} className="bg-white border-2 border-slate-100 hover:border-[#2bd6eb] p-6 rounded-2xl shadow-sm cursor-pointer transition-all flex flex-col items-center justify-center text-center h-full relative overflow-hidden">
                                  <div className="text-4xl mb-3 group-hover:scale-110 transition-transform relative z-10">📁</div>
                                  <h4 className="font-black text-slate-700 text-sm line-clamp-2 relative z-10">{sf.title}</h4>
                                  <button onClick={(e) => { e.stopPropagation(); setEditingFolderId(sf.id); }} className="absolute top-2 right-2 text-blue-400 hover:text-blue-600 opacity-0 group-hover:opacity-100 transition-opacity bg-blue-50 p-1.5 rounded text-xs z-10">✏️</button>
                               </div>
                            )}
                            {editingFolderId !== sf.id && (
                               <button onClick={(e) => { e.stopPropagation(); handleDeleteFolder(sf.id); }} className="absolute -top-2 -right-2 bg-red-500 hover:bg-red-600 text-white w-7 h-7 rounded-full opacity-0 group-hover:opacity-100 transition-opacity shadow-lg flex items-center justify-center text-xs font-bold z-20">✕</button>
                            )}
                          </div>
                        ))}
                      </div>
                    )}{currentFolderId && currentSubFolders.length === 0 && (
                      <div className="border-t-2 border-dashed border-slate-200 pt-8 mt-2">
                         <div className="flex justify-between items-center mb-6">
                            <h3 className="font-black text-slate-800 text-lg">📝 Đề thi trong mục này</h3>
                            <button onClick={() => setShowAssignModal(true)} className="bg-[#2bd6eb] hover:bg-[#1bc1d6] transition text-white px-5 py-2 rounded-lg font-bold text-xs shadow-sm">+ GÁN ĐỀ</button>
                         </div>
                         {currentTests.length === 0 ? (
                           <div className="text-center py-10 border-2 border-dashed border-slate-200 rounded-2xl text-slate-400 font-medium">Chưa có đề thi nào. Bấm nút + Gán đề để thêm từ Kho tổng.</div>
                         ) : (
                           <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4">
                             {currentTests.map(t => (
                               <div key={t.id} className="bg-slate-50 border border-slate-200 p-4 rounded-xl flex justify-between items-center group hover:bg-white transition-colors">
                                 <div className="flex items-center gap-3">
                                   <input type="number" defaultValue={t.order_index || 0} onBlur={e => handleUpdateTestOrder(t.id, parseInt(e.target.value) || 0)} className="w-10 h-6 text-center text-[11px] font-bold border border-slate-200 rounded outline-none focus:border-[#2bd6eb]" title="Thứ tự hiển thị" />
                                   <span className="font-bold text-[14px] text-slate-700">{t.title}</span>
                                 </div>
                                 <div className="flex gap-3">
                                   <button onClick={() => setEditingTest(t)} className="text-[#2bd6eb] font-bold text-xs hover:underline opacity-0 group-hover:opacity-100 transition-opacity">Sửa</button>
                                   <button onClick={() => handleUnassignTest(t.id)} className="text-red-400 font-bold text-xs hover:underline opacity-0 group-hover:opacity-100 transition-opacity">Gỡ ✖</button>
                                 </div>
                               </div>
                             ))}
                           </div>
                         )}
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          )}

          {activeTab === 'lectures-library' && (
            <div className="space-y-6">
              <div className="flex flex-col sm:flex-row justify-between gap-4 bg-white p-4 rounded-xl border border-slate-200 shadow-sm relative z-20">
                 <input type="text" placeholder="Tìm kiếm tên bài giảng..." onChange={e => setSearchQuery(e.target.value)} className="w-full sm:max-w-xs pl-4 pr-4 py-2.5 border border-slate-200 rounded-xl outline-none focus:border-[#2bd6eb] text-sm transition-colors" />
                 <select value={filterLectureCourse} onChange={e => setFilterLectureCourse(e.target.value)} className="px-4 py-2.5 border border-slate-200 rounded-xl text-sm font-bold text-slate-600 outline-none w-full sm:w-auto bg-white">
                    <option value="all">Tất cả khóa học</option>
                    {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                 </select>
              </div>
              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                <table className="w-full text-left border-collapse min-w-[900px]">
                  <thead className="bg-[#f8fafc] text-[11px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200">
                    <tr><th className="px-6 py-4 w-12 text-center">#</th><th className="px-6 py-4">TÊN BÀI GIẢNG</th><th className="px-6 py-4">KHÓA HỌC</th><th className="px-6 py-4 text-center">KIỂU NỘI DUNG</th><th className="px-6 py-4">THÔNG TIN CẬP NHẬT</th><th className="px-6 py-4 text-center">TRẠNG THÁI</th><th className="px-6 py-4 text-center">THỨ TỰ</th><th className="px-6 py-4 text-right">THAO TÁC</th></tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {filteredGlobalLectures.map((lec, index) => (
                      <tr key={lec.id} className="hover:bg-slate-50 transition-colors group">
                        <td className="px-6 py-5 text-center text-[13px] font-bold text-slate-400">{index + 1}</td>
                        <td className="px-6 py-5 font-bold text-[#0a5482] text-[14px]">{lec.title}</td>
                        <td className="px-6 py-5">{lec.courses ? <span className="px-2 py-1 bg-slate-100 border border-slate-200 rounded text-[11px] font-bold text-slate-600">{lec.courses.title}</span> : <span className="text-[11px] italic text-slate-400">-- Trống --</span>}</td>
                        <td className="px-6 py-5 text-center text-[12px] font-bold text-slate-500">HTML</td>
                        <td className="px-6 py-5"><div className="text-[11px] text-slate-500 font-medium">Tạo: {formatDateTime(lec.created_at)}</div></td>
                        <td className="px-6 py-5 text-center"><button onClick={() => handleToggleLectureStatus(lec.id, lec.is_published)} className={`text-[12px] font-bold px-3 py-1 rounded transition-colors ${lec.is_published ? 'text-emerald-600 bg-emerald-50 hover:bg-emerald-100' : 'text-slate-500 bg-slate-100 hover:bg-slate-200'}`}>{lec.is_published ? 'Hiển thị' : 'Đang ẩn'}</button></td>
                        <td className="px-6 py-5 text-center"><input type="number" defaultValue={lec.order_index || 0} onBlur={e => handleUpdateLectureOrder(lec.id, parseInt(e.target.value) || 0)} className="w-12 text-center text-[13px] font-bold border border-slate-200 rounded py-1 outline-none focus:border-[#2bd6eb]" /></td>
                        <td className="px-6 py-5 text-right space-x-2">
                           <button onClick={() => setEditingLecture(lec)} className="text-[#2bd6eb] font-bold text-xs bg-white border border-[#2bd6eb] px-3 py-1.5 rounded hover:bg-blue-50 transition">Sửa</button>
                           <button onClick={() => handleDuplicateLecture(lec)} className="text-emerald-600 font-bold text-xs bg-white border border-emerald-300 px-3 py-1.5 rounded hover:bg-emerald-50 transition">Nhân bản</button>
                           <button onClick={() => handlePermanentDeleteLecture(lec.id)} className="text-red-500 font-bold text-xs bg-white border border-red-200 px-3 py-1.5 rounded hover:bg-red-50 transition opacity-0 group-hover:opacity-100">Xóa</button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'library' && (
            <div className="space-y-6">
              <div className="flex flex-col lg:flex-row justify-between gap-4 bg-white p-4 rounded-xl border border-slate-200 shadow-sm relative z-20">
                <div className="flex bg-slate-100 rounded-lg p-1 border border-slate-200 shadow-sm shrink-0">
                  <button onClick={() => handleBulkVisibility(true)} className="px-4 py-1.5 text-[13px] font-bold text-emerald-600 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">👁️ Hiển thị</button>
                  <button onClick={() => handleBulkVisibility(false)} className="px-4 py-1.5 text-[13px] font-bold text-slate-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">👁️‍🗨️ Ẩn đi</button>
                  <button onClick={handleBulkDelete} className="px-4 py-1.5 text-[13px] font-bold text-red-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">🗑️ Xóa</button>
                </div>
                <div className="flex flex-col sm:flex-row gap-4 flex-1 justify-end">
                  <input type="text" placeholder="Tìm kiếm tên đề..." defaultValue={searchQuery} onChange={e => { clearTimeout(adminSearchTimer); adminSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350); }} className="w-full sm:max-w-xs pl-4 pr-4 py-2.5 border border-slate-200 rounded-xl outline-none focus:border-[#2bd6eb] text-sm transition-colors" />
                  <select value={filterCourse} onChange={e => setFilterCourse(e.target.value)} className="px-4 py-2.5 border border-slate-200 rounded-xl text-sm font-bold text-slate-600 outline-none w-full sm:w-auto bg-white">
                    <option value="all">Tất cả khóa học</option>{courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                  </select>
                </div>
              </div>

              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden z-10 relative">
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse min-w-[1000px]">
                    <thead className="bg-[#f8fafc] text-[11px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200">
                      <tr><th className="px-4 py-4 w-12 text-center">#</th><th className="px-2 py-4 w-10"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.length > 0 && selectedTests.length === filteredLibraryTests.length} onChange={(e) => handleSelectAll(e, filteredLibraryTests)} /></th><th className="px-6 py-4">TÊN ĐỀ THI</th><th className="px-6 py-4">KHÓA HỌC</th><th className="px-6 py-4">KỸ NĂNG</th><th className="px-6 py-4">THÔNG TIN CẬP NHẬT</th><th className="px-6 py-4 text-center">TRẠNG THÁI</th><th className="px-6 py-4 text-center">THỨ TỰ</th><th className="px-6 py-4 text-right">THAO TÁC</th></tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {filteredLibraryTests.length === 0 ? <tr><td colSpan={9} className="text-center py-10 text-slate-400 font-medium">Không tìm thấy đề thi nào phù hợp.</td></tr> : (
                        filteredLibraryTests.map((test, index) => (
                          <tr key={test.id} className={`hover:bg-slate-50 transition group bg-white ${selectedTests.includes(test.id) ? 'bg-blue-50/30' : ''}`}>
                            <td className="px-4 py-5 text-center text-[13px] font-bold text-slate-400">{index + 1}</td>
                            <td className="px-2 py-5"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.includes(test.id)} onChange={() => handleSelectOne(test.id)} /></td>
                            <td className="px-6 py-5"><div className="font-bold text-[#0a5482] text-[15px]">{test.title}</div><div className="text-[11px] text-slate-400 mt-1 font-medium uppercase tracking-tight">{test.folder_id ? 'Đã gán thư mục' : 'Chưa gán thư mục'}</div></td>
                            <td className="px-6 py-5">{test.course_id ? <span className="px-2 py-1 bg-slate-100 border border-slate-200 rounded text-[11px] font-bold text-slate-600">{getCourseNameForTest(test.course_id)}</span> : <span className="text-[11px] italic text-slate-400">-- Dùng chung --</span>}</td>
                            <td className="px-6 py-5 font-black text-blue-600 uppercase text-[11px] tracking-tight">{test.test_type}</td>
                            <td className="px-6 py-5"><div className="text-[11px] text-slate-500 font-medium">Tạo: {formatDateTime(test.created_at)}</div></td>
                            <td className="px-6 py-5 text-center"><button onClick={() => handleToggleTestVisibility(test)} className={`text-[12px] font-bold px-3 py-1 rounded transition-colors ${test.is_published ? 'text-emerald-600 bg-emerald-50 hover:bg-emerald-100' : 'text-slate-500 bg-slate-100 hover:bg-slate-200'}`}>{test.is_published ? 'Hiển thị' : 'Đang ẩn'}</button></td>
                            <td className="px-6 py-5 text-center"><input type="number" defaultValue={test.order_index || 0} onBlur={e => handleUpdateTestOrder(test.id, parseInt(e.target.value) || 0)} className="w-12 text-center text-[13px] font-bold border border-slate-200 rounded py-1 outline-none focus:border-[#2bd6eb]" /></td>
                            <td className="px-6 py-5 text-right space-x-2"><button onClick={() => setEditingTest(test)} className="text-[#2bd6eb] bg-white border border-[#2bd6eb] px-3 py-1.5 rounded hover:bg-blue-50 font-bold text-xs transition">Sửa</button><button onClick={() => handleDeleteTest(test.id)} className="text-red-500 font-bold text-xs bg-white border border-red-200 px-3 py-1.5 rounded hover:bg-red-50 transition opacity-0 group-hover:opacity-100">Xóa</button></td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'students' && <StudentManagement />}
        </div>

        {/* ========================================================================================= */}
        {/* CÁC MODALS */}
        {/* ========================================================================================= */}
        
        {showClassModal && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><form onSubmit={handleCreateClass} className="bg-white rounded-3xl w-full max-w-md p-8 space-y-6 animate-in zoom-in-95 shadow-2xl"><h2 className="text-lg font-black uppercase text-[#0a5482]">Thêm Lớp Mới</h2><input name="name" required autoFocus placeholder="VD: Lớp IELTS K20" className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:border-[#0a5482] transition-colors" /><div className="flex gap-4"><button type="button" onClick={() => setShowClassModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button><button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-3 rounded-xl shadow-lg">TẠO LỚP</button></div></form></div> )}
        
        {showAssignClassModuleModal && selectedClass && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><div className="bg-white rounded-3xl w-full max-w-lg shadow-2xl overflow-hidden animate-in fade-in"><div className="bg-[#0f172a] p-6 text-white flex justify-between items-center"><h2 className="font-black uppercase text-sm tracking-widest">Chọn học phần mở cho lớp</h2><button onClick={() => setShowAssignClassModuleModal(false)} className="text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button></div><div className="p-6 max-h-[60vh] overflow-y-auto space-y-3 custom-scrollbar">{lectureModules.filter(m => !classModules.includes(m.id)).map(mod => (<div key={mod.id} className="flex justify-between items-center p-4 border border-slate-200 rounded-xl bg-slate-50 hover:border-emerald-400 transition-colors"><p className="font-black text-slate-700 text-sm">{mod.title}</p><button onClick={() => handleAssignModuleToClass(mod.id)} className="bg-emerald-500 hover:bg-emerald-600 transition text-white px-5 py-2 rounded-xl font-bold text-xs shadow-sm">MỞ KHÓA ➜</button></div>))}{lectureModules.filter(m => !classModules.includes(m.id)).length === 0 && <p className="text-center text-slate-400 text-sm">Tất cả học phần của khóa học này đã được mở cho lớp.</p>}</div></div></div> )}
        
        {showAssignStudentModal && selectedClass && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><div className="bg-white rounded-3xl w-full max-w-lg shadow-2xl overflow-hidden animate-in fade-in"><div className="bg-[#0f172a] p-6 text-white flex justify-between items-center"><h2 className="font-black uppercase text-sm tracking-widest">Thêm Học Sinh Vào Lớp</h2><button onClick={() => setShowAssignStudentModal(false)} className="text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button></div><div className="p-6 max-h-[60vh] overflow-y-auto space-y-3 custom-scrollbar">{courseStudentsList.filter(cs => !classStudentsList.some(cls => cls.user_id === cs.user_id)).map(st => (<div key={st.user_id} className="flex justify-between items-center p-4 border border-slate-200 rounded-xl bg-slate-50 hover:border-blue-400 transition-colors"><div><p className="font-black text-slate-700 text-sm">{st.full_name || 'Học viên'}</p><p className="text-[11px] text-slate-500">{st.email}</p></div><button onClick={() => handleAssignStudentToClass(st.user_id)} className="bg-blue-500 hover:bg-blue-600 transition text-white px-5 py-2 rounded-xl font-bold text-xs shadow-sm">THÊM ➜</button></div>))}{courseStudentsList.filter(cs => !classStudentsList.some(cls => cls.user_id === cs.user_id)).length === 0 && (<p className="text-center text-slate-400 text-sm">Tất cả học sinh của khóa học đã nằm trong lớp này, hoặc Khóa học chưa có học sinh nào.</p>)}</div></div></div> )}
        
        {showAssignLectureModal.show && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><div className="bg-white rounded-3xl w-full max-w-xl shadow-2xl overflow-hidden animate-in fade-in"><div className="bg-[#0f172a] p-6 text-white flex justify-between items-center"><h2 className="font-black uppercase text-sm tracking-widest">Chọn bài giảng từ Kho chung</h2><button onClick={() => setShowAssignLectureModal({show: false, moduleId: null})} className="text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button></div><div className="p-6 max-h-[60vh] overflow-y-auto space-y-3 custom-scrollbar">{globalLectures.filter(l => !l.module_id && l.course_id === selectedCourse.id).map(lec => (<div key={lec.id} className="flex justify-between items-center p-4 border border-slate-100 rounded-2xl hover:border-blue-400 transition bg-slate-50"><p className="font-black text-slate-700 text-sm">{lec.title}</p><button onClick={() => handleAssignLecture(lec.id, showAssignLectureModal.moduleId!)} className="bg-blue-600 hover:bg-blue-700 transition text-white px-5 py-2 rounded-xl font-bold text-xs shadow-sm">GÁN ➜</button></div>))}{globalLectures.filter(l => !l.module_id && l.course_id === selectedCourse.id).length === 0 && <p className="text-center text-slate-400 text-sm italic">Không có bài giảng nào của khóa này chờ gán.</p>}</div></div></div> )}
        
        {showCreateCourseModal && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><form onSubmit={handleCreateCourse} className="bg-white rounded-3xl w-full max-w-md p-8 space-y-6 animate-in zoom-in-95 shadow-2xl"><h2 className="text-xl font-black text-slate-800 uppercase tracking-tight">Thêm Khóa Học Mới</h2><div className="space-y-4"><input name="title" required autoFocus placeholder="Tên khóa học..." className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:border-[#0a5482] transition-colors" /><select name="type" className="w-full border border-slate-200 rounded-xl px-4 py-3 bg-white outline-none"><option value="IELTS">Hệ IELTS</option><option value="Standard">Hệ Standard (IGCSE/TOEIC)</option></select></div><div className="flex gap-4"><button type="button" onClick={() => setShowCreateCourseModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button><button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-3 rounded-xl shadow-lg">LƯU</button></div></form></div> )}
        
        {showModuleModal && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><form onSubmit={handleCreateLectureModule} className="bg-white rounded-3xl w-full max-w-md p-8 space-y-6 animate-in zoom-in-95 shadow-2xl"><h2 className="text-lg font-black uppercase text-[#0a5482]">Thêm Học Phần Mới</h2><input name="title" required autoFocus placeholder="VD: Lesson 1: Grammar..." className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:border-[#0a5482] transition-colors" /><div className="flex gap-4"><button type="button" onClick={() => setShowModuleModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button><button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-3 rounded-xl shadow-lg">TẠO MỚI</button></div></form></div> )}
        
        {showFolderModal && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><form onSubmit={handleCreateFolder} className="bg-white rounded-3xl w-full max-w-md p-8 space-y-6 animate-in zoom-in-95 shadow-2xl"><h2 className="text-lg font-black uppercase text-emerald-600">{currentFolderId ? 'Thêm Thư Mục Con' : 'Thêm Thư Mục Cấp 1'}</h2><input name="title" required autoFocus placeholder="Tên thư mục đề thi..." className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:border-emerald-500 transition-colors" /><div className="flex gap-4"><button type="button" onClick={() => setShowFolderModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button><button type="submit" className="flex-1 bg-[#00a651] hover:bg-[#008f45] transition text-white font-black py-3 rounded-xl shadow-lg">TẠO MỚI</button></div></form></div> )}
        
        {showAssignModal && ( <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4"><div className="bg-white rounded-3xl w-full max-w-xl shadow-2xl overflow-hidden animate-in fade-in"><div className="bg-[#0f172a] p-6 text-white flex justify-between items-center"><h2 className="font-black uppercase text-sm tracking-widest">Chọn đề từ Kho (của khóa học này)</h2><button onClick={() => setShowAssignModal(false)} className="text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button></div><div className="p-6 max-h-[60vh] overflow-y-auto space-y-3 custom-scrollbar">{libraryTests.filter(t => !t.folder_id && t.course_id === selectedCourse.id).map(test => (<div key={test.id} className="flex justify-between items-center p-4 border border-slate-100 rounded-2xl hover:border-[#2bd6eb] transition bg-slate-50 group"><div><p className="font-black text-slate-700 text-sm">{test.title}</p><p className="text-[10px] font-black text-slate-400 uppercase tracking-tighter mt-1">{test.test_type}</p></div><button onClick={() => handleAssignTest(test.id)} className="bg-white group-hover:bg-[#2bd6eb] group-hover:text-white px-5 py-2 rounded-xl font-bold text-xs transition border border-slate-200 shadow-sm">GÁN ➜</button></div>))}{libraryTests.filter(t => !t.folder_id && t.course_id === selectedCourse.id).length === 0 && <p className="text-center text-slate-400 text-sm italic">Không có đề thi nào của khóa học này đang chờ gán.</p>}</div></div></div> )}
        
        {/* ========================================================================================= */}
        {/* CÁC MODAL EDITORS CHÍNH - QUAN TRỌNG NHẤT */}
        {/* ========================================================================================= */}
        {editingLecture && ( 
           <LectureEditorModal 
              lectureData={editingLecture} 
              courses={courses} 
              onClose={() => setEditingLecture(null)} 
              onRefresh={() => { fetchGlobalLectures(); if(selectedCourse) fetchCourseDetailsData(selectedCourse.id); }} 
           /> 
        )}
        
        {editingTest && ( 
           editingTest.test_type === 'Case-Study' || editingTest.mode === 'case-study' ? ( 
             <CaseStudyEditorModal 
                testData={editingTest} 
                courses={courses} 
                onClose={() => setEditingTest(null)} 
                onSave={(finalData: any) => handleSaveTestContent(editingTest.id, finalData)} 
             /> 
           ) : ( 
             <TestEditorModal 
                testData={editingTest} 
                courses={courses} 
                folders={allFolders} 
                onClose={() => setEditingTest(null)} 
                onSave={(finalData: any) => handleSaveTestContent(editingTest.id, finalData)} 
             /> 
           ) 
        )}

      </main>
    </div>
  );
}