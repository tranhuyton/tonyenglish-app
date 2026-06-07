import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import TestEditorModal from './TestEditorModal';
import CaseStudyEditorModal from './CaseStudyEditorModal'; 
import StudentManagement from './StudentManagement'; 
import LectureEditorModal from './LectureEditorModal';
import IgcseTestEditorModal from './IgcseTestEditorModal';
import './tailwind.css';

let adminSearchTimer: any;

export default function AdminPanel({ onNavigate, onStartTest }: { onNavigate?: (view: string) => void, onStartTest?: any }) {
  const [activeTab, setActiveTab] = useState('courses'); 
  const [showCreateDropdown, setShowCreateDropdown] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  // 🚀 TỐI ƯU MOBILE: State quản lý Sidebar trượt trên điện thoại
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

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
  
  const [selectedLectures, setSelectedLectures] = useState<string[]>([]);
  const [lectureCurrentPage, setLectureCurrentPage] = useState(1);
  const lectureItemsPerPage = 20;
  const [targetMoveCourseId, setTargetMoveCourseId] = useState('');
  const [targetMoveTestCourseId, setTargetMoveTestCourseId] = useState('');

  const [lectureModules, setLectureModules] = useState<any[]>([]);
  const [lectures, setLectures] = useState<any[]>([]);
  
  const [classes, setClasses] = useState<any[]>([]);
  const [selectedClass, setSelectedClass] = useState<any>(null);
  const [classModules, setClassModules] = useState<any[]>([]); 
  
  const [courseStudentsList, setCourseStudentsList] = useState<any[]>([]); 
  const [classStudentsList, setClassStudentsList] = useState<any[]>([]); 
  const [showAssignStudentModal, setShowAssignStudentModal] = useState(false); 
  
  // --- STORAGE & PDF MANAGEMENT STATES ---
  const [pdfFiles, setPdfFiles] = useState<any[]>([]);
  const [isUploadingPdf, setIsUploadingPdf] = useState(false);
  const [pdfSearchQuery, setPdfSearchQuery] = useState('');
  const [pdfSortOrder, setPdfSortOrder] = useState('date-desc'); 
  const fileInputRef = useRef<HTMLInputElement>(null);

  // 🚀 VIRTUAL FOLDERS SYSTEM FOR PDF
  const [pdfFolders, setPdfFolders] = useState<{id: string, name: string, parentId: string|null}[]>([]);
  const [pdfFileMapping, setPdfFileMapping] = useState<Record<string, string>>({}); // filename -> folderId
  const [currentPdfFolderId, setCurrentPdfFolderId] = useState<string | null>(null);
  const [showPdfFolderModal, setShowPdfFolderModal] = useState(false);
  const [editingPdfFolderId, setEditingPdfFolderId] = useState<string | null>(null);
  const [showMoveFileModal, setShowMoveFileModal] = useState<string | null>(null);

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
  const [filterCategory, setFilterCategory] = useState('all'); 
  const [sortTest, setSortTest] = useState('date-desc');
  const [sortLecture, setSortLecture] = useState('date-desc');
  const [selectedTests, setSelectedTests] = useState<string[]>([]);
  const [editingTest, setEditingTest] = useState<any>(null);
  const [igcseEditorOpen, setIgcseEditorOpen] = useState(false);
  const [igcseEditingTestId, setIgcseEditingTestId] = useState<string | null>(null);
  const [showCreateCourseModal, setShowCreateCourseModal] = useState(false);
  const [showFolderModal, setShowFolderModal] = useState(false);
  const [showAssignModal, setShowAssignModal] = useState(false);
  
  const [editingCourseId, setEditingCourseId] = useState<string | null>(null);
  const [editingClassId, setEditingClassId] = useState<string | null>(null);
  const [editingModuleId, setEditingModuleId] = useState<string | null>(null);
  const [editingFolderId, setEditingFolderId] = useState<string | null>(null);

  // 🚀 QUẢN LÝ DEADLINE CHO BÀI TẬP/ĐỀ THI
  const [deadlineModal, setDeadlineModal] = useState<{show: boolean, test: any}>({show: false, test: null});
  const [showAssignDeadlineModal, setShowAssignDeadlineModal] = useState(false);
  const [assignTestSearch, setAssignTestSearch] = useState('');
  const [assignTestSort, setAssignTestSort] = useState('date-desc');
  const [selectedDeadlineTests, setSelectedDeadlineTests] = useState<string[]>([]);
  const [deadlineInput, setDeadlineInput] = useState('');

  // 🚀 QUẢN LÝ CHUÔNG THÔNG BÁO TỪ HỌC VIÊN
  const [notifications, setNotifications] = useState<any[]>([]);
  const [showNotifications, setShowNotifications] = useState(false);
  const [unreadCount, setUnreadCount] = useState(0);
  const notifRef = useRef<HTMLDivElement>(null);
  const [viewingNotif, setViewingNotif] = useState<any>(null);
  const [notifTargetUserId, setNotifTargetUserId] = useState<string | null>(null);
  const [notifTargetTab, setNotifTargetTab] = useState<string | null>(null);

  const fetchNotifications = async () => {
    try {
        const { data: logs } = await supabase
            .from('activity_logs')
            .select('*')
            .order('created_at', { ascending: false })
            .limit(30);
            
        if (!logs) return;
        
        const userIds = [...new Set(logs.map(l => l.user_id))];
        const { data: profiles } = await supabase
            .from('profiles')
            .select('id, full_name, email')
            .in('id', userIds);
            
        const profileMap = (profiles || []).reduce((acc:any, p:any) => { 
            acc[p.id] = p; 
            return acc; 
        }, {});
        
        const enrichedLogs = logs.map(l => ({ ...l, user: profileMap[l.user_id] || {} }));
        setNotifications(enrichedLogs);
        setUnreadCount(enrichedLogs.filter(l => !l.is_read).length);
    } catch (e) {
        console.error("Lỗi lấy thông báo:", e);
    }
  };

  const markNotificationsAsRead = async () => {
    const unreadIds = notifications.filter(n => !n.is_read).map(n => n.id);
    if (unreadIds.length === 0) return;
    
    await supabase.from('activity_logs').update({ is_read: true }).in('id', unreadIds);
    setUnreadCount(0);
    setNotifications(prev => prev.map(n => ({...n, is_read: true})));
  };
  
  useEffect(() => {
    fetchCourses();
    fetchLibraryTests();
    fetchAllFolders(); 
    fetchGlobalLectures();
    fetchPdfFiles(); 
    fetchNotifications();

    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
          setShowCreateDropdown(false);
      }
      if (notifRef.current && !notifRef.current.contains(event.target as Node)) {
          setShowNotifications(false); 
      }
    };
    
    document.addEventListener('mousedown', handleClickOutside);
    const interval = setInterval(fetchNotifications, 10000); 
    
    return () => {
        document.removeEventListener('mousedown', handleClickOutside);
        clearInterval(interval);
    }
  }, []);

  useEffect(() => {
    setLectureCurrentPage(1);
  }, [searchQuery, filterLectureCourse]);

  const formatDateTime = (iso: string) => {
    if (!iso) return '';
    const d = new Date(iso);
    return `${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')} - ${d.getDate().toString().padStart(2, '0')}/${(d.getMonth()+1).toString().padStart(2, '0')}/${d.getFullYear()}`;
  }

  const getDefaultDateTime = (isoString: string) => {
      if (!isoString) return '';
      const date = new Date(isoString);
      return new Date(date.getTime() - date.getTimezoneOffset() * 60000).toISOString().slice(0,16);
  };

  // =========================================================================================
  // SUPABASE STORAGE LOGIC (QUẢN LÝ FILE PDF & FOLDER ẢO)
  // =========================================================================================
  const BUCKET_NAME = 'documents'; 

  const fetchVirtualFolders = async () => {
      try {
          const { data } = supabase.storage.from(BUCKET_NAME).getPublicUrl('_virtual_folders.json');
          const response = await fetch(`${data.publicUrl}?t=${new Date().getTime()}`, { cache: 'no-store' });
          if (response.ok) {
              const json = await response.json();
              setPdfFolders(json.folders || []);
              setPdfFileMapping(json.mapping || {});
          }
      } catch (e) {
          console.log("Chưa có cấu trúc thư mục ảo.");
      }
  };

  const saveVirtualFolders = async (newFolders: any[], newMapping: any) => {
      const jsonStr = JSON.stringify({ folders: newFolders, mapping: newMapping });
      const blob = new Blob([jsonStr], { type: 'application/json' });
      await supabase.storage.from(BUCKET_NAME).upload('_virtual_folders.json', blob, { upsert: true, cacheControl: '0' });
      setPdfFolders(newFolders);
      setPdfFileMapping(newMapping);
  };

  const fetchPdfFiles = async () => {
      try {
          await fetchVirtualFolders(); 
          const { data, error } = await supabase.storage.from(BUCKET_NAME).list('', { limit: 1000, offset: 0, sortBy: { column: 'created_at', order: 'desc' } });
          if (error) return;
          const filesOnly = data?.filter(f => f.id !== null && f.name !== '_virtual_folders.json') || [];
          const filesWithUrl = filesOnly.map(f => {
              const { data: publicUrlData } = supabase.storage.from(BUCKET_NAME).getPublicUrl(f.name);
              return { ...f, publicUrl: publicUrlData.publicUrl };
          });
          setPdfFiles(filesWithUrl);
      } catch (err) {
          console.error("Lỗi lấy PDF:", err);
      }
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
      const files = event.target.files;
      if (!files || files.length === 0) return;

      const validFiles: File[] = [];
      const invalidFiles: string[] = [];

      for (let i = 0; i < files.length; i++) {
          const file = files[i];
          if ((file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) || file.size > 50 * 1024 * 1024) {
              invalidFiles.push(file.name);
          } else {
              validFiles.push(file);
          }
      }

      if (validFiles.length === 0) {
          alert('Tất cả file đã chọn đều không hợp lệ!');
          if (fileInputRef.current) fileInputRef.current.value = ''; 
          return;
      }

      if (invalidFiles.length > 0) {
          if (!window.confirm(`Có ${invalidFiles.length} file không hợp lệ sẽ bị bỏ qua. Tiếp tục tải lên?`)) {
              if (fileInputRef.current) fileInputRef.current.value = '';
              return;
          }
      }

      setIsUploadingPdf(true);
      try {
          const newMapping = { ...pdfFileMapping };
          let uploadedCount = 0;

          await Promise.all(validFiles.map(async (file) => {
              const fileName = file.name.replace(/\s+/g, '_');
              const { error } = await supabase.storage.from(BUCKET_NAME).upload(fileName, file, { cacheControl: '3600', upsert: false });
              if (!error) {
                  uploadedCount++;
                  if (currentPdfFolderId) newMapping[fileName] = currentPdfFolderId;
              }
          }));
          
          if (currentPdfFolderId && uploadedCount > 0) {
              await saveVirtualFolders(pdfFolders, newMapping);
          }
          alert(`Tải lên thành công ${uploadedCount} file!`);
          fetchPdfFiles(); 
      } catch (error: any) {
          alert(`Lỗi khi tải file: ${error.message}`);
      } finally {
          setIsUploadingPdf(false);
          if (fileInputRef.current) fileInputRef.current.value = ''; 
      }
  };

  const handleDeleteFile = async (fileName: string) => {
      if (!window.confirm(`Xác nhận xóa file "${fileName}" vĩnh viễn?`)) return;
      try {
          const { error } = await supabase.storage.from(BUCKET_NAME).remove([fileName]);
          if (error) throw error;
          
          const newMapping = { ...pdfFileMapping };
          if (newMapping[fileName]) {
              delete newMapping[fileName];
              saveVirtualFolders(pdfFolders, newMapping);
          }
          fetchPdfFiles();
      } catch (error: any) {
          alert(`Lỗi khi xóa file: ${error.message}`);
      }
  };

  const handleCreatePdfFolder = async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      const name = new FormData(e.currentTarget).get('name') as string;
      const newFolder = { id: 'f_' + Date.now(), name, parentId: currentPdfFolderId };
      await saveVirtualFolders([...pdfFolders, newFolder], pdfFileMapping);
      setShowPdfFolderModal(false);
  };

  const handleUpdatePdfFolderName = async (folderId: string, newName: string) => {
      if (!newName.trim()) { setEditingPdfFolderId(null); return; }
      const newFolders = pdfFolders.map(f => f.id === folderId ? { ...f, name: newName } : f);
      await saveVirtualFolders(newFolders, pdfFileMapping);
      setEditingPdfFolderId(null);
  };

  const handleDeletePdfFolder = async (folderId: string) => {
      if (window.confirm("Xóa thư mục này? Các file bên trong sẽ được giữ nguyên và tự động chuyển về Thư mục gốc.")) {
          const newFolders = pdfFolders.filter(f => f.id !== folderId && f.parentId !== folderId);
          const newMapping = { ...pdfFileMapping };
          Object.keys(newMapping).forEach(key => {
              if (newMapping[key] === folderId) delete newMapping[key];
          });
          await saveVirtualFolders(newFolders, newMapping);
      }
  };

  const handleMovePdfFile = async (fileName: string, targetFolderId: string | null) => {
      const newMapping = { ...pdfFileMapping };
      if (targetFolderId) newMapping[fileName] = targetFolderId;
      else delete newMapping[fileName];
      
      await saveVirtualFolders(pdfFolders, newMapping);
      setShowMoveFileModal(null);
  };

  const copyToClipboard = (text: string) => {
      navigator.clipboard.writeText(text).then(() => {
          alert('Đã copy đường dẫn (URL) thành công!');
      });
  };

  const formatFileSize = (bytes: number) => {
      if (bytes === 0) return '0 Bytes';
      const k = 1024; const sizes = ['Bytes', 'KB', 'MB', 'GB'];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  // =========================================================================================

  const fetchCourses = async () => {
    setIsLoadingCourses(true); 
    const { data } = await supabase.from('courses').select('*').order('order_index', { ascending: true }).order('created_at', { ascending: false });
    setCourses(data || []);
    setIsLoadingCourses(false); 
  };

  const fetchLibraryTests = async () => {
    const { data } = await supabase.from('tests').select('id, title, course_id, folder_id, is_published, order_index, created_at, test_type').order('order_index', { ascending: true }).order('created_at', { ascending: false });
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
    } else {
      setLectures([]);
    }

    const { data: cls } = await supabase.from('classes').select('*').eq('course_id', courseId).order('created_at', { ascending: false });
    setClasses(cls || []);
    
    const { data: flds } = await supabase.from('folders').select('*').eq('course_id', courseId).order('display_order', { ascending: true });
    setFolders(flds || []);
    
    const { data: ast } = await supabase.from('tests').select('id, title, course_id, folder_id, is_published, order_index, created_at, test_type').eq('course_id', courseId).order('order_index', { ascending: true });
    setAssignedTests(ast || []);
    
    // Lazy-load content_json in background for deadline/category features
    if (ast && ast.length > 0) {
      const loadedCourseId = courseId; // Closure to detect stale responses
      supabase.from('tests').select('id, content_json').eq('course_id', courseId).then(({ data: cjData }) => {
        if (cjData && selectedCourse?.id === loadedCourseId) {
          const cjMap = new Map(cjData.map(c => [c.id, c.content_json]));
          setAssignedTests(prev => prev.map(t => {
            const cj = cjMap.get(t.id);
            return cj !== undefined ? { ...t, content_json: cj } : t;
          }));
        }
      });
    }

    const { data: enrolls } = await supabase.from('enrollments').select('user_id').eq('course_id', courseId);
    if (enrolls && enrolls.length > 0) {
       const userIds = enrolls.map(e => e.user_id);
       const { data: profiles } = await supabase.from('profiles').select('id, full_name, email').in('id', userIds);
       if (profiles) setCourseStudentsList(profiles.map(p => ({ user_id: p.id, full_name: p.full_name, email: p.email })));
    } else {
       setCourseStudentsList([]);
    }
  };

  // Lightweight refresh: only refetch assigned tests for current course (no modules/classes/enrollments)
  const refreshAssignedTestsOnly = async (courseId: string) => {
    const { data: ast } = await supabase.from('tests').select('id, title, course_id, folder_id, is_published, order_index, created_at, test_type').eq('course_id', courseId).order('order_index', { ascending: true });
    setAssignedTests(ast || []);
  };

  const fetchClassDetails = async (classId: string) => {
    const { data: modData } = await supabase.from('class_modules').select('module_id').eq('class_id', classId);
    if (modData) setClassModules(modData.map(d => d.module_id));

    const { data: stuData } = await supabase.from('class_students').select('user_id').eq('class_id', classId);
    if (stuData && stuData.length > 0) {
       const userIds = stuData.map(e => e.user_id);
       const { data: profiles } = await supabase.from('profiles').select('id, full_name, email').in('id', userIds);
       if (profiles) setClassStudentsList(profiles.map(p => ({ user_id: p.id, full_name: p.full_name, email: p.email })));
    } else {
       setClassStudentsList([]);
    }
  };

  const handleUpdateCourseOrder = async (id: string, newOrder: number) => {
    await supabase.from('courses').update({ order_index: newOrder }).eq('id', id); 
    fetchCourses();
  };

  const handleUpdateModuleOrder = async (id: string, newOrder: number) => {
    await supabase.from('lecture_modules').update({ order_index: newOrder }).eq('id', id); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleUpdateLectureOrder = async (id: string, newOrder: number) => {
    await supabase.from('lectures').update({ order_index: newOrder }).eq('id', id); 
    fetchGlobalLectures(); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleUpdateTestOrder = async (id: string, newOrder: number) => {
    await supabase.from('tests').update({ order_index: newOrder }).eq('id', id); 
    fetchLibraryTests(); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleUpdateFolderOrder = async (id: string, newOrder: number) => {
    await supabase.from('folders').update({ display_order: newOrder }).eq('id', id); 
    fetchAllFolders(); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleToggleLectureStatus = async (id: string, currentStatus: boolean) => {
    await supabase.from('lectures').update({ is_published: !currentStatus }).eq('id', id); 
    fetchGlobalLectures(); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  const handleAssignStudentToClass = async (userId: string) => {
     if (!selectedClass) return;
     await supabase.from('class_students').insert([{ class_id: selectedClass.id, user_id: userId }]); 
     fetchClassDetails(selectedClass.id);
  };

  const handleUnassignStudentFromClass = async (userId: string) => {
     if (!selectedClass) return;
     if (window.confirm("Gỡ học sinh này khỏi lớp?")) {
        await supabase.from('class_students').delete().match({ class_id: selectedClass.id, user_id: userId }); 
        fetchClassDetails(selectedClass.id);
     }
  };

  const handleCreateCourse = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const title = new FormData(e.currentTarget).get('title') as string;
    const type = new FormData(e.currentTarget).get('type') as string;
    const { data, error } = await supabase.from('courses').insert([{ title, type, order_index: courses.length + 1 }]).select();
    if (!error && data) { 
        fetchCourses(); 
        setShowCreateCourseModal(false); 
    }
  };
  
  const handleUpdateCourseInfo = async (courseId: string, newTitle: string, newType: string) => {
    if (!newTitle.trim()) { setEditingCourseId(null); return; }
    await supabase.from('courses').update({ title: newTitle, type: newType }).eq('id', courseId);
    fetchCourses();
    setEditingCourseId(null);
  };

  const handleDeleteCourse = async () => {
    if (window.confirm("Xác nhận xóa khóa học? Mọi dữ liệu (lớp, học phần, đề thi) bên trong sẽ bị xóa.") && selectedCourse) {
      await supabase.from('courses').delete().eq('id', selectedCourse.id); 
      fetchCourses(); 
      setActiveTab('courses');
    }
  };

  const handleUpdateModuleName = async (moduleId: string, newTitle: string) => {
    if (!newTitle.trim()) { setEditingModuleId(null); return; }
    await supabase.from('lecture_modules').update({ title: newTitle }).eq('id', moduleId);
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    setEditingModuleId(null);
  };

  const handleCreateLectureModule = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); 
    if (!selectedCourse) return;
    const title = (new FormData(e.currentTarget).get('title') as string);
    const { data } = await supabase.from('lecture_modules').insert([{ course_id: selectedCourse.id, title, order_index: lectureModules.length + 1 }]).select();
    if (data) { 
        fetchCourseDetailsData(selectedCourse.id); 
        setShowModuleModal(false); 
    }
  };

  const handleDeleteLectureModule = async (id: string) => {
    if (window.confirm("Xóa học phần này? Các bài giảng bên trong sẽ tự động trả về Kho tổng.")) {
      await supabase.from('lecture_modules').delete().eq('id', id); 
      fetchCourseDetailsData(selectedCourse.id); 
      fetchGlobalLectures();
    }
  };
  
  const handleAssignLecture = async (lectureId: string, moduleId: string) => {
    const { data: existingLecs } = await supabase.from('lectures').select('order_index').eq('module_id', moduleId);
    let maxOrder = 0;
    if (existingLecs && existingLecs.length > 0) {
        maxOrder = Math.max(...existingLecs.map(l => l.order_index || 0));
    }
    await supabase.from('lectures').update({ module_id: moduleId, order_index: maxOrder + 1 }).eq('id', lectureId);
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); 
    fetchGlobalLectures(); 
  };
  
  const handleUnassignLecture = async (lectureId: string) => {
    if (window.confirm("Gỡ bài giảng này về Kho Tổng?")) {
      await supabase.from('lectures').update({ module_id: null }).eq('id', lectureId);
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); 
      fetchGlobalLectures();
    }
  };

  const handlePermanentDeleteLecture = async (id: string) => {
    if (window.confirm("XÓA VĨNH VIỄN bài giảng khỏi hệ thống? Sẽ không thể khôi phục!")) {
      await supabase.from('lectures').delete().eq('id', id); 
      fetchGlobalLectures(); 
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    }
  };

  const handleDuplicateLecture = async (lectureData: any) => {
    const { data: newLecture, error: lecErr } = await supabase.from('lectures').insert([{ 
       title: lectureData.title + ' (Bản sao)', 
       course_id: lectureData.course_id, 
       module_id: null, 
       order_index: globalLectures.length + 1 
    }]).select().single();

    if (lecErr) return alert("Lỗi nhân bản bài giảng!");

    const { data: pages } = await supabase.from('lecture_pages').select('*').eq('lecture_id', lectureData.id);
    if (pages && pages.length > 0) {
       const newPages = pages.map(p => ({ 
           lecture_id: newLecture.id, 
           page_number: p.page_number, 
           content_html: p.content_html 
       }));
       await supabase.from('lecture_pages').insert(newPages);
    }
    fetchGlobalLectures(); 
    alert("✅ Đã nhân bản bài giảng thành công! Bản sao đã được lưu vào Kho.");
  };

  const handleSelectAllLectures = (e: React.ChangeEvent<HTMLInputElement>, currentList: any[]) => {
    if (e.target.checked) setSelectedLectures(currentList.map(l => l.id));
    else setSelectedLectures([]);
  };

  const handleSelectOneLecture = (id: string) => {
    if (selectedLectures.includes(id)) setSelectedLectures(selectedLectures.filter(l => l !== id));
    else setSelectedLectures([...selectedLectures, id]);
  };

  const handleBulkLectureVisibility = async (status: boolean) => {
    if (selectedLectures.length === 0) return alert("Vui lòng chọn ít nhất 1 bài giảng!");
    await supabase.from('lectures').update({ is_published: status }).in('id', selectedLectures);
    fetchGlobalLectures();
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
    setSelectedLectures([]);
  };

  const handleBulkLectureDelete = async () => {
    if (selectedLectures.length === 0) return alert("Vui lòng chọn ít nhất 1 bài giảng!");
    if (window.confirm(`Xác nhận xóa VĨNH VIỄN ${selectedLectures.length} bài giảng đã chọn?`)) {
      await supabase.from('lectures').delete().in('id', selectedLectures);
      fetchGlobalLectures();
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
      setSelectedLectures([]);
    }
  };

  const handleBulkMoveCourse = async () => {
    if (selectedLectures.length === 0) return alert("Vui lòng chọn ít nhất 1 bài giảng!");
    if (!targetMoveCourseId) return alert("Vui lòng chọn khóa học đích để chuyển tới!");
    if (window.confirm(`Chuyển ${selectedLectures.length} bài giảng sang khóa học đã chọn?`)) {
      await supabase.from('lectures').update({ 
         course_id: targetMoveCourseId === 'none' ? null : targetMoveCourseId,
         module_id: null 
      }).in('id', selectedLectures);
      
      fetchGlobalLectures();
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
      setSelectedLectures([]);
      setTargetMoveCourseId('');
      alert("✅ Chuyển danh mục thành công!");
    }
  };

  const handleUpdateClassName = async (classId: string, newName: string) => {
    if (!newName.trim()) { setEditingClassId(null); return; }
    await supabase.from('classes').update({ name: newName }).eq('id', classId);
    setClasses(classes.map(c => c.id === classId ? { ...c, name: newName } : c));
    if (selectedClass?.id === classId) setSelectedClass({ ...selectedClass, name: newName });
    setEditingClassId(null);
  };

  const handleCreateClass = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault(); 
    if (!selectedCourse) return;
    const name = (new FormData(e.currentTarget).get('name') as string);
    const { data } = await supabase.from('classes').insert([{ course_id: selectedCourse.id, name }]).select();
    if (data) { setClasses([data[0], ...classes]); setShowClassModal(false); }
  };

  const handleDeleteClass = async (id: string) => {
    if (window.confirm("Xóa lớp học này? (Dữ liệu học viên trong lớp sẽ bị ảnh hưởng)")) {
      await supabase.from('classes').delete().eq('id', id); 
      setClasses(classes.filter(c => c.id !== id)); 
      if (selectedClass?.id === id) setSelectedClass(null);
    }
  };

  const handleAssignModuleToClass = async (moduleId: string) => {
    if (!selectedClass) return;
    await supabase.from('class_modules').insert([{ class_id: selectedClass.id, module_id: moduleId }]); 
    fetchClassDetails(selectedClass.id);
  };

  const handleUnassignModuleFromClass = async (moduleId: string) => {
    if (!selectedClass) return;
    await supabase.from('class_modules').delete().match({ class_id: selectedClass.id, module_id: moduleId }); 
    fetchClassDetails(selectedClass.id);
  };

  const handleInitiateTest = (mode: 'manual' | 'import' | 'case-study') => {
    setShowCreateDropdown(false);
    setEditingTest({ 
        id: 'new', 
        title: '', 
        folder_id: currentFolderId || '', 
        test_type: mode === 'case-study' ? 'Case-Study' : 'IELTS-Listening', 
        content_json: null, 
        mode 
    });
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
       folder_id: finalData.folder_id !== undefined ? finalData.folder_id : (editingTest?.folder_id || currentFolderId || null), 
       course_id: assignedCourseId, 
       is_published: true, 
       insert_pdf_url: finalData.basicInfo?.insert_pdf_url || null 
    };
    
    if (testId === 'new') {
       payload.order_index = 0;
       const { error } = await supabase.from('tests').insert([payload]);
       if (error) { console.error(error); alert("Lỗi khi lưu: " + error.message); return; }
    } else {
       const { error } = await supabase.from('tests').update(payload).eq('id', testId);
       if (error) { console.error(error); alert("Lỗi khi cập nhật: " + error.message); return; }
    }
    
    setEditingTest(null); 
    fetchLibraryTests(); 
    if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
  };

  // 🚀 LƯU DEADLINE CHỈNH SỬA NHANH CHO 1 BÀI TẬP
  const handleSaveDeadline = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const datetime = new FormData(e.currentTarget).get('datetime') as string;
    const test = deadlineModal.test;
    if (!test || !selectedClass) return;

    const newContent = { ...(test.content_json || {}) };
    if (!newContent.basicInfo) newContent.basicInfo = {};
    if (!newContent.basicInfo.classDeadlines) newContent.basicInfo.classDeadlines = {};
    
    if (datetime) {
        newContent.basicInfo.classDeadlines[selectedClass.id] = new Date(datetime).toISOString();
    } else {
        delete newContent.basicInfo.classDeadlines[selectedClass.id];
    }
    
    await supabase.from('tests').update({ content_json: newContent }).eq('id', test.id);
    
    setAssignedTests(prev => prev.map(t => t.id === test.id ? { ...t, content_json: newContent } : t));
    setDeadlineModal({show: false, test: null});
    alert("✅ Đã cập nhật hạn nộp bài thành công!");
  };

  // 🚀 LƯU HÀNG LOẠT DEADLINE CÁC ĐỀ TỪ POPUP
  const handleSaveBulkDeadline = async () => {
    if (selectedDeadlineTests.length === 0) return alert("Vui lòng chọn ít nhất 1 bài tập/đề thi!");
    if (!selectedClass) return;

    const isRemoving = !deadlineInput;
    const updatedTests = assignedTests.map(t => {
        if (selectedDeadlineTests.includes(t.id)) {
            const newContent = { ...(t.content_json || {}) };
            if (!newContent.basicInfo) newContent.basicInfo = {};
            if (!newContent.basicInfo.classDeadlines) newContent.basicInfo.classDeadlines = {};
            
            if (!isRemoving) {
                newContent.basicInfo.classDeadlines[selectedClass.id] = new Date(deadlineInput).toISOString();
            } else {
                delete newContent.basicInfo.classDeadlines[selectedClass.id];
            }
            return { ...t, content_json: newContent };
        }
        return t;
    });

    setAssignedTests(updatedTests);
    
    try {
        for (const t of updatedTests.filter(testItem => selectedDeadlineTests.includes(testItem.id))) {
            await supabase.from('tests').update({ content_json: t.content_json }).eq('id', t.id);
        }
        alert(isRemoving ? "✅ Đã gỡ hạn nộp bài thành công!" : "✅ Đã cài đặt hạn nộp bài thành công!");
        setSelectedDeadlineTests([]); 
    } catch (err: any) {
        alert("❌ Có lỗi xảy ra: " + err.message);
    }
  };

  const handleSelectAllDeadlineTests = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.checked) setSelectedDeadlineTests(filteredAssignTests.map(t => t.id));
    else setSelectedDeadlineTests([]);
  };

  const handleSelectOneDeadlineTest = (id: string) => {
    if (selectedDeadlineTests.includes(id)) setSelectedDeadlineTests(selectedDeadlineTests.filter(t => t !== id));
    else setSelectedDeadlineTests([...selectedDeadlineTests, id]);
  };

  const handleUpdateFolderName = async (folderId: string, newTitle: string) => {
    if (!newTitle.trim()) { setEditingFolderId(null); return; }
    await supabase.from('folders').update({ title: newTitle }).eq('id', folderId);
    setFolders(folders.map(f => f.id === folderId ? { ...f, title: newTitle } : f)); fetchAllFolders(); setEditingFolderId(null);
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
    
    // Optimistic update: immediately move test to folder in UI
    const testToAssign = libraryTests.find(t => t.id === testId);
    if (testToAssign) {
      const updatedTest = { ...testToAssign, folder_id: currentFolderId };
      setAssignedTests(prev => {
        const exists = prev.some(t => t.id === testId);
        if (exists) return prev.map(t => t.id === testId ? updatedTest : t);
        return [...prev, updatedTest];
      });
      setLibraryTests(prev => prev.map(t => t.id === testId ? updatedTest : t));
    }
    
    // Persist to DB (non-blocking for UI)
    supabase.from('tests').update({ folder_id: currentFolderId }).eq('id', testId).then(() => {
      // Lightweight background sync
      fetchLibraryTests();
      if (selectedCourse) refreshAssignedTestsOnly(selectedCourse.id);
    });
  };

  const handleUnassignTest = async (testId: string) => {
    if (window.confirm("Gỡ đề thi khỏi thư mục này? Đề sẽ trở về Kho Tổng.")) {
      // Optimistic update: immediately remove from folder
      setAssignedTests(prev => prev.map(t => t.id === testId ? { ...t, folder_id: null } : t));
      setLibraryTests(prev => prev.map(t => t.id === testId ? { ...t, folder_id: null } : t));
      
      // Persist to DB (non-blocking)
      supabase.from('tests').update({ folder_id: null }).eq('id', testId).then(() => {
        fetchLibraryTests();
        if (selectedCourse) refreshAssignedTestsOnly(selectedCourse.id);
      });
    }
  };

  const handleDeleteTest = async (id: string) => {
    if (window.confirm("Xóa vĩnh viễn đề thi khỏi kho?")) {
      // Optimistic update
      setLibraryTests(prev => prev.filter(t => t.id !== id));
      setAssignedTests(prev => prev.filter(t => t.id !== id));
      // Persist
      await supabase.from('tests').delete().eq('id', id);
    }
  };

  const handleDuplicateTest = async (testData: any) => {
    // Fetch full test data to ensure all fields are available
    const { data: fullTest } = await supabase.from('tests').select('*').eq('id', testData.id).single();
    if (!fullTest) return alert("Lỗi tải dữ liệu đề thi gốc!");
    
    const { data: newTest, error: err } = await supabase.from('tests').insert([{ 
       title: fullTest.title + ' (Bản sao)', 
       course_id: fullTest.course_id, 
       folder_id: fullTest.folder_id, 
       test_type: fullTest.test_type,
       content_json: fullTest.content_json,
       json_config: fullTest.json_config,
       insert_pdf_url: fullTest.insert_pdf_url,
       pdf_url: fullTest.pdf_url,
       skill: fullTest.skill,
       time_limit: fullTest.time_limit,
       is_published: false,
       order_index: libraryTests.length + 1 
    }]).select().single();

    if (err) return alert("Lỗi nhân bản đề thi!");
    fetchLibraryTests();
    alert("✨ Đã nhân bản đề thi thành công!");
  };

  const handleToggleTestVisibility = async (test: any) => {
    const newStatus = !test.is_published;
    // Optimistic update both lists
    setLibraryTests(prev => prev.map(t => t.id === test.id ? { ...t, is_published: newStatus } : t));
    setAssignedTests(prev => prev.map(t => t.id === test.id ? { ...t, is_published: newStatus } : t));
    // Non-blocking persist
    supabase.from('tests').update({ is_published: newStatus }).eq('id', test.id);
  };

  const handleBulkVisibility = async (status: boolean) => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi/bài tập!");
    const ids = new Set(selectedTests);
    // Optimistic update
    setLibraryTests(prev => prev.map(t => ids.has(t.id) ? { ...t, is_published: status } : t));
    setAssignedTests(prev => prev.map(t => ids.has(t.id) ? { ...t, is_published: status } : t));
    setSelectedTests([]);
    // Persist
    supabase.from('tests').update({ is_published: status }).in('id', [...ids]);
  };

  const handleBulkDelete = async () => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 mục!");
    if (window.confirm(`Xác nhận xóa vĩnh viễn ${selectedTests.length} mục đã chọn?`)) {
      const ids = new Set(selectedTests);
      // Optimistic update
      setLibraryTests(prev => prev.filter(t => !ids.has(t.id)));
      setAssignedTests(prev => prev.filter(t => !ids.has(t.id)));
      setSelectedTests([]);
      // Persist
      await supabase.from('tests').delete().in('id', [...ids]);
    }
  };

  const handleBulkDuplicateTests = async () => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi/bài tập!");
    if (!window.confirm(`Nhân bản ${selectedTests.length} đề thi đã chọn?`)) return;
    let successCount = 0;
    for (const testId of selectedTests) {
      const { data: fullTest } = await supabase.from('tests').select('*').eq('id', testId).single();
      if (!fullTest) continue;
      const { id, created_at, ...rest } = fullTest;
      const { error } = await supabase.from('tests').insert([{
        ...rest,
        title: fullTest.title + ' (Bản sao)',
        folder_id: null,
        is_published: false,
        order_index: libraryTests.length + successCount + 1
      }]);
      if (!error) successCount++;
    }
    fetchLibraryTests(); setSelectedTests([]);
    alert(`✅ Đã nhân bản thành công ${successCount}/${selectedTests.length} đề thi!`);
  };

  const handleBulkMoveTestCourse = async () => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi/bài tập!");
    if (!targetMoveTestCourseId) return alert("Vui lòng chọn khóa học đích để chuyển tới!");
    if (window.confirm(`Chuyển ${selectedTests.length} đề thi sang khóa học đã chọn?`)) {
      await supabase.from('tests').update({
        course_id: targetMoveTestCourseId === 'none' ? null : targetMoveTestCourseId,
        folder_id: null
      }).in('id', selectedTests);
      fetchLibraryTests();
      if (selectedCourse) fetchCourseDetailsData(selectedCourse.id);
      setSelectedTests([]);
      setTargetMoveTestCourseId('');
      alert("✅ Chuyển khóa học thành công!");
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

  // Course Test Folders
  const breadcrumbs = []; let curr = folders.find(f => f.id === currentFolderId);
  while (curr) { breadcrumbs.unshift(curr); curr = folders.find(f => f.id === curr.parent_id); }
  
  const currentSubFolders = useMemo(() => {
      return folders.filter(f => currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')).sort((a,b) => (a.display_order||0) - (b.display_order||0));
  }, [folders, currentFolderId]);
  
  const currentTests = useMemo(() => { return assignedTests.filter(t => t.folder_id === currentFolderId); }, [assignedTests, currentFolderId]);

  // LỌC CÁC BÀI TẬP ĐƯỢC GIAO CÓ DEADLINE CHO LỚP HIỆN TẠI
  const classAssignedTests = useMemo(() => {
      if (!selectedClass) return [];
      return assignedTests.filter(t => t.content_json?.basicInfo?.classDeadlines?.[selectedClass.id]);
  }, [assignedTests, selectedClass]);

  // PDF Folders Breadcrumbs
  const pdfBreadcrumbs = [];
  let pCurr = pdfFolders.find(f => f.id === currentPdfFolderId);
  while (pCurr) { pdfBreadcrumbs.unshift(pCurr); pCurr = pdfFolders.find(f => f.id === pCurr.parentId); }
  const currentPdfSubFolders = pdfFolders.filter(f => currentPdfFolderId ? f.parentId === currentPdfFolderId : !f.parentId);
  
  // TỐI ƯU SEARCH TÀI LIỆU VÀ SẮP XẾP BỘ LỌC TÀI LIỆU PDF
  const isSearchingPdf = pdfSearchQuery.trim().length > 0;
  const filteredPdfFiles = useMemo(() => {
      let result = pdfFiles.filter(f => f.name.toLowerCase().includes(pdfSearchQuery.toLowerCase()));
      result = result.sort((a, b) => {
          if (pdfSortOrder === 'name-asc') return a.name.localeCompare(b.name);
          if (pdfSortOrder === 'name-desc') return b.name.localeCompare(a.name);
          if (pdfSortOrder === 'date-desc') return new Date(b.created_at).getTime() - new Date(a.created_at).getTime();
          if (pdfSortOrder === 'date-asc') return new Date(a.created_at).getTime() - new Date(b.created_at).getTime();
          if (pdfSortOrder === 'size-desc') return (b.metadata?.size || 0) - (a.metadata?.size || 0);
          if (pdfSortOrder === 'size-asc') return (a.metadata?.size || 0) - (b.metadata?.size || 0);
          return 0;
      });
      return result;
  }, [pdfFiles, pdfSearchQuery, pdfSortOrder]);

  const currentPdfFiles = filteredPdfFiles.filter(f => isSearchingPdf ? true : ((pdfFileMapping[f.name] || null) === currentPdfFolderId));

  const filteredLibraryTests = useMemo(() => {
      let result = libraryTests.filter(test => {
          const matchesSearch = test.title.toLowerCase().includes(searchQuery.toLowerCase());
          const matchesCourse = filterCourse === 'all' || test.course_id === filterCourse;
          const matchesCategory = filterCategory === 'all';
          return matchesSearch && matchesCourse && matchesCategory;
      });
      result = [...result].sort((a, b) => {
          if (sortTest === 'name-asc') return (a.title || '').localeCompare(b.title || '');
          if (sortTest === 'name-desc') return (b.title || '').localeCompare(a.title || '');
          if (sortTest === 'date-desc') return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime();
          if (sortTest === 'date-asc') return new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime();
          if (sortTest === 'type') return (a.test_type || '').localeCompare(b.test_type || '');
          return 0;
      });
      return result;
  }, [libraryTests, searchQuery, filterCourse, filterCategory, sortTest]);

  const filteredGlobalLectures = useMemo(() => {
      let result = globalLectures.filter(lec => {
          const matchesSearch = lec.title.toLowerCase().includes(searchQuery.toLowerCase());
          if (filterLectureCourse === 'all') return matchesSearch;
          return matchesSearch && lec.course_id === filterLectureCourse;
      });
      result = [...result].sort((a, b) => {
          if (sortLecture === 'name-asc') return (a.title || '').localeCompare(b.title || '');
          if (sortLecture === 'name-desc') return (b.title || '').localeCompare(a.title || '');
          if (sortLecture === 'date-desc') return new Date(b.updated_at || b.created_at || 0).getTime() - new Date(a.updated_at || a.created_at || 0).getTime();
          if (sortLecture === 'date-asc') return new Date(a.updated_at || a.created_at || 0).getTime() - new Date(b.updated_at || b.created_at || 0).getTime();
          return 0;
      });
      return result;
  }, [globalLectures, searchQuery, filterLectureCourse, sortLecture]);

  const totalLecturePages = Math.ceil(filteredGlobalLectures.length / lectureItemsPerPage);
  const paginatedLectures = filteredGlobalLectures.slice((lectureCurrentPage - 1) * lectureItemsPerPage, lectureCurrentPage * lectureItemsPerPage);

  // 🚀 TỐI ƯU SEARCH VÀ SORT CHO BẢNG GIAO DEADLINE POPUP
  const filteredAssignTests = useMemo(() => {
      let result = assignedTests.filter(t => (t.title || '').toLowerCase().includes(assignTestSearch.toLowerCase()));
      result = result.sort((a, b) => {
          if (assignTestSort === 'name-asc') return (a.title || '').localeCompare(b.title || '');
          if (assignTestSort === 'name-desc') return (b.title || '').localeCompare(a.title || '');
          if (assignTestSort === 'date-desc') return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime();
          if (assignTestSort === 'date-asc') return new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime();
          return 0;
      });
      return result;
  }, [assignedTests, assignTestSearch, assignTestSort]);

  return (
    <div className="h-[100dvh] bg-[#f8fafc] flex font-sans text-slate-800 overflow-hidden relative overscroll-none">
      
      {isSidebarOpen && (
        <div className="fixed inset-0 bg-slate-900/60 z-40 md:hidden transition-opacity" onClick={() => setIsSidebarOpen(false)} />
      )}

      <aside className={`fixed md:relative inset-y-0 left-0 z-50 h-[100dvh] w-[260px] md:w-64 bg-[#1e293b] text-slate-300 flex flex-col shrink-0 shadow-2xl md:shadow-xl transition-transform duration-300 ease-in-out ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}`}>
        <div className="h-16 md:h-20 flex items-center justify-between px-6 bg-[#0f172a] border-b border-slate-800 shrink-0">
          <div className="font-black text-xl tracking-tight text-white uppercase mt-1 cursor-pointer" onClick={() => onNavigate?.('home')}>TONY<span className="text-[#2bd6eb]">ADMIN</span></div>
          <button onClick={() => setIsSidebarOpen(false)} className="md:hidden text-slate-400 hover:text-white text-2xl font-bold">&times;</button>
        </div>
        <div className="p-4 space-y-1 flex-1 overflow-y-auto custom-scrollbar" style={{ WebkitOverflowScrolling: 'touch' }}>
          <p className="text-[10px] font-black uppercase text-slate-500 tracking-widest ml-3 mb-2 mt-4">Hệ thống LMS</p>
          <button onClick={() => {setActiveTab('courses'); setSelectedCourse(null); setIsSidebarOpen(false);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'courses' || activeTab === 'course-detail' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📁 Khóa học & Lớp</button>
          <button onClick={() => {setActiveTab('library'); setIsSidebarOpen(false);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'library' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📚 Kho Đề thi & Bài tập</button>
          <button onClick={() => {setActiveTab('lectures-library'); setIsSidebarOpen(false);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'lectures-library' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📖 Kho Bài giảng</button>
          <button onClick={() => {setActiveTab('documents'); setIsSidebarOpen(false);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'documents' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>☁️ Quản lý Tài Liệu (PDF)</button>
          <button onClick={() => {setActiveTab('students'); setIsSidebarOpen(false);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'students' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>👨‍🎓 Quản lý học viên</button>
        </div>
      </aside>

      <main className="flex-1 flex flex-col min-w-0 relative h-[100dvh] overflow-hidden">
        
        <header className="h-16 md:h-20 bg-white border-b border-slate-200 px-4 md:px-8 flex items-center justify-between sticky top-0 z-30 shadow-sm shrink-0">
          <div className="flex items-center gap-3 min-w-0">
             <button onClick={() => setIsSidebarOpen(true)} className="md:hidden text-slate-500 hover:text-slate-800 p-1 -ml-1">
               <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" /></svg>
             </button>
             <h1 className="text-[16px] md:text-xl font-black text-slate-800 uppercase tracking-tight truncate">
               {activeTab === 'courses' ? 'Khóa học' : activeTab === 'course-detail' ? 'Chi tiết' : activeTab === 'lectures-library' ? 'Kho Bài Giảng' : activeTab === 'library' ? 'Kho Đề & Bài tập' : activeTab === 'documents' ? 'Tài Liệu Cloud' : 'Học viên'}
             </h1>
          </div>
          
          <div className="flex items-center gap-2 md:gap-4 shrink-0">
            <div className="relative shrink-0 mr-2" ref={notifRef}>
                <button onClick={() => { setShowNotifications(!showNotifications); if(!showNotifications) markNotificationsAsRead(); }} className="relative p-2 text-slate-400 hover:text-[#2bd6eb] transition-colors">
                    <span className="text-xl md:text-2xl">🔔</span>
                    {unreadCount > 0 && <span className="absolute top-1 right-1 w-4 h-4 bg-red-500 text-white text-[10px] font-bold rounded-full flex items-center justify-center animate-pulse">{unreadCount}</span>}
                </button>
                {showNotifications && (
                    <div className="absolute right-0 mt-2 w-[320px] bg-white border border-slate-200 rounded-2xl shadow-2xl z-50 py-2 animate-in fade-in zoom-in-95 overflow-hidden">
                        <div className="px-4 py-3 border-b border-slate-100 flex justify-between items-center bg-slate-50">
                            <h3 className="font-black text-slate-800 text-[13px] uppercase tracking-widest">Thông báo hoạt động</h3>
                        </div>
                        <div className="max-h-[60vh] overflow-y-auto custom-scrollbar">
                            {notifications.length === 0 ? (
                                <div className="p-6 text-center text-slate-400 text-sm font-medium">Chưa có thông báo nào.</div>
                            ) : (
                                notifications.map(notif => (
                                    <div key={notif.id} onClick={() => {
                                        setShowNotifications(false);
                                        // Determine which tab to auto-open based on action type
                                        const targetTab = notif.action_type === 'finish_test' ? 'history' : 'activity';
                                        setNotifTargetUserId(notif.user_id);
                                        setNotifTargetTab(targetTab);
                                        setActiveTab('students');
                                    }} className={`p-4 border-b border-slate-50 hover:bg-slate-100 transition-colors cursor-pointer ${!notif.is_read ? 'bg-blue-50/30' : ''}`}>
                                        <p className="text-[13px] text-slate-700 leading-snug">
                                            <span className="font-bold text-[#0a5482]">{notif.user?.full_name || notif.user?.email || 'Học viên'}</span>
                                            {notif.action_type === 'login' && ' vừa đăng nhập vào hệ thống.'}
                                            {notif.action_type === 'finish_test' && ` vừa nộp bài: "${notif.details?.test_title}"`}
                                            {notif.action_type === 'call_tutor' && ` vừa gọi Gia Sư AI (${notif.details?.duration || 0} giây).`}
                                            {notif.action_type === 'finish_lecture' && ` vừa hoàn thành bài giảng: "${notif.details?.lecture_title}"`}
                                        </p>
                                        <span className="text-[10px] text-slate-400 mt-1 block font-bold">{formatDateTime(notif.created_at)}</span>
                                    </div>
                                ))
                            )}
                        </div>
                    </div>
                )}
            </div>

            {activeTab === 'courses' && <button onClick={() => setShowCreateCourseModal(true)} className="bg-[#0a5482] text-white font-black px-3 py-1.5 md:px-6 md:py-2.5 rounded-lg md:rounded-xl shadow-md text-[11px] md:text-sm transition hover:bg-[#084266] whitespace-nowrap">+ THÊM</button>}
            {activeTab === 'lectures-library' && <button onClick={() => setEditingLecture({ id: 'new', title: '', course_id: null })} className="bg-[#00a651] text-white font-black px-3 py-1.5 md:px-6 md:py-2.5 rounded-lg md:rounded-xl shadow-md text-[11px] md:text-sm transition hover:bg-[#008f45] whitespace-nowrap">+ BÀI GIẢNG</button>}
            
            {activeTab === 'documents' && (
                <div>
                   <input type="file" accept="application/pdf" multiple className="hidden" ref={fileInputRef} onChange={handleFileUpload} />
                   <button disabled={isUploadingPdf} onClick={() => fileInputRef.current?.click()} className="bg-[#2bd6eb] text-white font-black px-3 py-1.5 md:px-6 md:py-2.5 rounded-lg md:rounded-xl shadow-md text-[11px] md:text-sm transition hover:bg-[#1bc1d6] whitespace-nowrap disabled:opacity-50">
                      {isUploadingPdf ? '⏳ ĐANG TẢI...' : '+ UPLOAD PDF'}
                   </button>
                </div>
            )}

            {activeTab === 'library' && (
              <div className="relative shrink-0" ref={dropdownRef}>
                <button onClick={() => setShowCreateDropdown(!showCreateDropdown)} className="bg-[#2bd6eb] text-white font-black px-3 py-1.5 md:px-6 md:py-2.5 rounded-lg md:rounded-xl shadow-md flex items-center gap-1.5 md:gap-2 text-[11px] md:text-sm transition hover:bg-[#1bc1d6] whitespace-nowrap">+ TẠO MỚI <span className={`text-[9px] md:text-[10px] transition-transform ${showCreateDropdown ? 'rotate-180' : ''}`}>▼</span></button>
                {showCreateDropdown && (
                  <div className="absolute right-0 mt-2 w-56 md:w-64 max-w-[calc(100vw-2rem)] bg-white border border-slate-200 rounded-2xl shadow-2xl z-50 py-2 animate-in fade-in zoom-in-95">
                    <button onClick={() => handleInitiateTest('manual')} className="w-full text-left px-4 md:px-5 py-2.5 md:py-3 hover:bg-slate-50 font-bold text-[12px] md:text-[13px] border-b border-slate-100">✍️ Tạo thủ công (Standard)</button>
                    <button onClick={() => handleInitiateTest('case-study')} className="w-full text-left px-4 md:px-5 py-2.5 md:py-3 hover:bg-blue-50 font-bold text-[12px] md:text-[13px] text-[#0a5482] border-b border-slate-100">📄 Tạo Case Study</button>
                    <button onClick={() => { setShowCreateDropdown(false); setIgcseEditingTestId(null); setIgcseEditorOpen(true); }} className="w-full text-left px-4 md:px-5 py-2.5 md:py-3 hover:bg-emerald-50 font-bold text-[12px] md:text-[13px] text-emerald-700 border-b border-slate-100">🔬 Tạo đề IGCSE (Science/Math)</button>
                    <button onClick={() => handleInitiateTest('import')} className="w-full text-left px-4 md:px-5 py-2.5 md:py-3 hover:bg-slate-50 font-bold text-[12px] md:text-[13px]">📥 Import Excel/CSV</button>
                  </div>
                )}
              </div>
            )}
          </div>
        </header>

        <div className="flex-1 p-4 md:p-8 overflow-y-auto custom-scrollbar" style={{ WebkitOverflowScrolling: 'touch' }}>
          
          {/* VIEW: DANH SÁCH KHÓA HỌC */}
          {activeTab === 'courses' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6">
              {isLoadingCourses ? ( <div className="text-slate-400">Đang tải...</div> ) : (
                courses.map(course => (
                  <div key={course.id} className="bg-white rounded-2xl p-5 md:p-6 border border-slate-200 shadow-sm hover:shadow-xl transition-all group flex flex-col min-h-[160px] md:h-48 relative">
                    <div className="flex justify-between items-start">
                       <span className="px-2.5 py-1 rounded-md text-[10px] font-black uppercase bg-blue-100 text-blue-700">{course.type}</span>
                       <div className="flex items-center gap-2 md:gap-3">
                         <button onClick={(e) => { e.stopPropagation(); setEditingCourseId(course.id); }} className="md:opacity-0 group-hover:opacity-100 text-slate-400 hover:text-[#0a5482] transition-opacity p-1">✏️</button>
                         <div className="flex items-center gap-1 bg-slate-50 px-2 py-1 rounded border border-slate-200" onClick={e => e.stopPropagation()}>
                           <span className="text-[10px] font-bold text-slate-400">TT:</span>
                           <input type="number" defaultValue={course.order_index || 0} onBlur={e => handleUpdateCourseOrder(course.id, parseInt(e.target.value) || 0)} className="w-6 md:w-8 text-center text-xs font-bold outline-none bg-transparent" />
                         </div>
                       </div>
                    </div>
                    <div className="flex-1 mt-3 md:mt-4 mb-2">
                       {editingCourseId === course.id ? (
                         <form onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateCourseInfo(course.id, new FormData(e.currentTarget).get('title') as string, new FormData(e.currentTarget).get('type') as string); }}>
                            <input name="title" autoFocus defaultValue={course.title} className="w-full border border-slate-300 rounded-lg px-2 py-1 font-black text-[13px] md:text-[15px] outline-none mb-2 focus:border-[#0a5482]" />
                            <select name="type" defaultValue={course.type} className="w-full border border-slate-300 rounded-lg px-2 py-1 font-bold text-[12px] outline-none mb-2 focus:border-[#0a5482]">
                               <option value="IELTS">Hệ IELTS</option>
                               <option value="Standard">Hệ Standard (IGCSE/TOEIC)</option>
                            </select>
                            <div className="flex gap-2">
                                <button type="submit" className="text-[10px] md:text-xs font-bold text-white bg-emerald-500 px-2 md:px-3 py-1 rounded">Lưu</button>
                                <button type="button" onClick={() => setEditingCourseId(null)} className="text-[10px] md:text-xs font-bold bg-slate-100 px-2 md:px-3 py-1 rounded border border-slate-200 text-slate-600">Hủy</button>
                            </div>
                         </form>
                       ) : ( 
                         <h3 className="font-black text-[16px] md:text-lg text-slate-800 line-clamp-2 leading-snug">{course.title}</h3> 
                       )}
                    </div>
                    <button onClick={() => handleViewCourseDetail(course)} className="w-full bg-[#f8fafc] hover:bg-[#2bd6eb] hover:text-white text-slate-600 border border-slate-200 font-bold py-2 md:py-2.5 rounded-xl transition shadow-sm text-[12px] md:text-sm">Quản lý Lớp & Nội dung ➜</button>
                  </div>
                ))
              )}
            </div>
          )}

          {/* VIEW: QUẢN LÝ TÀI LIỆU PDF */}
          {activeTab === 'documents' && (
             <div className="space-y-4 md:space-y-6 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl border border-slate-200 shadow-sm overflow-hidden flex flex-col h-[calc(100vh-140px)]">
                    <div className="p-4 md:p-6 bg-slate-50 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 shrink-0">
                        <div className="flex items-center gap-2 md:gap-3">
                            {!isSearchingPdf && currentPdfFolderId && (
                                <button onClick={() => setCurrentPdfFolderId(null)} className="text-slate-400 hover:text-[#0a5482] font-bold mr-1 transition text-[11px] md:text-[13px] bg-white border border-slate-200 px-2 py-1 rounded-lg">← Trở về</button>
                            )}
                            <div>
                                <h2 className="font-black text-slate-700 text-[13px] md:text-lg uppercase tracking-tight">
                                    {isSearchingPdf ? 'Kết quả tìm kiếm' : (currentPdfFolderId ? `Mục: ${pdfBreadcrumbs[pdfBreadcrumbs.length-1]?.name}` : 'KHO TÀI LIỆU ĐÁM MÂY')}
                                </h2>
                                <p className="text-slate-500 text-[10px] md:text-xs mt-1">Dung lượng tối đa 50MB. (Cấu trúc Folder ảo, link gốc không đổi).</p>
                            </div>
                        </div>
                        <div className="flex flex-col sm:flex-row gap-2 w-full sm:w-auto">
                            {!isSearchingPdf && (
                                <button onClick={() => setShowPdfFolderModal(true)} className="bg-[#00a651] text-white px-3 py-1.5 md:px-4 md:py-2 rounded-xl font-black text-[10px] md:text-xs shadow-sm hover:bg-[#008f45] whitespace-nowrap">+ THƯ MỤC</button>
                            )}
                            <select value={pdfSortOrder} onChange={(e) => setPdfSortOrder(e.target.value)} className="w-full sm:w-32 px-2 md:px-3 py-2 rounded-xl border border-slate-200 outline-none focus:border-[#2bd6eb] text-[11px] md:text-xs font-bold text-slate-600 shadow-sm bg-white cursor-pointer">
                                <option value="date-desc">Mới nhất trước</option>
                                <option value="date-asc">Cũ nhất trước</option>
                                <option value="name-asc">Tên (A-Z)</option>
                                <option value="name-desc">Tên (Z-A)</option>
                                <option value="size-desc">Size (Lớn nhất)</option>
                                <option value="size-asc">Size (Nhỏ nhất)</option>
                            </select>
                            <input type="text" placeholder="Tìm tên file..." value={pdfSearchQuery} onChange={(e) => setPdfSearchQuery(e.target.value)} className="w-full sm:w-48 px-4 py-2 rounded-xl border border-slate-200 outline-none focus:border-[#2bd6eb] text-xs shadow-sm font-medium" />
                        </div>
                    </div>

                    <div className="flex-1 overflow-y-auto p-4 md:p-6 custom-scrollbar bg-slate-50/50 relative">
                        {!isSearchingPdf && currentPdfSubFolders.length > 0 && (
                            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-6 md:mb-8">
                               {currentPdfSubFolders.map(sf => (
                                  <div key={sf.id} className="relative group h-[100px] md:h-[120px]">
                                     {editingPdfFolderId === sf.id ? (
                                         <div className="bg-white border-2 border-[#2bd6eb] p-2 md:p-3 rounded-xl md:rounded-2xl shadow-sm h-full flex flex-col items-center justify-center">
                                            <form className="w-full flex flex-col items-center" onSubmit={(e) => handleUpdatePdfFolderName(sf.id, new FormData(e.currentTarget).get('name') as string)}>
                                               <input name="name" autoFocus defaultValue={sf.name} className="w-full border border-slate-300 rounded px-2 py-1 text-[11px] md:text-xs font-bold mb-2 text-center outline-none focus:border-[#0a5482]" />
                                               <div className="flex gap-2">
                                                  <button type="submit" className="bg-emerald-500 text-white px-2 py-1 rounded text-[10px] font-bold">Lưu</button>
                                                  <button type="button" onClick={() => setEditingPdfFolderId(null)} className="bg-slate-200 text-slate-600 px-2 py-1 rounded text-[10px] font-bold">Hủy</button>
                                               </div>
                                            </form>
                                         </div>
                                     ) : (
                                         <div onClick={() => setCurrentPdfFolderId(sf.id)} className="bg-white border-2 border-slate-100 hover:border-[#2bd6eb] p-3 md:p-4 rounded-xl md:rounded-2xl shadow-sm cursor-pointer h-full flex flex-col items-center justify-center text-center relative overflow-hidden transition-all">
                                             <div className="text-3xl md:text-4xl mb-2 group-hover:scale-110 transition-transform">📁</div>
                                             <h4 className="font-black text-slate-700 text-[11px] md:text-[13px] line-clamp-2 px-1">{sf.name}</h4>
                                             <button onClick={(e) => { e.stopPropagation(); setEditingPdfFolderId(sf.id); }} className="absolute top-2 right-2 text-blue-400 opacity-0 group-hover:opacity-100 bg-blue-50 p-1 md:p-1.5 rounded text-[10px] md:text-xs transition-opacity">✏️</button>
                                         </div>
                                     )}
                                     {editingPdfFolderId !== sf.id && (
                                         <button onClick={(e) => { e.stopPropagation(); handleDeletePdfFolder(sf.id); }} className="absolute -top-2 -right-2 bg-red-500 hover:bg-red-600 transition-colors text-white w-6 h-6 md:w-7 md:h-7 rounded-full opacity-0 group-hover:opacity-100 flex items-center justify-center text-[10px] md:text-xs font-bold shadow-lg z-10">✕</button>
                                     )}
                                  </div>
                               ))}
                            </div>
                        )}

                        {!isSearchingPdf && currentPdfSubFolders.length > 0 && currentPdfFiles.length > 0 && (
                            <div className="w-full h-px bg-transparent mb-6 border-t-2 border-dashed border-slate-200"></div>
                        )}

                        {currentPdfFiles.length === 0 ? (
                            <div className="h-[200px] flex flex-col items-center justify-center text-slate-400">
                                <span className="text-4xl md:text-5xl mb-3 opacity-50">{isSearchingPdf ? '🔍' : '☁️'}</span>
                                <p className="font-medium text-sm md:text-base">{isSearchingPdf ? 'Không tìm thấy tài liệu phù hợp.' : 'Không có tài liệu nào trong mục này.'}</p>
                            </div>
                        ) : (
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                {currentPdfFiles.map(file => (
                                    <div key={file.id} className="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow group flex flex-col">
                                        <div className="flex items-start gap-3 mb-3">
                                            <div className="w-10 h-10 rounded-lg bg-red-50 text-red-500 flex items-center justify-center text-xl shrink-0 border border-red-100">📄</div>
                                            <div className="flex-1 min-w-0">
                                                <h4 className="font-bold text-slate-700 text-[13px] md:text-sm truncate" title={file.name}>{file.name}</h4>
                                                <p className="text-[11px] text-slate-400 mt-0.5">{formatFileSize(file.metadata?.size || 0)} • {formatDateTime(file.created_at)}</p>
                                            </div>
                                        </div>
                                        <div className="mt-auto flex gap-2 pt-3 border-t border-slate-100">
                                            <button onClick={() => setShowMoveFileModal(file.name)} className="w-9 flex items-center justify-center bg-blue-50 text-blue-500 hover:bg-blue-500 hover:text-white transition-colors border border-blue-100 rounded-lg text-sm" title="Chuyển thư mục">📂</button>
                                            <button onClick={() => copyToClipboard(file.publicUrl)} className="flex-1 bg-[#f0f9ff] text-[#0ea5e9] hover:bg-[#0ea5e9] hover:text-white transition-colors border border-[#bae6fd] font-bold py-1.5 rounded-lg text-xs flex items-center justify-center gap-1"><span>🔗</span> Copy Link</button>
                                            <a href={file.publicUrl} target="_blank" rel="noopener noreferrer" className="w-9 flex items-center justify-center bg-slate-50 hover:bg-slate-200 transition-colors border border-slate-200 rounded-lg text-slate-600 text-sm" title="Mở xem thử">👁️</a>
                                            <button onClick={() => handleDeleteFile(file.name)} className="w-9 flex items-center justify-center bg-red-50 hover:bg-red-500 hover:text-white transition-colors border border-red-100 rounded-lg text-red-400 opacity-0 group-hover:opacity-100 text-sm" title="Xóa file">🗑️</button>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
             </div>
          )}

          {/* VIEW: CHI TIẾT KHÓA HỌC */}
          {activeTab === 'course-detail' && selectedCourse && (
            <div className="space-y-4 md:space-y-6">
              
              <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-white p-4 md:p-5 rounded-xl md:rounded-2xl border border-slate-200 shadow-sm">
                <div className="flex flex-wrap items-center gap-2 text-[12px] md:text-sm font-bold text-slate-500">
                  <button onClick={() => setActiveTab('courses')} className="hover:text-[#2bd6eb] transition-colors">Khóa học</button> 
                  <span className="text-slate-300">/</span> 
                  <span className="text-slate-800 font-black">{selectedCourse.title}</span>
                </div>
                <button onClick={handleDeleteCourse} className="text-red-500 hover:bg-red-50 px-3 py-1.5 md:px-4 md:py-2 rounded-lg font-bold text-[11px] md:text-xs border border-red-100 transition whitespace-nowrap">🗑️ Xóa Khóa</button>
              </div>

              <div className="flex gap-4 md:gap-6 border-b border-slate-200 px-1 md:px-2 overflow-x-auto custom-scrollbar whitespace-nowrap" style={{ WebkitOverflowScrolling: 'touch' }}>
                 <button onClick={() => setCourseViewMode('classes')} className={`pb-2 md:pb-3 font-black text-[11px] md:text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'classes' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>👨‍🏫 LỚP HỌC</button>
                 <button onClick={() => setCourseViewMode('modules')} className={`pb-2 md:pb-3 font-black text-[11px] md:text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'modules' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>📚 GIÁO TRÌNH</button>
                 <button onClick={() => setCourseViewMode('tests')} className={`pb-2 md:pb-3 font-black text-[11px] md:text-[13px] uppercase tracking-widest px-2 border-b-[3px] transition-colors ${courseViewMode === 'tests' ? 'border-[#2bd6eb] text-[#0a5482]' : 'border-transparent text-slate-400 hover:text-slate-600'}`}>📁 KHO ĐỀ & BÀI TẬP</button>
              </div>

              {courseViewMode === 'classes' && (
                <div className="flex flex-col lg:flex-row gap-4 md:gap-6 h-auto lg:h-[600px] animate-in fade-in">
                   <div className="w-full lg:w-1/3 bg-white rounded-2xl md:rounded-3xl border border-slate-200 shadow-sm flex flex-col overflow-hidden h-[300px] lg:h-auto shrink-0">
                      <div className="p-4 md:p-5 bg-slate-50 border-b border-slate-200 flex justify-between items-center shrink-0">
                         <h3 className="font-black text-slate-700 uppercase text-[11px] md:text-xs tracking-widest">Danh sách Lớp</h3>
                         <button onClick={() => setShowClassModal(true)} className="bg-[#0a5482] hover:bg-[#084266] transition text-white px-3 py-1.5 md:px-4 md:py-1.5 rounded-lg text-[11px] md:text-xs font-bold">+ THÊM LỚP</button>
                      </div>
                      <div className="flex-1 overflow-y-auto p-3 md:p-4 space-y-2 custom-scrollbar">
                         {classes.length === 0 ? <p className="text-[12px] md:text-sm text-slate-400 text-center mt-4 italic">Chưa có lớp nào</p> : (
                            classes.map(cls => (
                               <div key={cls.id} onClick={() => { setSelectedClass(cls); fetchClassDetails(cls.id); }} className={`p-3 md:p-4 border rounded-xl cursor-pointer transition-all flex justify-between items-center group ${selectedClass?.id === cls.id ? 'bg-blue-50 border-blue-400' : 'bg-white border-slate-200 hover:border-[#2bd6eb]'}`}>
                                  <div className="flex-1 mr-2 min-w-0">
                                     {editingClassId === cls.id ? (
                                        <form onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateClassName(cls.id, new FormData(e.currentTarget).get('name') as string); }}>
                                           <input name="name" autoFocus defaultValue={cls.name} className="w-full border border-slate-300 rounded px-2 py-1 font-black text-[12px] md:text-sm outline-none mb-1 focus:border-[#0a5482]" />
                                           <div className="flex gap-2">
                                               <button type="submit" className="text-[10px] font-bold text-white bg-emerald-500 px-2 py-0.5 rounded">Lưu</button>
                                               <button type="button" onClick={() => setEditingClassId(null)} className="text-[10px] font-bold bg-slate-200 px-2 py-0.5 rounded text-slate-600">Hủy</button>
                                           </div>
                                        </form>
                                     ) : ( <p className={`font-black text-[13px] md:text-sm truncate ${selectedClass?.id === cls.id ? 'text-blue-800' : 'text-slate-700'}`}>{cls.name}</p> )}
                                  </div>
                                  <div className="flex items-center gap-1.5 md:opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                                     <button onClick={(e) => { e.stopPropagation(); setEditingClassId(cls.id); }} className="text-blue-400 hover:text-blue-600 text-xs font-bold transition-colors bg-white p-1 md:p-1.5 rounded border border-blue-200">✏️</button>
                                     <button onClick={(e) => { e.stopPropagation(); handleDeleteClass(cls.id); }} className="text-red-400 hover:text-red-600 text-xs font-bold transition-colors bg-white p-1 md:p-1.5 rounded border border-red-200">✕</button>
                                  </div>
                               </div>
                            ))
                         )}
                      </div>
                   </div>

                   <div className="flex-1 bg-white rounded-2xl md:rounded-3xl border border-slate-200 shadow-sm flex flex-col overflow-hidden min-h-[400px] lg:min-h-0">
                      {!selectedClass ? (
                         <div className="flex-1 flex items-center justify-center text-slate-400 font-medium border-2 border-dashed border-slate-100 m-4 md:m-8 rounded-2xl text-[13px] md:text-base text-center px-4">👈 Chọn một lớp học để xem dữ liệu</div>
                      ) : (
                         <div className="flex-1 flex flex-col overflow-hidden animate-in fade-in">
                            <div className="p-4 md:p-6 bg-blue-50/50 border-b border-blue-100 shrink-0"><h2 className="text-[15px] md:text-lg font-black text-[#0a5482] uppercase tracking-wide truncate">LỚP: {selectedClass.name}</h2></div>
                            
                            <div className="flex-1 flex flex-col md:flex-row overflow-hidden">
                               <div className="w-full md:w-1/3 border-b md:border-b-0 md:border-r border-slate-200 flex flex-col h-[250px] md:h-auto shrink-0 md:shrink">
                                  <div className="p-3 md:p-4 bg-slate-50 border-b border-slate-200 flex justify-between items-center shrink-0">
                                     <h3 className="font-bold text-[12px] md:text-sm text-slate-700">Học phần của lớp</h3>
                                     <button onClick={() => setShowAssignClassModuleModal(true)} className="text-[10px] md:text-xs bg-emerald-500 hover:bg-emerald-600 transition text-white font-bold px-2 md:px-3 py-1.5 rounded-lg shadow-sm whitespace-nowrap">+ Gán</button>
                                  </div>
                                  <div className="flex-1 overflow-y-auto p-3 md:p-4 space-y-2 custom-scrollbar">
                                     {lectureModules.filter(m => classModules.includes(m.id)).length === 0 ? <p className="text-[11px] md:text-xs text-slate-400 italic text-center mt-4">Chưa có học phần nào.</p> : (
                                        lectureModules.filter(m => classModules.includes(m.id)).map(m => (
                                           <div key={m.id} className="p-2.5 md:p-3 bg-white border border-slate-200 rounded-lg flex justify-between items-center shadow-sm hover:border-slate-300 transition">
                                              <span className="font-bold text-[12px] md:text-sm text-slate-700 truncate mr-2">{m.title}</span>
                                              <button onClick={() => handleUnassignModuleFromClass(m.id)} className="text-red-500 text-[11px] md:text-xs font-bold hover:underline transition shrink-0">Gỡ</button>
                                           </div>
                                        ))
                                     )}
                                  </div>
                               </div>

                               <div className="w-full md:w-1/3 border-b md:border-b-0 md:border-r border-slate-200 flex flex-col bg-[#f8fafc] h-[250px] md:h-auto shrink-0 md:shrink">
                                  <div className="p-3 md:p-4 bg-slate-50 border-b border-slate-200 flex justify-between items-center shrink-0">
                                     <h3 className="font-bold text-[12px] md:text-sm text-slate-700">Học sinh trong lớp</h3>
                                     <button onClick={() => setShowAssignStudentModal(true)} className="text-[10px] md:text-xs bg-blue-500 hover:bg-blue-600 transition text-white font-bold px-2 md:px-3 py-1.5 rounded-lg shadow-sm whitespace-nowrap">+ Thêm</button>
                                  </div>
                                  <div className="flex-1 overflow-y-auto p-3 md:p-4 space-y-2 custom-scrollbar">
                                     {classStudentsList.length === 0 ? <p className="text-[11px] md:text-xs text-slate-400 italic text-center mt-4">Chưa có học sinh nào.</p> : (
                                        classStudentsList.map(st => (
                                           <div key={st.user_id} className="p-2.5 md:p-3 bg-white border border-slate-200 rounded-lg flex justify-between items-center shadow-sm">
                                              <div className="min-w-0 pr-2">
                                                  <p className="font-bold text-[12px] md:text-sm text-slate-700 truncate">{st.full_name || 'Học viên'}</p>
                                                  <p className="text-[9px] md:text-[10px] text-slate-400 truncate">{st.email}</p>
                                              </div>
                                              <button onClick={() => handleUnassignStudentFromClass(st.user_id)} className="text-red-500 text-[11px] md:text-xs font-bold hover:underline shrink-0">Gỡ</button>
                                           </div>
                                        ))
                                     )}
                                  </div>
                               </div>

                               {/* CỘT 3: BÀI TẬP VÀ DEADLINE CỦA LỚP */}
                               <div className="w-full md:w-1/3 flex flex-col bg-orange-50/20 h-[250px] md:h-auto shrink-0 md:shrink">
                                  <div className="p-3 md:p-4 bg-orange-50 border-b border-orange-100 flex justify-between items-center shrink-0">
                                     <h3 className="font-bold text-[12px] md:text-sm text-orange-800">Bài tập & Deadline</h3>
                                     
                                     {/* 🚀 NÚT MỞ POPUP GIAO NHIỀU BÀI */}
                                     <button 
                                        onClick={() => {
                                            setSelectedDeadlineTests([]);
                                            setDeadlineInput('');
                                            setShowAssignDeadlineModal(true);
                                        }} 
                                        className="text-[10px] md:text-xs bg-orange-500 hover:bg-orange-600 transition text-white font-bold px-2 md:px-3 py-1.5 rounded-lg shadow-sm whitespace-nowrap"
                                     >
                                         + Giao bài
                                     </button>
                                  </div>
                                  <div className="flex-1 overflow-y-auto p-3 md:p-4 space-y-2 custom-scrollbar">
                                     {classAssignedTests.length === 0 ? <p className="text-[11px] md:text-xs text-slate-400 italic text-center mt-4">Chưa giao bài nào.</p> : (
                                        classAssignedTests.map(t => {
                                            const dl = t.content_json?.basicInfo?.classDeadlines?.[selectedClass.id];
                                            return (
                                                <div key={t.id} className="p-2.5 md:p-3 bg-white border border-slate-200 rounded-lg flex flex-col justify-between items-start shadow-sm group hover:border-orange-300 transition-colors">
                                                    <span className="font-bold text-[12px] md:text-sm text-slate-700 truncate w-full mb-1">{t.title}</span>
                                                    <div className="flex justify-between items-center w-full">
                                                        <span className="text-[10px] font-bold text-orange-600 bg-orange-50 px-2 py-0.5 rounded border border-orange-100">
                                                            ⏳ {dl ? formatDateTime(dl) : ''}
                                                        </span>
                                                        <button 
                                                            onClick={() => {
                                                                setDeadlineModal({show: true, test: t});
                                                            }} 
                                                            className="text-[#0a5482] text-[10px] font-bold hover:underline transition md:opacity-0 group-hover:opacity-100"
                                                        >
                                                            Sửa
                                                        </button>
                                                    </div>
                                                </div>
                                            )
                                        })
                                     )}
                                  </div>
                               </div>
                            </div>
                         </div>
                      )}
                   </div>
                </div>
              )}

              {/* TAB GIÁO TRÌNH */}
              {courseViewMode === 'modules' && (
                <div className="bg-white rounded-2xl md:rounded-3xl border border-slate-200 overflow-hidden shadow-sm animate-in fade-in">
                  <div className="p-4 md:p-6 bg-slate-50 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
                    <p className="font-black text-slate-600 text-[11px] md:text-xs uppercase tracking-widest">Giáo trình Khóa học</p>
                    <button onClick={() => setShowModuleModal(true)} className="bg-[#0a5482] hover:bg-[#084266] transition text-white px-4 md:px-6 py-2 md:py-2.5 rounded-xl font-black text-[11px] md:text-xs shadow-sm">+ THÊM HỌC PHẦN</button>
                  </div>
                  <div className="p-4 md:p-8">
                     {lectureModules.length === 0 ? <div className="text-center py-10 md:py-12 border-2 border-dashed border-slate-200 rounded-2xl text-slate-400 font-medium text-[13px] md:text-base">Khóa học này chưa có Học phần nào.</div> : (
                        lectureModules.map(mod => {
                           const moduleLectures = lectures.filter(l => l.module_id === mod.id);
                           return (
                             <div key={mod.id} className="border border-slate-200 rounded-2xl overflow-hidden shadow-sm mb-6 group/mod">
                                <div className="bg-slate-50 px-4 md:px-6 py-3 md:py-4 border-b border-slate-200 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-3 lg:gap-0">
                                   <div className="flex flex-wrap items-center gap-3 w-full lg:flex-1 lg:mr-4">
                                      {editingModuleId === mod.id ? (
                                         <form className="flex-1 flex gap-2 w-full" onClick={(e) => e.stopPropagation()} onSubmit={(e) => { e.preventDefault(); e.stopPropagation(); handleUpdateModuleName(mod.id, new FormData(e.currentTarget).get('title') as string); }}>
                                            <input name="title" autoFocus defaultValue={mod.title} className="flex-1 border border-slate-300 rounded-lg px-2 md:px-3 py-1 font-black text-[13px] md:text-[15px] outline-none focus:border-[#0a5482]" />
                                            <button type="submit" className="text-[11px] md:text-xs font-bold text-white bg-emerald-500 px-2 md:px-3 py-1 rounded">Lưu</button>
                                            <button type="button" onClick={() => setEditingModuleId(null)} className="text-[11px] md:text-xs font-bold bg-slate-100 px-2 md:px-3 py-1 rounded border border-slate-200 text-slate-600">Hủy</button>
                                         </form>
                                      ) : (
                                        <>
                                           <div className="flex items-center gap-2 md:gap-3 flex-1 min-w-0">
                                              <h3 className="font-black text-slate-800 text-[14px] md:text-[16px] flex items-center gap-2 truncate">📑 {mod.title}</h3>
                                              <button onClick={() => setEditingModuleId(mod.id)} className="text-blue-500 hover:text-blue-700 transition-colors text-[10px] md:text-[11px] font-bold bg-blue-50 hover:bg-blue-100 px-2 py-1 rounded border border-blue-200 shadow-sm shrink-0">✏️ Sửa</button>
                                           </div>
                                           <div className="flex items-center gap-1 bg-white px-2 py-1 rounded border border-slate-200 shrink-0"><span className="text-[9px] md:text-[10px] font-bold text-slate-400 uppercase">TT:</span><input type="number" defaultValue={mod.order_index || 0} onBlur={e => handleUpdateModuleOrder(mod.id, parseInt(e.target.value) || 0)} className="w-8 md:w-10 text-center text-[11px] md:text-xs font-bold outline-none" /></div>
                                        </>
                                      )}
                                   </div>
                                   <div className="flex flex-wrap gap-2 w-full lg:w-auto">
                                      <button onClick={() => setShowAssignLectureModal({show: true, moduleId: mod.id})} className="flex-1 lg:flex-none bg-white border border-slate-300 text-blue-600 px-2 md:px-4 py-1.5 rounded-lg text-[10px] md:text-xs font-bold hover:border-blue-400 transition whitespace-nowrap">+ Nhặt Từ Kho</button>
                                      <button onClick={() => setEditingLecture({ id: 'new', title: '', course_id: selectedCourse.id, module_id: mod.id })} className="flex-1 lg:flex-none bg-[#00a651] hover:bg-[#008f45] transition text-white px-2 md:px-4 py-1.5 rounded-lg text-[10px] md:text-xs font-bold whitespace-nowrap">+ Tạo Mới</button>
                                      <button onClick={() => handleDeleteLectureModule(mod.id)} className="bg-white border border-slate-300 text-red-500 hover:bg-red-50 hover:border-red-300 px-3 py-1.5 rounded-lg text-[10px] md:text-xs transition shrink-0">✖</button>
                                   </div>
                                </div>
                                <div className="p-2 md:p-4 bg-white">
                                   {moduleLectures.length === 0 ? <p className="text-[12px] md:text-sm text-slate-400 italic px-2 py-2">Chưa có bài giảng nào.</p> : (
                                      moduleLectures.map((lec) => (
                                         <div key={lec.id} className="flex flex-col sm:flex-row sm:justify-between sm:items-center p-2.5 md:p-3 hover:bg-blue-50 rounded-lg group border border-transparent hover:border-blue-100 transition-colors gap-2">
                                            <div className="flex items-center gap-2 md:gap-3 flex-1 min-w-0">
                                               <input type="number" defaultValue={lec.order_index || 0} onBlur={e => handleUpdateLectureOrder(lec.id, parseInt(e.target.value) || 0)} className="w-8 md:w-10 h-6 text-center text-[10px] md:text-[11px] font-bold border border-slate-200 rounded outline-none focus:border-[#2bd6eb] shrink-0" title="Thứ tự hiển thị" />
                                               <span className="font-semibold text-slate-700 text-[13px] md:text-sm truncate">{lec.title}</span>
                                            </div>
                                            <div className="flex gap-2 sm:opacity-0 group-hover:opacity-100 transition-opacity w-full sm:w-auto justify-end">
                                               <button onClick={() => handleUnassignLecture(lec.id)} className="text-orange-500 font-bold text-[10px] md:text-xs bg-white border border-orange-200 px-2 md:px-3 py-1 rounded hover:bg-orange-50 transition">Gỡ (Về Kho)</button>
                                               <button onClick={() => setEditingLecture(lec)} className="text-blue-600 font-bold text-[10px] md:text-xs bg-white border border-blue-200 px-2 md:px-3 py-1 rounded hover:bg-blue-50 transition">✏️ Sửa</button>
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

              {/* TAB KHO ĐỀ & BÀI TẬP */}
              {courseViewMode === 'tests' && (
                <div className="bg-white rounded-2xl md:rounded-3xl border border-slate-200 overflow-hidden shadow-sm animate-in fade-in">
                  <div className="p-4 md:p-6 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                    <div className="flex items-center gap-1 md:gap-2">
                       {currentFolderId && <button onClick={() => {
                         const currentFolder = folders.find(f => f.id === currentFolderId);
                         setCurrentFolderId(currentFolder?.parent_id || null);
                       }} className="text-slate-400 hover:text-black font-bold mr-1 md:mr-2 transition text-[11px] md:text-[13px]">← Trở về</button>}
                       <p className="font-black text-slate-500 text-[10px] md:text-xs uppercase tracking-widest truncate max-w-[150px] md:max-w-none">{currentFolderId ? `Mục: ${breadcrumbs[breadcrumbs.length-1]?.title}` : 'Thư mục gốc'}</p>
                    </div>
                    <button onClick={() => setShowFolderModal(true)} className="bg-[#00a651] hover:bg-[#008f45] transition text-white px-3 py-1.5 md:px-6 md:py-2.5 rounded-lg md:rounded-xl font-black text-[10px] md:text-xs shadow-md whitespace-nowrap">+ THƯ MỤC</button>
                  </div>
                  <div className="p-4 md:p-8">
                    {currentSubFolders.length > 0 && (
                      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-8">
                        {currentSubFolders.map(sf => (
                          <div key={sf.id} className="relative group h-full">
                            <div className="absolute top-1 left-1 md:top-2 md:left-2 bg-white/90 backdrop-blur-sm px-1 md:px-2 py-0.5 rounded border border-slate-200 flex items-center gap-1 z-10 md:opacity-0 group-hover:opacity-100 transition-opacity">
                               <span className="text-[9px] md:text-[10px] font-bold text-slate-400 hidden sm:inline">TT:</span>
                               <input type="number" defaultValue={sf.display_order || 0} onBlur={e => handleUpdateFolderOrder(sf.id, parseInt(e.target.value) || 0)} className="w-6 md:w-8 text-center text-[10px] md:text-xs font-bold outline-none bg-transparent" title="Thứ tự hiển thị" />
                            </div>

                            {editingFolderId === sf.id ? (
                               <div className="bg-white border-2 border-[#2bd6eb] p-3 md:p-4 rounded-xl md:rounded-2xl shadow-sm h-full flex flex-col justify-center items-center" onClick={e => e.stopPropagation()}>
                                  <form className="w-full flex flex-col items-center" onSubmit={(e) => { e.preventDefault(); handleUpdateFolderName(sf.id, new FormData(e.currentTarget).get('title') as string); }}>
                                     <input name="title" autoFocus defaultValue={sf.title} className="w-full border border-slate-300 rounded px-2 py-1.5 text-[12px] md:text-sm font-bold outline-none mb-2 text-center focus:border-[#0a5482]" />
                                     <div className="flex gap-1.5 md:gap-2">
                                        <button type="submit" className="text-[10px] md:text-xs font-bold text-white bg-emerald-500 px-2 md:px-3 py-1 rounded shadow-sm">Lưu</button>
                                        <button type="button" onClick={() => setEditingFolderId(null)} className="text-[10px] md:text-xs font-bold bg-slate-100 px-2 md:px-3 py-1 rounded border border-slate-200 text-slate-600">Hủy</button>
                                     </div>
                                  </form>
                               </div>
                            ) : (
                               <div onClick={() => setCurrentFolderId(sf.id)} className="bg-white border-2 border-slate-100 hover:border-[#2bd6eb] p-4 md:p-6 rounded-xl md:rounded-2xl shadow-sm cursor-pointer transition-all flex flex-col items-center justify-center text-center h-full relative overflow-hidden">
                                  <div className="text-3xl md:text-4xl mb-2 md:mb-3 group-hover:scale-110 transition-transform relative z-10">📁</div>
                                  <h4 className="font-black text-slate-700 text-[12px] md:text-sm line-clamp-2 relative z-10 px-1">{sf.title}</h4>
                                  <button onClick={(e) => { e.stopPropagation(); setEditingFolderId(sf.id); }} className="absolute top-1 right-1 md:top-2 md:right-2 text-blue-400 hover:text-blue-600 md:opacity-0 group-hover:opacity-100 transition-opacity bg-blue-50 p-1 md:p-1.5 rounded text-[10px] md:text-xs z-10">✏️</button>
                               </div>
                            )}
                            {editingFolderId !== sf.id && (
                               <button onClick={(e) => { e.stopPropagation(); handleDeleteFolder(sf.id); }} className="absolute -top-1 -right-1 md:-top-2 md:-right-2 bg-red-500 hover:bg-red-600 text-white w-6 h-6 md:w-7 md:h-7 rounded-full md:opacity-0 group-hover:opacity-100 transition-opacity shadow-lg flex items-center justify-center text-[10px] md:text-xs font-bold z-20">✕</button>
                            )}
                          </div>
                        ))}
                      </div>
                    )}{currentFolderId && currentSubFolders.length === 0 && (
                      <div className="border-t-2 border-dashed border-slate-200 pt-6 md:pt-8 mt-2">
                         <div className="flex justify-between items-center mb-4 md:mb-6">
                            <h3 className="font-black text-slate-800 text-[14px] md:text-lg">📝 Đề thi / Bài tập</h3>
                            <button onClick={() => setShowAssignModal(true)} className="bg-[#2bd6eb] hover:bg-[#1bc1d6] transition text-white px-3 py-1.5 md:px-5 md:py-2 rounded-lg font-bold text-[10px] md:text-xs shadow-sm whitespace-nowrap">+ GÁN THÊM</button>
                         </div>
                         {currentTests.length === 0 ? (
                           <div className="text-center py-8 md:py-10 border-2 border-dashed border-slate-200 rounded-xl md:rounded-2xl text-slate-400 font-medium text-[12px] md:text-[14px]">Chưa có mục nào. Bấm nút + Gán thêm từ Kho tổng.</div>
                         ) : (
                           <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-3 md:gap-4">
                             {currentTests.map(t => (
                               <div key={t.id} className="bg-slate-50 border border-slate-200 p-3 md:p-4 rounded-xl flex justify-between items-center group hover:bg-white transition-colors">
                                 <div className="flex items-center gap-2 md:gap-3 flex-1 min-w-0 pr-2">
                                   <input type="number" defaultValue={t.order_index || 0} onBlur={e => handleUpdateTestOrder(t.id, parseInt(e.target.value) || 0)} className="w-8 md:w-10 h-6 text-center text-[10px] md:text-[11px] font-bold border border-slate-200 rounded outline-none focus:border-[#2bd6eb] shrink-0" title="Thứ tự hiển thị" />
                                   <div className="flex flex-col min-w-0">
                                      <span className="font-bold text-[13px] md:text-[14px] text-slate-700 truncate">{t.title}</span>
                                      <span className={`text-[8px] md:text-[9px] w-fit px-1 md:px-1.5 py-0.5 rounded uppercase font-black mt-1 ${t.content_json?.basicInfo?.category === 'exercise' ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'}`}>
                                          {t.content_json?.basicInfo?.category === 'exercise' ? 'BÀI TẬP' : 'ĐỀ THI'}
                                      </span>
                                   </div>
                                 </div>
                                 <div className="flex gap-2 md:gap-3 shrink-0">
                                   <button onClick={() => { if (t.test_type === 'IGCSE-Science' || t.test_type === 'IGCSE-Math' || t.test_type === 'IGCSE-Direct') { setIgcseEditingTestId(t.id); setIgcseEditorOpen(true); } else { setEditingTest(t); } }} className="text-[#2bd6eb] font-bold text-[10px] md:text-xs hover:underline md:opacity-0 group-hover:opacity-100 transition-opacity">Sửa</button>
                                   <button onClick={() => handleUnassignTest(t.id)} className="text-red-400 font-bold text-[10px] md:text-xs hover:underline md:opacity-0 group-hover:opacity-100 transition-opacity">Gỡ ✖</button>
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

          {/* ========================================================= */}
          {/* VIEW: KHO BÀI GIẢNG CHUNG */}
          {activeTab === 'lectures-library' && (
            <div className="space-y-4 md:space-y-6">
              
              <div className="flex flex-col xl:flex-row justify-between gap-3 md:gap-4 bg-white p-3 md:p-4 rounded-xl border border-slate-200 shadow-sm relative z-20">
                 
                 <div className="flex flex-wrap items-center gap-3">
                    <div className="flex bg-slate-100 rounded-lg p-1 border border-slate-200 shadow-sm shrink-0">
                       <button onClick={() => handleBulkLectureVisibility(true)} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-emerald-600 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">👁️ Hiện</button>
                       <button onClick={() => handleBulkLectureVisibility(false)} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-slate-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">👁️‍🗨️ Ẩn</button>
                       <button onClick={handleBulkLectureDelete} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-red-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">🗑️ Xóa</button>
                    </div>

                    <div className="flex items-center gap-2 bg-blue-50 p-1.5 md:p-2 rounded-lg border border-blue-100 shadow-sm">
                       <span className="text-[11px] font-bold text-blue-800 hidden sm:inline ml-1 uppercase tracking-tight">Chuyển:</span>
                       <select value={targetMoveCourseId} onChange={e=>setTargetMoveCourseId(e.target.value)} className="border border-blue-200 bg-white rounded px-2 py-1 md:py-1.5 text-[11px] md:text-[13px] font-bold text-slate-700 outline-none w-[140px] md:w-[200px] truncate focus:border-[#0a5482]">
                          <option value="">-- Chọn Khóa Học --</option>
                          <option value="none">-- 📦 Không thuộc khóa nào --</option>
                          {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                       </select>
                       <button onClick={handleBulkMoveCourse} className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-3 py-1 md:py-1.5 rounded shadow-sm text-[11px] transition-colors whitespace-nowrap active:scale-95">ÁP DỤNG</button>
                    </div>
                 </div>

                 <div className="flex flex-col sm:flex-row gap-3 flex-1 justify-end w-full xl:w-auto">
                   <input type="text" placeholder="Tìm kiếm tên bài giảng..." defaultValue={searchQuery} onChange={e => { clearTimeout(adminSearchTimer); adminSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350); }} className="w-full sm:max-w-[250px] pl-3 pr-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl outline-none focus:border-[#2bd6eb] text-[13px] md:text-sm transition-colors" />
                   <select value={filterLectureCourse} onChange={e => setFilterLectureCourse(e.target.value)} className="w-full sm:w-auto px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl text-[13px] md:text-sm font-bold text-slate-600 outline-none bg-white">
                      <option value="all">Tất cả khóa học</option>
                      {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                   </select>
                   <select value={sortLecture} onChange={e => setSortLecture(e.target.value)} className="w-full sm:w-auto px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl text-[13px] md:text-sm font-bold text-slate-600 outline-none bg-white">
                      <option value="date-desc">🕐 Mới nhất</option>
                      <option value="date-asc">🕐 Cũ nhất</option>
                      <option value="name-asc">🔤 Tên A → Z</option>
                      <option value="name-desc">🔤 Tên Z → A</option>
                   </select>
                 </div>
              </div>

              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col">
                <div className="overflow-x-auto custom-scrollbar flex-1" style={{ WebkitOverflowScrolling: 'touch' }}>
                  <table className="w-full text-left border-collapse min-w-[800px] md:min-w-[1000px]">
                    <thead className="sticky top-0 bg-[#f8fafc] text-[10px] md:text-[11px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200 shadow-[0_1px_2px_rgba(0,0,0,0.05)] z-10">
                      <tr>
                        <th className="px-4 md:px-6 py-3 md:py-4 w-10 text-center">#</th>
                        <th className="px-2 py-3 md:py-4 w-10"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedLectures.length > 0 && selectedLectures.length === paginatedLectures.length} onChange={(e) => handleSelectAllLectures(e, paginatedLectures)} /></th>
                        <th className="px-4 md:px-6 py-3 md:py-4">TÊN BÀI GIẢNG</th>
                        <th className="px-4 md:px-6 py-3 md:py-4">KHÓA HỌC</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-center">KIỂU NỘI DUNG</th>
                        <th className="px-4 md:px-6 py-3 md:py-4">CẬP NHẬT</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-center">TRẠNG THÁI</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-center">THỨ TỰ</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-right">THAO TÁC</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {paginatedLectures.length === 0 ? <tr><td colSpan={9} className="text-center py-8 md:py-10 text-[13px] md:text-sm text-slate-400 font-medium">Không tìm thấy bài giảng nào.</td></tr> : (
                        paginatedLectures.map((lec, index) => (
                          <tr key={lec.id} className={`hover:bg-slate-50 transition-colors group ${selectedLectures.includes(lec.id) ? 'bg-blue-50/30' : ''}`}>
                            <td className="px-4 md:px-6 py-4 text-center text-[12px] md:text-[13px] font-bold text-slate-400">{(lectureCurrentPage - 1) * lectureItemsPerPage + index + 1}</td>
                            <td className="px-2 py-4"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedLectures.includes(lec.id)} onChange={() => handleSelectOneLecture(lec.id)} /></td>
                            <td className="px-4 md:px-6 py-4 font-bold text-[#0a5482] text-[13px] md:text-[14px]">{lec.title}</td>
                            <td className="px-4 md:px-6 py-4">{lec.courses ? <span className="px-2 py-1 bg-slate-100 border border-slate-200 rounded text-[10px] md:text-[11px] font-bold text-slate-600">{lec.courses.title}</span> : <span className="text-[10px] md:text-[11px] italic text-slate-400">-- Trống --</span>}</td>
                            <td className="px-4 md:px-6 py-4 text-center text-[11px] md:text-[12px] font-bold text-slate-500">HTML</td>
                            <td className="px-4 md:px-6 py-4"><div className="text-[10px] md:text-[11px] text-slate-500 font-medium">{formatDateTime(lec.created_at)}</div></td>
                            <td className="px-4 md:px-6 py-4 text-center"><button onClick={() => handleToggleLectureStatus(lec.id, lec.is_published)} className={`text-[10px] md:text-[12px] font-bold px-2 py-1 md:px-3 rounded transition-colors ${lec.is_published ? 'text-emerald-600 bg-emerald-50 hover:bg-emerald-100' : 'text-slate-500 bg-slate-100 hover:bg-slate-200'}`}>{lec.is_published ? 'Hiển thị' : 'Đang ẩn'}</button></td>
                            <td className="px-4 md:px-6 py-4 text-center"><input type="number" defaultValue={lec.order_index || 0} onBlur={e => handleUpdateLectureOrder(lec.id, parseInt(e.target.value) || 0)} className="w-10 md:w-12 text-center text-[12px] md:text-[13px] font-bold border border-slate-200 rounded py-1 outline-none focus:border-[#2bd6eb]" /></td>
                            <td className="px-4 md:px-6 py-4 text-right space-x-1 md:space-x-2 whitespace-nowrap">
                               <button onClick={() => setEditingLecture(lec)} className="text-[#2bd6eb] font-bold text-[10px] md:text-xs bg-white border border-[#2bd6eb] px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-blue-50 transition">Sửa</button>
                               <button onClick={() => handleDuplicateLecture(lec)} className="text-emerald-600 font-bold text-[10px] md:text-xs bg-white border border-emerald-300 px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-emerald-50 transition">Nhân bản</button>
                               <button onClick={() => handlePermanentDeleteLecture(lec.id)} className="text-red-500 font-bold text-[10px] md:text-xs bg-white border border-red-200 px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-red-50 transition md:opacity-0 group-hover:opacity-100">Xóa</button>
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>

                {totalLecturePages > 1 && (
                  <div className="p-4 border-t border-slate-200 bg-slate-50 flex justify-center items-center gap-4 shrink-0">
                     <button disabled={lectureCurrentPage === 1} onClick={() => setLectureCurrentPage(p => p - 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                        ← Trang trước
                     </button>
                     <span className="text-[13px] font-black text-slate-500">
                        Trang {lectureCurrentPage} <span className="font-medium text-slate-400">/ {totalLecturePages}</span>
                     </span>
                     <button disabled={lectureCurrentPage === totalLecturePages} onClick={() => setLectureCurrentPage(p => p + 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                        Trang sau →
                     </button>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* ========================================================= */}
          {/* VIEW: KHO ĐỀ THI VÀ BÀI TẬP */}
          {activeTab === 'library' && (
            <div className="space-y-4 md:space-y-6">
              <div className="flex flex-col lg:flex-row justify-between gap-3 md:gap-4 bg-white p-3 md:p-4 rounded-xl border border-slate-200 shadow-sm relative z-20">
                <div className="flex flex-wrap items-center gap-3">
                <div className="flex bg-slate-100 rounded-lg p-1 border border-slate-200 shadow-sm shrink-0 overflow-x-auto custom-scrollbar">
                  <button onClick={() => handleBulkVisibility(true)} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-emerald-600 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">👁️ Hiện</button>
                  <button onClick={() => handleBulkVisibility(false)} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-slate-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">👁️‍🗨️ Ẩn</button>
                  <button onClick={handleBulkDuplicateTests} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-purple-600 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">📋 Nhân bản</button>
                  <button onClick={handleBulkDelete} className="px-3 md:px-4 py-1.5 text-[11px] md:text-[13px] font-bold text-red-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95 whitespace-nowrap">🗑️ Xóa</button>
                </div>

                <div className="flex items-center gap-2 bg-blue-50 p-1.5 md:p-2 rounded-lg border border-blue-100 shadow-sm">
                   <span className="text-[11px] font-bold text-blue-800 hidden sm:inline ml-1 uppercase tracking-tight">Chuyển:</span>
                   <select value={targetMoveTestCourseId} onChange={e=>setTargetMoveTestCourseId(e.target.value)} className="border border-blue-200 bg-white rounded px-2 py-1 md:py-1.5 text-[11px] md:text-[13px] font-bold text-slate-700 outline-none w-[140px] md:w-[200px] truncate focus:border-[#0a5482]">
                      <option value="">-- Chọn Khóa Học --</option>
                      <option value="none">-- 📦 Không thuộc khóa nào --</option>
                      {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                   </select>
                   <button onClick={handleBulkMoveTestCourse} className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-3 py-1 md:py-1.5 rounded shadow-sm text-[11px] transition-colors whitespace-nowrap active:scale-95">ÁP DỤNG</button>
                </div>
              </div>
                
                <div className="flex flex-col sm:flex-row gap-3 flex-1 justify-end w-full lg:w-auto">
                  <input type="text" placeholder="Tìm kiếm tên..." defaultValue={searchQuery} onChange={e => { clearTimeout(adminSearchTimer); adminSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350); }} className="w-full sm:max-w-[200px] px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl outline-none focus:border-[#2bd6eb] text-[13px] md:text-sm transition-colors" />
                  
                  <select value={filterCourse} onChange={e => setFilterCourse(e.target.value)} className="w-full sm:w-auto px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl text-[13px] md:text-sm font-bold text-slate-600 outline-none bg-white">
                    <option value="all">Tất cả khóa học</option>{courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                  </select>

                  <select value={filterCategory} onChange={e => setFilterCategory(e.target.value)} className="w-full sm:w-auto px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl text-[13px] md:text-sm font-bold text-slate-600 outline-none bg-white">
                    <option value="all">Tất cả loại</option>
                    <option value="test">Chỉ Đề thi</option>
                    <option value="exercise">Chỉ Bài tập</option>
                  </select>
                  <select value={sortTest} onChange={e => setSortTest(e.target.value)} className="w-full sm:w-auto px-3 py-2 md:py-2.5 border border-slate-200 rounded-lg md:rounded-xl text-[13px] md:text-sm font-bold text-slate-600 outline-none bg-white">
                    <option value="date-desc">🕐 Mới nhất</option>
                    <option value="date-asc">🕐 Cũ nhất</option>
                    <option value="name-asc">🔤 Tên A → Z</option>
                    <option value="name-desc">🔤 Tên Z → A</option>
                    <option value="type">📂 Theo loại đề</option>
                  </select>
                </div>
              </div>

              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden z-10 relative">
                <div className="overflow-x-auto custom-scrollbar" style={{ WebkitOverflowScrolling: 'touch' }}>
                  <table className="w-full text-left border-collapse min-w-[900px] md:min-w-[1000px]">
                    <thead className="bg-[#f8fafc] text-[10px] md:text-[11px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200">
                      <tr>
                        <th className="px-3 md:px-4 py-3 md:py-4 w-10 text-center">#</th>
                        <th className="px-2 py-3 md:py-4 w-10"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.length > 0 && selectedTests.length === filteredLibraryTests.length} onChange={(e) => handleSelectAll(e, filteredLibraryTests)} /></th>
                        <th className="px-4 md:px-6 py-3 md:py-4">TÊN MỤC</th>
                        <th className="px-4 md:px-6 py-3 md:py-4">KHÓA HỌC</th>
                        <th className="px-4 md:px-6 py-3 md:py-4">KỸ NĂNG</th>
                        <th className="px-4 md:px-6 py-3 md:py-4">CẬP NHẬT</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-center">TRẠNG THÁI</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-center">THỨ TỰ</th>
                        <th className="px-4 md:px-6 py-3 md:py-4 text-right">THAO TÁC</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {filteredLibraryTests.length === 0 ? <tr><td colSpan={9} className="text-center py-8 md:py-10 text-[13px] md:text-sm text-slate-400 font-medium">Không tìm thấy mục nào phù hợp.</td></tr> : (
                        filteredLibraryTests.map((test, index) => (
                          <tr key={test.id} className={`hover:bg-slate-50 transition group bg-white ${selectedTests.includes(test.id) ? 'bg-blue-50/30' : ''}`}>
                            <td className="px-3 md:px-4 py-4 md:py-5 text-center text-[12px] md:text-[13px] font-bold text-slate-400">{index + 1}</td>
                            <td className="px-2 py-4 md:py-5"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.includes(test.id)} onChange={() => handleSelectOne(test.id)} /></td>
                            <td className="px-4 md:px-6 py-4 md:py-5">
                               <div className="font-bold text-[#0a5482] text-[13px] md:text-[15px] flex items-center gap-2">
                                  {test.title}
                                  <span className="text-[8px] md:text-[9px] px-1 md:px-1.5 py-0.5 rounded uppercase tracking-wider font-black bg-sky-100 text-sky-700">
                                     {test.test_type || 'Đề thi'}
                                  </span>
                               </div>
                               <div className="text-[10px] md:text-[11px] text-slate-400 mt-1 font-medium uppercase tracking-tight">{test.folder_id ? 'Đã gán thư mục' : 'Chưa gán thư mục'}</div>
                            </td>
                            <td className="px-4 md:px-6 py-4 md:py-5">{test.course_id ? <span className="px-2 py-1 bg-slate-100 border border-slate-200 rounded text-[10px] md:text-[11px] font-bold text-slate-600">{getCourseNameForTest(test.course_id)}</span> : <span className="text-[10px] md:text-[11px] italic text-slate-400">-- Chung --</span>}</td>
                            <td className="px-4 md:px-6 py-4 md:py-5 font-black text-blue-600 uppercase text-[10px] md:text-[11px] tracking-tight">{test.test_type}</td>
                            <td className="px-4 md:px-6 py-4 md:py-5"><div className="text-[10px] md:text-[11px] text-slate-500 font-medium">{formatDateTime(test.created_at)}</div></td>
                            <td className="px-4 md:px-6 py-4 md:py-5 text-center"><button onClick={() => handleToggleTestVisibility(test)} className={`text-[10px] md:text-[12px] font-bold px-2 md:px-3 py-1 rounded transition-colors ${test.is_published ? 'text-emerald-600 bg-emerald-50 hover:bg-emerald-100' : 'text-slate-500 bg-slate-100 hover:bg-slate-200'}`}>{test.is_published ? 'Hiển thị' : 'Đang ẩn'}</button></td>
                            <td className="px-4 md:px-6 py-4 md:py-5 text-center"><input type="number" defaultValue={test.order_index || 0} onBlur={e => handleUpdateTestOrder(test.id, parseInt(e.target.value) || 0)} className="w-10 md:w-12 text-center text-[12px] md:text-[13px] font-bold border border-slate-200 rounded py-1 outline-none focus:border-[#2bd6eb]" /></td>
                            <td className="px-4 md:px-6 py-4 md:py-5 text-right space-x-1 md:space-x-2 whitespace-nowrap">
                                 <button onClick={async () => { if (test.test_type === 'IGCSE-Science' || test.test_type === 'IGCSE-Math' || test.test_type === 'IGCSE-Direct') { setIgcseEditingTestId(test.id); setIgcseEditorOpen(true); } else { const { data: fullTest } = await supabase.from('tests').select('*').eq('id', test.id).single(); if (fullTest) setEditingTest(fullTest); else alert('Lỗi tải dữ liệu đề thi!'); } }} className="text-[#2bd6eb] bg-white border border-[#2bd6eb] px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-blue-50 font-bold text-[10px] md:text-xs transition shadow-sm">Sửa</button>
                                 <button onClick={() => handleDuplicateTest(test)} className="text-emerald-600 font-bold text-[10px] md:text-xs bg-white border border-emerald-300 px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-emerald-50 transition shadow-sm">Nhân bản</button>
                                 <button onClick={() => handleDeleteTest(test.id)} className="text-red-500 font-bold text-[10px] md:text-xs bg-white border border-red-200 px-2 md:px-3 py-1 md:py-1.5 rounded hover:bg-red-50 transition md:opacity-0 group-hover:opacity-100 shadow-sm">Xóa</button>
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'students' && <StudentManagement onStartTest={onStartTest} autoSelectUserId={notifTargetUserId} autoTab={notifTargetTab as any} onAutoSelectDone={() => { setNotifTargetUserId(null); setNotifTargetTab(null); }} />}
        </div>

        {/* ========================================================================================= */}
        {/* CÁC MODALS */}
        {/* ========================================================================================= */}

        {/* 🚀 MODAL CÀI ĐẶT DEADLINE NỘP BÀI (SỬA NHANH CHO 1 BÀI) */}
        {deadlineModal.show && deadlineModal.test && (
            <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleSaveDeadline} className="bg-white rounded-3xl w-full max-w-sm p-6 md:p-8 shadow-2xl animate-in zoom-in-95">
                    <h2 className="text-lg font-black text-slate-800 mb-2 uppercase tracking-tight">Cài đặt Deadline</h2>
                    <p className="text-[13px] text-slate-500 mb-6 truncate font-medium bg-slate-50 p-2 rounded border border-slate-100">📝 {deadlineModal.test.title}</p>
                    
                    <div className="space-y-4 mb-6">
                        <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block">Hạn chót nộp bài</label>
                        <input 
                            name="datetime" 
                            type="datetime-local" 
                            defaultValue={getDefaultDateTime(deadlineModal.test.content_json?.basicInfo?.classDeadlines?.[selectedClass?.id])}
                            className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-orange-500 text-sm font-bold text-slate-700 bg-slate-50" 
                        />
                        <p className="text-[10px] text-slate-400 italic">* Để trống và bấm Lưu nếu muốn gỡ bỏ deadline.</p>
                    </div>
                    
                    <div className="flex gap-3">
                        <button type="button" onClick={() => setDeadlineModal({show: false, test: null})} className="flex-1 font-bold py-3 text-slate-500 bg-slate-100 hover:bg-slate-200 rounded-xl transition text-[13px]">Hủy</button>
                        <button type="submit" className="flex-1 bg-orange-500 text-white font-black py-3 rounded-xl shadow-md hover:bg-orange-600 transition text-[13px]">LƯU HẠN NỘP</button>
                    </div>
                </form>
            </div>
        )}

        {/* 🚀 MODAL GIAO NHIỀU BÀI & ĐẶT DEADLINE CHO LỚP (BẢN CHUYÊN NGHIỆP) */}
        {showAssignDeadlineModal && selectedClass && (
            <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-3xl w-full max-w-3xl shadow-2xl flex flex-col max-h-[90vh] overflow-hidden animate-in zoom-in-95">
                    
                    <div className="bg-[#0f172a] p-4 md:p-6 text-white flex justify-between items-center shrink-0">
                        <div>
                            <h2 className="font-black uppercase text-[12px] md:text-[15px] tracking-widest text-orange-400">Giao Bài & Đặt Deadline</h2>
                            <p className="text-[11px] md:text-[12px] text-slate-400 mt-1">Lớp: {selectedClass.name}</p>
                        </div>
                        <button onClick={() => setShowAssignDeadlineModal(false)} className="text-xl md:text-2xl hover:text-red-400 transition-colors">&times;</button>
                    </div>

                    <div className="p-4 bg-slate-50 border-b border-slate-200 flex flex-col sm:flex-row gap-3 shrink-0">
                        <div className="relative flex-1">
                            <input 
                                type="text" 
                                placeholder="Tìm kiếm tên bài..." 
                                value={assignTestSearch}
                                onChange={(e) => setAssignTestSearch(e.target.value)}
                                className="w-full border border-slate-300 rounded-xl px-4 py-2 text-sm outline-none focus:border-orange-500 transition-colors"
                            />
                        </div>
                        <select 
                            value={assignTestSort} 
                            onChange={(e) => setAssignTestSort(e.target.value)}
                            className="w-full sm:w-40 border border-slate-300 rounded-xl px-3 py-2 text-sm font-bold text-slate-600 outline-none focus:border-orange-500 bg-white"
                        >
                            <option value="date-desc">Mới nhất trước</option>
                            <option value="date-asc">Cũ nhất trước</option>
                            <option value="name-asc">Tên (A-Z)</option>
                            <option value="name-desc">Tên (Z-A)</option>
                        </select>
                    </div>

                    <div className="flex-1 overflow-y-auto p-4 custom-scrollbar bg-slate-50/50">
                        <table className="w-full text-left border-collapse">
                            <thead className="sticky top-0 bg-white shadow-sm z-10 rounded-lg overflow-hidden">
                                <tr>
                                    <th className="px-4 py-3 w-12 text-center bg-slate-100">
                                        <input 
                                            type="checkbox" 
                                            checked={selectedDeadlineTests.length > 0 && selectedDeadlineTests.length === filteredAssignTests.length} 
                                            onChange={handleSelectAllDeadlineTests} 
                                            className="rounded cursor-pointer w-4 h-4" 
                                        />
                                    </th>
                                    <th className="px-4 py-3 text-[11px] font-black text-slate-500 uppercase tracking-widest bg-slate-100">Tên Bài Tập / Đề Thi</th>
                                    <th className="px-4 py-3 text-[11px] font-black text-slate-500 uppercase tracking-widest text-right bg-slate-100">Hạn Nộp Hiện Tại</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-100">
                                {filteredAssignTests.length === 0 ? (
                                    <tr><td colSpan={3} className="text-center py-10 text-sm text-slate-400 font-medium">Không tìm thấy bài tập nào.</td></tr>
                                ) : (
                                    filteredAssignTests.map(t => {
                                        const dl = t.content_json?.basicInfo?.classDeadlines?.[selectedClass.id];
                                        const isSelected = selectedDeadlineTests.includes(t.id);
                                        return (
                                            <tr key={t.id} className={`hover:bg-orange-50/50 transition-colors cursor-pointer ${isSelected ? 'bg-orange-50/30' : 'bg-white'}`} onClick={() => handleSelectOneDeadlineTest(t.id)}>
                                                <td className="px-4 py-4 text-center">
                                                    <input type="checkbox" checked={isSelected} readOnly className="rounded cursor-pointer pointer-events-none w-4 h-4 accent-orange-500" />
                                                </td>
                                                <td className="px-4 py-4">
                                                    <p className="font-bold text-[13px] text-slate-700 leading-snug">{t.title}</p>
                                                    <p className="text-[10px] text-slate-400 mt-1 uppercase font-black">{t.test_type}</p>
                                                </td>
                                                <td className="px-4 py-4 text-right">
                                                    {dl ? (
                                                        <span className="text-[11px] font-bold text-orange-600 bg-orange-100 border border-orange-200 px-2.5 py-1 rounded-md whitespace-nowrap">
                                                            ⏳ {formatDateTime(dl)}
                                                        </span>
                                                    ) : (
                                                        <span className="text-[11px] text-slate-400 italic">-- Chưa có --</span>
                                                    )}
                                                </td>
                                            </tr>
                                        )
                                    })
                                )}
                            </tbody>
                        </table>
                    </div>

                    <div className="p-4 md:p-6 bg-white border-t border-slate-200 shrink-0">
                        <div className="flex flex-col sm:flex-row gap-4 items-end sm:items-center">
                            <div className="flex-1 w-full">
                                <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest block mb-2">Hạn chót nộp bài (Để trống để Gỡ Hạn)</label>
                                <input 
                                    type="datetime-local" 
                                    value={deadlineInput}
                                    onChange={(e) => setDeadlineInput(e.target.value)}
                                    className="w-full border border-slate-300 rounded-xl px-4 py-2.5 outline-none focus:ring-2 focus:ring-orange-500 text-sm font-bold text-slate-700 bg-slate-50" 
                                />
                            </div>
                            <div className="flex gap-2 w-full sm:w-auto shrink-0">
                                <button onClick={handleSaveBulkDeadline} className={`flex-1 sm:flex-none text-white font-black py-2.5 px-6 rounded-xl shadow-md transition-colors text-[13px] uppercase tracking-widest whitespace-nowrap ${deadlineInput ? 'bg-orange-500 hover:bg-orange-600' : 'bg-red-500 hover:bg-red-600'}`}>
                                    {deadlineInput ? 'LƯU HẠN NỘP' : 'GỠ HẠN NỘP'} ({selectedDeadlineTests.length})
                                </button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        )}


        {/* Modal TẠO FOLDER PDF MỚI */}
        {showPdfFolderModal && (
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleCreatePdfFolder} className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 shadow-2xl animate-in zoom-in-95">
                    <h2 className="text-base md:text-lg font-black uppercase text-emerald-600">Thêm Thư Mục Tài Liệu</h2>
                    <input name="name" required autoFocus placeholder="VD: Sách Reading, Ngữ pháp..." className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 outline-none focus:border-emerald-500 text-[14px]" />
                    <div className="flex gap-3 md:gap-4">
                        <button type="button" onClick={() => setShowPdfFolderModal(false)} className="flex-1 font-bold py-2.5 md:py-3 text-slate-400 hover:bg-slate-50 rounded-lg md:rounded-xl transition text-[13px] md:text-base">Hủy</button>
                        <button type="submit" className="flex-1 bg-[#00a651] hover:bg-[#008f45] transition text-white font-black py-2.5 md:py-3 rounded-lg md:rounded-xl shadow-lg text-[13px] md:text-base">TẠO</button>
                    </div>
                </form>
            </div>
        )}

        {/* Modal DI CHUYỂN FILE PDF */}
        {showMoveFileModal && (
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 shadow-2xl animate-in zoom-in-95">
                    <h2 className="text-base md:text-lg font-black uppercase text-[#0a5482]">Chuyển Thư Mục</h2>
                    <p className="text-[13px] md:text-sm text-slate-600 truncate font-medium bg-slate-50 p-2 rounded-lg border border-slate-200">
                        📄 {showMoveFileModal}
                    </p>
                    <div className="max-h-[40vh] overflow-y-auto border border-slate-200 rounded-xl p-2 space-y-1 custom-scrollbar">
                        <button onClick={() => handleMovePdfFile(showMoveFileModal, null)} className={`w-full text-left px-3 md:px-4 py-2 md:py-3 rounded-lg text-[13px] md:text-sm font-bold flex items-center gap-2 ${!pdfFileMapping[showMoveFileModal] ? 'bg-[#2bd6eb] text-white' : 'hover:bg-slate-100 text-slate-700'}`}>
                            📁 Thư mục gốc (Mặc định)
                        </button>
                        {pdfFolders.map(f => (
                            <button key={f.id} onClick={() => handleMovePdfFile(showMoveFileModal, f.id)} className={`w-full text-left px-3 md:px-4 py-2 md:py-3 rounded-lg text-[13px] md:text-sm font-bold flex items-center gap-2 ${pdfFileMapping[showMoveFileModal] === f.id ? 'bg-[#2bd6eb] text-white' : 'hover:bg-slate-100 text-slate-700'}`}>
                                📁 {f.name}
                            </button>
                        ))}
                    </div>
                    <button onClick={() => setShowMoveFileModal(null)} className="w-full font-bold py-2.5 md:py-3 bg-slate-100 hover:bg-slate-200 rounded-lg md:rounded-xl transition text-[13px] md:text-base text-slate-600">Đóng</button>
                </div>
            </div>
        )}
        
        {/* Modal Class */}
        {showClassModal && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleCreateClass} className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 animate-in zoom-in-95 shadow-2xl">
                    <h2 className="text-base md:text-lg font-black uppercase text-[#0a5482]">Thêm Lớp Mới</h2>
                    <input name="name" required autoFocus placeholder="VD: Lớp IELTS K20" className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 outline-none focus:border-[#0a5482] transition-colors text-[14px]" />
                    <div className="flex gap-3 md:gap-4">
                        <button type="button" onClick={() => setShowClassModal(false)} className="flex-1 font-bold py-2.5 md:py-3 text-[13px] md:text-base text-slate-400 hover:bg-slate-50 rounded-lg md:rounded-xl transition">Hủy</button>
                        <button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-2.5 md:py-3 rounded-lg md:rounded-xl shadow-lg text-[13px] md:text-base">TẠO LỚP</button>
                    </div>
                </form>
            </div> 
        )}
        
        {/* Modal Gán Học phần */}
        {showAssignClassModuleModal && selectedClass && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-lg shadow-2xl overflow-hidden animate-in fade-in">
                    <div className="bg-[#0f172a] p-4 md:p-6 text-white flex justify-between items-center">
                        <h2 className="font-black uppercase text-[11px] md:text-sm tracking-widest">Chọn học phần mở cho lớp</h2>
                        <button onClick={() => setShowAssignClassModuleModal(false)} className="text-xl md:text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button>
                    </div>
                    <div className="p-4 md:p-6 max-h-[60vh] overflow-y-auto space-y-2 md:space-y-3 custom-scrollbar">
                        {lectureModules.filter(m => !classModules.includes(m.id)).map(mod => (
                            <div key={mod.id} className="flex justify-between items-center p-3 md:p-4 border border-slate-200 rounded-xl bg-slate-50 hover:border-emerald-400 transition-colors">
                                <p className="font-black text-slate-700 text-[13px] md:text-sm truncate pr-2">{mod.title}</p>
                                <button onClick={() => handleAssignModuleToClass(mod.id)} className="bg-emerald-500 hover:bg-emerald-600 transition text-white px-3 md:px-5 py-1.5 md:py-2 rounded-lg md:rounded-xl font-bold text-[10px] md:text-xs shadow-sm shrink-0 whitespace-nowrap">MỞ ➜</button>
                            </div>
                        ))}
                        {lectureModules.filter(m => !classModules.includes(m.id)).length === 0 && <p className="text-center text-slate-400 text-[13px] md:text-sm">Đã mở tất cả học phần.</p>}
                    </div>
                </div>
            </div> 
        )}
        
        {/* Modal Gán Học Sinh */}
        {showAssignStudentModal && selectedClass && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-lg shadow-2xl overflow-hidden animate-in fade-in">
                    <div className="bg-[#0f172a] p-4 md:p-6 text-white flex justify-between items-center">
                        <h2 className="font-black uppercase text-[11px] md:text-sm tracking-widest">Thêm Học Sinh</h2>
                        <button onClick={() => setShowAssignStudentModal(false)} className="text-xl md:text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button>
                    </div>
                    <div className="p-4 md:p-6 max-h-[60vh] overflow-y-auto space-y-2 md:space-y-3 custom-scrollbar">
                        {courseStudentsList.filter(cs => !classStudentsList.some(cls => cls.user_id === cs.user_id)).map(st => (
                            <div key={st.user_id} className="flex justify-between items-center p-3 md:p-4 border border-slate-200 rounded-xl bg-slate-50 hover:border-blue-400 transition-colors">
                                <div className="min-w-0 pr-2">
                                    <p className="font-black text-slate-700 text-[13px] md:text-sm truncate">{st.full_name || 'Học viên'}</p>
                                    <p className="text-[10px] md:text-[11px] text-slate-500 truncate">{st.email}</p>
                                </div>
                                <button onClick={() => handleAssignStudentToClass(st.user_id)} className="bg-blue-500 hover:bg-blue-600 transition text-white px-3 md:px-5 py-1.5 md:py-2 rounded-lg md:rounded-xl font-bold text-[10px] md:text-xs shadow-sm shrink-0 whitespace-nowrap">THÊM ➜</button>
                            </div>
                        ))}
                        {courseStudentsList.filter(cs => !classStudentsList.some(cls => cls.user_id === cs.user_id)).length === 0 && (
                            <p className="text-center text-slate-400 text-[13px] md:text-sm">Không còn học sinh nào để thêm.</p>
                        )}
                    </div>
                </div>
            </div> 
        )}
        
        {/* Modal Gán Bài Giảng */}
        {showAssignLectureModal.show && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-xl shadow-2xl overflow-hidden animate-in fade-in">
                    <div className="bg-[#0f172a] p-4 md:p-6 text-white flex justify-between items-center">
                        <h2 className="font-black uppercase text-[11px] md:text-sm tracking-widest">Chọn bài giảng từ Kho</h2>
                        <button onClick={() => setShowAssignLectureModal({show: false, moduleId: null})} className="text-xl md:text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button>
                    </div>
                    <div className="p-4 md:p-6 max-h-[60vh] overflow-y-auto space-y-2 md:space-y-3 custom-scrollbar">
                        {globalLectures.filter(l => !l.module_id && l.course_id === selectedCourse.id).map(lec => (
                            <div key={lec.id} className="flex justify-between items-center p-3 md:p-4 border border-slate-100 rounded-xl md:rounded-2xl hover:border-blue-400 transition bg-slate-50">
                                <p className="font-black text-slate-700 text-[13px] md:text-sm truncate pr-2">{lec.title}</p>
                                <button onClick={() => handleAssignLecture(lec.id, showAssignLectureModal.moduleId!)} className="bg-blue-600 hover:bg-blue-700 transition text-white px-3 md:px-5 py-1.5 md:py-2 rounded-lg md:rounded-xl font-bold text-[10px] md:text-xs shadow-sm shrink-0 whitespace-nowrap">GÁN ➜</button>
                            </div>
                        ))}
                        {globalLectures.filter(l => !l.module_id && l.course_id === selectedCourse.id).length === 0 && <p className="text-center text-slate-400 text-[13px] md:text-sm italic">Không có bài giảng nào chờ gán.</p>}
                    </div>
                </div>
            </div> 
        )}
        
        {/* Modal Khóa Học */}
        {showCreateCourseModal && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleCreateCourse} className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 animate-in zoom-in-95 shadow-2xl">
                    <h2 className="text-lg md:text-xl font-black text-slate-800 uppercase tracking-tight">Thêm Khóa Học</h2>
                    <div className="space-y-3 md:space-y-4">
                        <input name="title" required autoFocus placeholder="Tên khóa học..." className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 outline-none focus:border-[#0a5482] transition-colors text-[14px]" />
                        <select name="type" className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 bg-white outline-none text-[14px]">
                            <option value="IELTS">Hệ IELTS</option>
                            <option value="Standard">Hệ Standard (IGCSE/TOEIC)</option>
                        </select>
                    </div>
                    <div className="flex gap-3 md:gap-4">
                        <button type="button" onClick={() => setShowCreateCourseModal(false)} className="flex-1 font-bold py-2.5 md:py-3 text-slate-400 hover:bg-slate-50 rounded-lg md:rounded-xl transition text-[13px] md:text-base">Hủy</button>
                        <button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-2.5 md:py-3 rounded-lg md:rounded-xl shadow-lg text-[13px] md:text-base">LƯU</button>
                    </div>
                </form>
            </div> 
        )}
        
        {/* Modal Module */}
        {showModuleModal && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleCreateLectureModule} className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 animate-in zoom-in-95 shadow-2xl">
                    <h2 className="text-base md:text-lg font-black uppercase text-[#0a5482]">Thêm Học Phần Mới</h2>
                    <input name="title" required autoFocus placeholder="VD: Lesson 1: Grammar..." className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 outline-none focus:border-[#0a5482] transition-colors text-[14px]" />
                    <div className="flex gap-3 md:gap-4">
                        <button type="button" onClick={() => setShowModuleModal(false)} className="flex-1 font-bold py-2.5 md:py-3 text-slate-400 hover:bg-slate-50 rounded-lg md:rounded-xl transition text-[13px] md:text-base">Hủy</button>
                        <button type="submit" className="flex-1 bg-[#0a5482] hover:bg-[#084266] transition text-white font-black py-2.5 md:py-3 rounded-lg md:rounded-xl shadow-lg text-[13px] md:text-base">TẠO MỚI</button>
                    </div>
                </form>
            </div> 
        )}
        
        {/* Modal Thư mục */}
        {showFolderModal && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <form onSubmit={handleCreateFolder} className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-md p-6 md:p-8 space-y-4 md:space-y-6 animate-in zoom-in-95 shadow-2xl">
                    <h2 className="text-base md:text-lg font-black uppercase text-emerald-600">{currentFolderId ? 'Thêm Mục Con' : 'Thêm Mục Mới'}</h2>
                    <input name="title" required autoFocus placeholder="Tên thư mục..." className="w-full border border-slate-200 rounded-lg md:rounded-xl px-3 md:px-4 py-2.5 md:py-3 outline-none focus:border-emerald-500 transition-colors text-[14px]" />
                    <div className="flex gap-3 md:gap-4">
                        <button type="button" onClick={() => setShowFolderModal(false)} className="flex-1 font-bold py-2.5 md:py-3 text-slate-400 hover:bg-slate-50 rounded-lg md:rounded-xl transition text-[13px] md:text-base">Hủy</button>
                        <button type="submit" className="flex-1 bg-[#00a651] hover:bg-[#008f45] transition text-white font-black py-2.5 md:py-3 rounded-lg md:rounded-xl shadow-lg text-[13px] md:text-base">TẠO MỚI</button>
                    </div>
                </form>
            </div> 
        )}
        
        {/* Modal Gán Đề Thi */}
        {showAssignModal && ( 
            <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 animate-in fade-in">
                <div className="bg-white rounded-2xl md:rounded-3xl w-full max-w-[95vw] md:max-w-xl shadow-2xl overflow-hidden animate-in fade-in">
                    <div className="bg-[#0f172a] p-4 md:p-6 text-white flex justify-between items-center">
                        <h2 className="font-black uppercase text-[11px] md:text-sm tracking-widest">Gán từ Kho chung</h2>
                        <button onClick={() => setShowAssignModal(false)} className="text-xl md:text-2xl hover:text-[#2bd6eb] transition-colors">&times;</button>
                    </div>
                    <div className="p-4 md:p-6 max-h-[60vh] overflow-y-auto space-y-2 md:space-y-3 custom-scrollbar">
                        {libraryTests.filter(t => !t.folder_id && t.course_id === selectedCourse.id).map(test => (
                            <div key={test.id} className="flex justify-between items-center p-3 md:p-4 border border-slate-100 rounded-xl md:rounded-2xl hover:border-[#2bd6eb] transition bg-slate-50 group">
                                <div className="min-w-0 pr-2">
                                    <p className="font-black text-slate-700 text-[13px] md:text-sm truncate">{test.title}</p>
                                    <p className="text-[9px] md:text-[10px] font-black text-slate-400 uppercase tracking-tighter mt-1">{test.test_type}</p>
                                </div>
                                <button onClick={() => handleAssignTest(test.id)} className="bg-white md:group-hover:bg-[#2bd6eb] md:group-hover:text-white px-3 md:px-5 py-1.5 md:py-2 rounded-lg md:rounded-xl font-bold text-[10px] md:text-xs transition border border-slate-200 shadow-sm shrink-0 whitespace-nowrap">GÁN ➜</button>
                            </div>
                        ))}
                        {libraryTests.filter(t => !t.folder_id && t.course_id === selectedCourse.id).length === 0 && <p className="text-center text-slate-400 text-[13px] md:text-sm italic">Không có đề thi chờ gán.</p>}
                    </div>
                </div>
            </div> 
        )}
        
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

        <IgcseTestEditorModal
          isOpen={igcseEditorOpen}
          onClose={() => { setIgcseEditorOpen(false); setIgcseEditingTestId(null); }}
          courseId={selectedCourse?.id || ''}
          existingTestId={igcseEditingTestId}
          onSaveSuccess={() => { fetchLibraryTests(); if (selectedCourse) fetchCourseDetailsData(selectedCourse.id); }}
        />

      </main>
    </div>
  );
}