import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip, Legend, ResponsiveContainer
} from 'recharts';

const FOLDER_COLORS = ['bg-[#3b82f6]', 'bg-[#10b981]', 'bg-[#f59e0b]', 'bg-[#8b5cf6]', 'bg-[#ec4899]', 'bg-[#14b8a6]', 'bg-[#f43f5e]'];
const ITEMS_PER_PAGE = 12;

const formatDateShort = (isoString: string) => {
  if (!isoString) return '';
  const d = new Date(isoString);
  return `${d.getDate()}/${d.getMonth() + 1}`;
};

const formatDate = (isoString: string) => {
  if (!isoString) return '';
  const d = new Date(isoString);
  return `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth() + 1).toString().padStart(2, '0')}/${d.getFullYear()} ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
};

export default function StudentPortal({ onNavigate, onStartTest }: { onNavigate?: (view: string) => void, onStartTest?: (type: string, data: any) => void }) {
  const [activeTab, setActiveTab] = useState<'library' | 'analytics' | 'profile'>('library');
  const [activeView, setActiveView] = useState<'dashboard' | 'course'>('dashboard');
  
  const [courses, setCourses] = useState<any[]>([]);
  const [selectedCourse, setSelectedCourse] = useState<any>(null);
  const [folders, setFolders] = useState<any[]>([]);
  const [tests, setTests] = useState<any[]>([]);
  
  const [allFolders, setAllFolders] = useState<any[]>([]);
  const [allTestsCount, setAllTestsCount] = useState<any[]>([]);

  const [historyData, setHistoryData] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [userProfile, setUserProfile] = useState<any>(null);

  const [currentFolderId, setCurrentFolderId] = useState<string | null>(null);
  const [searchTest, setSearchTest] = useState('');
  const [sortTest, setSortTest] = useState('name-asc');
  const [folderPage, setFolderPage] = useState(1);
  const [testPage, setTestPage] = useState(1);

  const [analyticsCourse, setAnalyticsCourse] = useState('all');
  const [historySort, setHistorySort] = useState('date-desc');

  const [showModeSelection, setShowModeSelection] = useState(false);
  const [testToStart, setTestToStart] = useState<any>(null);

  const [newPassword, setNewPassword] = useState('');
  const [newFullName, setNewFullName] = useState('');
  const [isUpdatingProfile, setIsUpdatingProfile] = useState(false);

  useEffect(() => {
    checkUserAndFetchData();
  }, [activeTab]);

  const checkUserAndFetchData = async () => {
    const { data: { user } } = await supabase.auth.getUser();
    setCurrentUser(user);
    
    if (user) {
      const { data: profile } = await supabase.from('profiles').select('*').eq('id', user.id).single();
      setUserProfile(profile);
      if (profile && !newFullName) setNewFullName(profile.full_name || '');
    }

    if (activeTab === 'library') {
      fetchCourses(user?.id);
      fetchAllFolders(); 
      fetchAllTestsCount();
    }
    if (activeTab === 'analytics') {
      if (courses.length === 0) fetchCourses(user?.id);
      fetchUserHistory(user?.id);
    }
  };

  // --- LOGIC LỌC KHÓA HỌC DỰA TRÊN BẢNG ENROLLMENTS ---
  const fetchCourses = async (userId?: string) => {
    if (!userId) return;
    
    // Bước 1: Lấy danh sách ID các khóa học đã được gán
    const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', userId);
    const courseIds = enrolls?.map(e => e.course_id) || [];

    // Bước 2: Tải thông tin các khóa học đó
    if (courseIds.length > 0) {
      const { data } = await supabase.from('courses').select('*').in('id', courseIds).order('created_at', { ascending: false });
      setCourses(data || []);
    } else {
      setCourses([]); // Nếu chưa được gán khóa nào thì rỗng
    }
  };

  const fetchUserHistory = async (userId?: string) => {
    if (!userId) return;
    try {
      const { data, error } = await supabase.from('test_results').select('*').eq('user_id', userId).order('created_at', { ascending: false });
      
      if (data && data.length > 0) {
        const formattedHistory = data.map((item: any) => ({
          id: item.id,
          name: item.test_title || 'Bài thi không tên',
          courseId: item.course_id,
          subject: item.test_type || 'Standard',
          scoreObj: { value: item.score || 0, display: `${item.score || 0} / ${item.total_score || 0}` },
          timeSpent: Math.round((item.time_spent || 0) / 60), 
          date: item.created_at
        }));
        setHistoryData(formattedHistory);
      } else {
        setHistoryData([]); 
      }
    } catch (e) {
      console.error(e);
      setHistoryData([]);
    }
  };

  const fetchAllFolders = async () => {
    const { data } = await supabase.from('folders').select('id, course_id');
    setAllFolders(data || []);
  };

  const fetchAllTestsCount = async () => {
    const { data } = await supabase.from('tests').select('id, content_json, folder_id, is_published').eq('is_published', true);
    setAllTestsCount(data || []);
  };

  const fetchCourseContent = async (courseId: string) => {
    const { data: folderData } = await supabase.from('folders').select('*').eq('course_id', courseId).order('display_order', { ascending: true });
    setFolders(folderData || []);

    const { data: testData } = await supabase.from('tests').select('*').eq('is_published', true);
    const courseTests = (testData || []).filter(t => {
      const inFolder = folderData?.some((f: any) => f.id === t.folder_id);
      const inJson = t.content_json?.basicInfo?.courseId === courseId;
      return inFolder || inJson;
    });
    setTests(courseTests);
  };

  const handleUpdateProfile = async () => {
    setIsUpdatingProfile(true);
    try {
      if (newFullName && currentUser?.id) {
        await supabase.from('profiles').update({ full_name: newFullName }).eq('id', currentUser.id);
      }
      
      if (newPassword && newPassword.length >= 6) {
        const { error } = await supabase.auth.updateUser({ password: newPassword });
        if (error) throw error;
        setNewPassword('');
      } else if (newPassword && newPassword.length < 6) {
        alert("Mật khẩu mới phải có ít nhất 6 ký tự!");
        setIsUpdatingProfile(false);
        return;
      }
      
      alert("🎉 Cập nhật tài khoản thành công!");
      checkUserAndFetchData(); // Tải lại tên hiển thị
    } catch (error: any) {
      alert("Lỗi cập nhật: " + error.message);
    } finally {
      setIsUpdatingProfile(false);
    }
  };

  const handleLogout = async () => {
    try {
      await supabase.auth.signOut(); 
    } catch (error) {
      console.error("Lỗi đăng xuất Supabase:", error);
    } finally {
      localStorage.clear();
      sessionStorage.clear();
      onNavigate?.('home'); 
      setTimeout(() => window.location.reload(), 100);
    }
  };

  const handleOpenCourse = (course: any) => {
    setSelectedCourse(course);
    setCurrentFolderId(null); 
    setSearchTest('');
    setFolderPage(1);
    setTestPage(1);
    fetchCourseContent(course.id);
    setActiveView('course');
  };

  const handleFolderClick = (id: string) => {
    setCurrentFolderId(id);
    setFolderPage(1);
    setTestPage(1);
  };

  const handleStartTestClick = (test: any) => {
    if (!onStartTest) return;
    const type = test.test_type || '';
    
    if (type === 'IELTS-Writing') onStartTest('ielts-writing', test);
    else if (type === 'IELTS-Speaking') onStartTest('ielts-speaking', test);
    else if (type === 'IELTS-Listening' || type === 'IELTS-Reading') {
      setTestToStart(test);
      setShowModeSelection(true);
    } else if (test.title.toLowerCase().includes('business') || test.title.toLowerCase().includes('econ')) {
      onStartTest('case-study', test);
    } else {
      onStartTest('standard', test);
    }
  };

  const handleConfirmMode = (mode: 'computer' | 'paper') => {
    setShowModeSelection(false);
    if (onStartTest && testToStart) onStartTest(mode, testToStart);
  };

  const getCourseStyle = (title: string, type: string) => {
    const lowerTitle = title.toLowerCase();
    if (lowerTitle.includes('ielts') || type === 'IELTS') return { bg: 'bg-[#3b82f6]', label: 'IELTS Master' };
    if (lowerTitle.includes('igcse') || lowerTitle.includes('science')) return { bg: 'bg-[#10b981]', label: 'IGCSE Science' };
    if (lowerTitle.includes('toeic')) return { bg: 'bg-[#e81e62]', label: 'TOEIC' };
    return { bg: 'bg-[#6b7280]', label: title };
  };

  const getTestIcon = (testType: string) => {
    if (testType.includes('Listening')) return '🎧';
    if (testType.includes('Speaking')) return '🎙️';
    if (testType.includes('Writing')) return '✍️';
    return '📖';
  };

  const processedHistory = [...historyData]
    .filter(h => analyticsCourse === 'all' || h.courseId === analyticsCourse)
    .sort((a, b) => {
      if (historySort === 'date-desc') return new Date(b.date).getTime() - new Date(a.date).getTime();
      if (historySort === 'date-asc') return new Date(a.date).getTime() - new Date(b.date).getTime();
      if (historySort === 'score-desc') return b.scoreObj.value - a.scoreObj.value;
      if (historySort === 'score-asc') return a.scoreObj.value - b.scoreObj.value;
      return 0;
    });

  const totalTestsDone = processedHistory.length;
  const avgScore = totalTestsDone > 0 ? (processedHistory.reduce((acc, curr) => acc + curr.scoreObj.value, 0) / totalTestsDone).toFixed(1) : '0';
  const totalTimeMinutes = processedHistory.reduce((acc, curr) => acc + curr.timeSpent, 0);
  const totalTimeHours = (totalTimeMinutes / 60).toFixed(1);

  const sparklineScoreArr = processedHistory.slice(0, 5).reverse().map(h => ({ v: h.scoreObj.value }));
  const sparklineCompletedArr = processedHistory.slice(0, 5).reverse().map((h, i) => ({ v: i + 1 })); 
  const sparklineAttemptsArr = processedHistory.slice(0, 5).reverse().map((h, i) => ({ v: (i + 1) * 2 })); 
  const sparklineTimeArr = processedHistory.slice(0, 5).reverse().map(h => ({ v: h.timeSpent }));

  const ieltsHistory = processedHistory.filter(h => h.subject.includes('IELTS')).slice(0, 10).reverse();
  const dynamicProgressData = ieltsHistory.map((h, i) => ({
    date: formatDateShort(h.date) || `Lần ${i+1}`,
    listening: h.subject.includes('Listening') ? h.scoreObj.value : undefined,
    reading: h.subject.includes('Reading') ? h.scoreObj.value : undefined,
  }));

  const breadcrumbs = [];
  let curr = folders.find(f => f.id === currentFolderId);
  while (curr) {
    breadcrumbs.unshift(curr);
    curr = folders.find(f => f.id === curr.parent_id);
  }

  const currentSubFolders = folders.filter(f => 
    currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')
  );

  let currentTests = tests.filter(t => t.folder_id === currentFolderId);
  if (!currentFolderId || currentSubFolders.length > 0) currentTests = []; 

  const processedTests = currentTests
    .filter(t => t.title.toLowerCase().includes(searchTest.toLowerCase()))
    .sort((a, b) => {
       if (sortTest === 'name-asc') return a.title.localeCompare(b.title);
       if (sortTest === 'name-desc') return b.title.localeCompare(a.title);
       if (sortTest === 'date-desc') return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime();
       if (sortTest === 'date-asc') return new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime();
       return 0;
    });

  const totalFolderPages = Math.ceil(currentSubFolders.length / ITEMS_PER_PAGE);
  const paginatedFolders = currentSubFolders.slice((folderPage - 1) * ITEMS_PER_PAGE, folderPage * ITEMS_PER_PAGE);
  const totalTestPages = Math.ceil(processedTests.length / ITEMS_PER_PAGE);
  const paginatedTests = processedTests.slice((testPage - 1) * ITEMS_PER_PAGE, testPage * ITEMS_PER_PAGE);

  const renderPagination = (currentPage: number, totalPages: number, setPage: (p: number) => void) => {
    if (totalPages <= 1) return null;
    return (
      <div className="flex justify-center items-center gap-4 mt-10">
        <button disabled={currentPage === 1} onClick={() => setPage(currentPage - 1)} className="w-12 h-12 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:bg-[#1e88e5] hover:text-white transition-all disabled:opacity-30 disabled:hover:bg-white disabled:hover:text-slate-500 shadow-sm font-black text-xl">←</button>
        <span className="text-[15px] font-bold text-slate-500 bg-white px-5 py-2.5 rounded-xl border border-slate-200 shadow-sm">Trang {currentPage} / {totalPages}</span>
        <button disabled={currentPage === totalPages} onClick={() => setPage(currentPage + 1)} className="w-12 h-12 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:bg-[#1e88e5] hover:text-white transition-all disabled:opacity-30 disabled:hover:bg-white disabled:hover:text-slate-500 shadow-sm font-black text-xl">→</button>
      </div>
    );
  };

  const currentAnalyticsCourseObj = courses.find(c => String(c.id) === String(analyticsCourse));
  const showIeltsCharts = currentAnalyticsCourseObj?.type === 'IELTS' && dynamicProgressData.length > 0; 

  const displayUserName = userProfile?.full_name || (currentUser?.email ? currentUser.email.split('@')[0] : 'Tài khoản Học viên');
  const displayUserInitial = displayUserName.charAt(0).toUpperCase();

  return (
    <div className="min-h-screen bg-[#f4f6f9] font-sans text-slate-800">
      
      {/* HEADER */}
      <header className="bg-[#f8f9fb] border-b border-slate-200 px-6 py-3 flex items-center justify-between sticky top-0 z-30 shadow-sm">
        <div className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity" onClick={() => window.location.href = 'https://tonyenglish.vn/vi'}>
          <div className="flex flex-col items-end">
            <h1 className="font-black text-2xl tracking-tighter text-[#1e88e5] leading-none">TONY<span className="text-slate-800">ENGLISH</span></h1>
            <span className="text-[10px] italic text-slate-500 font-medium mt-0.5 pr-0.5">The future begins here</span>
          </div>
          <div className="w-10 h-10 flex items-center justify-center overflow-hidden"><img src="/logo-shield.png" alt="TonyEnglish Logo" className="w-auto h-full object-contain" /></div>
        </div>

        <div className="hidden md:flex items-center gap-2 lg:gap-6 bg-slate-100/50 rounded-xl p-1 border border-slate-200">
          <button onClick={() => { setActiveTab('library'); setActiveView('dashboard'); setSelectedCourse(null); }} className={`flex items-center gap-2 px-5 py-2.5 rounded-lg font-bold text-sm transition-all ${activeTab === 'library' ? 'bg-white shadow-md text-[#1e88e5]' : 'text-slate-500 hover:text-slate-800'}`}><span className="text-lg">📚</span> Thư viện đề</button>
          <button onClick={() => setActiveTab('analytics')} className={`flex items-center gap-2 px-5 py-2.5 rounded-lg font-bold text-sm transition-all ${activeTab === 'analytics' ? 'bg-white shadow-md text-[#1e88e5]' : 'text-slate-500 hover:text-slate-800'}`}><span className="text-lg">📊</span> Phân tích & Lịch sử</button>
          <button onClick={() => setActiveTab('profile')} className={`flex items-center gap-2 px-5 py-2.5 rounded-lg font-bold text-sm transition-all ${activeTab === 'profile' ? 'bg-white shadow-md text-[#1e88e5]' : 'text-slate-500 hover:text-slate-800'}`}><span className="text-lg">👤</span> Tài khoản</button>
        </div>

        <div className="flex items-center gap-4">
          <div className="flex items-center gap-4 cursor-pointer hover:opacity-80 transition group" onClick={() => setActiveTab('profile')}>
            <div className="text-right hidden sm:block">
              <div className="font-black text-sm text-slate-800 group-hover:text-[#1e88e5] transition-colors">{displayUserName}</div>
              <div className="text-[11px] font-medium text-slate-500 uppercase tracking-wider">Học viên</div>
            </div>
            <div className="w-10 h-10 rounded-full bg-[#0a5482] group-hover:bg-[#1e88e5] transition-colors text-white flex items-center justify-center font-black shadow-inner border-2 border-white">{displayUserInitial}</div>
          </div>
          <div className="h-8 w-px bg-slate-300 mx-1"></div>
          <button onClick={handleLogout} className="text-[#e53935] font-black text-[13px] bg-red-50 hover:bg-red-100 border border-red-100 px-4 py-2 rounded-lg transition active:scale-95">Đăng Xuất</button>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="max-w-7xl w-full mx-auto p-6 md:p-10">
        
        {/* ================= TAB 1: THƯ VIỆN ĐỀ ================= */}
        {activeTab === 'library' && (
          <>
            {activeView === 'dashboard' && (
              <div className="animate-in fade-in duration-300">
                <div className="bg-[#f0f2f5] rounded-xl px-6 py-4 mb-8 border border-slate-200">
                  <h2 className="font-bold text-slate-700 text-[15px]">Khóa học của tôi</h2>
                </div>

                {courses.length === 0 ? (
                  <div className="bg-white border-2 border-dashed border-slate-200 rounded-2xl py-20 text-center shadow-sm">
                    <span className="text-5xl block mb-4 opacity-50">🔒</span>
                    <h3 className="font-bold text-slate-700 text-lg mb-2">Chưa có khóa học nào</h3>
                    <p className="text-slate-500 text-sm">Anh/chị vui lòng liên hệ TonyEnglish để được cấp quyền truy cập vào các Khóa học nhé!</p>
                  </div>
                ) : (
                  <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">
                    {courses.map(course => {
                      const style = getCourseStyle(course.title, course.type);
                      const courseFolderIds = allFolders.filter(f => f.course_id === course.id).map(f => f.id);
                      const testCount = allTestsCount.filter(t => courseFolderIds.includes(t.folder_id)).length;

                      return (
                        <div key={course.id} onClick={() => handleOpenCourse(course)} className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer flex flex-col h-64 relative group">
                          <div className={`${style.bg} h-36 flex items-center justify-center relative p-6`}>
                            <h3 className="text-white text-3xl font-black text-center leading-tight tracking-wide drop-shadow-sm group-hover:scale-105 transition-transform">{style.label}</h3>
                            <div className="absolute -bottom-4 right-0 bg-[#f4f6f9] text-slate-600 font-bold text-[12px] px-4 py-1.5 rounded-l-lg border-y border-l border-slate-200 shadow-sm z-10">
                              {testCount > 0 ? `${testCount} đề thi` : 'Chưa có đề thi'}
                            </div>
                          </div>
                          <div className="flex-1 bg-white p-5 flex flex-col justify-center relative mt-2">
                            <h4 className="font-black text-lg text-slate-800 mb-1 truncate">{course.title}</h4>
                            <div className="flex justify-between items-center text-slate-400">
                              <p className="text-[12px] font-medium group-hover:text-[#1e88e5] transition-colors">Bấm để xem chi tiết</p>
                              <span className="text-[#1e88e5] font-black group-hover:translate-x-1 transition-transform">→</span>
                            </div>
                          </div>
                        </div>
                      )
                    })}
                  </div>
                )}
              </div>
            )}

            {activeView === 'course' && selectedCourse && (
              <div className="animate-in fade-in slide-in-from-right-4 duration-300">
                <div className="flex flex-wrap items-center gap-2 text-[14px] font-bold text-slate-500 mb-6 bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
                   <button onClick={() => { setActiveView('dashboard'); setSelectedCourse(null); }} className="hover:text-[#1e88e5] transition-colors">Khóa học</button>
                   <span className="text-slate-300">/</span>
                   <button onClick={() => { setCurrentFolderId(null); setFolderPage(1); setTestPage(1); }} className={`hover:text-[#1e88e5] transition-colors ${!currentFolderId ? 'text-[#1e88e5]' : ''}`}>{selectedCourse.title}</button>
                   {breadcrumbs.map((b, i) => (
                     <React.Fragment key={b.id}>
                       <span className="text-slate-300">/</span>
                       <button onClick={() => handleFolderClick(b.id)} className={`hover:text-[#1e88e5] transition-colors ${i === breadcrumbs.length - 1 ? 'text-[#1e88e5]' : ''}`}>{b.title}</button>
                     </React.Fragment>
                   ))}
                </div>

                <div className="space-y-8">
                  {currentSubFolders.length > 0 && (
                    <div>
                      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                        {paginatedFolders.map((subFolder, idx) => {
                          const childCount = folders.filter(f => f.parent_id === subFolder.id).length;
                          const testCount = tests.filter(t => t.folder_id === subFolder.id).length;
                          const colorClass = FOLDER_COLORS[idx % FOLDER_COLORS.length];

                          return (
                            <div key={subFolder.id} onClick={() => handleFolderClick(subFolder.id)} className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer flex flex-col h-[200px] relative group">
                              <div className={`${colorClass} h-[110px] flex items-center justify-center relative p-5`}>
                                <h3 className="text-white text-xl font-black text-center leading-tight tracking-wide drop-shadow-sm group-hover:scale-105 transition-transform line-clamp-2">{subFolder.title}</h3>
                              </div>
                              <div className="flex-1 bg-white p-5 flex flex-col justify-center relative">
                                <h4 className="font-black text-[15px] text-slate-800 mb-1 truncate">{subFolder.title}</h4>
                                <div className="flex justify-between items-center text-slate-400 mt-1">
                                  <p className="text-[12px] font-bold">{childCount > 0 ? `${childCount} mục con` : `${testCount} đề thi`}</p>
                                  <span className="text-[#1e88e5] font-black group-hover:translate-x-1 transition-transform">→</span>
                                </div>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                      {renderPagination(folderPage, totalFolderPages, setFolderPage)}
                    </div>
                  )}

                  {currentTests.length > 0 && (
                    <div className="bg-white rounded-[1.5rem] border border-slate-200 overflow-hidden shadow-sm mt-8 animate-in fade-in zoom-in-95">
                      <div className="bg-slate-50 px-6 py-4 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-4">
                        <div className="relative w-full sm:w-80">
                          <input type="text" placeholder="Tìm kiếm bài thi..." value={searchTest} onChange={(e) => {setSearchTest(e.target.value); setTestPage(1);}} className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 font-medium text-[13px] outline-none focus:ring-2 focus:ring-[#1e88e5] bg-white" />
                          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">🔍</span>
                        </div>
                        <div className="w-full sm:w-48">
                          <select value={sortTest} onChange={(e) => setSortTest(e.target.value)} className="w-full px-4 py-2.5 border border-slate-300 rounded-xl outline-none focus:ring-2 focus:ring-[#1e88e5] text-[13px] font-bold text-slate-600 bg-white cursor-pointer">
                            <option value="name-asc">A-Z (Tên bài)</option><option value="name-desc">Z-A (Tên bài)</option>
                            <option value="date-desc">Mới nhất trước</option><option value="date-asc">Cũ nhất trước</option>
                          </select>
                        </div>
                      </div>

                      <div className="p-6 md:p-8 bg-white">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                          {paginatedTests.map(test => (
                            <div key={test.id} onClick={() => handleStartTestClick(test)} className="bg-white border-2 border-slate-100 hover:border-[#1e88e5] p-5 rounded-2xl shadow-sm hover:shadow-lg transition-all cursor-pointer flex flex-col justify-between group h-full">
                              <div>
                                <div className="flex justify-between items-start mb-4">
                                  <div className="w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center text-2xl group-hover:scale-110 transition-transform shadow-inner">{getTestIcon(test.test_type)}</div>
                                  <span className="text-[10px] font-black text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-md uppercase tracking-widest border border-emerald-100">Sẵn sàng</span>
                                </div>
                                <h3 className="font-bold text-slate-800 text-[15px] group-hover:text-[#1e88e5] transition-colors mb-3 line-clamp-2 leading-relaxed">{test.title}</h3>
                                <div className="flex gap-2">
                                  <span className="text-[10px] font-black text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md uppercase tracking-wider">{test.test_type}</span>
                                </div>
                              </div>
                              <button className="mt-6 w-full text-center text-[#1e88e5] font-bold text-[13px] bg-blue-50 py-3 rounded-xl group-hover:bg-[#1e88e5] group-hover:text-white transition-colors uppercase tracking-widest">BẮT ĐẦU LÀM BÀI</button>
                            </div>
                          ))}
                        </div>
                        {processedTests.length === 0 ? (
                          <div className="text-center py-12 text-slate-400 font-medium">Không có bài thi nào khớp với tìm kiếm của bạn.</div>
                        ) : (
                          renderPagination(testPage, totalTestPages, setTestPage)
                        )}
                      </div>
                    </div>
                  )}

                  {currentSubFolders.length === 0 && currentTests.length === 0 && (
                    <div className="text-center py-20 bg-white rounded-2xl border-2 border-dashed border-slate-200 text-slate-400 font-medium text-lg">📭 Thư mục này hiện đang trống.</div>
                  )}
                </div>
              </div>
            )}
          </>
        )}

        {/* ================= TAB 2: PHÂN TÍCH & LỊCH SỬ ================= */}
        {activeTab === 'analytics' && (
          <div className="space-y-6 animate-in fade-in duration-300">
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
              <div>
                <h2 className="text-xl font-black text-slate-800">Hiệu Suất Học Tập</h2>
                <p className="text-sm text-slate-500 font-medium">Lựa chọn khóa học để xem biểu đồ và lịch sử chi tiết</p>
              </div>
              <select value={analyticsCourse} onChange={(e) => setAnalyticsCourse(e.target.value)} className="w-full md:w-64 border-2 border-slate-200 rounded-xl px-4 py-2.5 font-bold text-[15px] text-[#0a5482] outline-none focus:border-[#2ab4e8] bg-slate-50 cursor-pointer">
                <option value="all">Tất cả khóa học</option>
                {courses.length > 0 && courses.map(course => ( <option key={course.id} value={course.id}>{course.title}</option> ))}
              </select>
            </div>

            {totalTestsDone === 0 ? (
              <div className="bg-white rounded-2xl border-2 border-dashed border-slate-200 py-20 text-center shadow-sm">
                <span className="text-6xl mb-4 block opacity-50">📊</span>
                <h3 className="text-xl font-bold text-slate-600 mb-2">Chưa có dữ liệu làm bài</h3>
                <p className="text-slate-400 font-medium">Anh hãy vào Thư viện đề, làm thử một bài test và nộp bài để hệ thống phân tích nhé!</p>
              </div>
            ) : (
              <>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col">
                    <div className="p-5 pb-0 flex justify-between items-start">
                      <div className="flex items-center gap-2"><span className="w-6 h-6 rounded bg-blue-100 flex items-center justify-center text-[12px]">📊</span><span className="font-bold text-slate-600 text-[14px]">Điểm trung bình</span></div>
                      <span className="font-black text-blue-500 text-xl">{avgScore}</span>
                    </div>
                    <div className="h-20 w-full mt-2 px-2 bg-blue-50/50">
                      <ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineScoreArr}><Line type="monotone" dataKey="v" stroke="#3b82f6" strokeWidth={3} dot={{r: 4, fill: '#3b82f6', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer>
                    </div>
                  </div>

                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col">
                    <div className="p-5 pb-0 flex justify-between items-start">
                      <div className="flex items-center gap-2"><span className="w-6 h-6 rounded bg-emerald-100 flex items-center justify-center text-[12px]">📝</span><span className="font-bold text-slate-600 text-[14px]">Bài hoàn thành</span></div>
                      <span className="font-black text-emerald-500 text-xl">{totalTestsDone}</span>
                    </div>
                    <div className="h-20 w-full mt-2 px-2 bg-emerald-50/50">
                      <ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineCompletedArr}><Line type="monotone" dataKey="v" stroke="#10b981" strokeWidth={3} dot={{r: 4, fill: '#10b981', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer>
                    </div>
                  </div>

                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col">
                    <div className="p-5 pb-0 flex justify-between items-start">
                      <div className="flex items-center gap-2"><span className="w-6 h-6 rounded bg-fuchsia-100 flex items-center justify-center text-[12px]">🔄</span><span className="font-bold text-slate-600 text-[14px]">Lượt làm bài</span></div>
                      <span className="font-black text-fuchsia-500 text-xl">{totalTestsDone}</span>
                    </div>
                    <div className="h-20 w-full mt-2 px-2 bg-fuchsia-50/30">
                      <ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineAttemptsArr}><Line type="monotone" dataKey="v" stroke="#d946ef" strokeWidth={3} dot={{r: 4, fill: '#d946ef', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer>
                    </div>
                  </div>

                  <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col">
                    <div className="p-5 pb-0 flex justify-between items-start">
                      <div className="flex items-center gap-2"><span className="w-6 h-6 rounded bg-orange-100 flex items-center justify-center text-[12px]">⏱️</span><span className="font-bold text-slate-600 text-[14px]">Thời gian học</span></div>
                      <span className="font-black text-orange-500 text-xl">{totalTimeHours}h</span>
                    </div>
                    <div className="h-20 w-full mt-2 px-2 bg-orange-50/50">
                      <ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineTimeArr}><Line type="monotone" dataKey="v" stroke="#f97316" strokeWidth={3} dot={{r: 4, fill: '#f97316', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer>
                    </div>
                  </div>
                </div>

                {showIeltsCharts && (
                  <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm mt-6 animate-in slide-in-from-bottom-4">
                    <h3 className="font-black text-lg text-slate-800 mb-6">📈 Tiến Độ Band Score (IELTS)</h3>
                    <div className="h-[300px] w-full">
                      <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={dynamicProgressData} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                          <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                          <XAxis dataKey="date" axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 13, fontWeight: 600}} dy={10} />
                          <YAxis domain={[0, 9]} ticks={[0, 3, 5, 6, 7, 8, 9]} axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 13, fontWeight: 600}} dx={-10} />
                          <RechartsTooltip contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 15px rgba(0,0,0,0.1)', fontWeight: 'bold' }} />
                          <Legend iconType="circle" wrapperStyle={{ paddingTop: '20px', fontWeight: 'bold', fontSize: '14px' }} />
                          <Line type="monotone" dataKey="listening" name="Listening" stroke="#10b981" strokeWidth={3} activeDot={{ r: 6 }} connectNulls />
                          <Line type="monotone" dataKey="reading" name="Reading" stroke="#a855f7" strokeWidth={3} activeDot={{ r: 6 }} connectNulls />
                        </LineChart>
                      </ResponsiveContainer>
                    </div>
                  </div>
                )}

                <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden mt-6">
                  <div className="p-6 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-slate-50/50">
                    <h3 className="font-black text-lg text-slate-800">🕰️ Lịch Sử Đề Thi Đã Làm</h3>
                    <select value={historySort} onChange={(e) => setHistorySort(e.target.value)} className="border border-slate-300 rounded-lg px-4 py-2 font-medium text-[14px] outline-none focus:ring-2 focus:ring-[#1e88e5] cursor-pointer bg-white">
                      <option value="date-desc">Ngày gần nhất</option><option value="date-asc">Ngày cũ nhất</option>
                      <option value="score-desc">Điểm cao nhất</option><option value="score-asc">Điểm thấp nhất</option>
                    </select>
                  </div>
                  <div className="overflow-x-auto">
                    <table className="w-full text-left border-collapse">
                      <thead>
                        <tr className="bg-white border-b border-slate-200 text-[12px] uppercase tracking-wider text-slate-500">
                          <th className="px-6 py-4 font-bold">Đề thi</th><th className="px-6 py-4 font-bold text-center">Môn học</th>
                          <th className="px-6 py-4 font-bold text-center">Điểm số</th><th className="px-6 py-4 font-bold text-center">Thời gian làm</th>
                          <th className="px-6 py-4 font-bold text-center">Ngày nộp</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100">
                        {processedHistory.map(history => (
                          <tr key={history.id} className="hover:bg-slate-50 transition-colors">
                            <td className="px-6 py-4 font-bold text-[14px] text-slate-800">{history.name}</td>
                            <td className="px-6 py-4 text-center"><span className="bg-slate-100 text-slate-600 px-2.5 py-1 rounded text-[12px] font-bold border border-slate-200">{history.subject}</span></td>
                            <td className="px-6 py-4 text-center font-bold text-[15px] text-emerald-600">{history.scoreObj.display}</td>
                            <td className="px-6 py-4 text-center font-medium text-[14px] text-slate-600">{history.timeSpent} phút</td>
                            <td className="px-6 py-4 text-center text-slate-500 font-medium text-[13px]">{formatDate(history.date)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </>
            )}
          </div>
        )}

        {/* ================= TAB 3: TÀI KHOẢN ================= */}
        {activeTab === 'profile' && (
          <div className="max-w-2xl mx-auto mt-8 animate-in fade-in duration-300">
            <div className="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm text-center">
              <div className="w-24 h-24 rounded-full bg-[#0a5482] text-white flex items-center justify-center font-black text-4xl mx-auto mb-4 shadow-md border-4 border-white ring-4 ring-blue-50">
                {displayUserInitial}
              </div>
              <h2 className="text-2xl font-black text-slate-800">{displayUserName}</h2>
              <p className="text-slate-500 font-medium mb-8">Học viên TonyEnglish</p>
              <div className="space-y-5 border-t border-slate-100 pt-8 text-left">
                <h3 className="font-black text-lg text-slate-800 mb-2">🔐 Cấu hình thông tin</h3>
                <div className="space-y-1">
                  <label className="text-[13px] font-bold text-slate-500 uppercase">Họ và tên</label>
                  <input 
                    type="text" 
                    value={newFullName} 
                    onChange={e => setNewFullName(e.target.value)} 
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:ring-2 focus:ring-[#1e88e5] outline-none" 
                    placeholder="Nhập họ và tên..."
                  />
                </div>
                <div className="space-y-1">
                  <label className="text-[13px] font-bold text-slate-500 uppercase">Email đăng nhập</label>
                  <input type="email" defaultValue={currentUser?.email || ""} disabled className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 font-medium text-slate-700 outline-none" />
                </div>
                <div className="space-y-1">
                  <label className="text-[13px] font-bold text-slate-500 uppercase">Mật khẩu mới (Nếu muốn đổi)</label>
                  <input type="password" placeholder="••••••••" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} className="w-full border border-slate-300 rounded-xl px-4 py-3 font-medium focus:ring-2 focus:ring-[#1e88e5] outline-none" />
                </div>
                <button onClick={handleUpdateProfile} disabled={isUpdatingProfile} className="bg-[#1e88e5] hover:bg-[#1565c0] disabled:bg-slate-300 text-white font-bold px-6 py-3 rounded-xl transition shadow-md w-full mt-4">
                  {isUpdatingProfile ? 'Đang cập nhật...' : 'Cập nhật tài khoản'}
                </button>
              </div>
            </div>
          </div>
        )}

      </main>

      {/* POPUP CHỌN HÌNH THỨC THI IELTS */}
      {showModeSelection && testToStart && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl w-full max-w-lg shadow-2xl p-8 animate-in zoom-in-95">
            <h2 className="text-2xl font-black text-slate-800 mb-2">{testToStart.title}</h2>
            <p className="text-slate-500 font-medium mb-8">Vui lòng chọn hình thức thi bạn muốn tham gia:</p>
            
            <div className="space-y-4">
              <button onClick={() => handleConfirmMode('computer')} className="w-full flex items-center gap-4 p-5 rounded-2xl border-2 border-slate-200 hover:border-[#3b82f6] hover:bg-blue-50 transition-all text-left group">
                <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">💻</div>
                <div><h3 className="font-bold text-[16px] text-slate-800">Thi trên máy tính (Computer-delivered)</h3><p className="text-[13px] text-slate-500 mt-1">Giao diện chuẩn thi máy, làm bài trực tiếp trên màn hình.</p></div>
              </button>
              <button onClick={() => handleConfirmMode('paper')} className="w-full flex items-center gap-4 p-5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 transition-all text-left group">
                <div className="w-12 h-12 rounded-full bg-emerald-100 flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">📝</div>
                <div><h3 className="font-bold text-[16px] text-slate-800">Thi trên giấy (Paper-based)</h3><p className="text-[13px] text-slate-500 mt-1">Giao diện mô phỏng phiếu trả lời, kết hợp đề thi giấy PDF.</p></div>
              </button>
            </div>
            <button onClick={() => setShowModeSelection(false)} className="mt-8 w-full py-3 font-bold text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy bỏ</button>
          </div>
        </div>
      )}
    </div>
  );
}