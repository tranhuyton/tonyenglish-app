import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import { LineChart, Line, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const FOLDER_IMAGES = [
  'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1513001900722-370f803f498d?auto=format&fit=crop&q=80&w=800', 
  'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=800',
  'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&q=80&w=800'
];

const ITEMS_PER_PAGE = 16;
const HISTORY_PER_PAGE = 10;

const formatDate = (isoString: string) => {
  if (!isoString) return '';
  const d = new Date(isoString);
  return `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth() + 1).toString().padStart(2, '0')}/${d.getFullYear()} ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
};

const checkTestHasAudio = (test: any) => {
  const content = test.content_json || {};
  if (content?.basicInfo?.audioUrl) return true;
  const parts = Array.isArray(content?.parts) ? content.parts : [];
  for (const p of parts) {
      if (p?.audioUrl) return true;
      const sections = Array.isArray(p?.sections) ? p.sections : [];
      for (const s of sections) {
          if (s?.audioUrl) return true;
          const questions = Array.isArray(s?.questions) ? s.questions : [];
          for (const q of questions) { 
              if (q?.audioUrl) return true; 
          }
      }
  }
  return false;
};

const getTestSkillConfig = (test: any) => {
  const type = String(test.test_type || '').toLowerCase();
  const title = String(test.title || '').toLowerCase();

  if (type.includes('listening') || title.includes('listening')) 
      return { icon: '🎧', bg: 'bg-amber-50', text: 'text-amber-600', border: 'border-amber-200' };
  if (type.includes('speaking') || title.includes('speaking')) 
      return { icon: '🎙️', bg: 'bg-purple-50', text: 'text-purple-600', border: 'border-purple-200' };
  if (type.includes('reading') || title.includes('reading')) 
      return { icon: '📖', bg: 'bg-blue-50', text: 'text-blue-600', border: 'border-blue-200' };
  if (type.includes('writing') || title.includes('writing')) 
      return { icon: '✍️', bg: 'bg-emerald-50', text: 'text-emerald-600', border: 'border-emerald-200' };
  if (type.includes('case-study') || title.includes('case-study')) 
      return { icon: '📊', bg: 'bg-indigo-50', text: 'text-indigo-600', border: 'border-indigo-200' };
      
  return { icon: '📝', bg: 'bg-slate-50', text: 'text-slate-600', border: 'border-slate-200' };
};

const getCourseCover = (course: any) => {
  const t = (course.title || '').toLowerCase();
  if (t.includes('biology')) return { image: 'https://images.unsplash.com/photo-1530026405186-ed1f139313f8?auto=format&fit=crop&q=80&w=800', badge: 'Biology', color: 'text-emerald-600' };
  if (t.includes('chemistry')) return { image: 'https://images.unsplash.com/photo-1603126857599-f6e15782afa5?auto=format&fit=crop&q=80&w=800', badge: 'Chemistry', color: 'text-cyan-600' };
  if (t.includes('physics')) return { image: 'https://images.unsplash.com/photo-1636466497217-26a8cbeaf0aa?auto=format&fit=crop&q=80&w=800', badge: 'Physics', color: 'text-indigo-600' };
  if (t.includes('science')) return { image: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=800', badge: 'Science', color: 'text-teal-600' };
  if (t.includes('math')) return { image: 'https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&q=80&w=800', badge: 'Mathematics', color: 'text-purple-600' };
  if (t.includes('econ')) return { image: 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&q=80&w=800', badge: 'Economics', color: 'text-amber-600' };
  if (t.includes('business')) return { image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800', badge: 'Business', color: 'text-blue-600' };
  if (t.includes('pronunciation') || t.includes('phát âm')) return { image: 'https://images.unsplash.com/photo-1590402494587-44b71d7772f6?auto=format&fit=crop&q=80&w=800', badge: 'Pronunciation', color: 'text-rose-500' };
  if (t.includes('reflex') || t.includes('phản ứng') || t.includes('phản xạ')) return { image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&q=80&w=800', badge: 'Comm. Reflex', color: 'text-orange-500' };
  if (t.includes('communication') || t.includes('giao tiếp')) return { image: 'https://images.unsplash.com/photo-1577563908411-50cb989766a3?auto=format&fit=crop&q=80&w=800', badge: 'Communication', color: 'text-pink-600' };
  if (t.includes('esl') || t.includes('english')) return { image: 'https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&q=80&w=800', badge: 'ESL Program', color: 'text-rose-600' };
  if (t.includes('ielts') || course.type === 'IELTS') return { image: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=800', badge: 'IELTS Mastery', color: 'text-blue-600' };
  return { image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=800', badge: course.type || 'Khóa học', color: 'text-slate-600' };
};

export default function StudentPortal({ onNavigate, onStartTest, onOpenLecture }: any) {
  const [isLoading, setIsLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'library'|'analytics'|'games'|'profile'>(() => {
    const saved = sessionStorage.getItem('lms_portal_tab');
    if (saved === 'library' || saved === 'analytics' || saved === 'games' || saved === 'profile') {
      return saved as 'library'|'analytics'|'games'|'profile';
    }
    return 'library';
  });

  useEffect(() => {
    sessionStorage.setItem('lms_portal_tab', activeTab);
  }, [activeTab]);
  
  const [activeView, setActiveView] = useState<'dashboard'|'course'>(() => {
      return (sessionStorage.getItem('portal_active_view') as any) || 'dashboard';
  });
  const [selectedCourseId, setSelectedCourseId] = useState<string | null>(() => {
      return sessionStorage.getItem('portal_selected_course_id') || null;
  });
  const [currentFolderId, setCurrentFolderId] = useState<string | null>(() => {
      return sessionStorage.getItem('portal_current_folder_id') || null;
  });

  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  const [courses, setCourses] = useState<any[]>([]);
  const [allFolders, setAllFolders] = useState<any[]>([]);
  const [allTests, setAllTests] = useState<any[]>([]);
  const [allLectures, setAllLectures] = useState<any[]>([]);
  const [historyData, setHistoryData] = useState<any[]>([]);
  const [lectureProgressData, setLectureProgressData] = useState<any[]>([]);
  
  const [inProgressIds, setInProgressIds] = useState<Set<string>>(new Set());
  const [currentUser, setCurrentUser] = useState<any>(null);
  const [userProfile, setUserProfile] = useState<any>(null);
  const [userClassIds, setUserClassIds] = useState<string[]>([]);
  
  const [targetIelts, setTargetIelts] = useState<string>('6.5');
  
  const [searchTest, setSearchTest] = useState('');
  const [sortTest, setSortTest] = useState('name-asc');
  const [filterType, setFilterType] = useState('all');
  const [folderPage, setFolderPage] = useState(1);
  const [testPage, setTestPage] = useState(1);
  const [historyPage, setHistoryPage] = useState(1);

  const [analyticsCourse, setAnalyticsCourse] = useState('all');
  const [analyticsCategory, setAnalyticsCategory] = useState('all');
  const [viewingHistoryDetail, setViewingHistoryDetail] = useState<any>(null);
  
  const [showModeSelection, setShowModeSelection] = useState(false);
  const [testToStart, setTestToStart] = useState<any>(null);

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

  useEffect(() => { 
    checkUserAndFetchData(); 
  }, []);

  useEffect(() => {
    const computeInProgress = () => {
      const inProg = new Set<string>();
      try {
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (!key) continue;
          
          let match = key.match(/^(?:ielts_ans_|ielts_paper_ans_|std_ans_|case_study_ans_)(.+)$/);
          if (match) {
              const data = localStorage.getItem(key);
              if (data && Object.keys(JSON.parse(data)).length > 0) {
                  inProg.add(match[1]);
              }
          } else {
              match = key.match(/^(?:ielts_endtime_|standard_endtime_|case_study_endtime_|ielts_paper_endtime_)(.+)$/);
              if (match) {
                 const endTime = parseInt(localStorage.getItem(key) || '0');
                 if (endTime > Date.now()) {
                     inProg.add(match[1]);
                 }
              }
          }
        }
      } catch(e) {}
      setInProgressIds(inProg);
    };
    computeInProgress();
  }, [activeTab, activeView]);

  const checkUserAndFetchData = async () => {
    setIsLoading(true);
    const { data: { user } } = await supabase.auth.getUser();
    setCurrentUser(user);
    
    if (user) {
      const { data: profile } = await supabase.from('profiles').select('*').eq('id', user.id).single();
      setUserProfile(profile);
      if (profile) {
          if (!newFullName) setNewFullName(profile.full_name || '');
          if (profile.target_ielts) setTargetIelts(profile.target_ielts.toString());
      }
      
      const { data: lp } = await supabase.from('lecture_progress').select('lecture_id, is_completed').eq('user_id', user.id);
      setLectureProgressData(lp || []);

      const { data: cStudents } = await supabase.from('class_students').select('class_id').eq('user_id', user.id);
      if (cStudents) {
          setUserClassIds(cStudents.map(c => c.class_id));
      }
    }

    const { data: allT } = await supabase.from('tests').select('*').eq('is_published', true);
    const parsedTests = (allT || []).map((t: any) => {
        let content = t.content_json;
        if (typeof content === 'string') {
            try { content = JSON.parse(content); } catch(e) { content = {}; }
        }
        return { 
            ...t, 
            content_json: content, 
            _hasAudio: checkTestHasAudio({ content_json: content }) 
        };
    });
    setAllTests(parsedTests);

    const { data: allL } = await supabase.from('lectures').select('id, course_id').eq('is_published', true);
    setAllLectures(allL || []);
    
    const { data: allF } = await supabase.from('folders').select('*');
    setAllFolders(allF || []);

    if (user) {
      const { data: enrolls } = await supabase.from('enrollments').select('course_id').eq('user_id', user.id);
      const courseIds = enrolls?.map(e => e.course_id) || [];
      
      if (courseIds.length > 0) {
        const { data: cData } = await supabase.from('courses').select('*').in('id', courseIds);
        setCourses((cData || []).sort((a, b) => (a.order_index ?? 999) - (b.order_index ?? 999)));
      }
      
      const { data: hData } = await supabase.from('test_results').select('*').eq('user_id', user.id).order('created_at', { ascending: false });
      if (hData) {
        
        // 🚀 BỘ LỌC BÀN TAY SẮT: LỌC BỎ CÁC BÀI ĐIỂM QUÁ THẤP (< 3 điểm hoặc < Band 3.0)
        const validHistory = hData.filter((item: any) => {
            const type = String(item.test_type || '').toLowerCase();
            const title = String(item.test_title || '').toLowerCase();
            const isIelts = type.includes('ielts') || title.includes('ielts');
            
            if (isIelts) {
                const band = parseFloat(item.details?.bandScore || item.score || 0);
                return band >= 3.0; // IELTS >= 3.0 mới tính
            } else {
                const score = parseFloat(item.score || 0);
                return score >= 3; // Các bài khác phải đúng >= 3 câu mới tính
            }
        });

        setHistoryData(validHistory.map((item: any) => ({
          id: item.id, 
          testId: item.test_id, 
          name: item.test_title || 'Bài thi không tên', 
          courseId: item.course_id,
          scoreObj: { 
              value: item.score || 0, 
              display: `${item.score || 0} / ${item.total_score || 0}` 
          },
          timeSpent: Math.round((item.time_spent || 0) / 60), 
          date: item.created_at, 
          details: item.details || {}
        })));
      }
    }
    setIsLoading(false);
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
      alert("Cập nhật tài khoản thành công!");
    } catch (error: any) { 
        alert("Lỗi cập nhật: " + error.message); 
    } finally { 
        setIsUpdatingProfile(false); 
    }
  };

  const handleUpdateTarget = async (newVal: string) => {
      setTargetIelts(newVal);
      if (currentUser?.id) {
          await supabase.from('profiles').update({ target_ielts: newVal }).eq('id', currentUser.id);
      }
  };

  const handleLogout = async () => {
    await supabase.auth.signOut();
    localStorage.clear(); 
    sessionStorage.clear(); 
    window.dispatchEvent(new CustomEvent('tony-clear-chat'));
    window.dispatchEvent(new CustomEvent('tony-close-sidebar'));
    onNavigate?.('home'); 
    setTimeout(() => window.location.reload(), 100);
  };

  const resetWorkspaceAndChat = () => {
      window.dispatchEvent(new CustomEvent('tony-clear-chat'));
      window.dispatchEvent(new CustomEvent('tony-close-sidebar'));
  };

  const handleOpenCourse = (course: any) => {
    resetWorkspaceAndChat();
    setSelectedCourseId(String(course.id)); 
    setCurrentFolderId(null); 
    setSearchTest(''); 
    setFolderPage(1); 
    setTestPage(1);
    setActiveView('course');
    sessionStorage.setItem('portal_selected_course_id', String(course.id));
    sessionStorage.setItem('portal_active_view', 'course');
    sessionStorage.removeItem('portal_current_folder_id');
  };

  const handleFolderClick = (id: string) => { 
      setCurrentFolderId(id); 
      setFolderPage(1); 
      setTestPage(1); 
      sessionStorage.setItem('portal_current_folder_id', id);
  };

  const handleStartTestClick = (test: any) => {
    if (!onStartTest) return;
    
    const category = test.content_json?.basicInfo?.category;
    if (category === 'game') {
      const theme = test.content_json?.basicInfo?.gameTheme || 'siege-game';
      onStartTest(theme, test);
      return; 
    }
    
    const type = String(test.test_type || '').toLowerCase();
    if (type.includes('standard')) onStartTest('standard', test);
    else if (type.includes('case-study') || type.includes('business')) onStartTest('case-study', test);
    else if (type === 'ielts-writing') onStartTest('ielts-writing', test);
    else if (type === 'ielts-speaking') onStartTest('ielts-speaking', test);
    else if (type.includes('ielts')) { 
      setTestToStart(test); 
      setShowModeSelection(true); 
    } else {
        onStartTest('standard', test);
    }
  };

  const handleConfirmMode = (mode: 'computer' | 'paper') => { 
    setShowModeSelection(false); 
    if (onStartTest && testToStart) {
        onStartTest(mode, testToStart); 
    }
  };

  const handleRetakeFromHistory = (historyItem: any) => {
    const testId = historyItem.testId || historyItem.details?.test_id;
    let foundTest = allTests.find(t => String(t.id) === String(testId));
    if (!foundTest) foundTest = allTests.find(t => t.title.trim() === historyItem.name.trim());
    
    if (foundTest) { 
        setViewingHistoryDetail(null); 
        handleStartTestClick(foundTest); 
    } else {
        alert("Đề thi này không còn tồn tại hoặc đã bị ẩn khỏi hệ thống.");
    }
  };

  const toggleFullScreen = () => { 
    if (!document.fullscreenElement) { 
        document.documentElement.requestFullscreen().catch(); 
    } else { 
        if (document.exitFullscreen) document.exitFullscreen(); 
    } 
  };

  const nameParts = (userProfile?.full_name || currentUser?.email?.split('@')[0] || 'User').trim().split(/\s+/);
  const displayUserName = nameParts[nameParts.length - 1]; 
  const displayUserInitial = displayUserName.charAt(0).toUpperCase();

  const selectedCourse = useMemo(() => courses.find(c => String(c.id) === selectedCourseId) || null, [courses, selectedCourseId]);
  
  const courseFolders = useMemo(() => {
      if (!selectedCourse) return [];
      return allFolders.filter(f => f.course_id === selectedCourse.id).sort((a,b) => (a.display_order||0) - (b.display_order||0));
  }, [selectedCourse, allFolders]);

  const courseTests = useMemo(() => {
      if (!selectedCourse) return [];
      return allTests.filter(t => courseFolders.some(f => f.id === t.folder_id) || t.content_json?.basicInfo?.courseId === selectedCourse.id);
  }, [selectedCourse, allTests, courseFolders]);

  const currentSubFolders = useMemo(() => {
      return courseFolders.filter(f => currentFolderId ? f.parent_id === currentFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')).sort((a,b) => (a.display_order||0) - (b.display_order||0));
  }, [courseFolders, currentFolderId]);

  const currentTests = useMemo(() => {
      if (currentFolderId) return courseTests.filter(t => t.folder_id === currentFolderId);
      if (currentSubFolders.length === 0) return courseTests.filter(t => !t.folder_id || t.folder_id === 'null' || t.folder_id === '');
      return [];
  }, [courseTests, currentFolderId, currentSubFolders.length]);

  const processedTests = useMemo(() => {
      return currentTests.filter(t => (t.title || '').toLowerCase().includes(searchTest.toLowerCase()))
                         .filter(t => filterType === 'all' || t.content_json?.basicInfo?.category === filterType)
                         .sort((a, b) => {
                             if (sortTest === 'name-asc') return (a.title || '').localeCompare(b.title || '');
                             if (sortTest === 'name-desc') return (b.title || '').localeCompare(a.title || '');
                             if (sortTest === 'date-desc') return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime();
                             return new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime();
                         });
  }, [currentTests, searchTest, filterType, sortTest]);

  const upcomingDeadlines = useMemo(() => {
    const enrolledCourseIds = courses.map(c => c.id);
    const validTests = allTests.filter(t => t.course_id && enrolledCourseIds.includes(t.course_id) || enrolledCourseIds.includes(t.content_json?.basicInfo?.courseId));
    
    return validTests.filter(t => {
        const classDeadlines = t.content_json?.basicInfo?.classDeadlines || {};
        const matchedClassId = userClassIds.find(id => classDeadlines[id]);
        
        if (!matchedClassId) return false;
        
        const isCompleted = historyData.some(h => String(h.testId) === String(t.id) || String(h.details?.test_id) === String(t.id));
        if (isCompleted) return false;
        
        t._deadlineStr = classDeadlines[matchedClassId];
        return true; 
    }).sort((a, b) => new Date(a._deadlineStr).getTime() - new Date(b._deadlineStr).getTime());
  }, [allTests, courses, historyData, userClassIds]);

  const totalFolderPages = Math.ceil(currentSubFolders.length / ITEMS_PER_PAGE);
  const paginatedFolders = useMemo(() => currentSubFolders.slice((folderPage - 1) * ITEMS_PER_PAGE, folderPage * ITEMS_PER_PAGE), [currentSubFolders, folderPage]);
  
  const totalTestPages = Math.ceil(processedTests.length / ITEMS_PER_PAGE);
  const paginatedTests = useMemo(() => processedTests.slice((testPage - 1) * ITEMS_PER_PAGE, testPage * ITEMS_PER_PAGE), [processedTests, testPage]);

  // CHUẨN BỊ DỮ LIỆU BÁO CÁO TỪ HISTORY ĐÃ LỌC CÁC BÀI ĐIỂM < 3
  const processedHistory = useMemo(() => {
      return historyData.filter(h => analyticsCourse === 'all' || String(h.courseId) === String(analyticsCourse)).filter(h => {
         if (analyticsCategory === 'all') return true;
         const ft = allTests.find(t => String(t.id) === String(h.testId));
         return (ft?.content_json?.basicInfo?.category || 'test') === analyticsCategory;
      }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }, [historyData, analyticsCourse, analyticsCategory, allTests]);

  // 🚀 TÍNH TOÁN DỮ LIỆU CHO 4 AREA CHART TỔNG QUAN THEO NGÀY (CÓ XỬ LÝ GÃY KHÚC BIỂU ĐỒ TRỐNG)
  const aggregatedByDate = useMemo(() => {
      const map = new Map();
      const reversed = [...processedHistory].reverse(); 
      
      reversed.forEach(h => {
          const d = new Date(h.date);
          const dateStr = `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth()+1).toString().padStart(2, '0')}`;
          
          if (!map.has(dateStr)) {
              map.set(dateStr, { name: dateStr, stdScoreSum: 0, stdCount: 0, timeSum: 0, bandSum: 0, bandCount: 0, totalAttempts: 0 });
          }
          const entry = map.get(dateStr);
          entry.totalAttempts += 1;
          entry.timeSum += h.timeSpent;
          
          const type = String(h.details?.test_type || h.name).toLowerCase();
          const isIelts = type.includes('ielts');
          
          if (isIelts) {
              const band = parseFloat(h.details?.bandScore);
              if (!isNaN(band) && band > 0) {
                  entry.bandSum += band;
                  entry.bandCount += 1;
              }
          } else {
              entry.stdScoreSum += (h.scoreObj.value || 0);
              entry.stdCount += 1;
          }
      });
      
      let cumulativeDone = 0;

      return Array.from(map.values()).map(entry => {
          cumulativeDone += entry.totalAttempts;
          return {
              name: entry.name,
              attempts: entry.totalAttempts,
              cumulativeDone: cumulativeDone,
              time: parseFloat((entry.timeSum / 60).toFixed(1)), 
              avgScore: entry.stdCount > 0 ? parseFloat((entry.stdScoreSum / entry.stdCount).toFixed(1)) : null,
              avgBand: entry.bandCount > 0 ? parseFloat((entry.bandSum / entry.bandCount).toFixed(1)) : null
          };
      }).slice(-14); 
  }, [processedHistory]);

  const isIeltsContext = analyticsCourse === 'all' 
      ? courses.some(c => (c.title||'').toLowerCase().includes('ielts') || c.type === 'IELTS')
      : courses.find(c => String(c.id) === String(analyticsCourse))?.title.toLowerCase().includes('ielts');

  const { analyticsTotalTestsDone, analyticsTotalTimeHours, avgScore, avgIelts } = useMemo(() => {
      const total = processedHistory.length;
      const hours = (processedHistory.reduce((acc, curr) => acc + curr.timeSpent, 0) / 60).toFixed(1);
      
      let stdSum = 0, stdCount = 0;
      let bandSum = 0, bandCount = 0;

      processedHistory.forEach(h => {
          const type = String(h.details?.test_type || h.name).toLowerCase();
          const isIeltsTest = type.includes('ielts');
          
          if (isIeltsTest) {
              const band = parseFloat(h.details?.bandScore);
              if (!isNaN(band) && band > 0) {
                  bandSum += band;
                  bandCount++;
              }
          } else {
              stdSum += (h.scoreObj.value || 0);
              stdCount++;
          }
      });

      const score = stdCount > 0 ? (stdSum / stdCount).toFixed(1) : '0';
      const ielts = bandCount > 0 ? (bandSum / bandCount).toFixed(1) : '0.0';
      
      return { analyticsTotalTestsDone: total, analyticsTotalTimeHours: hours, avgScore: score, avgIelts: ielts };
  }, [processedHistory, historyData]);

  // 🚀 TÍNH TOÁN DỮ LIỆU CHO LINE CHART: 4 KỸ NĂNG IELTS
  const ieltsSkillChartData = useMemo(() => {
      const map = new Map();
      const reversed = [...processedHistory].reverse();
      
      reversed.forEach(h => {
          const d = new Date(h.date);
          const dateStr = `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth()+1).toString().padStart(2, '0')}`;
          
          if (!map.has(dateStr)) {
              map.set(dateStr, { name: dateStr, Nghe: [], Nói: [], Đọc: [], Viết: [] });
          }
          const entry = map.get(dateStr);
          
          const type = String(h.details?.test_type || h.name).toLowerCase();
          const band = parseFloat(h.details?.bandScore);
          
          if (!isNaN(band) && band > 0) {
              if (type.includes('listen')) entry.Nghe.push(band);
              else if (type.includes('speak')) entry.Nói.push(band);
              else if (type.includes('read')) entry.Đọc.push(band);
              else if (type.includes('writ')) entry.Viết.push(band);
          }
      });
      
      return Array.from(map.values()).map(entry => ({
          name: entry.name,
          Nghe: entry.Nghe.length > 0 ? parseFloat((entry.Nghe.reduce((a:any,b:any)=>a+b,0)/entry.Nghe.length).toFixed(1)) : null,
          Nói: entry.Nói.length > 0 ? parseFloat((entry.Nói.reduce((a:any,b:any)=>a+b,0)/entry.Nói.length).toFixed(1)) : null,
          Đọc: entry.Đọc.length > 0 ? parseFloat((entry.Đọc.reduce((a:any,b:any)=>a+b,0)/entry.Đọc.length).toFixed(1)) : null,
          Viết: entry.Viết.length > 0 ? parseFloat((entry.Viết.reduce((a:any,b:any)=>a+b,0)/entry.Viết.length).toFixed(1)) : null,
      })).slice(-14);
  }, [processedHistory]);

  // 🚀 TÍNH TOÁN DỮ LIỆU CHO LINE CHART: TỶ LỆ THEO TỪNG DẠNG BÀI THEO NGÀY
  const ieltsTypeChartData = useMemo(() => {
      const map = new Map();
      const reversed = [...processedHistory].reverse();
      
      reversed.forEach(h => {
          const d = new Date(h.date);
          const dateStr = `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth()+1).toString().padStart(2, '0')}`;
          
          if (!map.has(dateStr)) {
              map.set(dateStr, { name: dateStr, fill: {c:0,t:0}, tfng: {c:0,t:0}, mcq: {c:0,t:0}, match: {c:0,t:0} });
          }
          const entry = map.get(dateStr);
          const types = h.details?.type_stats || h.details?.questionTypeStats || h.details?.typeStats || {};
          
          Object.keys(types).forEach(k => {
              const kLow = k.toLowerCase();
              const c = types[k].correct || 0;
              const t = types[k].total || 0;
              
              if (t > 0) {
                  if (kLow.includes('điền từ') || kLow.includes('fill') || kLow.includes('completion') || kLow.includes('blank')) {
                      entry.fill.c += c; entry.fill.t += t;
                  } else if (kLow.includes('tfng') || kLow.includes('true') || kLow.includes('false') || kLow.includes('yes') || kLow.includes('ng') || kLow.includes('nhận định')) {
                      entry.tfng.c += c; entry.tfng.t += t;
                  } else if (kLow.includes('trắc nghiệm') || kLow.includes('multiple') || kLow.includes('choice') || kLow.includes('checkbox') || kLow.includes('combo') || kLow.includes('mcq')) {
                      entry.mcq.c += c; entry.mcq.t += t;
                  } else if (kLow.includes('kéo thả') || kLow.includes('matching') || kLow.includes('droplist') || kLow.includes('nối') || kLow.includes('drag')) {
                      entry.match.c += c; entry.match.t += t;
                  }
              }
          });
      });
      
      return Array.from(map.values()).map(entry => ({
          name: entry.name,
          "Điền từ": entry.fill.t > 0 ? Math.round((entry.fill.c / entry.fill.t)*100) : null,
          "Nhận định": entry.tfng.t > 0 ? Math.round((entry.tfng.c / entry.tfng.t)*100) : null,
          "Trắc nghiệm": entry.mcq.t > 0 ? Math.round((entry.mcq.c / entry.mcq.t)*100) : null,
          "Matching": entry.match.t > 0 ? Math.round((entry.match.c / entry.match.t)*100) : null,
      })).filter(e => e["Điền từ"] !== null || e["Nhận định"] !== null || e["Trắc nghiệm"] !== null || e["Matching"] !== null).slice(-14);
  }, [processedHistory]);

  // 🚀 TÍNH DỮ LIỆU THANH PROGRESS CHO TỶ LỆ DẠNG BÀI
  const ieltsTypeStats = useMemo(() => {
      const stats: Record<string, {correct: number, total: number}> = {
          'Điền từ (Completion)': { correct: 0, total: 0 },
          'T/F/NG (Nhận định)': { correct: 0, total: 0 },
          'Trắc nghiệm (MCQ)': { correct: 0, total: 0 },
          'Matching (Nối đáp án)': { correct: 0, total: 0 }
      };
      
      processedHistory.forEach(h => {
          const types = h.details?.type_stats || h.details?.questionTypeStats || h.details?.typeStats || {};
          Object.keys(types).forEach(k => {
              const kLow = k.toLowerCase();
              let mappedKey = '';
              
              if (kLow.includes('điền từ') || kLow.includes('fill') || kLow.includes('completion') || kLow.includes('blank')) {
                  mappedKey = 'Điền từ (Completion)';
              } else if (kLow.includes('tfng') || kLow.includes('true') || kLow.includes('false') || kLow.includes('yes') || kLow.includes('ng') || kLow.includes('nhận định')) {
                  mappedKey = 'T/F/NG (Nhận định)';
              } else if (kLow.includes('trắc nghiệm') || kLow.includes('multiple') || kLow.includes('choice') || kLow.includes('checkbox') || kLow.includes('combo') || kLow.includes('mcq')) {
                  mappedKey = 'Trắc nghiệm (MCQ)';
              } else if (kLow.includes('kéo thả') || kLow.includes('matching') || kLow.includes('droplist') || kLow.includes('nối') || kLow.includes('drag')) {
                  mappedKey = 'Matching (Nối đáp án)';
              }
              
              if (mappedKey && stats[mappedKey]) {
                  stats[mappedKey].correct += (types[k].correct || 0);
                  stats[mappedKey].total += (types[k].total || 0);
              }
          });
      });
      return stats;
  }, [processedHistory]);

  const totalHistoryPages = Math.ceil(processedHistory.length / HISTORY_PER_PAGE);
  const paginatedHistory = useMemo(() => processedHistory.slice((historyPage - 1) * HISTORY_PER_PAGE, historyPage * HISTORY_PER_PAGE), [processedHistory, historyPage]);

  const globalTotalTestsDone = historyData.length;
  const globalTotalTimeHours = useMemo(() => (historyData.reduce((acc, curr) => acc + curr.timeSpent, 0) / 60).toFixed(1), [historyData]);
  
  const inProgressTestId = Array.from(inProgressIds)[0];
  const inProgressTest = useMemo(() => allTests.find(t => String(t.id) === inProgressTestId), [allTests, inProgressTestId]);

  const hour = new Date().getHours();
  let bannerConfig = { greeting: '', gradient: '', icon: '', subtitle: '' };
  
  if (hour >= 5 && hour < 12) {
      bannerConfig = { greeting: 'Chào buổi sáng', gradient: 'from-[#0f172a] to-[#334155]', icon: '🌅', subtitle: 'Bắt đầu ngày mới tràn đầy năng lượng! Một chút nỗ lực hôm nay sẽ mang lại kết quả lớn ngày mai.' };
  } else if (hour >= 12 && hour < 18) {
      bannerConfig = { greeting: 'Chào buổi chiều', gradient: 'from-[#0a5482] to-[#1e88e5]', icon: '🌤️', subtitle: 'Tiếp tục hành trình chinh phục mục tiêu nào! Giữ vững sự tập trung nhé.' };
  } else {
      bannerConfig = { greeting: 'Chào buổi tối', gradient: 'from-slate-800 to-[#1e1b4b]', icon: '🌙', subtitle: 'Thời gian tĩnh lặng tuyệt vời để tập trung ôn tập và nhìn lại những gì đã học.' };
  }

  const breadcrumbs = useMemo(() => {
      const b: any[] = [];
      let curr = courseFolders.find(f => f.id === currentFolderId);
      while (curr) { 
          b.unshift(curr); 
          curr = courseFolders.find(f => f.id === curr.parent_id); 
      }
      return b;
  }, [currentFolderId, courseFolders]);

  const renderPagination = (currentPage: number, totalPages: number, setPage: (p: number) => void) => {
    if (totalPages <= 1) return null;
    return (
      <div className="flex justify-center items-center gap-4 mt-8">
        <button disabled={currentPage === 1} onClick={() => setPage(currentPage - 1)} className="w-10 h-10 rounded-xl flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:border-[#1e88e5] hover:text-[#1e88e5] transition-colors disabled:opacity-40 shadow-sm font-black">←</button>
        <span className="text-[13px] font-bold text-slate-500 bg-white px-5 py-2.5 rounded-xl border border-slate-200 shadow-sm">Trang {currentPage} / {totalPages}</span>
        <button disabled={currentPage === totalPages} onClick={() => setPage(currentPage + 1)} className="w-10 h-10 rounded-xl flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:border-[#1e88e5] hover:text-[#1e88e5] transition-colors disabled:opacity-40 shadow-sm font-black">→</button>
      </div>
    );
  };

  return (
    <div className="min-h-[100dvh] bg-[#f8fafc] font-sans text-slate-800 overscroll-none w-full">
      <header className="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-sm">
        <div className="max-w-[1200px] w-full mx-auto px-4 md:px-6 py-3 flex items-center justify-between">
          
          <div className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity" onClick={() => {
              resetWorkspaceAndChat(); 
              onNavigate?.('home');
          }}>
            <div className="flex flex-col items-end">
              <h1 className="font-black text-2xl text-[#0a5482] leading-none">TONY<span className="text-slate-800">ENGLISH</span></h1>
            </div>
            <div className="w-10 h-10 flex items-center justify-center overflow-hidden">
                <img src="/logo-shield.png" alt="Logo" className="w-auto h-full object-contain" />
            </div>
          </div>

          <div className="hidden md:flex items-center gap-2 bg-slate-50 rounded-xl p-1 border border-slate-200">
            <button 
                onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('library'); 
                    setActiveView('dashboard'); 
                    setSelectedCourseId(null); 
                    setCurrentFolderId(null);
                }} 
                className={`px-6 py-2 rounded-lg font-bold text-[13px] transition-colors duration-200 ${activeTab === 'library' ? 'bg-white shadow-sm text-[#1e88e5] border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'}`}
            >
                📚 Không gian học tập
            </button>
            <button 
                onClick={() => {
                    resetWorkspaceAndChat(); 
                    setActiveTab('analytics');
                }} 
                className={`px-6 py-2 rounded-lg font-bold text-[13px] transition-colors duration-200 ${activeTab === 'analytics' ? 'bg-white shadow-sm text-[#1e88e5] border border-slate-200' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'}`}
            >
                📊 Báo cáo
            </button>
            <button 
                onClick={() => {
                    resetWorkspaceAndChat(); 
                    setActiveTab('games');
                }} 
                className={`px-6 py-2 rounded-lg font-bold text-[13px] transition-colors duration-200 ${activeTab === 'games' ? 'bg-white shadow-sm text-amber-600 border border-slate-200' : 'text-slate-500 hover:text-amber-600 hover:bg-slate-200/50'}`}
            >
                🎮 Mini Games
            </button>
          </div>

          <div className="flex items-center gap-3 md:gap-5">
            <div className="hidden lg:flex items-center gap-3">
               <div className="flex items-center gap-1.5 bg-white text-slate-700 px-3 py-1.5 rounded-lg border border-slate-200 font-bold text-[12px] shadow-sm uppercase tracking-wide">
                   🔥 {globalTotalTestsDone} Bài
               </div>
               <div className="flex items-center gap-1.5 bg-white text-slate-700 px-3 py-1.5 rounded-lg border border-slate-200 font-bold text-[12px] shadow-sm uppercase tracking-wide">
                   ⏱️ {globalTotalTimeHours}h
               </div>
               <div className="h-6 w-px bg-slate-200 mx-1"></div>
               <button onClick={toggleFullScreen} className="w-9 h-9 rounded-lg flex items-center justify-center text-slate-500 hover:bg-slate-100 border border-transparent hover:border-slate-200 hover:text-[#1e88e5] transition-colors">
                 {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>}
               </button>
            </div>

            <div className="relative" ref={dropdownRef}>
               <button onClick={() => setIsDropdownOpen(!isDropdownOpen)} className="flex items-center gap-3 bg-white pr-2 pl-4 py-1.5 rounded-full border border-slate-200 shadow-sm hover:border-[#1e88e5] transition-colors focus:outline-none">
                 <div className="text-right hidden sm:block">
                   <div className="font-black text-[13px] text-slate-800">{displayUserName}</div>
                   <div className="text-[10px] font-medium text-slate-500 uppercase tracking-wider">
                       {userProfile?.role === 'admin' ? 'Quản trị' : 'Học viên'}
                   </div>
                 </div>
                 <div className="w-9 h-9 rounded-full bg-[#1e88e5] text-white flex items-center justify-center font-black shadow-inner text-[13px]">
                     {displayUserInitial}
                 </div>
               </button>

               {isDropdownOpen && (
                  <div className="absolute right-0 mt-3 w-56 bg-white rounded-xl shadow-xl border border-slate-200 py-2 z-50 animate-in fade-in zoom-in-95 duration-200">
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('library'); 
                         setActiveView('dashboard'); 
                         setSelectedCourseId(null); 
                         setCurrentFolderId(null); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-bold text-slate-700 hover:bg-slate-50">
                         📚 Học tập
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('analytics'); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-bold text-slate-700 hover:bg-slate-50">
                         📊 Báo cáo
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('games'); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-bold text-amber-600 hover:bg-amber-50">
                         🎮 Mini Games
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('profile'); 
                         setIsDropdownOpen(false); 
                     }} className="w-full text-left px-5 py-3 text-sm font-bold text-slate-700 hover:bg-slate-50 hover:text-[#1e88e5] transition-colors">
                         👤 Cấu hình tài khoản
                     </button>
                     {userProfile?.role === 'admin' && (
                         <button onClick={() => {
                             resetWorkspaceAndChat();
                             if(onNavigate) onNavigate('admin');
                         }} className="w-full text-left px-5 py-3 text-sm font-black text-[#8b5cf6] hover:bg-purple-50 transition-colors">
                             ⚙️ Trang Quản Trị
                         </button>
                     )}
                     <div className="h-px bg-slate-100 my-1"></div>
                     <button onClick={handleLogout} className="w-full text-left px-5 py-3 text-sm font-bold text-red-600 hover:bg-red-50 transition-colors">
                         🚪 Đăng xuất
                     </button>
                  </div>
               )}
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-[1200px] w-full mx-auto p-4 md:p-8">
        
        {activeTab === 'library' && activeView === 'dashboard' && (
          <div className="animate-in fade-in duration-300">
            <div className={`relative bg-gradient-to-r ${bannerConfig.gradient} rounded-2xl p-6 md:p-10 mb-8 md:mb-10 overflow-hidden shadow-md`}>
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,255,255,0.1),transparent_50%)] pointer-events-none"></div>
              
              <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6 md:gap-10">
                <div className="text-white flex-1 text-center md:text-left">
                  <h2 className="text-2xl md:text-3xl lg:text-4xl font-black mb-2 md:mb-3 drop-shadow-sm">
                      {bannerConfig.greeting}, {displayUserName}! {bannerConfig.icon}
                  </h2>
                  <p className="text-white/80 text-[14px] md:text-[16px] lg:text-lg font-medium leading-relaxed max-w-xl">
                      {bannerConfig.subtitle}
                  </p>
                </div>

                {inProgressTest ? (
                   <div className="bg-black/20 border border-white/10 p-5 md:p-6 rounded-xl w-full md:w-80 shadow-sm text-white hover:bg-black/30 transition-colors cursor-pointer" onClick={() => handleStartTestClick(inProgressTest)}>
                      <div className="flex items-center gap-2 mb-3">
                         <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                         <span className="text-[11px] font-black uppercase tracking-widest text-amber-300">Đang làm dở</span>
                      </div>
                      <h3 className="font-bold text-base md:text-lg mb-4 line-clamp-2 leading-tight">{inProgressTest.title}</h3>
                      <button className="w-full bg-white text-slate-800 hover:bg-slate-100 font-black py-2.5 rounded-lg text-[13px] transition-colors uppercase tracking-wide">
                         Tiếp tục ngay
                      </button>
                   </div>
                ) : courses.length > 0 && (
                  <div className="bg-black/20 border border-white/10 p-5 md:p-6 rounded-xl w-full md:w-80 shadow-sm text-white hover:bg-black/30 transition-colors cursor-pointer" onClick={() => {
                      resetWorkspaceAndChat(); 
                      if(onOpenLecture) onOpenLecture(courses[0].id);
                  }}>
                    <div className="flex items-center gap-2 mb-3">
                       <span className="text-[11px] font-black uppercase tracking-widest text-white/70">Gợi ý học tập</span>
                    </div>
                    <h3 className="font-bold text-base md:text-lg mb-4 line-clamp-2 leading-tight">Khóa học {courses[0].title}</h3>
                    <button className="w-full bg-white text-slate-800 hover:bg-slate-100 font-black py-2.5 rounded-lg text-[13px] transition-colors uppercase tracking-wide">
                        Vào học ngay
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* BẢNG CẢNH BÁO DEADLINE */}
            {upcomingDeadlines.length > 0 && (
                <div className="bg-orange-50 border border-orange-200 rounded-2xl p-5 md:p-6 mb-8 md:mb-10 shadow-sm flex items-start gap-4 animate-in slide-in-from-top-4">
                    <div className="text-3xl md:text-4xl animate-bounce">⏰</div>
                    <div className="flex-1 min-w-0">
                        <h3 className="font-black text-orange-800 text-[15px] md:text-lg mb-2 uppercase tracking-tight">Nhiệm vụ cần hoàn thành ({upcomingDeadlines.length})</h3>
                        <div className="flex flex-col gap-2">
                            {upcomingDeadlines.slice(0, 3).map(t => {
                                const dDate = new Date(t._deadlineStr);
                                const isOverdue = dDate < new Date();
                                return (
                                    <div key={t.id} onClick={() => handleStartTestClick(t)} className="flex justify-between items-center bg-white p-3 rounded-xl border border-orange-100 hover:border-orange-300 cursor-pointer transition-colors shadow-sm group">
                                        <span className="font-bold text-slate-700 text-[13px] md:text-sm truncate pr-2 group-hover:text-orange-700">{t.title}</span>
                                        <span className={`text-[10px] md:text-xs font-black px-2.5 py-1 rounded-md whitespace-nowrap border ${isOverdue ? 'bg-red-50 text-red-600 border-red-200' : 'bg-orange-50 text-orange-600 border-orange-200'}`}>
                                            {isOverdue ? '⚠️ QUÁ HẠN' : '⏳ ' + formatDate(t._deadlineStr)}
                                        </span>
                                    </div>
                                )
                            })}
                            {upcomingDeadlines.length > 3 && (
                                <div className="text-[12px] font-bold text-orange-600 pl-1 mt-1">+ {upcomingDeadlines.length - 3} bài tập khác...</div>
                            )}
                        </div>
                    </div>
                </div>
            )}

            <h2 className="font-black text-2xl text-slate-800 mb-6 px-2">Khóa học của tôi</h2>
            
            {isLoading ? (
              <div className="flex flex-col gap-6">
                 {[1,2].map(i => (
                   <div key={i} className="bg-white rounded-xl h-[180px] w-full border border-slate-200 flex p-6 animate-pulse">
                      <div className="w-[300px] h-full bg-slate-100 rounded-lg"></div>
                      <div className="flex-1 px-8 py-2 flex flex-col justify-between">
                          <div className="h-6 w-1/2 bg-slate-100 rounded-md"></div>
                          <div className="h-4 w-1/3 bg-slate-100 rounded-md mt-4"></div>
                          <div className="mt-auto h-2 w-full bg-slate-100 rounded-full"></div>
                      </div>
                   </div>
                 ))}
              </div>
            ) : courses.length === 0 ? (
              <div className="bg-white border border-slate-200 rounded-xl py-24 text-center shadow-sm mx-2">
                <span className="text-4xl block mb-4 opacity-30 grayscale">🔒</span>
                <h3 className="font-bold text-slate-700 text-lg mb-2">Chưa có khóa học nào</h3>
                <p className="text-slate-500 text-sm">Vui lòng liên hệ TonyEnglish để được cấp quyền truy cập nhé!</p>
              </div>
            ) : (
              <div className="flex flex-col gap-6">
                {courses.map(course => {
                  const cover = getCourseCover(course);
                  
                  const courseFolderIds = allFolders.filter(f => f.course_id === course.id).map(f => f.id);
                  const courseTestsForCount = allTests.filter(t => 
                      courseFolderIds.includes(t.folder_id) || 
                      t.course_id === course.id || 
                      t.content_json?.basicInfo?.courseId === course.id
                  );
                  const testCount = courseTestsForCount.length;
                  const validTestIds = courseTestsForCount.map(t => String(t.id));

                  const uniqueCompletedTests = new Set(
                      historyData
                      .filter(h => validTestIds.includes(String(h.testId)) || validTestIds.includes(String(h.details?.test_id)))
                      .map(h => String(h.testId || h.details?.test_id))
                  ).size;
                  const testProgress = testCount > 0 ? Math.min(100, Math.round((uniqueCompletedTests / testCount) * 100)) : 0;

                  const courseLectures = allLectures.filter(l => l.course_id === course.id);
                  const lectureCount = courseLectures.length;
                  const courseLectureIds = courseLectures.map(l => l.id);
                  const completedLecs = lectureProgressData.filter(lp => lp.is_completed && courseLectureIds.includes(lp.lecture_id)).length;
                  const lecProgress = lectureCount > 0 ? Math.min(100, Math.round((completedLecs / lectureCount) * 100)) : 0;

                  return (
                    <div key={course.id} className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm hover:border-[#1e88e5] transition-colors flex flex-col md:flex-row mx-2 md:mx-0 group">
                      <div className="w-full md:w-[320px] h-[180px] shrink-0 bg-slate-50 p-4 border-r border-slate-100">
                         <div className="w-full h-full rounded-lg overflow-hidden relative border border-slate-200 shadow-sm bg-black">
                           <img src={cover.image} loading="lazy" alt={course.title} className="w-full h-full object-cover group-hover:opacity-85 transition-opacity duration-300" />
                           <div className={`absolute top-2 left-2 bg-white px-3 py-1.5 rounded text-[10px] font-black uppercase tracking-widest ${cover.color} shadow-sm border border-slate-100`}>
                               {cover.badge}
                           </div>
                         </div>
                      </div>
                      <div className="flex-1 p-6 lg:p-8 flex flex-col justify-center border-r border-slate-100">
                        <h4 className="font-black text-xl text-slate-800 mb-3 group-hover:text-[#1e88e5] transition-colors">{course.title}</h4>
                        <div className="flex items-center gap-4 mb-6 text-[13px] font-bold text-slate-500">
                          <span className="flex items-center gap-1.5"><span className="text-emerald-500 text-lg">📚</span> {lectureCount} Bài giảng</span>
                          <span className="flex items-center gap-1.5"><span className="text-blue-500 text-lg">📝</span> {testCount} Đề & Bài tập</span>
                        </div>
                        <div className="w-full mt-auto flex gap-6">
                          <div className="flex-1">
                              <div className="flex justify-between mb-2">
                                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ bài giảng</span>
                                  <span className="text-[12px] font-black text-emerald-600">{lecProgress}%</span>
                              </div>
                              <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden border border-slate-200/50">
                                  <div className="h-full bg-emerald-500 rounded-full" style={{ width: `${lecProgress}%` }}></div>
                              </div>
                          </div>
                          <div className="flex-1">
                              <div className="flex justify-between mb-2">
                                  <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ làm bài</span>
                                  <span className="text-[12px] font-black text-blue-600">{testProgress}%</span>
                              </div>
                              <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden border border-slate-200/50">
                                  <div className="h-full bg-blue-500 rounded-full" style={{ width: `${testProgress}%` }}></div>
                              </div>
                          </div>
                        </div>
                      </div>
                      <div className="w-full md:w-[260px] p-6 flex flex-col justify-center gap-3 bg-slate-50/50 shrink-0">
                         <button onClick={() => {
                             resetWorkspaceAndChat(); 
                             if(onOpenLecture) onOpenLecture(course.id);
                         }} className="w-full bg-white border border-emerald-200 hover:border-emerald-500 hover:bg-emerald-50 text-emerald-600 font-bold text-[12px] py-3 rounded-lg transition-colors flex items-center justify-center gap-2 shadow-sm uppercase tracking-wide">
                             📖 Bài giảng
                         </button>
                         <button onClick={() => handleOpenCourse(course)} className="w-full bg-[#1e88e5] hover:bg-[#1565c0] text-white font-bold text-[12px] py-3 rounded-lg transition-colors shadow-sm flex items-center justify-center gap-2 uppercase tracking-wide">
                             📝 Đề & Bài tập
                         </button>
                      </div>
                    </div>
                  )
                })}
              </div>
            )}
          </div>
        )}

        {activeTab === 'library' && activeView === 'course' && selectedCourse && (
          <div className="animate-in fade-in slide-in-from-right-4 duration-300">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6 bg-white p-3 md:p-4 rounded-xl border border-slate-200 shadow-sm mx-2 md:mx-0">
                <div className="flex flex-wrap items-center gap-2 text-[13px] md:text-[14px] font-bold text-slate-500">
                    <button onClick={() => { setActiveView('dashboard'); setSelectedCourseId(null); }} className="hover:text-[#1e88e5] transition-colors">
                        Khóa học
                    </button>
                    <span className="text-slate-300">/</span>
                    <button onClick={() => { setCurrentFolderId(null); setFolderPage(1); setTestPage(1); }} className={`hover:text-[#1e88e5] transition-colors ${!currentFolderId ? 'text-[#1e88e5]' : ''}`}>
                        {selectedCourse.title}
                    </button>
                    {breadcrumbs.map((b, i) => (
                      <React.Fragment key={b.id}>
                        <span className="text-slate-300">/</span>
                        <button onClick={() => handleFolderClick(b.id)} className={`hover:text-[#1e88e5] transition-colors ${i === breadcrumbs.length - 1 ? 'text-[#1e88e5]' : ''}`}>
                            {b.title}
                        </button>
                      </React.Fragment>
                    ))}
                </div>
                
                <button 
                  onClick={() => {
                      resetWorkspaceAndChat(); 
                      if(onOpenLecture && selectedCourse) onOpenLecture(selectedCourse.id);
                  }} 
                  className="bg-emerald-50 text-emerald-600 border border-emerald-200 hover:bg-emerald-500 hover:text-white font-bold text-[12px] px-5 py-2.5 rounded-lg transition-colors flex items-center justify-center gap-2 shadow-sm uppercase tracking-wide w-full sm:w-auto shrink-0"
                >
                  📖 Mở Bài Giảng
                </button>
            </div>

            <div className="space-y-6 md:space-y-8 px-2 md:px-0">
              {currentSubFolders.length > 0 && (
                <div>
                  <h3 className="font-black text-lg md:text-xl text-slate-800 mb-4 ml-1 uppercase tracking-tight">Danh mục</h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-5">
                    {paginatedFolders.map((subFolder, idx) => {
                      const childCount = allFolders.filter(f => f.parent_id === subFolder.id).length;
                      const testCount = allTests.filter(t => t.folder_id === subFolder.id).length;
                      const defaultImage = FOLDER_IMAGES[idx % FOLDER_IMAGES.length];
                      const displayImage = subFolder.thumbnail_url || defaultImage;

                      return (
                        <div key={subFolder.id} onClick={() => handleFolderClick(subFolder.id)} className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm hover:border-[#1e88e5] transition-colors cursor-pointer flex flex-col h-[160px] md:h-[180px] group bg-black">
                          <div className={`h-[100px] md:h-[110px] relative p-4 md:p-5 overflow-hidden flex items-end border-b border-slate-100`}>
                            <img src={displayImage} loading="lazy" className="absolute inset-0 w-full h-full object-cover group-hover:opacity-80 transition-opacity duration-300" alt="folder" />
                            <div className={`absolute inset-0 bg-gradient-to-t from-slate-900/90 to-transparent`}></div>
                            <h3 className={`relative z-10 text-[16px] md:text-[18px] font-black leading-tight line-clamp-2 w-full text-white`}>
                                {subFolder.title}
                            </h3>
                          </div>
                          <div className="flex-1 bg-white p-4 md:p-5 flex flex-col justify-center relative">
                            <div className="flex justify-between items-center text-slate-500">
                              <p className="text-[11px] md:text-[12px] font-bold bg-slate-50 px-3 py-1 rounded-md border border-slate-200 uppercase tracking-wide">
                                  {childCount > 0 ? `${childCount} mục con` : `${testCount} bài`}
                              </p>
                              <span className="text-[#1e88e5] font-black bg-blue-50 w-7 h-7 rounded flex items-center justify-center group-hover:bg-[#1e88e5] group-hover:text-white transition-colors">
                                  →
                              </span>
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
                <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm mt-6 md:mt-8 animate-in fade-in">
                  <div className="bg-white px-4 md:px-6 py-4 md:py-5 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-3 md:gap-4">
                    <div className="relative w-full sm:w-96">
                      <input type="text" placeholder="Tìm kiếm đề thi / bài tập..." value={searchTest} onChange={(e) => {setSearchTest(e.target.value); setTestPage(1);}} className="w-full pl-10 pr-4 py-2.5 rounded-lg bg-slate-50 border border-slate-200 font-medium text-[13px] md:text-[14px] outline-none focus:border-[#1e88e5] focus:bg-white transition-colors shadow-sm" />
                      <span className="absolute left-3 md:left-4 top-1/2 -translate-y-1/2 text-slate-400 text-base md:text-lg">🔍</span>
                    </div>
                    <div className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
                       <select value={filterType} onChange={(e) => setFilterType(e.target.value)} className="w-full sm:w-auto bg-white border border-slate-200 shadow-sm rounded-lg px-4 py-2.5 font-bold text-[12px] md:text-[13px] text-slate-600 outline-none cursor-pointer focus:border-[#1e88e5]">
                          <option value="all">Tất cả thể loại</option>
                          <option value="test">Chỉ xem Đề thi</option>
                          <option value="exercise">Chỉ xem Bài tập</option>
                       </select>
                       <select value={sortTest} onChange={(e) => setSortTest(e.target.value)} className="w-full sm:w-auto bg-white border border-slate-200 shadow-sm rounded-lg px-4 py-2.5 font-bold text-[12px] md:text-[13px] text-slate-600 outline-none cursor-pointer focus:border-[#1e88e5]">
                         <option value="name-asc">A-Z (Tên bài)</option>
                         <option value="name-desc">Z-A (Tên bài)</option>
                         <option value="date-desc">Mới nhất trước</option>
                         <option value="date-asc">Cũ nhất trước</option>
                       </select>
                    </div>
                  </div>

                  <div className="p-4 md:p-6 lg:p-8 bg-slate-50/50">
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6">
                      {paginatedTests.map(test => {
                        const inProgress = inProgressIds.has(String(test.id));
                        const isCompleted = historyData.some(h => String(h.testId) === String(test.id) || String(h.details?.test_id) === String(test.id));
                        
                        const skillConfig = getTestSkillConfig(test);

                        // 🚀 KIỂM TRA DEADLINE NẾU ĐƯỢC GIAO TỪ LỚP
                        let isOverdue = false;
                        let deadlineLabel = '';
                        
                        const classDeadlines = test.content_json?.basicInfo?.classDeadlines || {};
                        const matchedClassId = userClassIds.find(id => classDeadlines[id]);
                        
                        if (matchedClassId) {
                            const deadlineStr = classDeadlines[matchedClassId];
                            const dDate = new Date(deadlineStr);
                            isOverdue = dDate < new Date();
                            deadlineLabel = `${dDate.getDate().toString().padStart(2, '0')}/${(dDate.getMonth() + 1).toString().padStart(2, '0')} ${dDate.getHours().toString().padStart(2, '0')}:${dDate.getMinutes().toString().padStart(2, '0')}`;
                        }

                        let statusConfig = { progress: 0, badge: "Chưa làm", badgeClass: "text-slate-500 bg-white border border-slate-200", btnText: "Làm bài ngay", btnClass: "bg-white text-[#1e88e5] border border-blue-200 hover:bg-[#1e88e5] hover:text-white" };
                        
                        if (isCompleted) {
                            statusConfig = { progress: 100, badge: "Hoàn thành", badgeClass: "text-emerald-700 bg-emerald-50 border border-emerald-200", btnText: "Làm lại bài", btnClass: "bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-600 hover:text-white" };
                        }
                        else if (inProgress) {
                            statusConfig = { progress: 50, badge: "Đang làm dở", badgeClass: "text-amber-700 bg-amber-50 border border-amber-200", btnText: "Tiếp tục làm", btnClass: "bg-amber-50 text-amber-700 border border-amber-200 hover:bg-amber-500 hover:text-white" };
                        }
                        else if (isOverdue) {
                            statusConfig.btnText = "Nộp muộn";
                            statusConfig.btnClass = "bg-red-50 text-red-600 border border-red-200 hover:bg-red-600 hover:text-white";
                        }

                        return (
                          <div key={test.id} onClick={() => handleStartTestClick(test)} className="bg-white border border-slate-200 p-5 md:p-6 rounded-xl shadow-sm hover:border-[#1e88e5] transition-colors cursor-pointer flex flex-col justify-between group relative overflow-hidden">
                            <div className="absolute top-0 left-0 right-0 h-1 bg-slate-100">
                               <div className={`h-full transition-all duration-500 ${isCompleted ? 'bg-emerald-500' : inProgress ? 'bg-amber-500' : 'bg-transparent'}`} style={{ width: `${statusConfig.progress}%` }}></div>
                            </div>
                            <div>
                              <div className="flex justify-between items-center mb-4 md:mb-5 mt-1 md:mt-2">
                                <div className={`w-10 h-10 md:w-12 md:h-12 rounded-lg ${skillConfig.bg} border ${skillConfig.border} flex items-center justify-center text-xl md:text-2xl ${skillConfig.text} transition-colors shadow-sm`}>
                                    {skillConfig.icon}
                                </div>
                                <span className={`text-[9px] md:text-[10px] font-black px-2 md:px-3 py-1 md:py-1.5 rounded-md uppercase tracking-widest ${statusConfig.badgeClass}`}>{statusConfig.badge}</span>
                              </div>
                              <h3 className="font-bold text-slate-800 text-[15px] md:text-[16px] group-hover:text-[#1e88e5] transition-colors mb-2 line-clamp-2 leading-snug">{test.title}</h3>
                              
                              <div className="flex flex-wrap items-center gap-2 mb-2 md:mb-3 mt-3">
                                  <span className={`text-[9px] px-1.5 py-0.5 rounded-sm uppercase font-black tracking-wider border ${test.content_json?.basicInfo?.category === 'exercise' ? 'bg-slate-50 text-slate-600 border-slate-200' : 'bg-slate-800 text-white border-slate-800'}`}>
                                      {test.content_json?.basicInfo?.category === 'exercise' ? 'BÀI TẬP' : 'ĐỀ THI'}
                                  </span>
                                  {/* 🚀 HIỂN THỊ CHỮ DEADLINE */}
                                  {matchedClassId && !isCompleted && (
                                      <span className={`text-[9px] px-1.5 py-0.5 rounded-sm uppercase font-black tracking-wider border ${isOverdue ? 'bg-red-100 text-red-600 border-red-200' : 'bg-orange-100 text-orange-600 border-orange-200'}`}>
                                          {isOverdue ? 'QUÁ HẠN' : '⏳ ' + deadlineLabel}
                                      </span>
                                  )}
                              </div>
                            </div>
                            <button className={`mt-4 md:mt-6 w-full font-bold text-[12px] md:text-[13px] uppercase tracking-wide py-2.5 rounded-lg transition-colors shadow-sm ${statusConfig.btnClass}`}>
                                {statusConfig.btnText}
                            </button>
                          </div>
                        );
                      })}
                    </div>
                    {processedTests.length === 0 ? (
                      <div className="text-center py-16 text-slate-400 font-medium flex flex-col items-center justify-center">
                        <svg className="w-12 h-12 mb-3 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                        Không có bài thi nào khớp với tìm kiếm của bạn.
                      </div>
                    ) : (
                      renderPagination(testPage, totalTestPages, setTestPage)
                    )}
                  </div>
                </div>
              )}

              {currentSubFolders.length === 0 && currentTests.length === 0 && (
                <div className="text-center py-16 md:py-20 bg-white rounded-xl border border-slate-200 text-slate-400 font-medium text-base shadow-sm mx-2 md:mx-0 flex flex-col items-center justify-center">
                   <svg className="w-16 h-16 text-slate-300 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 7v10a2 2 0 002 2h14a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" /></svg>
                   Thư mục này hiện đang trống.
                </div>
              )}
            </div>
          </div>
        )}

        {/* =====================================================================
            🚀 TRANG BÁO CÁO (ANALYTICS) VỚI CÁC AREA CHART TUYỆT ĐẸP VÀ CHUẨN XÁC
            ===================================================================== */}
        {activeTab === 'analytics' && (
          <div className="space-y-6 md:space-y-8 animate-in fade-in duration-300">
            
            <div className="bg-white px-5 md:px-8 py-5 md:py-6 rounded-xl border border-slate-200 shadow-sm flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 md:gap-4 mx-2 md:mx-0">
              <div>
                <h2 className="text-[20px] md:text-[22px] font-black text-slate-800">Hiệu Suất Học Tập</h2>
                <p className="text-[13px] md:text-sm text-slate-500 font-medium mt-1">Lựa chọn bộ lọc để xem thống kê</p>
              </div>
              <div className="flex flex-col sm:flex-row gap-3 w-full lg:w-auto">
                <div className="w-full sm:w-48 bg-white border border-slate-200 rounded-lg px-4 py-2 flex items-center justify-between cursor-pointer focus-within:border-[#1e88e5] transition-colors shadow-sm">
                  <select value={analyticsCourse} onChange={(e) => setAnalyticsCourse(e.target.value)} className="w-full bg-transparent font-bold text-[12px] md:text-[13px] text-slate-700 outline-none cursor-pointer appearance-none py-1">
                    <option value="all">Tất cả khóa học</option>
                    {courses.length > 0 && courses.map(course => ( <option key={course.id} value={course.id}>{course.title}</option> ))}
                  </select>
                  <span className="text-slate-400 text-xs">▼</span>
                </div>

                <div className="w-full sm:w-48 bg-white border border-slate-200 rounded-lg px-4 py-2 flex items-center justify-between cursor-pointer focus-within:border-[#1e88e5] transition-colors shadow-sm">
                  <select value={analyticsCategory} onChange={(e) => setAnalyticsCategory(e.target.value)} className="w-full bg-transparent font-bold text-[12px] md:text-[13px] text-slate-700 outline-none cursor-pointer appearance-none py-1">
                    <option value="all">Tất cả bài làm</option><option value="test">Chỉ xem Đề thi</option><option value="exercise">Chỉ xem Bài tập</option>
                  </select>
                  <span className="text-slate-400 text-xs">▼</span>
                </div>
              </div>
            </div>

            {analyticsTotalTestsDone === 0 ? (
              <div className="bg-white rounded-xl border border-slate-200 py-16 md:py-24 text-center shadow-sm flex flex-col items-center justify-center mx-2 md:mx-0">
                <div className="text-5xl mb-4 opacity-50 grayscale block">📊</div>
                <h3 className="text-lg md:text-xl font-black text-slate-700 mb-2 px-4">Chưa có dữ liệu làm bài hợp lệ</h3>
                <p className="text-slate-500 font-medium text-[13px] md:text-[15px] max-w-sm px-4">Hệ thống chỉ tính những bài đạt trên 3.0 điểm (hoặc IELTS Band &gt;= 3.0) để đảm bảo phân tích chính xác.</p>
              </div>
            ) : (
              <>
                <div className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 md:gap-6 mx-2 md:mx-0`}>
                  
                  {/* CARD 1: BÀI HOÀN THÀNH (CUMULATIVE AREA CHART) */}
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-5 flex flex-col justify-between hover:border-emerald-300 transition-colors group">
                    <div className="flex justify-between items-center mb-3 relative z-10">
                      <div className="flex items-center gap-2"><span className="font-bold text-slate-500 text-[11px] uppercase tracking-widest group-hover:text-emerald-600 transition-colors">Đã làm</span></div>
                      <span className="font-black text-emerald-600 text-xl md:text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-16 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorDone" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip 
                                   labelFormatter={(label) => `Ngày ${label}`}
                                   formatter={(value: any, name: string) => [`${value} bài`, 'Tổng số bài đã làm']}
                                   contentStyle={{ borderRadius: '8px', fontSize: '12px', fontWeight: 'bold', border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} 
                                   labelStyle={{ color: '#64748b', marginBottom: '4px' }} 
                                   cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} 
                                />
                                <Area type="monotone" dataKey="cumulativeDone" name="Tổng bài" stroke="#10b981" strokeWidth={3} fillOpacity={1} fill="url(#colorDone)" activeDot={{ r: 5, fill: '#10b981', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 2: LƯỢT LÀM BÀI (DAILY AREA CHART) */}
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-5 flex flex-col justify-between hover:border-fuchsia-300 transition-colors group">
                    <div className="flex justify-between items-center mb-3 relative z-10">
                      <div className="flex items-center gap-2"><span className="font-bold text-slate-500 text-[11px] uppercase tracking-widest group-hover:text-fuchsia-600 transition-colors">Lượt làm</span></div>
                      <span className="font-black text-fuchsia-600 text-xl md:text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-16 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorAttempts" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#d946ef" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#d946ef" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip 
                                   labelFormatter={(label) => `Ngày ${label}`}
                                   formatter={(value: any, name: string) => [`${value} lượt`, 'Số bài làm trong ngày']}
                                   contentStyle={{ borderRadius: '8px', fontSize: '12px', fontWeight: 'bold', border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} 
                                   labelStyle={{ color: '#64748b', marginBottom: '4px' }} 
                                   cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} 
                                />
                                <Area type="monotone" dataKey="attempts" name="Lượt" stroke="#d946ef" strokeWidth={3} fillOpacity={1} fill="url(#colorAttempts)" activeDot={{ r: 5, fill: '#d946ef', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 3: GIỜ HỌC (DAILY AREA CHART) */}
                  <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-5 flex flex-col justify-between hover:border-orange-300 transition-colors group">
                    <div className="flex justify-between items-center mb-3 relative z-10">
                      <div className="flex items-center gap-2"><span className="font-bold text-slate-500 text-[11px] uppercase tracking-widest group-hover:text-orange-600 transition-colors">Giờ học</span></div>
                      <span className="font-black text-orange-600 text-xl md:text-2xl">{analyticsTotalTimeHours}h</span>
                    </div>
                    <div className="h-16 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorTime" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#f97316" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#f97316" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip 
                                   labelFormatter={(label) => `Ngày ${label}`}
                                   formatter={(value: any, name: string) => [`${value} giờ`, 'Thời gian học']}
                                   contentStyle={{ borderRadius: '8px', fontSize: '12px', fontWeight: 'bold', border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} 
                                   labelStyle={{ color: '#64748b', marginBottom: '4px' }} 
                                   cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} 
                                />
                                <Area type="monotone" dataKey="time" name="Giờ" stroke="#f97316" strokeWidth={3} fillOpacity={1} fill="url(#colorTime)" activeDot={{ r: 5, fill: '#f97316', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 4: DARK CARD (AVERAGE) */}
                  <div className="bg-slate-800 rounded-xl border border-slate-700 shadow-sm p-5 flex flex-col justify-center text-center">
                    <h4 className="font-bold text-slate-400 text-[11px] uppercase tracking-widest mb-1">
                        {isIeltsContext ? 'IELTS Average' : 'ĐIỂM TRUNG BÌNH'}
                    </h4>
                    <span className="font-black text-white text-3xl md:text-4xl">
                        {isIeltsContext ? avgIelts : avgScore}
                    </span>
                    <p className="text-[10px] text-slate-500 mt-2 font-medium">
                        {isIeltsContext ? '(4 bài gần nhất)' : '(Toàn bộ hệ thống)'}
                    </p>
                  </div>
                  
                  {/* CARD 5: DARK CARD (TARGET) */}
                  <div className="bg-slate-800 rounded-xl border border-amber-500 shadow-md p-5 flex flex-col justify-center text-center relative overflow-hidden group hover:border-amber-400 transition-colors">
                    <div className="absolute -right-4 -bottom-4 text-6xl opacity-10 pointer-events-none">🎯</div>
                    <h4 className="font-bold text-amber-200 text-[11px] uppercase tracking-widest mb-1 relative z-10">
                        {isIeltsContext ? 'Mục tiêu IELTS' : 'Mục tiêu Điểm'}
                    </h4>
                    <input 
                        type="number" step="0.5" min="0" max={isIeltsContext ? "9.0" : "100"} 
                        value={targetIelts || ''} 
                        onChange={(e) => handleUpdateTarget(e.target.value)}
                        placeholder="N/A"
                        className="font-black text-amber-400 text-3xl md:text-4xl bg-transparent w-full text-center outline-none cursor-pointer placeholder:text-amber-400/50 relative z-10"
                        title={isIeltsContext ? "Click để sửa (VD: 7.5)" : "Click để sửa (VD: 85)"}
                    />
                    <p className="text-[10px] text-amber-200/60 mt-2 font-medium relative z-10 group-hover:text-amber-200 transition-colors">Cố gắng lên nhé!</p>
                  </div>

                </div>

                {isIeltsContext && (
                  <div className="mt-8 bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mx-2 md:mx-0 p-6 md:p-8">
                     <div className="flex flex-col md:flex-row gap-8 lg:gap-12 mb-10">
                        
                        {/* CHART 1: BIỂU ĐỒ 4 KỸ NĂNG IELTS */}
                        <div className="flex-1 w-full">
                           <h3 className="font-black text-[15px] md:text-lg text-slate-800 uppercase tracking-tight mb-4">Phân Tích Kỹ Năng</h3>
                           <div className="w-full h-[280px]">
                              <ResponsiveContainer width="100%" height="100%">
                                  <LineChart data={ieltsSkillChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                      <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#64748b' }} dy={10} />
                                      <YAxis domain={[0, 9]} ticks={[0, 3, 5, 7, 9]} axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#64748b' }} />
                                      <Tooltip labelFormatter={(label) => `Ngày ${label}`} contentStyle={{ borderRadius: '8px', fontSize: '12px', fontWeight: 'bold', border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                      <Legend iconType="circle" wrapperStyle={{ fontSize: '12px', fontWeight: 'bold', paddingTop: '10px' }} />
                                      
                                      <Line type="monotone" dataKey="Nghe" name="Listening" stroke="#10b981" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Nói" name="Speaking" stroke="#f97316" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Đọc" name="Reading" stroke="#3b82f6" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Viết" name="Writing" stroke="#d946ef" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                  </LineChart>
                              </ResponsiveContainer>
                           </div>
                        </div>
                        
                        {/* CHART 2: BIỂU ĐỒ TỶ LỆ THEO DẠNG BÀI */}
                        <div className="flex-1 w-full">
                           <h3 className="font-black text-[15px] md:text-lg text-slate-800 uppercase tracking-tight mb-4">Tỷ Lệ Dạng Bài (%)</h3>
                           <div className="w-full h-[280px]">
                              <ResponsiveContainer width="100%" height="100%">
                                  <LineChart data={ieltsTypeChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                      <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#64748b' }} dy={10} />
                                      <YAxis domain={[0, 100]} ticks={[0, 25, 50, 75, 100]} axisLine={false} tickLine={false} tick={{ fontSize: 11, fill: '#64748b' }} />
                                      <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any, name: string) => [`${value}%`, name]} contentStyle={{ borderRadius: '8px', fontSize: '12px', fontWeight: 'bold', border: '1px solid #e2e8f0', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                      <Legend iconType="circle" wrapperStyle={{ fontSize: '12px', fontWeight: 'bold', paddingTop: '10px' }} />
                                      
                                      <Line type="monotone" dataKey="Điền từ" name="Điền từ" stroke="#10b981" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Nhận định" name="T/F/NG" stroke="#f97316" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Trắc nghiệm" name="MCQ/Checkbox" stroke="#3b82f6" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Matching" name="Matching" stroke="#d946ef" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 6 }} connectNulls={true} />
                                  </LineChart>
                              </ResponsiveContainer>
                           </div>
                        </div>

                     </div>

                     <div className="h-px w-full bg-slate-200 mb-8 border-t-2 border-dashed border-slate-200"></div>

                     <h3 className="font-black text-[15px] md:text-lg text-slate-800 uppercase tracking-tight mb-6">Tỷ lệ đúng hiện tại</h3>
                     <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                       {Object.entries(ieltsTypeStats).map(([key, data]) => {
                          const percent = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
                          return (
                            <div key={key} className="bg-slate-50 border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-colors">
                                <div className="flex justify-between items-center mb-2">
                                    <span className="font-bold text-slate-700 text-[13px]">{key}</span>
                                    <span className="font-black text-[#1e88e5] text-[14px]">{percent}%</span>
                                </div>
                                <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden mb-2">
                                    <div className="h-full bg-[#1e88e5] rounded-full transition-all duration-1000" style={{width: `${percent}%`}}></div>
                                </div>
                                <p className="text-[10px] text-slate-500 font-bold text-right tracking-widest">{data.correct} / {data.total} câu</p>
                            </div>
                          );
                       })}
                     </div>
                  </div>
                )}

                <div className="mt-8 md:mt-10 bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mx-2 md:mx-0">
                  <div className="px-5 md:px-6 py-4 md:py-5 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                     <h3 className="font-black text-[16px] md:text-lg text-slate-800 uppercase tracking-tight">Lịch sử làm bài hợp lệ</h3>
                  </div>
                  <div className="overflow-x-auto custom-scrollbar" style={{ WebkitOverflowScrolling: 'touch' }}>
                    <table className="w-full text-left border-collapse min-w-[700px] md:min-w-[800px]">
                      <thead>
                        <tr className="border-b border-slate-200 text-[11px] md:text-[12px] text-slate-500 bg-white uppercase tracking-widest">
                          <th className="px-5 md:px-6 py-4 font-bold w-2/5">Tên bài kiểm tra</th>
                          <th className="px-5 md:px-6 py-4 font-bold text-center">Ngày làm bài</th>
                          <th className="px-5 md:px-6 py-4 font-bold text-center">Điểm số</th>
                          <th className="px-5 md:px-6 py-4 font-bold text-right">Thao tác</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100">
                        {paginatedHistory.map(history => {
                          const isHigh = history.scoreObj.value > 60 || parseFloat(history.details?.bandScore) >= 6.0;
                          return (
                          <tr key={history.id} className="hover:bg-slate-50/50 transition-colors group">
                            <td className="px-5 md:px-6 py-4">
                              <div className="font-bold text-[14px] text-slate-800 mb-1.5 flex flex-wrap items-center gap-2">
                                 {history.name}
                                 {(() => {
                                    const foundTest = allTests.find(t => String(t.id) === String(history.testId));
                                    const isEx = foundTest?.content_json?.basicInfo?.category === 'exercise';
                                    return (
                                         <span className={`text-[9px] px-1.5 py-0.5 rounded-sm uppercase font-black border ${isEx ? 'bg-slate-50 text-slate-500 border-slate-200' : 'bg-blue-50 text-blue-600 border-blue-200'}`}>
                                             {isEx ? 'BÀI TẬP' : 'ĐỀ THI'}
                                         </span>
                                    );
                                 })()}
                              </div>
                            </td>
                            <td className="px-5 md:px-6 py-4 text-center">
                              <div className="font-bold text-[13px] text-slate-700">{formatDate(history.date).split(' ')[0]}</div>
                              <div className="text-[11px] font-medium text-slate-400 mt-0.5">{formatDate(history.date).split(' ')[1]}</div>
                            </td>
                            <td className="px-5 md:px-6 py-4 text-center">
                              <span className={`inline-flex items-center justify-center px-3 py-1.5 rounded-md text-[12px] md:text-[13px] font-bold border ${isHigh ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-slate-50 text-slate-700 border-slate-200'}`}>
                                {history.details?.bandScore ? `Band ${history.details.bandScore}` : `${history.scoreObj.value} điểm`}
                              </span>
                            </td>
                            <td className="px-5 md:px-6 py-4 text-right">
                              <button onClick={() => setViewingHistoryDetail(history)} className="inline-flex items-center bg-white border border-slate-300 text-slate-600 font-bold px-4 py-2 rounded-lg hover:border-[#1e88e5] hover:text-[#1e88e5] transition-colors text-[11px] uppercase tracking-wider whitespace-nowrap shadow-sm">
                                Chi tiết
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

        {activeTab === 'profile' && (
          <div className="max-w-xl mx-auto mt-8 animate-in fade-in duration-300">
            <div className="bg-white p-8 md:p-10 rounded-xl border border-slate-200 shadow-sm text-center mx-2 md:mx-0">
              <div className="w-20 h-20 md:w-24 md:h-24 rounded-full bg-slate-800 text-white flex items-center justify-center font-black text-3xl md:text-4xl mx-auto mb-4 shadow-sm border border-slate-200">
                {displayUserInitial}
              </div>
              <h2 className="text-xl md:text-2xl font-black text-slate-800 mb-1">{displayUserName}</h2>
              <p className="text-slate-500 font-medium mb-8 text-[13px] md:text-[14px]">
                {userProfile?.role === 'admin' ? 'Quản trị viên' : 'Học viên TonyEnglish'}
              </p>
              
              <div className="space-y-4 border-t border-slate-200 pt-8 text-left">
                <h3 className="font-black text-sm text-slate-800 mb-4 uppercase tracking-widest">Cấu hình tài khoản</h3>
                <div className="space-y-1.5">
                  <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Họ và tên</label>
                  <input type="text" value={newFullName} onChange={e => setNewFullName(e.target.value)} className="w-full bg-white border border-slate-300 rounded-lg px-4 py-3 font-medium focus:border-[#1e88e5] outline-none transition-colors text-[13px] shadow-sm" placeholder="Nhập họ và tên..." />
                </div>
                <div className="space-y-1.5">
                  <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Mục tiêu IELTS</label>
                  <input type="text" value={targetIelts} onChange={e => handleUpdateTarget(e.target.value)} className="w-full bg-white border border-slate-300 rounded-lg px-4 py-3 font-medium focus:border-amber-500 outline-none transition-colors text-[13px] shadow-sm" placeholder="Ví dụ: 7.0" />
                </div>
                <div className="space-y-1.5">
                  <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Email đăng nhập</label>
                  <input type="email" defaultValue={currentUser?.email || ""} disabled className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-3 font-medium text-slate-500 outline-none cursor-not-allowed text-[13px]" />
                </div>
                <div className="space-y-1.5">
                  <label className="text-[11px] font-bold text-slate-500 uppercase tracking-widest">Mật khẩu mới (Tùy chọn)</label>
                  <input type="password" placeholder="••••••••" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} className="w-full bg-white border border-slate-300 rounded-lg px-4 py-3 font-medium focus:border-[#1e88e5] outline-none transition-colors text-[13px] shadow-sm" />
                </div>
                <button onClick={handleUpdateProfile} disabled={isUpdatingProfile} className="bg-slate-800 hover:bg-black disabled:bg-slate-300 text-white font-bold px-6 py-3.5 rounded-lg transition-colors w-full mt-4 text-[13px] uppercase tracking-widest shadow-sm">
                  {isUpdatingProfile ? 'Đang lưu...' : 'Lưu thay đổi'}
                </button>
              </div>
            </div>
          </div>
        )}

      </main>

      {viewingHistoryDetail && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white rounded-xl w-full max-w-lg shadow-xl overflow-hidden border border-slate-200">
             <div className="bg-slate-50 px-6 py-4 border-b border-slate-200 flex justify-between items-center">
                <h3 className="font-bold text-slate-800 text-[12px] uppercase tracking-widest">Bảng Kết Quả</h3>
                <button onClick={() => setViewingHistoryDetail(null)} className="text-slate-400 hover:text-red-500 text-2xl font-black transition-colors leading-none">&times;</button>
             </div>
             
             <div className="p-8">
                <div className="text-center mb-8 border-b border-slate-200 pb-8">
                   <h2 className="text-xl font-black text-slate-800 mb-2 leading-snug">{viewingHistoryDetail.name}</h2>
                   <p className="text-slate-500 font-medium text-[12px] mb-6">Nộp lúc: {formatDate(viewingHistoryDetail.date)}</p>
                   
                   <div className="flex justify-center gap-4">
                      <div className="bg-slate-50 border border-slate-200 px-6 py-4 rounded-lg flex-1">
                         <p className="text-[10px] font-bold uppercase text-slate-500 tracking-widest mb-1">Thời gian làm</p>
                         <p className="text-xl font-black text-slate-800">{viewingHistoryDetail.timeSpent} <span className="text-[11px] font-bold">phút</span></p>
                      </div>
                      <div className="bg-emerald-50 border border-emerald-200 px-6 py-4 rounded-lg flex-1">
                         <p className="text-[10px] font-bold uppercase text-emerald-600 tracking-widest mb-1">Kết quả chung</p>
                         <p className="text-xl font-black text-emerald-700">
                           {viewingHistoryDetail.details?.bandScore ? `Band ${viewingHistoryDetail.details.bandScore}` : viewingHistoryDetail.scoreObj.display}
                         </p>
                      </div>
                   </div>
                </div>

                <div className="flex flex-col gap-3">
                    <button onClick={() => {
                        const testId = viewingHistoryDetail.testId || viewingHistoryDetail.details?.test_id;
                        let foundTest = allTests.find(t => String(t.id) === String(testId));
                        if (!foundTest) foundTest = allTests.find(t => t.title.trim() === viewingHistoryDetail.name.trim());
                        
                        if (foundTest && onStartTest) {
                            const type = String(foundTest.test_type || '').toLowerCase();
                            let targetMode = 'standard';
                            if (type.includes('case-study') || type.includes('business')) targetMode = 'case-study';
                            else if (type === 'ielts-writing') targetMode = 'ielts-writing';
                            else if (type === 'ielts-speaking') targetMode = 'ielts-speaking';
                            else if (type.includes('ielts')) targetMode = 'computer';
                            
                            const totalStr = String(viewingHistoryDetail.scoreObj.display).split('/')[1];
                            onStartTest(targetMode, { 
                                ...foundTest, 
                                history_id: viewingHistoryDetail.id, 
                                isReview: true,
                                past_answers: viewingHistoryDetail.details?.userAnswers || viewingHistoryDetail.details?.answers || {},
                                past_score: viewingHistoryDetail.scoreObj.value,
                                past_total: totalStr ? totalStr.trim() : 0,
                                past_band: viewingHistoryDetail.details?.bandScore || '0.0'
                            });
                            setViewingHistoryDetail(null);
                        } else {
                            alert("Đề thi này không còn tồn tại trên hệ thống.");
                        }
                    }} className="w-full bg-[#1e88e5] hover:bg-blue-600 text-white font-bold py-3.5 rounded-lg transition-colors uppercase tracking-widest text-[12px] shadow-sm">
                        Xem chi tiết chữa bài
                    </button>
                    
                    <button onClick={() => handleRetakeFromHistory(viewingHistoryDetail)} className="w-full bg-slate-800 hover:bg-black text-white font-bold py-3.5 rounded-lg transition-colors uppercase tracking-widest text-[12px] shadow-sm">
                       Làm lại bài này ngay
                    </button>
                </div>
             </div>
          </div>
        </div>
      )}

      {showModeSelection && testToStart && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/60 p-4 animate-in fade-in duration-200">
          <div className="bg-white w-full max-w-[450px] p-8 md:p-10 rounded-xl shadow-xl border border-slate-200">
            
            <div className="mb-8">
              <h2 className="text-[20px] md:text-[22px] font-black text-slate-800 mb-2 leading-tight line-clamp-2" title={testToStart.title}>{testToStart.title}</h2>
              <p className="text-[14px] text-slate-500 font-medium">
                Vui lòng chọn hình thức thi bạn muốn tham gia:
              </p>
            </div>

            <div className="space-y-4">
              <button 
                onClick={() => handleConfirmMode('computer')}
                className="w-full flex items-center p-4 md:p-5 bg-white border border-slate-200 hover:border-blue-500 hover:bg-blue-50 rounded-lg transition-colors duration-200 text-left group shadow-sm cursor-pointer"
              >
                <div className="w-12 h-12 md:w-14 md:h-14 shrink-0 flex items-center justify-center bg-slate-100 text-slate-500 group-hover:bg-blue-600 group-hover:text-white rounded-md mr-4 md:mr-5 transition-colors duration-200 border border-slate-200 group-hover:border-blue-600">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 md:w-7 md:h-7">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 17.25v1.007a3 3 0 0 1-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0 1 15 18.257V17.25m6-12V15a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 15V5.25m18 0A2.25 2.25 0 0 0 18.75 3H5.25A2.25 2.25 0 0 0 3 5.25m18 0V12a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 12V5.25" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[15px] md:text-[16px] font-bold text-slate-800 group-hover:text-blue-700 transition-colors">Thi trên máy tính</h3>
                  <p className="text-[12px] md:text-[13px] text-slate-500 mt-0.5 font-medium">Làm bài trực tiếp trên màn hình</p>
                </div>
              </button>

              <button 
                onClick={() => handleConfirmMode('paper')}
                className="w-full flex items-center p-4 md:p-5 bg-white border border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 rounded-lg transition-colors duration-200 text-left group shadow-sm cursor-pointer"
              >
                <div className="w-12 h-12 md:w-14 md:h-14 shrink-0 flex items-center justify-center bg-slate-100 text-slate-500 group-hover:bg-emerald-600 group-hover:text-white rounded-md mr-4 md:mr-5 transition-colors duration-200 border border-slate-200 group-hover:border-emerald-600">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6 md:w-7 md:h-7">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[15px] md:text-[16px] font-bold text-slate-800 group-hover:text-emerald-700 transition-colors">Thi trên giấy</h3>
                  <p className="text-[12px] md:text-[13px] text-slate-500 mt-0.5 font-medium">Làm trên giấy, xem đề PDF</p>
                </div>
              </button>
            </div>

            <div className="mt-8 pt-4 flex justify-center border-t border-slate-100">
              <button 
                onClick={() => setShowModeSelection(false)}
                className="text-[13px] font-black text-slate-400 hover:text-slate-600 hover:bg-slate-50 uppercase tracking-widest transition-colors py-2 px-6 rounded-lg"
              >
                Hủy bỏ
              </button>
            </div>

          </div>
        </div>
      )}
    </div>
  );
}