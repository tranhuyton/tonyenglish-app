import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import TestEditorModal from './TestEditorModal';
import CaseStudyEditorModal from './CaseStudyEditorModal'; 
import StudentManagement from './StudentManagement'; // <-- IMPORT GIAO DIỆN QUẢN LÝ HỌC VIÊN
import './tailwind.css';

export default function AdminPanel({ onNavigate }: { onNavigate?: (view: string) => void }) {
  const [activeTab, setActiveTab] = useState('library'); 
  const [showCreateDropdown, setShowCreateDropdown] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  // --- DATABASE STATES ---
  const [courses, setCourses] = useState<any[]>([]);
  const [folders, setFolders] = useState<any[]>([]);
  const [allFolders, setAllFolders] = useState<any[]>([]); 
  const [libraryTests, setLibraryTests] = useState<any[]>([]); 
  const [assignedTests, setAssignedTests] = useState<any[]>([]); 
  const [selectedCourse, setSelectedCourse] = useState<any>(null);
  
  // --- UI STATES ---
  const [currentFolderId, setCurrentFolderId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterCourse, setFilterCourse] = useState('all');
  const [sortLibrary, setSortLibrary] = useState('name-asc');
  const [selectedTests, setSelectedTests] = useState<string[]>([]);

  const [editingTest, setEditingTest] = useState<any>(null);
  const [showCreateCourseModal, setShowCreateCourseModal] = useState(false);
  const [showFolderModal, setShowFolderModal] = useState(false);
  const [showAssignModal, setShowAssignModal] = useState(false);
  
  const [newCourse, setNewCourse] = useState({ title: '', type: 'IELTS' });
  const [newFolderTitle, setNewFolderTitle] = useState('');

  useEffect(() => {
    fetchCourses();
    fetchLibraryTests();
    fetchAllFolders(); 
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setShowCreateDropdown(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const fetchCourses = async () => {
    const { data } = await supabase.from('courses').select('*').order('created_at', { ascending: false });
    setCourses(data || []);
  };

  const fetchLibraryTests = async () => {
    const { data } = await supabase.from('tests').select('*').order('created_at', { ascending: false });
    setLibraryTests(data || []);
  };

  const fetchAllFolders = async () => {
    const { data } = await supabase.from('folders').select('*').order('display_order', { ascending: true });
    setAllFolders(data || []);
  };

  const fetchFoldersByCourse = async (courseId: string) => {
    const { data } = await supabase.from('folders').select('*').eq('course_id', courseId).order('display_order', { ascending: true });
    setFolders(data || []);
  };

  const fetchAssignedTests = async (courseId: string) => {
    const { data } = await supabase.from('tests').select('*, folders!inner(course_id)').eq('folders.course_id', courseId);
    setAssignedTests(data || []);
  };

  const handleCreateCourse = async (e: React.FormEvent) => {
    e.preventDefault();
    const { data, error } = await supabase.from('courses').insert([newCourse]).select();
    if (!error && data) {
      setCourses([data[0], ...courses]);
      setShowCreateCourseModal(false);
      setNewCourse({ title: '', type: 'IELTS' });
    }
  };

  const handleCreateFolder = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedCourse) return;
    const { data, error } = await supabase.from('folders').insert([{ 
      course_id: selectedCourse.id, 
      title: newFolderTitle,
      parent_id: currentFolderId, 
      display_order: folders.length + 1
    }]).select();
    
    if (!error && data) {
      setFolders([...folders, data[0]]);
      fetchAllFolders(); 
      setShowFolderModal(false);
      setNewFolderTitle('');
    }
  };

  const handleDeleteCourse = async () => {
    if (window.confirm("Xác nhận xóa khóa học? Mọi thư mục bên trong sẽ bị xóa.") && selectedCourse) {
      await supabase.from('courses').delete().eq('id', selectedCourse.id);
      setCourses(courses.filter(c => c.id !== selectedCourse.id));
      setActiveTab('courses');
    }
  };

  const handleDeleteFolder = async (id: string) => {
    if (window.confirm("Xóa thư mục này và các thư mục con bên trong?")) {
      await supabase.from('folders').delete().eq('id', id);
      const newFolders = folders.filter(f => f.id !== id && f.parent_id !== id);
      setFolders(newFolders);
      fetchAllFolders();
    }
  };

  const handleInitiateTest = (mode: 'manual' | 'import' | 'case-study') => {
    setShowCreateDropdown(false);
    setEditingTest({ 
      id: 'new', 
      title: '', 
      folder_id: '', 
      test_type: mode === 'case-study' ? 'Case-Study' : 'IELTS-Listening', 
      content_json: null, 
      mode 
    });
  };

  const handleSaveTestContent = async (testId: string, finalData: any) => {
    let parsedJsonConfig = null;
    if (finalData.basicInfo?.skill === 'Case-Study' && finalData.json_config_string) {
      try {
        parsedJsonConfig = JSON.parse(finalData.json_config_string);
      } catch(e) {
        alert("⚠️ Lỗi cú pháp JSON. Anh vui lòng kiểm tra lại dấu ngoặc hoặc dấu phẩy trước khi lưu nhé!");
        return; 
      }
    }

    const payload: any = {
      title: finalData.basicInfo?.title || 'Untitled Test',
      test_type: finalData.basicInfo?.skill || 'IELTS-Listening',
      content_json: finalData,
      json_config: parsedJsonConfig, 
      folder_id: finalData.folder_id, 
      is_published: true,
      insert_pdf_url: finalData.basicInfo?.insert_pdf_url || null 
    };

    try {
      if (testId === 'new') {
        const { error } = await supabase.from('tests').insert([payload]);
        if (error) throw error;
      } else {
        const { error } = await supabase.from('tests').update(payload).eq('id', testId);
        if (error) throw error;
      }
      setEditingTest(null);
      fetchLibraryTests();
      if (selectedCourse) fetchAssignedTests(selectedCourse.id);
      alert("✅ Đã lưu đề thi thành công!");
    } catch (err: any) {
      alert("❌ Lỗi khi lưu vào Database: " + err.message);
    }
  };

  const handleAssignTest = async (testId: string) => {
    if (!currentFolderId) return;
    await supabase.from('tests').update({ folder_id: currentFolderId }).eq('id', testId);
    fetchLibraryTests();
    if (selectedCourse) fetchAssignedTests(selectedCourse.id);
    setShowAssignModal(false);
  };

  const handleUnassignTest = async (testId: string) => {
    if (window.confirm("Gỡ đề thi khỏi thư mục này?")) {
      await supabase.from('tests').update({ folder_id: null }).eq('id', testId);
      if (selectedCourse) fetchAssignedTests(selectedCourse.id);
      fetchLibraryTests();
    }
  };

  const handleDeleteTest = async (id: string) => {
    if (window.confirm("Xóa vĩnh viễn đề thi khỏi kho?")) {
      await supabase.from('tests').delete().eq('id', id);
      fetchLibraryTests();
      setSelectedTests(selectedTests.filter(testId => testId !== id));
    }
  };

  const handleToggleTestVisibility = async (test: any) => {
    const newStatus = !test.is_published;
    await supabase.from('tests').update({ is_published: newStatus }).eq('id', test.id);
    setLibraryTests(libraryTests.map(t => t.id === test.id ? { ...t, is_published: newStatus } : t));
  };

  const handleBulkVisibility = async (status: boolean) => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi!");
    await supabase.from('tests').update({ is_published: status }).in('id', selectedTests);
    fetchLibraryTests();
    setSelectedTests([]); 
  };

  const handleBulkDelete = async () => {
    if (selectedTests.length === 0) return alert("Vui lòng chọn ít nhất 1 đề thi!");
    if (window.confirm(`Xác nhận xóa vĩnh viễn ${selectedTests.length} đề thi đã chọn?`)) {
      await supabase.from('tests').delete().in('id', selectedTests);
      fetchLibraryTests();
      setSelectedTests([]);
    }
  };

  const handleSelectAll = (e: React.ChangeEvent<HTMLInputElement>, filteredList: any[]) => {
    if (e.target.checked) setSelectedTests(filteredList.map(t => t.id));
    else setSelectedTests([]);
  };

  const handleSelectOne = (id: string) => {
    if (selectedTests.includes(id)) setSelectedTests(selectedTests.filter(t => t !== id));
    else setSelectedTests([...selectedTests, id]);
  };

  const handleViewCourseDetail = (course: any) => {
    setSelectedCourse(course);
    setCurrentFolderId(null);
    fetchFoldersByCourse(course.id);
    fetchAssignedTests(course.id);
    setActiveTab('course-detail');
  };

  const getCourseNameByFolderId = (fId: string | null) => {
     if (!fId) return 'N/A';
     const folder = allFolders.find(f => f.id === fId);
     if (!folder) return 'N/A';
     const course = courses.find(c => c.id === folder.course_id);
     return course ? course.title : 'N/A';
  }

  const breadcrumbs = [];
  let curr = folders.find(f => f.id === currentFolderId);
  while (curr) {
    breadcrumbs.unshift(curr);
    curr = folders.find(f => f.id === curr.parent_id);
  }

  const currentSubFolders = folders.filter(f => 
    currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')
  );

  const currentTests = assignedTests.filter(t => t.folder_id === currentFolderId);

  const filteredLibraryTests = libraryTests
    .filter(test => {
      const matchesSearch = test.title.toLowerCase().includes(searchQuery.toLowerCase());
      if (filterCourse === 'all') return matchesSearch;
      const folder = allFolders.find(f => f.id === test.folder_id);
      return matchesSearch && folder?.course_id === filterCourse;
    })
    .sort((a, b) => {
      if (sortLibrary === 'name-asc') return a.title.localeCompare(b.title);
      if (sortLibrary === 'name-desc') return b.title.localeCompare(a.title);
      if (sortLibrary === 'date-desc') return new Date(b.created_at).getTime() - new Date(a.created_at).getTime();
      return 0;
    });

  return (
    <div className="min-h-screen bg-[#f8fafc] flex font-sans text-slate-800">
      
      {/* SIDEBAR */}
      <aside className="w-64 bg-[#1e293b] text-slate-300 flex flex-col shrink-0 sticky top-0 h-screen z-50 shadow-xl">
        <div className="h-20 flex items-center gap-3 px-6 bg-[#0f172a] border-b border-slate-800 cursor-pointer" onClick={() => onNavigate?.('home')}>
          <div className="font-black text-xl tracking-tight text-white uppercase mt-1">TONY<span className="text-[#2bd6eb]">ADMIN</span></div>
        </div>
        <div className="p-4 space-y-1">
          <p className="text-[10px] font-black uppercase text-slate-500 tracking-widest ml-3 mb-2 mt-4">Hệ thống LMS</p>
          <button onClick={() => {setActiveTab('courses'); setSelectedCourse(null);}} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'courses' || activeTab === 'course-detail' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📁 Khóa học</button>
          <button onClick={() => setActiveTab('library')} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'library' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>📚 Kho Đề thi</button>
          <button onClick={() => setActiveTab('students')} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'students' ? 'bg-[#2bd6eb]/10 text-[#2bd6eb]' : 'hover:bg-slate-800 hover:text-white'}`}>👨‍🎓 Quản lý học viên</button>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="flex-1 flex flex-col min-w-0 relative">
        
        {/* HEADER */}
        <header className="h-20 bg-white border-b border-slate-200 px-8 flex items-center justify-between sticky top-0 z-40 shadow-sm">
          <h1 className="text-xl font-black text-slate-800 uppercase tracking-tight">
            {activeTab === 'courses' ? 'Danh sách Khóa học' : activeTab === 'library' ? 'Kho lưu trữ đề thi' : activeTab === 'students' ? 'Quản lý Học viên' : 'Cấu trúc Khóa học'}
          </h1>
          
          <div className="flex items-center gap-4">
            {activeTab === 'courses' && (
              <button onClick={() => setShowCreateCourseModal(true)} className="bg-[#0a5482] hover:bg-[#084266] transition text-white font-black px-6 py-2.5 rounded-xl shadow-lg text-sm">+ THÊM KHÓA HỌC</button>
            )}

            {activeTab === 'library' && (
              <div className="relative shrink-0" ref={dropdownRef}>
                <button 
                  onClick={() => setShowCreateDropdown(!showCreateDropdown)}
                  className="bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white font-black px-6 py-2.5 rounded-xl shadow-md flex items-center gap-2 transition-transform active:scale-95 text-sm"
                >
                  + TẠO ĐỀ MỚI <span className={`text-[10px] transition-transform ${showCreateDropdown ? 'rotate-180' : ''}`}>▼</span>
                </button>
                {showCreateDropdown && (
                  <div className="absolute right-0 mt-2 w-64 bg-white border border-slate-200 rounded-2xl shadow-2xl z-50 py-2 animate-in fade-in zoom-in-95">
                    <button onClick={() => handleInitiateTest('manual')} className="w-full text-left px-5 py-3 hover:bg-slate-50 font-bold text-[13px] text-slate-700 border-b border-slate-100">✍️ Tạo thủ công (Standard)</button>
                    <button onClick={() => handleInitiateTest('case-study')} className="w-full text-left px-5 py-3 hover:bg-blue-50 font-bold text-[13px] text-[#0a5482] border-b border-slate-100">📄 Tạo đề Case Study (Kèm PDF)</button>
                    <button onClick={() => handleInitiateTest('import')} className="w-full text-left px-5 py-3 hover:bg-slate-50 font-bold text-[13px] text-slate-700">📥 Import Excel/CSV</button>
                  </div>
                )}
              </div>
            )}
          </div>
        </header>

        <div className="flex-1 p-8 overflow-y-auto">
          
          {/* TAB: COURSES */}
          {activeTab === 'courses' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {courses.map(course => {
                const folderIds = allFolders.filter(f => f.course_id === course.id).map(f => f.id);
                const testCount = libraryTests.filter(t => folderIds.includes(t.folder_id)).length;
                return (
                  <div key={course.id} className="bg-white rounded-2xl p-6 border border-slate-200 shadow-sm hover:shadow-xl transition-all group">
                    <span className="px-2.5 py-1 rounded-md text-[10px] font-black uppercase bg-blue-100 text-blue-700">{course.type}</span>
                    <h3 className="font-black text-lg mt-4 mb-2 text-slate-800 line-clamp-2">{course.title}</h3>
                    <p className="text-xs font-bold text-slate-400 mb-6">{testCount} đề thi đã gán</p>
                    <button onClick={() => handleViewCourseDetail(course)} className="w-full bg-[#f8fafc] group-hover:bg-[#2bd6eb] group-hover:text-white text-slate-600 border border-slate-200 font-bold py-3 rounded-xl transition shadow-sm">Quản lý cấu trúc ➜</button>
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB: COURSE DETAIL */}
          {activeTab === 'course-detail' && selectedCourse && (
            <div className="space-y-6">
              <div className="flex justify-between items-center bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
                <div className="flex items-center gap-2 text-sm font-bold text-slate-500">
                  <button onClick={() => setActiveTab('courses')} className="hover:text-[#2bd6eb] transition-colors">Khóa học</button>
                  <span className="text-slate-300">/</span>
                  <button onClick={() => setCurrentFolderId(null)} className={`hover:text-[#2bd6eb] transition-colors ${!currentFolderId ? 'text-[#2bd6eb]' : ''}`}>{selectedCourse.title}</button>
                  {breadcrumbs.map((b, i) => (
                    <React.Fragment key={b.id}>
                      <span className="text-slate-300">/</span>
                      <button onClick={() => setCurrentFolderId(b.id)} className={`hover:text-[#2bd6eb] transition-colors ${i === breadcrumbs.length - 1 ? 'text-[#2bd6eb]' : ''}`}>{b.title}</button>
                    </React.Fragment>
                  ))}
                </div>
                <button onClick={handleDeleteCourse} className="text-red-500 hover:bg-red-50 px-4 py-2 rounded-lg font-bold text-xs border border-red-100 transition">🗑️ Xóa Khóa học</button>
              </div>

              <div className="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm">
                <div className="p-6 bg-slate-50 border-b border-slate-200 flex justify-between items-center">
                  <p className="font-black text-slate-500 text-xs uppercase tracking-widest">{currentFolderId ? `Danh mục con của: ${breadcrumbs[breadcrumbs.length-1]?.title}` : 'Danh mục gốc'}</p>
                  <button onClick={() => setShowFolderModal(true)} className="bg-[#00a651] hover:bg-[#008f45] text-white px-6 py-2.5 rounded-xl font-black text-xs shadow-md transition">+ THÊM THƯ MỤC</button>
                </div>
                <div className="p-8">
                  {currentSubFolders.length > 0 && (
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                      {currentSubFolders.map(sf => (
                        <div key={sf.id} className="relative group">
                          <div onClick={() => setCurrentFolderId(sf.id)} className="bg-white border-2 border-slate-100 hover:border-[#2bd6eb] p-6 rounded-2xl shadow-sm cursor-pointer transition-all flex flex-col items-center text-center h-full">
                            <div className="text-4xl mb-3 group-hover:scale-110 transition-transform">📁</div>
                            <h4 className="font-black text-slate-700 text-sm line-clamp-2">{sf.title}</h4>
                          </div>
                          <button onClick={(e) => { e.stopPropagation(); handleDeleteFolder(sf.id); }} className="absolute -top-2 -right-2 bg-red-500 hover:bg-red-600 text-white w-7 h-7 rounded-full opacity-0 group-hover:opacity-100 transition-opacity shadow-lg flex items-center justify-center text-xs font-bold">✕</button>
                        </div>
                      ))}
                    </div>
                  )}

                  {currentFolderId && currentSubFolders.length === 0 && (
                    <div className="border-t-2 border-dashed border-slate-200 pt-8 mt-2">
                       <div className="flex justify-between items-center mb-6">
                          <h3 className="font-black text-slate-800 text-lg">📝 Đề thi trong mục này</h3>
                          <button onClick={() => setShowAssignModal(true)} className="bg-[#2bd6eb] hover:bg-[#1bc1d6] text-white px-5 py-2 rounded-lg font-bold text-xs shadow-sm transition">+ GÁN ĐỀ</button>
                       </div>
                       {currentTests.length === 0 ? (
                         <div className="text-center py-10 border-2 border-dashed border-slate-200 rounded-2xl text-slate-400 font-medium">Chưa có đề thi nào. Bấm nút + Gán đề để thêm từ Kho tổng.</div>
                       ) : (
                         <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4">
                           {currentTests.map(t => (
                             <div key={t.id} className="bg-slate-50 border border-slate-200 p-4 rounded-xl flex justify-between items-center group hover:bg-white transition-colors">
                               <div className="flex items-center gap-3">
                                 <span className="text-lg">{t.test_type.includes('Case-Study') ? '📄' : t.test_type.includes('Listening') ? '🎧' : '📖'}</span>
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
            </div>
          )}

          {/* TAB: LIBRARY */}
          {activeTab === 'library' && (
            <div className="space-y-6">
              <div className="flex flex-col lg:flex-row justify-between gap-4 bg-white p-4 rounded-xl border border-slate-200 shadow-sm relative z-20">
                <div className="flex bg-slate-100 rounded-lg p-1 border border-slate-200 shadow-sm shrink-0">
                  <button onClick={() => handleBulkVisibility(true)} className="px-4 py-1.5 text-[13px] font-bold text-emerald-600 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">👁️ Hiển thị</button>
                  <button onClick={() => handleBulkVisibility(false)} className="px-4 py-1.5 text-[13px] font-bold text-slate-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">👁️‍🗨️ Ẩn đi</button>
                  <button onClick={handleBulkDelete} className="px-4 py-1.5 text-[13px] font-bold text-red-500 hover:bg-white rounded transition flex items-center gap-1 active:scale-95">🗑️ Xóa</button>
                </div>
                <div className="flex flex-col sm:flex-row gap-4 flex-1 justify-end">
                  <input type="text" placeholder="Tìm kiếm tên đề..." value={searchQuery} onChange={e => setSearchQuery(e.target.value)} className="w-full sm:max-w-xs pl-4 pr-4 py-2.5 border border-slate-200 rounded-xl outline-none focus:border-[#2bd6eb] text-sm" />
                  <select value={filterCourse} onChange={e => setFilterCourse(e.target.value)} className="px-4 py-2.5 border border-slate-200 rounded-xl text-sm font-bold text-slate-600 outline-none w-full sm:w-auto">
                    <option value="all">Tất cả khóa học</option>
                    {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                  </select>
                </div>
              </div>

              <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden z-10 relative">
                <div className="overflow-x-auto">
                  <table className="w-full text-left border-collapse min-w-[900px]">
                    <thead className="bg-[#f8fafc] text-[11px] font-black uppercase text-slate-400 tracking-widest border-b border-slate-200">
                      <tr>
                        <th className="px-4 py-4 w-12 text-center">#</th>
                        <th className="px-2 py-4 w-10">
                          <input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.length > 0 && selectedTests.length === filteredLibraryTests.length} onChange={(e) => handleSelectAll(e, filteredLibraryTests)} />
                        </th>
                        <th className="px-6 py-4">TÊN ĐỀ THI</th>
                        <th className="px-6 py-4">THUỘC KHÓA HỌC</th>
                        <th className="px-6 py-4">KỸ NĂNG</th>
                        <th className="px-6 py-4 text-center">TRẠNG THÁI</th>
                        <th className="px-6 py-4 text-right">THAO TÁC</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                      {filteredLibraryTests.length === 0 ? (
                        <tr><td colSpan={7} className="text-center py-10 text-slate-400 font-medium">Không tìm thấy đề thi nào phù hợp.</td></tr>
                      ) : (
                        filteredLibraryTests.map((test, index) => (
                          <tr key={test.id} className={`hover:bg-slate-50 transition group bg-white ${selectedTests.includes(test.id) ? 'bg-blue-50/30' : ''}`}>
                            <td className="px-4 py-5 text-center text-[13px] font-bold text-slate-400">{index + 1}</td>
                            <td className="px-2 py-5"><input type="checkbox" className="rounded border-slate-300 cursor-pointer" checked={selectedTests.includes(test.id)} onChange={() => handleSelectOne(test.id)} /></td>
                            <td className="px-6 py-5"><div className="font-bold text-slate-800 text-[15px]">{test.title}</div><div className="text-[11px] text-slate-400 mt-1 font-medium uppercase tracking-tight">{test.folder_id ? 'Đã gán cấu trúc' : 'CẢNH BÁO: CHƯA GÁN'}</div></td>
                            <td className="px-6 py-5"><span className="px-2.5 py-1 rounded-md text-[11px] font-bold border bg-slate-100 border-slate-200 text-slate-600">{getCourseNameByFolderId(test.folder_id)}</span></td>
                            <td className="px-6 py-5 font-black text-blue-600 uppercase text-[11px] tracking-tight">{test.test_type}</td>
                            <td className="px-6 py-5 text-center"><button onClick={() => handleToggleTestVisibility(test)} className={`text-[12px] font-bold transition-colors ${test.is_published ? 'text-emerald-500' : 'text-slate-400'}`}>{test.is_published ? 'Hiển thị' : 'Đang ẩn'}</button></td>
                            <td className="px-6 py-5 text-right space-x-3 flex justify-end items-center gap-1">
                              <button onClick={() => setEditingTest(test)} className="text-[#2bd6eb] hover:bg-[#e0faff] px-4 py-2 rounded-lg font-bold text-[13px] flex items-center gap-1.5 transition">✏️ Editor</button>
                              <button onClick={() => handleDeleteTest(test.id)} className="text-slate-300 hover:text-red-500 hover:bg-red-50 p-2.5 rounded-lg transition">🗑️</button>
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

          {/* TAB: STUDENTS (QUẢN LÝ HỌC VIÊN) */}
          {activeTab === 'students' && (
            <StudentManagement />
          )}

        </div>

        {/* --- MODALS --- */}
        {showCreateCourseModal && (
          <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4">
            <form onSubmit={handleCreateCourse} className="bg-white rounded-3xl w-full max-w-md shadow-2xl p-8 space-y-6 animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 uppercase tracking-tight">Thêm Khóa Học Mới</h2>
              <div className="space-y-4">
                <input required value={newCourse.title} onChange={e => setNewCourse({...newCourse, title: e.target.value})} placeholder="Tên khóa học..." className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#2bd6eb]" />
                <select value={newCourse.type} onChange={e => setNewCourse({...newCourse, type: e.target.value})} className="w-full border border-slate-200 rounded-xl px-4 py-3 bg-white outline-none">
                  <option value="IELTS">Hệ IELTS</option><option value="Standard">Hệ Standard (IGCSE/TOEIC)</option>
                </select>
              </div>
              <div className="flex gap-4 pt-2">
                <button type="button" onClick={() => setShowCreateCourseModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084063]">LƯU</button>
              </div>
            </form>
          </div>
        )}

        {showFolderModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <form onSubmit={handleCreateFolder} className="bg-white rounded-3xl w-full max-w-md p-8 space-y-6 animate-in zoom-in-95">
              <h2 className="text-lg font-black uppercase text-emerald-600">{currentFolderId ? 'Thêm Thư Mục Con' : 'Thêm Thư Mục Cấp 1'}</h2>
              <input required autoFocus value={newFolderTitle} onChange={e => setNewFolderTitle(e.target.value)} placeholder="Tên thư mục..." className="w-full border border-slate-200 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-emerald-500" />
              <div className="flex gap-4">
                <button type="button" onClick={() => setShowFolderModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" className="flex-1 bg-[#00a651] hover:bg-[#008f45] text-white font-black py-3 rounded-xl shadow-lg transition">TẠO MỚI</button>
              </div>
            </form>
          </div>
        )}

        {showAssignModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-3xl w-full max-w-xl shadow-2xl overflow-hidden animate-in fade-in">
              <div className="bg-[#0f172a] p-6 text-white flex justify-between items-center">
                <h2 className="font-black uppercase text-sm tracking-widest">Chọn đề từ kho tổng</h2>
                <button onClick={() => setShowAssignModal(false)} className="text-2xl hover:text-[#2bd6eb] transition">&times;</button>
              </div>
              <div className="p-6 max-h-[60vh] overflow-y-auto space-y-3 custom-scrollbar">
                {libraryTests.filter(t => !t.folder_id).map(test => (
                  <div key={test.id} className="flex justify-between items-center p-4 border border-slate-100 rounded-2xl hover:border-[#2bd6eb] transition bg-slate-50 group">
                    <div><p className="font-black text-slate-700 text-sm">{test.title}</p><p className="text-[10px] font-black text-slate-400 uppercase tracking-tighter">{test.test_type}</p></div>
                    <button onClick={() => handleAssignTest(test.id)} className="bg-white group-hover:bg-[#2bd6eb] group-hover:text-white px-5 py-2 rounded-xl font-bold text-xs transition border border-slate-200">GÁN ➜</button>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* LOGIC CHIA NHÁNH RENDER EDITOR MODAL */}
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