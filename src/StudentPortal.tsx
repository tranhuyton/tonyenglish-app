import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import { LineChart, Line, BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip, Legend, ResponsiveContainer } from 'recharts';

const FOLDER_IMAGES = [
  'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1513001900722-370f803f498d?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=800',
  'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&q=80&w=800'
];

const ITEMS_PER_PAGE = 12;
const HISTORY_PER_PAGE = 10;

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

const checkInProgress = (testId: string) => {
  try {
      const compEndTime = localStorage.getItem(`ielts_endtime_${testId}`) || localStorage.getItem(`standard_endtime_${testId}`) || localStorage.getItem(`ielts_paper_endtime_${testId}`) || localStorage.getItem(`case_study_endtime_${testId}`);
      if (compEndTime && parseInt(compEndTime) > Date.now()) return true;
      const keys = [`ielts_ans_${testId}`, `ielts_paper_ans_${testId}`, `std_ans_${testId}`, `case_study_ans_${testId}`];
      for (const key of keys) {
          const data = localStorage.getItem(key);
          if (data && Object.keys(JSON.parse(data)).length > 0) return true;
      }
  } catch (e) {} return false;
};

export default function StudentPortal({ onNavigate, onStartTest, onOpenLecture }: { onNavigate?: (view: string) => void, onStartTest?: (type: string, data: any) => void, onOpenLecture?: (courseId: string) => void }) {
  const [activeTab, setActiveTab] = useState<'library' | 'analytics' | 'profile'>('library');
  const [activeView, setActiveView] = useState<'dashboard' | 'course'>('dashboard');
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  const [courses, setCourses] = useState<any[]>([]);
  const [selectedCourse, setSelectedCourse] = useState<any>(null);
  const [folders, setFolders] = useState<any[]>([]);
  const [tests, setTests] = useState<any[]>([]);
  
  const [allFolders, setAllFolders] = useState<any[]>([]);
  const [allTests, setAllTests] = useState<any[]>([]);
  const [allLectures, setAllLectures] = useState<any[]>([]);

  const [historyData, setHistoryData] = useState<any[]>([]);
  const [lectureProgressData, setLectureProgressData] = useState<any[]>([]);
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [userProfile, setUserProfile] = useState<any>(null);

  const [currentFolderId, setCurrentFolderId] = useState<string | null>(null);
  const [searchTest, setSearchTest] = useState('');
  const [sortTest, setSortTest] = useState('name-asc');
  const [folderPage, setFolderPage] = useState(1);
  const [testPage, setTestPage] = useState(1);
  const [historyPage, setHistoryPage] = useState(1);

  const [analyticsCourse, setAnalyticsCourse] = useState('all');
  const [historySort, setHistorySort] = useState('date-desc');

  const [showModeSelection, setShowModeSelection] = useState(false);
  const [testToStart, setTestToStart] = useState<any>(null);
  const [viewingHistoryDetail, setViewingHistoryDetail] = useState<any>(null);

  const [newPassword, setNewPassword] = useState('');
  const [newFullName, setNewFullName] = useState('');
  const [isUpdatingProfile, setIsUpdatingProfile] = useState(false);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsDropdownOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  useEffect(() => {
    const handleFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  useEffect(() => { checkUserAndFetchData(); }, [activeTab]);

  const checkUserAndFetchData = async () => {
    const { data: { user } } = await supabase.auth.getUser();
    setCurrentUser(user);
    if (user) {
      const { data: profile } = await supabase.from('profiles').select('*').eq('id', user.id).single();
      setUserProfile(profile);
      if (profile && !newFullName) setNewFullName(profile.full_name || '');
      
      const { data: lp } = await supabase.from('lecture_progress').select('lecture_id, is_completed').eq('user_id', user.id);
      setLectureProgressData(lp || []);
    }

    if (activeTab === 'library') {
      fetchCourses(user?.id); fetchAllFolders(); fetchAllTests(); fetchAllLectures(); fetchUserHistory(user?.id);
    }
    if (activeTab === 'analytics') {
      if (courses.length === 0) fetchCourses(user?.id);
      fetchUserHistory(user?.id);
      if (tests.length === 0) fetchAllTestsForRetake();
    }
  };

  const fetchAllLectures = async () => {
     const { data } = await supabase.from('lectures').select('id, course_id').eq('is_published', true);
     setAllLectures(data || []);
  };

  const fetchAllTestsForRetake = async () => {
     const { data } = await supabase.from('tests').select('*').eq('is_published', true);
     setTests(data || []);
  };

  const fetchCourses = async (userId?: string) => {
    if (!userId) return;
    const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', userId);
    const courseIds = enrolls?.map(e => e.course_id) || [];
    if (courseIds.length > 0) {
      const { data } = await supabase.from('courses').select('*').in('id', courseIds);
      const sortedData = (data || []).sort((a, b) => (a.order_index ?? 999) - (b.order_index ?? 999));
      setCourses(sortedData);
    } else { setCourses([]); }
  };

  const fetchUserHistory = async (userId?: string) => {
    if (!userId) return;
    try {
      const { data } = await supabase.from('test_results').select('*').eq('user_id', userId).order('created_at', { ascending: false });
      if (data && data.length > 0) {
        const formattedHistory = data.map((item: any) => ({
          id: item.id, testId: item.test_id, name: item.test_title || 'Bài thi không tên', courseId: item.course_id, subject: item.test_type || 'Standard',
          scoreObj: { value: item.score || 0, display: `${item.score || 0} / ${item.total_score || 0}` },
          timeSpent: Math.round((item.time_spent || 0) / 60), date: item.created_at, details: item.details || {}
        }));
        setHistoryData(formattedHistory);
      } else { setHistoryData([]); }
    } catch (e) {}
  };

  const fetchAllFolders = async () => {
    const { data } = await supabase.from('folders').select('*');
    setAllFolders(data || []);
  };

  const fetchAllTests = async () => {
    const { data } = await supabase.from('tests').select('*').eq('is_published', true);
    setAllTests(data || []);
  };

  const fetchCourseContent = async (courseId: string) => {
    const { data: folderData } = await supabase.from('folders').select('*').eq('course_id', courseId).order('display_order', { ascending: true });
    setFolders(folderData || []);
    const courseTests = allTests.filter(t => {
      const inFolder = folderData?.some((f: any) => f.id === t.folder_id);
      const inJson = t.content_json?.basicInfo?.courseId === courseId;
      return inFolder || inJson;
    });
    setTests(courseTests);
  };

  const handleUpdateProfile = async () => {
    setIsUpdatingProfile(true);
    try {
      if (newFullName && currentUser?.id) await supabase.from('profiles').update({ full_name: newFullName }).eq('id', currentUser.id);
      if (newPassword && newPassword.length >= 6) {
        const { error } = await supabase.auth.updateUser({ password: newPassword });
        if (error) throw error; setNewPassword('');
      } else if (newPassword && newPassword.length < 6) {
        alert("Mật khẩu mới phải có ít nhất 6 ký tự!"); setIsUpdatingProfile(false); return;
      }
      alert("🎉 Cập nhật tài khoản thành công!"); checkUserAndFetchData(); 
    } catch (error: any) { alert("Lỗi cập nhật: " + error.message); } finally { setIsUpdatingProfile(false); }
  };

  const handleLogout = async () => {
    try { await supabase.auth.signOut(); } catch (error) {} finally {
      localStorage.clear(); sessionStorage.clear(); onNavigate?.('home'); setTimeout(() => window.location.reload(), 100);
    }
  };

  const handleOpenCourse = (course: any) => {
    setSelectedCourse(course); setCurrentFolderId(null); setSearchTest(''); setFolderPage(1); setTestPage(1);
    fetchCourseContent(course.id); setActiveView('course');
  };

  const handleFolderClick = (id: string) => { setCurrentFolderId(id); setFolderPage(1); setTestPage(1); };

  const handleStartTestClick = (test: any) => {
    if (!onStartTest) return;
    const type = test.test_type || '';
    if (type === 'IELTS-Writing') onStartTest('ielts-writing', test);
    else if (type === 'IELTS-Speaking') onStartTest('ielts-speaking', test);
    else if (type === 'IELTS-Listening' || type === 'IELTS-Reading') { setTestToStart(test); setShowModeSelection(true); } 
    else if (test.title.toLowerCase().includes('business') || test.title.toLowerCase().includes('econ') || type === 'Case-Study') { onStartTest('case-study', test); } 
    else { onStartTest('standard', test); }
  };

  const handleRetakeFromHistory = (historyItem: any) => {
    const testId = historyItem.testId || historyItem.details?.test_id;
    let foundTest = tests.find(t => String(t.id) === String(testId));
    if (!foundTest) foundTest = tests.find(t => t.title.trim() === historyItem.name.trim());
    if (foundTest) { setViewingHistoryDetail(null); handleStartTestClick(foundTest); } 
    else alert("Đề thi này không còn tồn tại hoặc đã bị ẩn khỏi hệ thống.");
  };

  const handleConfirmMode = (mode: 'computer' | 'paper') => { setShowModeSelection(false); if (onStartTest && testToStart) onStartTest(mode, testToStart); };
  
  const toggleFullScreen = () => { 
    if (!document.fullscreenElement) { 
        document.documentElement.requestFullscreen().catch(); 
    } else { 
        if (document.exitFullscreen) document.exitFullscreen(); 
    } 
  };

  // --- LOGIC XỬ LÝ TÊN & BANNER THỜI GIAN ---
  const rawFullName = userProfile?.full_name || (currentUser?.email ? currentUser.email.split('@')[0] : 'Học viên');
  const nameParts = rawFullName.trim().split(' ');
  const displayUserName = nameParts[nameParts.length - 1]; 
  const displayUserInitial = displayUserName.charAt(0).toUpperCase();

  const hour = new Date().getHours();
  let bannerConfig = { greeting: '', gradient: '', icon: '', subtitle: '' };
  if (hour >= 5 && hour < 12) {
      bannerConfig = { greeting: 'Chào buổi sáng', gradient: 'from-amber-400 to-orange-500', icon: '🌅', subtitle: 'Bắt đầu ngày mới tràn đầy năng lượng! Một chút nỗ lực hôm nay sẽ mang lại kết quả lớn ngày mai.' };
  } else if (hour >= 12 && hour < 18) {
      bannerConfig = { greeting: 'Chào buổi chiều', gradient: 'from-[#0a5482] to-[#1e88e5]', icon: '🌤️', subtitle: 'Tiếp tục hành trình chinh phục mục tiêu nào! Giữ vững sự tập trung nhé.' };
  } else {
      bannerConfig = { greeting: 'Chào buổi tối', gradient: 'from-slate-800 to-indigo-900', icon: '🌙', subtitle: 'Thời gian tĩnh lặng tuyệt vời để tập trung ôn tập và nhìn lại những gì đã học.' };
  }

  const getCourseCover = (course: any) => {
    const lowerTitle = course.title?.toLowerCase() || '';

    // 1. Ưu tiên check môn học cụ thể trước
    if (lowerTitle.includes('business') || lowerTitle.includes('econ')) 
        return { image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800', badge: 'Business & Econ', color: 'text-amber-600' };
    if (lowerTitle.includes('science')) 
        return { image: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=800', badge: 'IGCSE Science', color: 'text-emerald-600' };
    if (lowerTitle.includes('math')) 
        return { image: 'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&q=80&w=800', badge: 'Mathematics', color: 'text-purple-600' };

    // 2. Sau đó mới check hệ chương trình chung
    if (lowerTitle.includes('ielts') || course.type === 'IELTS') 
        return { image: 'https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&q=80&w=800', badge: 'IELTS Mastery', color: 'text-blue-600' };
    if (lowerTitle.includes('igcse')) 
        return { image: 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&q=80&w=800', badge: 'IGCSE Program', color: 'text-teal-600' };
    
    // 3. Mặc định nếu không khớp
    return { image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=800', badge: course.type || 'Khóa học', color: 'text-slate-600' };
  };

  const getTestIcon = (testType: string) => {
    if (testType.includes('Listening')) return '🎧';
    if (testType.includes('Speaking')) return '🎙️';
    if (testType.includes('Writing')) return '✍️';
    if (testType.includes('Case-Study')) return '📄';
    return '📝';
  };

  const globalTotalTestsDone = historyData.length;
  const globalTotalTimeHours = (historyData.reduce((acc, curr) => acc + curr.timeSpent, 0) / 60).toFixed(1);
  const inProgressTest = allTests.find(t => checkInProgress(t.id));

  const currentSubFolders = folders.filter(f => currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')).sort((a,b) => (a.display_order||0) - (b.display_order||0));
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
        <button disabled={currentPage === 1} onClick={() => setPage(currentPage - 1)} className="w-10 h-10 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:bg-[#1e88e5] hover:text-white transition-colors disabled:opacity-30 shadow-sm font-black">→</button>
        <span className="text-[14px] font-bold text-slate-500 bg-white px-5 py-2 rounded-xl border border-slate-200 shadow-sm">Trang {currentPage} / {totalPages}</span>
        <button disabled={currentPage === totalPages} onClick={() => setPage(currentPage + 1)} className="w-10 h-10 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:bg-[#1e88e5] hover:text-white transition-colors disabled:opacity-30 shadow-sm font-black">→</button>
      </div>
    );
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

  const totalHistoryPages = Math.ceil(processedHistory.length / HISTORY_PER_PAGE);
  const paginatedHistory = processedHistory.slice((historyPage - 1) * HISTORY_PER_PAGE, historyPage * HISTORY_PER_PAGE);

  const analyticsTotalTestsDone = processedHistory.length;
  const avgScore = analyticsTotalTestsDone > 0 ? (processedHistory.reduce((acc, curr) => acc + curr.scoreObj.value, 0) / analyticsTotalTestsDone).toFixed(1) : '0';
  const analyticsTotalTimeMinutes = processedHistory.reduce((acc, curr) => acc + curr.timeSpent, 0);
  const analyticsTotalTimeHours = (analyticsTotalTimeMinutes / 60).toFixed(1);

  const getDynamicScoreFeedback = () => {
    if (analyticsTotalTestsDone < 2) return "Bạn mới bắt đầu luyện tập. Cứ làm từ từ, duy trì làm thêm nhiều bài để hệ thống phân tích nhé!";
    const recentScores = processedHistory.slice(0, 3).map(h => h.scoreObj.value);
    const olderScores = processedHistory.slice(3, 6).map(h => h.scoreObj.value);
    const avgRecent = recentScores.length ? recentScores.reduce((a,b)=>a+b,0)/recentScores.length : 0;
    const avgOlder = olderScores.length ? olderScores.reduce((a,b)=>a+b,0)/olderScores.length : 0;
    
    if (olderScores.length === 0) return "Khởi đầu rất tốt! Hãy duy trì làm bài đều đặn để nâng cao điểm trung bình nha.";
    if (avgRecent > avgOlder + 5) return "Tuyệt vời! Các bài kiểm tra gần đây bạn đang có sự tiến bộ vượt bậc.";
    if (avgRecent < avgOlder - 5) return "Điểm số đang có dấu hiệu giảm sút một chút. Hãy dành thời gian xem lại các lỗi sai thường gặp nhé.";
    return "Phong độ của bạn đang ở mức rất ổn định. Tiếp tục phát huy và thử thách với các đề khó hơn nhé!";
  };

  const getDynamicCompleteFeedback = () => {
    if (analyticsTotalTestsDone === 0) return "Cùng khởi động với bài thi đầu tiên nào!";
    if (analyticsTotalTestsDone < 5) return `Bạn đã hoàn thành ${analyticsTotalTestsDone} bài. Bước đệm hoàn hảo để bứt phá.`;
    return `Wow, bạn đã hoàn thành ${analyticsTotalTestsDone} bài thi! Sự kiên trì của bạn thực sự đáng nể đó.`;
  };

  const sparklineScoreArr = processedHistory.slice(0, 5).reverse().map(h => ({ v: h.scoreObj.value }));
  const sparklineCompletedArr = processedHistory.slice(0, 5).reverse().map((h, i) => ({ v: i + 1 })); 
  const sparklineAttemptsArr = processedHistory.slice(0, 5).reverse().map((h, i) => ({ v: (i + 1) * 2 })); 
  const sparklineTimeArr = processedHistory.slice(0, 5).reverse().map(h => ({ v: h.timeSpent }));

  const ieltsHistory = processedHistory.filter(h => h.subject.includes('IELTS')).slice().reverse(); 
  const dynamicProgressData = ieltsHistory.map((h, i) => {
    let band = parseFloat(h.details?.bandScore);
    if (isNaN(band)) band = (h.scoreObj.value / (h.scoreObj.value + 0.01)); 
    return {
      date: formatDateShort(h.date) || `Lần ${i+1}`,
      listening: h.subject.includes('Listening') ? band : null, reading: h.subject.includes('Reading') ? band : null,
      writing: h.subject.includes('Writing') ? band : null, speaking: h.subject.includes('Speaking') ? band : null,
    };
  });

  const breadcrumbs = [];
  let curr = folders.find(f => f.id === currentFolderId);
  while (curr) { breadcrumbs.unshift(curr); curr = folders.find(f => f.id === curr.parent_id); }

  return (
    <div className="min-h-screen bg-[#f4f7f9] font-sans text-slate-800">
      
      {/* HEADER: KHÔI PHỤC LẠI LOGO HÌNH ẢNH */}
      <header className="bg-white/80 backdrop-blur-md border-b border-slate-200/50 sticky top-0 z-40 shadow-sm">
        <div className="max-w-[1200px] w-full mx-auto px-6 py-3 flex items-center justify-between">
          
          <div className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity" onClick={() => onNavigate?.('home')}>
            <div className="flex flex-col items-end">
              <h1 className="font-black text-2xl tracking-tighter text-[#0a5482] leading-none">TONY<span className="text-slate-800">ENGLISH</span></h1>
              <span className="text-[10px] italic text-[#1e88e5] font-medium mt-0.5 pr-0.5">The future begins here</span>
            </div>
            {/* TRẢ LẠI LOGO KHIÊN GỐC */}
            <div className="w-10 h-10 flex items-center justify-center overflow-hidden">
               <img src="/logo-shield.png" alt="TonyEnglish Logo" className="w-auto h-full object-contain" />
            </div>
          </div>

          <div className="hidden md:flex items-center gap-2 bg-slate-100/50 rounded-2xl p-1 border border-slate-200/50">
            <button onClick={() => { setActiveTab('library'); setActiveView('dashboard'); setSelectedCourse(null); }} className={`flex items-center gap-2 px-6 py-2 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'library' ? 'bg-white shadow text-[#1e88e5]' : 'text-slate-500 hover:text-slate-800 hover:bg-white/50'}`}>📚 Không gian học tập</button>
            <button onClick={() => setActiveTab('analytics')} className={`flex items-center gap-2 px-6 py-2 rounded-xl font-bold text-[14px] transition-all ${activeTab === 'analytics' ? 'bg-white shadow text-[#1e88e5]' : 'text-slate-500 hover:text-slate-800 hover:bg-white/50'}`}>📊 Phân tích & Lịch sử</button>
          </div>

          <div className="flex items-center gap-5">
            <div className="hidden lg:flex items-center gap-3">
               <div className="flex items-center gap-1.5 bg-orange-50 text-orange-600 px-3 py-1.5 rounded-lg border border-orange-100 font-bold text-[13px] shadow-sm">
                  🔥 {globalTotalTestsDone}
               </div>
               <div className="flex items-center gap-1.5 bg-blue-50 text-blue-600 px-3 py-1.5 rounded-lg border border-blue-100 font-bold text-[13px] shadow-sm">
                  ⏱️ {globalTotalTimeHours}h
               </div>
               <div className="h-6 w-px bg-slate-200 mx-1"></div>
               <button onClick={toggleFullScreen} className="w-10 h-10 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#1e88e5] transition-colors">
                 {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0 4.5L15 15" /></svg>}
               </button>
            </div>

            <div className="relative" ref={dropdownRef}>
               <button onClick={() => setIsDropdownOpen(!isDropdownOpen)} className="flex items-center gap-3 hover:opacity-80 transition-opacity focus:outline-none">
                 <div className="text-right hidden sm:block">
                   <div className="font-black text-[14px] text-slate-800">{displayUserName}</div>
                   <div className="text-[11px] font-medium text-slate-500 uppercase tracking-wider">{userProfile?.role === 'admin' ? 'Quản trị viên' : 'Học viên'}</div>
                 </div>
                 <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-[#0a5482] to-[#1e88e5] text-white flex items-center justify-center font-black shadow-md border-2 border-white ring-2 ring-blue-50">{displayUserInitial}</div>
               </button>

               {isDropdownOpen && (
                  <div className="absolute right-0 mt-3 w-56 bg-white rounded-2xl shadow-xl border border-slate-100 py-2 z-50 animate-in fade-in slide-in-from-top-2">
                     <button onClick={() => window.open('https://tonyenglish.vn/vi', '_blank')} className="w-full text-left px-5 py-3 text-sm font-black text-emerald-600 hover:bg-emerald-50 flex items-center gap-3 transition-colors border-b border-slate-100 mb-1 pb-3">
                        <span className="text-lg">🏠</span> Về Website Chính
                     </button>
                     <button onClick={() => { setActiveTab('profile'); setIsDropdownOpen(false); }} className="w-full text-left px-5 py-3 text-sm font-bold text-slate-700 hover:bg-slate-50 hover:text-[#1e88e5] flex items-center gap-3 transition-colors mt-1">
                        <span className="text-lg">👤</span> Cấu hình tài khoản
                     </button>
                     {userProfile?.role === 'admin' && (
                       <button onClick={() => onNavigate?.('admin')} className="w-full text-left px-5 py-3 text-sm font-black text-[#8b5cf6] hover:bg-purple-50 flex items-center gap-3 transition-colors border-t border-slate-100 mt-1 pt-3">
                          <span className="text-lg">⚙️</span> Trang Quản Trị
                       </button>
                     )}
                     <div className="h-px bg-slate-100 my-1"></div>
                     <button onClick={handleLogout} className="w-full text-left px-5 py-3 text-sm font-bold text-red-600 hover:bg-red-50 flex items-center gap-3 transition-colors">
                        <span className="text-lg">🚪</span> Đăng xuất
                     </button>
                  </div>
               )}
            </div>
          </div>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="max-w-[1200px] w-full mx-auto p-6 md:p-8 relative">
        
        {/* ================= TAB 1: THƯ VIỆN ĐỀ ================= */}
        {activeTab === 'library' && (
          <>
            {activeView === 'dashboard' && (
              <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
                
                {/* HERO BANNER TỰ ĐỘNG ĐỔI MÀU THEO THỜI GIAN */}
                <div className={`relative bg-gradient-to-br ${bannerConfig.gradient} rounded-[2rem] p-8 md:p-12 mb-10 overflow-hidden shadow-xl`}>
                  <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3"></div>
                  <div className="absolute bottom-0 left-10 w-40 h-40 bg-white opacity-10 rounded-full blur-2xl translate-y-1/3"></div>
                  
                  <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
                    <div className="text-white flex-1 text-center md:text-left">
                      <h2 className="text-3xl md:text-4xl font-black mb-3 drop-shadow-md">{bannerConfig.greeting}, {displayUserName}! {bannerConfig.icon}</h2>
                      <p className="text-white/80 text-[16px] md:text-lg font-medium leading-relaxed max-w-xl">{bannerConfig.subtitle}</p>
                    </div>

                    {inProgressTest ? (
                       <div className="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-3xl w-full md:w-80 shadow-lg text-white group cursor-pointer hover:bg-white/20 transition-all" onClick={() => handleStartTestClick(inProgressTest)}>
                          <div className="flex items-center gap-2 mb-3">
                             <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                             <span className="text-[11px] font-black uppercase tracking-widest text-amber-300">Đang làm dở</span>
                          </div>
                          <h3 className="font-bold text-lg mb-4 line-clamp-2 leading-tight">{inProgressTest.title}</h3>
                          <button className="w-full bg-white text-slate-800 font-black py-2.5 rounded-xl text-sm group-hover:shadow-md transition-all">TIẾP TỤC NGAY →</button>
                       </div>
                    ) : courses.length > 0 && (
                      <div 
                        className="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-3xl w-full md:w-80 shadow-lg text-white group cursor-pointer hover:bg-white/20 transition-all" 
                        onClick={() => onOpenLecture && onOpenLecture(courses[0].id)}
                      >
                        <div className="flex items-center gap-2 mb-3">
                           <span className="text-[11px] font-black uppercase tracking-widest text-white/70">Gợi ý học tập</span>
                        </div>
                        <h3 className="font-bold text-lg mb-4 line-clamp-2 leading-tight">Khóa học {courses[0].title}</h3>
                        <button className="w-full bg-white text-slate-800 font-black py-2.5 rounded-xl text-sm group-hover:shadow-md transition-all">
                           VÀO HỌC NGAY →
                        </button>
                      </div>
                    )}
                  </div>
                </div>

                <div className="mb-6 flex items-center justify-between">
                  <h2 className="font-black text-2xl text-slate-800">Khóa học của tôi</h2>
                </div>

                {courses.length === 0 ? (
                  <div className="bg-white border-2 border-dashed border-slate-200 rounded-[2rem] py-24 text-center shadow-sm">
                    <span className="text-5xl block mb-4 opacity-50">🔒</span>
                    <h3 className="font-bold text-slate-700 text-lg mb-2">Chưa có khóa học nào</h3>
                    <p className="text-slate-500 text-sm">Vui lòng liên hệ TonyEnglish để được cấp quyền truy cập nhé!</p>
                  </div>
                ) : (
                  <div className="flex flex-col gap-6">
                    {courses.map(course => {
                      const cover = getCourseCover(course);
                      const courseFolderIds = allFolders.filter(f => f.course_id === course.id).map(f => f.id);
                      const testCount = allTests.filter(t => courseFolderIds.includes(t.folder_id)).length;
                      const lectureCount = allLectures.filter(l => l.course_id === course.id).length;
                      
                      // Tính tiến độ Bài giảng
                      const completedLecs = lectureProgressData.filter(lp => lp.is_completed && allLectures.find(l => l.id === lp.lecture_id && l.course_id === course.id)).length;
                      const lecProgress = lectureCount > 0 ? Math.min(100, Math.round((completedLecs / lectureCount) * 100)) : 0;
                      
                      // Tính tiến độ Đề thi
                      const uniqueCompletedTests = new Set(historyData.filter(h => h.courseId === course.id).map(h => h.testId)).size;
                      const testProgress = testCount > 0 ? Math.min(100, Math.round((uniqueCompletedTests / testCount) * 100)) : 0;

                      return (
                        <div key={course.id} className="bg-white rounded-[2rem] border border-slate-100 overflow-hidden shadow-sm hover:shadow-lg transition-all flex flex-col md:flex-row group relative">
                          <div className="w-full md:w-[300px] lg:w-[350px] min-h-[180px] relative overflow-hidden shrink-0 bg-slate-100">
                             <img src={cover.image} alt={course.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                             <div className={`absolute top-4 left-4 bg-white/95 backdrop-blur-sm px-3 py-1.5 rounded-lg text-[11px] font-black uppercase tracking-widest ${cover.color} shadow-sm`}>
                                {cover.badge}
                             </div>
                          </div>
                          
                          <div className="flex-1 p-6 md:p-8 flex flex-col justify-center border-b md:border-b-0 md:border-r border-slate-100">
                            <h4 className="font-black text-xl text-slate-800 mb-3">{course.title}</h4>
                            <div className="flex items-center gap-4 mb-6">
                              <span className="bg-slate-50 text-slate-600 text-[12px] font-bold px-3 py-1.5 rounded-lg border border-slate-100">📚 {lectureCount} bài giảng</span>
                              <span className="bg-slate-50 text-slate-600 text-[12px] font-bold px-3 py-1.5 rounded-lg border border-slate-100">📝 {testCount} đề thi</span>
                            </div>
                            
                            <div className="w-full mt-auto flex flex-col md:flex-row gap-6">
                              {/* Thanh 1: Tiến độ bài giảng */}
                              <div className="flex-1">
                                <div className="flex justify-between items-end mb-1.5">
                                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ bài giảng</span>
                                  <span className="text-[12px] font-black text-emerald-600">{lecProgress}%</span>
                                </div>
                                <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                                  <div className="h-full bg-emerald-500 rounded-full transition-all duration-1000" style={{ width: `${lecProgress}%` }}></div>
                                </div>
                              </div>
                              {/* Thanh 2: Tiến độ Đề thi */}
                              <div className="flex-1">
                                <div className="flex justify-between items-end mb-1.5">
                                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ đề thi</span>
                                  <span className="text-[12px] font-black text-blue-600">{testProgress}%</span>
                                </div>
                                <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                                  <div className="h-full bg-blue-500 rounded-full transition-all duration-1000" style={{ width: `${testProgress}%` }}></div>
                                </div>
                              </div>
                            </div>
                          </div>

                          <div className="w-full md:w-[260px] lg:w-[280px] p-6 flex flex-col justify-center gap-3 bg-slate-50/50 shrink-0">
                             <button onClick={() => onOpenLecture && onOpenLecture(course.id)} className="w-full bg-white hover:bg-emerald-50 border-2 border-emerald-100 hover:border-emerald-500 text-emerald-600 font-black text-[13px] py-3.5 rounded-xl transition-colors shadow-sm flex items-center justify-center gap-2">
                               <span className="text-lg">📖</span> VÀO BÀI GIẢNG
                             </button>
                             <button onClick={() => handleOpenCourse(course)} className="w-full bg-gradient-to-r from-[#0a5482] to-[#1e88e5] hover:from-[#1565c0] hover:to-[#0a5482] text-white font-black text-[13px] py-3.5 rounded-xl transition-all shadow-md flex items-center justify-center gap-2">
                               <span className="text-lg">📝</span> KHO ĐỀ THI
                             </button>
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
                <div className="flex flex-wrap items-center gap-2 text-[14px] font-bold text-slate-500 mb-6 bg-white p-4 rounded-2xl border border-slate-100 shadow-sm">
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
                      <h3 className="font-black text-xl text-slate-800 mb-4 ml-1">Danh mục</h3>
                      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                        {paginatedFolders.map((subFolder, idx) => {
                          const childCount = folders.filter(f => f.parent_id === subFolder.id).length;
                          const testCount = allTests.filter(t => t.folder_id === subFolder.id).length;
                          
                          // LẤY ẢNH NỀN GÁN SẴN HOẶC RANDOM ĐẸP MẮT
                          const defaultImage = FOLDER_IMAGES[idx % FOLDER_IMAGES.length];
                          const displayImage = subFolder.thumbnail_url || defaultImage;

                          return (
                            <div key={subFolder.id} onClick={() => handleFolderClick(subFolder.id)} className="bg-white rounded-3xl border border-slate-100 overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer flex flex-col h-[180px] relative group">
                              {/* PHẦN ĐẦU THƯ MỤC CÓ HÌNH ẢNH */}
                              <div className={`h-[110px] relative p-5 overflow-hidden flex items-end`}>
                                <img src={displayImage} className="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" alt="folder" />
                                <div className={`absolute inset-0 bg-gradient-to-t from-black/80 to-black/10`}></div>
                                <h3 className={`relative z-10 text-[18px] font-black leading-tight line-clamp-2 w-full text-white drop-shadow-md`}>
                                   {subFolder.title}
                                </h3>
                              </div>
                              <div className="flex-1 bg-white p-5 flex flex-col justify-center relative">
                                <div className="flex justify-between items-center text-slate-500">
                                  <p className="text-[12px] font-bold bg-slate-50 px-3 py-1 rounded-lg border border-slate-100">{childCount > 0 ? `${childCount} mục con` : `${testCount} đề thi`}</p>
                                  <span className="text-[#1e88e5] font-black group-hover:translate-x-1 transition-transform bg-blue-50 w-8 h-8 rounded-full flex items-center justify-center">→</span>
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
                    <div className="bg-white rounded-[2rem] border border-slate-100 overflow-hidden shadow-sm mt-8 animate-in fade-in zoom-in-95">
                      <div className="bg-white px-6 py-5 border-b border-slate-100 flex flex-col sm:flex-row justify-between items-center gap-4">
                        <div className="relative w-full sm:w-96">
                          <input type="text" placeholder="Tìm kiếm bài thi..." value={searchTest} onChange={(e) => {setSearchTest(e.target.value); setTestPage(1);}} className="w-full pl-12 pr-4 py-3 rounded-2xl bg-slate-50 border-none font-medium text-[14px] outline-none focus:ring-2 focus:ring-[#1e88e5] transition-shadow" />
                          <span className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-lg">🔍</span>
                        </div>
                        <div className="w-full sm:w-48 bg-slate-50 rounded-2xl px-4 py-1 border-none focus-within:ring-2 focus-within:ring-[#1e88e5] transition-shadow">
                          <select value={sortTest} onChange={(e) => setSortTest(e.target.value)} className="w-full py-2 bg-transparent outline-none text-[13px] font-bold text-slate-600 cursor-pointer appearance-none">
                            <option value="name-asc">A-Z (Tên bài)</option><option value="name-desc">Z-A (Tên bài)</option>
                            <option value="date-desc">Mới nhất trước</option><option value="date-asc">Cũ nhất trước</option>
                          </select>
                        </div>
                      </div>

                      <div className="p-6 md:p-8 bg-slate-50/50">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                          {paginatedTests.map(test => {
                            const inProgress = checkInProgress(test.id);
                            const isCompleted = historyData.some(h => 
                                (h.testId && String(h.testId) === String(test.id)) || 
                                (h.details?.test_id && String(h.details?.test_id) === String(test.id)) || 
                                (h.name && test.title && h.name.trim() === test.title.trim())
                            );

                            let statusConfig = { progress: 0, badge: "Chưa làm", badgeClass: "text-slate-500 bg-slate-100", btnText: "Bắt đầu làm bài", btnClass: "bg-white text-[#1e88e5] border border-blue-200 hover:bg-[#1e88e5] hover:text-white" };
                            if (isCompleted) statusConfig = { progress: 100, badge: "Hoàn thành", badgeClass: "text-emerald-600 bg-emerald-100", btnText: "Làm lại bài", btnClass: "bg-emerald-50 text-emerald-600 hover:bg-emerald-500 hover:text-white border-transparent" };
                            else if (inProgress) statusConfig = { progress: 50, badge: "Đang làm dở", badgeClass: "text-amber-600 bg-amber-100", btnText: "Tiếp tục bài", btnClass: "bg-amber-50 text-amber-600 hover:bg-amber-500 hover:text-white border-transparent" };

                            return (
                              <div key={test.id} onClick={() => handleStartTestClick(test)} className="bg-white border border-slate-100 p-6 rounded-3xl shadow-sm hover:shadow-xl transition-all cursor-pointer flex flex-col justify-between group relative overflow-hidden">
                                <div className="absolute top-0 left-0 right-0 h-1 bg-slate-100">
                                   <div className={`h-full transition-all duration-500 ${isCompleted ? 'bg-emerald-500' : inProgress ? 'bg-amber-500' : 'bg-transparent'}`} style={{ width: `${statusConfig.progress}%` }}></div>
                                </div>
                                <div>
                                  <div className="flex justify-between items-center mb-5 mt-2">
                                    <div className="w-12 h-12 rounded-2xl bg-blue-50 flex items-center justify-center text-2xl group-hover:scale-110 transition-transform shadow-sm">{getTestIcon(test.test_type)}</div>
                                    <span className={`text-[10px] font-black px-3 py-1.5 rounded-lg uppercase tracking-widest ${statusConfig.badgeClass}`}>{statusConfig.badge}</span>
                                  </div>
                                  <h3 className="font-bold text-slate-800 text-[16px] group-hover:text-[#1e88e5] transition-colors mb-3 line-clamp-2 leading-snug">{test.title}</h3>
                                  <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider">{test.test_type}</span>
                                </div>
                                <button className={`mt-6 w-full font-black text-[13px] py-3 rounded-xl transition-colors shadow-sm ${statusConfig.btnClass}`}>{statusConfig.btnText}</button>
                              </div>
                            );
                          })}
                        </div>
                        {processedTests.length === 0 ? (
                          <div className="text-center py-16 text-slate-400 font-medium">Không có bài thi nào khớp với tìm kiếm của bạn.</div>
                        ) : (
                          renderPagination(testPage, totalTestPages, setTestPage)
                        )}
                      </div>
                    </div>
                  )}

                  {currentSubFolders.length === 0 && currentTests.length === 0 && (
                    <div className="text-center py-20 bg-white rounded-3xl border border-slate-100 text-slate-400 font-medium text-lg shadow-sm">📭 Thư mục này hiện đang trống.</div>
                  )}
                </div>
              </div>
            )}
          </>
        )}

        {/* ================= TAB 2: PHÂN TÍCH & LỊCH SỬ ================= */}
        {activeTab === 'analytics' && (
          <div className="space-y-8 animate-in fade-in duration-300">
            
            <div className="bg-white px-8 py-6 rounded-[2rem] border border-slate-100 shadow-sm flex flex-col md:flex-row items-center justify-between gap-4">
              <div>
                <h2 className="text-[22px] font-black text-slate-800">Hiệu Suất Học Tập</h2>
                <p className="text-sm text-slate-500 font-medium mt-1">Lựa chọn khóa học để xem biểu đồ và lịch sử chi tiết</p>
              </div>
              <div className="w-full md:w-64 bg-slate-50 border border-slate-100 rounded-2xl px-5 py-3 flex items-center justify-between cursor-pointer focus-within:ring-2 focus-within:ring-[#1e88e5] transition-shadow">
                <select value={analyticsCourse} onChange={(e) => setAnalyticsCourse(e.target.value)} className="w-full bg-transparent font-bold text-[14px] text-slate-700 outline-none cursor-pointer appearance-none">
                  <option value="all">Tất cả khóa học</option>
                  {courses.length > 0 && courses.map(course => ( <option key={course.id} value={course.id}>{course.title}</option> ))}
                </select>
                <span className="text-slate-400 text-xs">▼</span>
              </div>
            </div>

            {analyticsTotalTestsDone === 0 ? (
              <div className="bg-white rounded-[2rem] border-2 border-dashed border-slate-200 py-24 text-center shadow-sm flex flex-col items-center justify-center">
                <div className="w-20 h-20 mb-6 flex items-center justify-center bg-slate-50 rounded-3xl border border-slate-100 shadow-sm">
                  <div className="flex items-end gap-1.5 h-10">
                    <div className="w-3 bg-emerald-200 h-6 rounded-sm"></div>
                    <div className="w-3 bg-pink-300 h-8 rounded-sm"></div>
                    <div className="w-3 bg-blue-400 h-10 rounded-sm"></div>
                  </div>
                </div>
                <h3 className="text-xl font-black text-slate-700 mb-2">Chưa có dữ liệu làm bài</h3>
                <p className="text-slate-500 font-medium text-[15px]">Anh/chị hãy vào Thư viện đề, làm thử một bài test và nộp bài để hệ thống phân tích nhé!</p>
              </div>
            ) : (
              <>
                {/* 4 Ô Sparklines */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                  <div className="bg-[#f8fafc] rounded-[2rem] border border-slate-100 shadow-sm p-6 flex flex-col justify-between hover:shadow-md transition-shadow">
                    <div className="flex justify-between items-center mb-4">
                      <div className="flex items-center gap-2"><span className="text-blue-500 text-xl">📊</span><span className="font-bold text-slate-700 text-[14px]">Điểm trung bình</span></div>
                      <span className="font-black text-blue-500 text-2xl">{avgScore}</span>
                    </div>
                    <div className="h-16 w-full -mx-1"><ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineScoreArr}><Line type="monotone" dataKey="v" stroke="#3b82f6" strokeWidth={3} dot={{r: 4, fill: '#3b82f6', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer></div>
                    <p className="text-[12px] text-slate-500 font-medium mt-4 leading-relaxed">{getDynamicScoreFeedback()}</p>
                  </div>

                  <div className="bg-[#f0fdf4] rounded-[2rem] border border-emerald-50 shadow-sm p-6 flex flex-col justify-between hover:shadow-md transition-shadow">
                    <div className="flex justify-between items-center mb-4">
                      <div className="flex items-center gap-2"><span className="text-emerald-500 text-xl">📝</span><span className="font-bold text-slate-700 text-[14px]">Bài hoàn thành</span></div>
                      <span className="font-black text-emerald-500 text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-16 w-full -mx-1"><ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineCompletedArr}><Line type="monotone" dataKey="v" stroke="#10b981" strokeWidth={3} dot={{r: 4, fill: '#10b981', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer></div>
                    <p className="text-[12px] text-slate-500 font-medium mt-4 leading-relaxed">{getDynamicCompleteFeedback()}</p>
                  </div>

                  <div className="bg-[#fdf4ff] rounded-[2rem] border border-fuchsia-50 shadow-sm p-6 flex flex-col justify-between hover:shadow-md transition-shadow">
                    <div className="flex justify-between items-center mb-4">
                      <div className="flex items-center gap-2"><span className="text-fuchsia-500 text-xl">🔄</span><span className="font-bold text-slate-700 text-[14px]">Lượt làm bài</span></div>
                      <span className="font-black text-fuchsia-500 text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-16 w-full -mx-1"><ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineAttemptsArr}><Line type="monotone" dataKey="v" stroke="#d946ef" strokeWidth={3} dot={{r: 4, fill: '#d946ef', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer></div>
                    <p className="text-[12px] text-slate-500 font-medium mt-4 leading-relaxed">Việc ôn tập và làm lại đề cũ giúp củng cố kiến thức cực kỳ hiệu quả.</p>
                  </div>

                  <div className="bg-[#fff7ed] rounded-[2rem] border border-orange-50 shadow-sm p-6 flex flex-col justify-between hover:shadow-md transition-shadow">
                    <div className="flex justify-between items-center mb-4">
                      <div className="flex items-center gap-2"><span className="text-orange-500 text-xl">⏱️</span><span className="font-bold text-slate-700 text-[14px]">Thời gian học</span></div>
                      <span className="font-black text-orange-500 text-2xl">{analyticsTotalTimeHours}h</span>
                    </div>
                    <div className="h-16 w-full -mx-1"><ResponsiveContainer width="100%" height="100%"><LineChart data={sparklineTimeArr}><Line type="monotone" dataKey="v" stroke="#f97316" strokeWidth={3} dot={{r: 4, fill: '#f97316', strokeWidth: 2, stroke: '#fff'}} isAnimationActive={false} /></LineChart></ResponsiveContainer></div>
                    <p className="text-[12px] text-slate-500 font-medium mt-4 leading-relaxed">Giờ bay tích lũy càng cao, kỹ năng giải đề của bạn sẽ càng phản xạ nhanh hơn.</p>
                  </div>
                </div>

                {/* Lịch sử làm bài: ĐÃ PHÂN TRANG VÀ LÀM LẠI BADGE MÀU SẮC */}
                <div className="mt-10 bg-white rounded-[2rem] border border-slate-100 shadow-sm overflow-hidden">
                  <div className="px-8 py-6 border-b border-slate-100 flex justify-between items-center">
                     <h3 className="font-black text-xl text-slate-800">Lịch sử làm bài kiểm tra</h3>
                  </div>
                  <div className="overflow-x-auto">
                    <table className="w-full text-left border-collapse min-w-[800px]">
                      <thead>
                        <tr className="border-b border-slate-100 text-[13px] text-slate-500 bg-slate-50/50 uppercase tracking-widest">
                          <th className="px-8 py-5 font-bold w-2/5">Tên bài kiểm tra</th>
                          <th className="px-8 py-5 font-bold text-center">Ngày làm bài</th>
                          <th className="px-8 py-5 font-bold text-center">Điểm số</th>
                          <th className="px-8 py-5 font-bold text-right">Thao tác</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-50">
                        {paginatedHistory.map(history => {
                          const isHigh = history.scoreObj.value > 60 || parseFloat(history.details?.bandScore) >= 6.0;
                          return (
                          <tr key={history.id} className="hover:bg-slate-50/50 transition-colors group">
                            <td className="px-8 py-6">
                              <div className="font-bold text-[15px] text-slate-800 mb-1.5">{history.name}</div>
                              <span className="text-[10px] font-bold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md uppercase tracking-wider">{history.subject}</span>
                            </td>
                            <td className="px-8 py-6 text-center">
                              <div className="font-bold text-[14px] text-slate-700">{formatDate(history.date).split(' ')[0]}</div>
                              <div className="text-[12px] font-medium text-slate-400 mt-0.5">{formatDate(history.date).split(' ')[1]}</div>
                            </td>
                            <td className="px-8 py-6 text-center">
                              <span className={`inline-flex items-center justify-center px-4 py-2 rounded-xl text-[13px] font-black border shadow-sm ${isHigh ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-slate-50 text-slate-700 border-slate-200'}`}>
                                {history.details?.bandScore ? `Band ${history.details.bandScore}` : `${history.scoreObj.value} điểm`}
                              </span>
                            </td>
                            <td className="px-8 py-6 text-right">
                              <button onClick={() => setViewingHistoryDetail(history)} className="inline-flex items-center gap-2 bg-white border border-slate-200 text-slate-600 font-bold px-5 py-2.5 rounded-xl hover:border-blue-500 hover:text-blue-600 shadow-sm transition-all text-[12px] uppercase tracking-wider">
                                👁️ Xem chi tiết
                              </button>
                            </td>
                          </tr>
                        )})}
                      </tbody>
                    </table>
                  </div>
                  {renderPagination(historyPage, totalHistoryPages, setHistoryPage)}
                </div>
              </>
            )}
          </div>
        )}

        {/* TAB 3: TÀI KHOẢN */}
        {activeTab === 'profile' && (
          <div className="max-w-2xl mx-auto mt-8 animate-in fade-in slide-in-from-bottom-4 duration-300">
            <div className="bg-white p-10 rounded-[2rem] border border-slate-100 shadow-xl text-center">
              <div className="w-28 h-28 rounded-full bg-gradient-to-tr from-[#0a5482] to-[#1e88e5] text-white flex items-center justify-center font-black text-5xl mx-auto mb-6 shadow-lg border-4 border-white ring-4 ring-blue-50">
                {displayUserInitial}
              </div>
              <h2 className="text-3xl font-black text-slate-800 mb-1">{displayUserName}</h2>
              <p className="text-slate-500 font-medium mb-10 text-lg">
                {userProfile?.role === 'admin' ? 'Quản trị viên hệ thống' : 'Học viên TonyEnglish'}
              </p>
              
              <div className="space-y-6 border-t border-slate-100 pt-8 text-left bg-slate-50/50 p-8 rounded-3xl">
                <h3 className="font-black text-xl text-slate-800 mb-4">🔐 Cấu hình thông tin</h3>
                <div className="space-y-2">
                  <label className="text-[13px] font-bold text-slate-500 uppercase ml-1">Họ và tên</label>
                  <input type="text" value={newFullName} onChange={e => setNewFullName(e.target.value)} className="w-full bg-white border border-slate-200 rounded-2xl px-5 py-3.5 font-medium focus:ring-2 focus:ring-[#1e88e5] outline-none shadow-sm transition-shadow" placeholder="Nhập họ và tên..." />
                </div>
                <div className="space-y-2">
                  <label className="text-[13px] font-bold text-slate-500 uppercase ml-1">Email đăng nhập</label>
                  <input type="email" defaultValue={currentUser?.email || ""} disabled className="w-full bg-slate-100 border border-slate-200 rounded-2xl px-5 py-3.5 font-medium text-slate-500 outline-none cursor-not-allowed" />
                </div>
                <div className="space-y-2">
                  <label className="text-[13px] font-bold text-slate-500 uppercase ml-1">Mật khẩu mới (Nếu muốn đổi)</label>
                  <input type="password" placeholder="••••••••" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} className="w-full bg-white border border-slate-200 rounded-2xl px-5 py-3.5 font-medium focus:ring-2 focus:ring-[#1e88e5] outline-none shadow-sm transition-shadow" />
                </div>
                <button onClick={handleUpdateProfile} disabled={isUpdatingProfile} className="bg-gradient-to-r from-[#0a5482] to-[#1e88e5] hover:from-[#1565c0] hover:to-[#0a5482] disabled:from-slate-300 disabled:to-slate-400 text-white font-black px-6 py-4 rounded-2xl transition-all shadow-lg hover:shadow-xl w-full mt-4 text-[15px]">
                  {isUpdatingProfile ? 'ĐANG CẬP NHẬT...' : 'CẬP NHẬT TÀI KHOẢN'}
                </button>
              </div>
            </div>
          </div>
        )}

      </main>

      {/* POPUP CHI TIẾT LỊCH SỬ */}
      {viewingHistoryDetail && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-[2rem] w-full max-w-xl shadow-2xl overflow-hidden animate-in zoom-in-95">
             <div className="bg-slate-50/80 px-8 py-6 border-b border-slate-100 flex justify-between items-center">
                <h3 className="font-black text-slate-800 text-lg uppercase tracking-widest">📝 Bảng Kết Quả</h3>
                <button onClick={() => setViewingHistoryDetail(null)} className="w-10 h-10 rounded-full bg-white border border-slate-200 text-slate-400 hover:text-red-500 hover:border-red-200 hover:bg-red-50 text-xl font-bold flex items-center justify-center transition-colors">&times;</button>
             </div>
             
             <div className="p-8">
                <div className="text-center mb-8 border-b-2 border-dashed border-slate-100 pb-8">
                   <h2 className="text-2xl font-black text-slate-800 mb-2">{viewingHistoryDetail.name}</h2>
                   <p className="text-slate-500 font-medium text-sm mb-8">Nộp lúc: {formatDate(viewingHistoryDetail.date)}</p>
                   
                   <div className="flex justify-center gap-6">
                      <div className="bg-blue-50/50 border border-blue-100 px-8 py-5 rounded-3xl">
                         <p className="text-[11px] font-black uppercase text-blue-500 tracking-widest mb-1.5">Thời gian làm</p>
                         <p className="text-2xl font-black text-blue-700">{viewingHistoryDetail.timeSpent} <span className="text-sm font-bold">phút</span></p>
                      </div>
                      <div className="bg-emerald-50/50 border border-emerald-100 px-10 py-5 rounded-3xl">
                         <p className="text-[11px] font-black uppercase text-emerald-500 tracking-widest mb-1.5">Kết quả chung</p>
                         <p className="text-3xl font-black text-emerald-600">
                           {viewingHistoryDetail.details?.bandScore ? `Band ${viewingHistoryDetail.details.bandScore}` : viewingHistoryDetail.scoreObj.display}
                         </p>
                      </div>
                   </div>
                </div>

                <button onClick={() => handleRetakeFromHistory(viewingHistoryDetail)} className="w-full bg-gradient-to-r from-[#0a5482] to-[#1e88e5] hover:from-[#1565c0] hover:to-[#0a5482] text-white font-black py-4 rounded-2xl shadow-lg hover:shadow-xl transition-all active:scale-95 uppercase tracking-widest flex items-center justify-center gap-3 text-[14px]">
                   🔄 Làm lại đề thi này ngay
                </button>
             </div>
          </div>
        </div>
      )}

      {/* POPUP CHỌN HÌNH THỨC THI IELTS */}
      {showModeSelection && testToStart && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-[2rem] w-full max-w-lg shadow-2xl p-10 animate-in zoom-in-95 duration-200">
            <h2 className="text-2xl font-black text-slate-800 mb-2 leading-tight">{testToStart.title}</h2>
            <p className="text-slate-500 font-medium mb-8 text-[15px]">Vui lòng chọn hình thức thi bạn muốn tham gia:</p>
            
            <div className="space-y-4">
              <button onClick={() => handleConfirmMode('computer')} className="w-full flex items-center gap-5 p-6 rounded-3xl border-2 border-slate-100 hover:border-blue-400 hover:bg-blue-50/50 transition-all duration-300 text-left group shadow-sm hover:shadow-md">
                <div className="w-14 h-14 shrink-0 rounded-2xl bg-blue-100 flex items-center justify-center text-3xl group-hover:scale-110 transition-transform duration-300">💻</div>
                <div><h3 className="font-black text-[16px] text-slate-800 group-hover:text-[#1e88e5] transition-colors">Thi trên máy tính</h3><p className="text-[13px] text-slate-500 mt-1 font-medium">Làm bài trực tiếp trên màn hình</p></div>
              </button>
              <button onClick={() => handleConfirmMode('paper')} className="w-full flex items-center gap-5 p-6 rounded-3xl border-2 border-slate-100 hover:border-emerald-400 hover:bg-emerald-50/50 transition-all duration-300 text-left group shadow-sm hover:shadow-md">
                <div className="w-14 h-14 shrink-0 rounded-2xl bg-emerald-100 flex items-center justify-center text-3xl group-hover:scale-110 transition-transform duration-300">📝</div>
                <div><h3 className="font-black text-[16px] text-slate-800 group-hover:text-emerald-600 transition-colors">Thi trên giấy</h3><p className="text-[13px] text-slate-500 mt-1 font-medium">Làm trên giấy, xem đề PDF</p></div>
              </button>
            </div>
            <button onClick={() => setShowModeSelection(false)} className="mt-8 w-full py-4 font-black text-slate-400 hover:text-slate-600 hover:bg-slate-50 rounded-2xl transition-colors">HỦY BỎ</button>
          </div>
        </div>
      )}
    </div>
  );
}