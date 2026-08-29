import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import AssignmentCalendar from './AssignmentCalendar';
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

  if (type === 'standard-listening' && !checkTestHasAudio(test)) {
      return { icon: '📖', bg: 'bg-blue-50', text: 'text-blue-600', border: 'border-blue-200' };
  }

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
  if (course.thumbnail) return { image: course.thumbnail, badge: course.type || 'Khóa học', color: 'text-indigo-600' };

  const t = (course.title || '').toLowerCase();
  if (t.includes('biology')) return { image: 'https://images.unsplash.com/photo-1530026405186-ed1f139313f8?auto=format&fit=crop&q=80&w=800', badge: 'Biology', color: 'text-emerald-600' };
  if (t.includes('chemistry')) return { image: 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/covers/chem_course_cover.png', badge: 'Chemistry', color: 'text-cyan-600' };
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
  
  const [activeTab, setActiveTab] = useState<'library'|'calendar'|'analytics'|'profile'>(() => {
    const saved = sessionStorage.getItem('lms_portal_tab');
    if (saved === 'library' || saved === 'calendar' || saved === 'analytics' || saved === 'profile') {
      return saved as 'library'|'calendar'|'analytics'|'profile';
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
  const [assignments, setAssignments] = useState<any[]>([]);
  
  const [targetIelts, setTargetIelts] = useState<string>(() => {
      try {
          return localStorage.getItem('tony_target_ielts') || '6.5';
      } catch (e) {
          return '6.5';
      }
  });
  
  const [searchTest, setSearchTest] = useState('');
  const [sortTest, setSortTest] = useState('name-asc');
  const [filterType, setFilterType] = useState('all');
  const [folderPage, setFolderPage] = useState(() => parseInt(sessionStorage.getItem('portal_folder_page') || '1', 10) || 1);
  const [testPage, setTestPage] = useState(() => parseInt(sessionStorage.getItem('portal_test_page') || '1', 10) || 1);

  useEffect(() => {
    sessionStorage.setItem('portal_folder_page', folderPage.toString());
  }, [folderPage]);

  useEffect(() => {
    sessionStorage.setItem('portal_test_page', testPage.toString());
  }, [testPage]);
  const [historyPage, setHistoryPage] = useState(1);

  const [analyticsCourse, setAnalyticsCourse] = useState('all');
  const [analyticsDropdownOpen, setAnalyticsDropdownOpen] = useState(false);
  const [analyticsTestType, setAnalyticsTestType] = useState<'ielts' | 'standard'>('ielts');
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

  const checkUserAndFetchData = async (retryCount = 0) => {
    setIsLoading(true);
    try {
        const { data: { session } } = await supabase.auth.getSession();
        const user = session?.user;
        setCurrentUser(user || null);
        
        if (!user) {
            setIsLoading(false);
            return;
        }

        // Step 1: Fetch user-specific records (profile, progress, enrollments, history)
        const [
            { data: profile },
            { data: lp },
            { data: cStudents },
            { data: enrolls },
            { data: hData },
            { data: assignData }
        ] = await Promise.all([
            supabase.from('profiles').select('*').eq('id', user.id).single(),
            supabase.from('lecture_progress').select('lecture_id, is_completed').eq('user_id', user.id),
            supabase.from('class_students').select('class_id').eq('user_id', user.id),
            supabase.from('enrollments').select('course_id').eq('user_id', user.id),
            supabase.from('test_results').select('id, test_title, course_id, score, total_score, time_spent, created_at, test_type, details').eq('user_id', user.id).order('created_at', { ascending: false }).limit(1000),
            supabase.from('assignments').select('*').eq('user_id', user.id).order('due_date', { ascending: true })
        ]);

        setUserProfile(profile);
        if (profile) {
            if (!newFullName) setNewFullName(profile.full_name || '');
            if (profile.avatar_url) {
                const targetScore = profile.avatar_url.toString();
                setTargetIelts(targetScore);
                try {
                    localStorage.setItem('tony_target_ielts', targetScore);
                } catch (e) {}
            }
        }
        
        setLectureProgressData(lp || []);
        if (cStudents) setUserClassIds(cStudents.map(c => c.class_id));
        setAssignments(assignData || []);

        const courseIds = enrolls?.map(e => e.course_id) || [];
        
        let allF: any[] = [];
        let allL: any[] = [];
        let allT: any[] = [];
        let allC: any[] = [];

        const fetchAllPages = async (queryFn: (from: number, to: number) => any) => {
            let allData: any[] = [];
            let from = 0;
            const step = 1000;
            while (true) {
                const { data, error } = await queryFn(from, from + step - 1);
                if (error) { console.error('Error fetching paginated data:', error); break; }
                if (!data || data.length === 0) break;
                allData = allData.concat(data);
                if (data.length < step) break;
                from += step;
            }
            return { data: allData };
        };

        // Step 2: Fetch catalog tables — PHASE 1: metadata only (no content_json) for fast loading
        if (courseIds.length > 0) {
            const [
                { data: fData },
                { data: lData },
                { data: tData },
                { data: cData }
            ] = await Promise.all([
                fetchAllPages((from, to) => supabase.from('folders').select('id, title, course_id, display_order, thumbnail_url, parent_id').in('course_id', courseIds).order('id').range(from, to)),
                fetchAllPages((from, to) => supabase.from('lectures').select('id, title, course_id, module_id, order_index, is_published').eq('is_published', true).in('course_id', courseIds).order('id').range(from, to)),
                fetchAllPages((from, to) => supabase.from('tests').select('id, title, course_id, folder_id, is_published, order_index, created_at, test_type').eq('is_published', true).or(`course_id.in.(${courseIds.join(',')}),course_id.is.null`).order('id').range(from, to)),
                supabase.from('courses').select('*').in('id', courseIds).limit(100)
            ]);
            allF = fData || [];
            allL = lData || [];
            allT = tData || [];
            allC = cData || [];
        }

        setAllFolders(allF);
        setAllLectures(allL);

        if (courseIds.length > 0) {
            const userCourses = (allC || []).filter(c => courseIds.includes(c.id));
            setCourses(userCourses.sort((a, b) => (a.order_index ?? 999) - (b.order_index ?? 999)));

            // PHASE 1: Set tests immediately with empty content_json for fast rendering
            const lightTests = (allT || []).map((t: any) => ({ ...t, content_json: {} }));
            setAllTests(lightTests);

            // PHASE 2: Background fetch content_json to enrich tests with categories, deadlines, audio
            // Chỉ fetch khi tab đang hiển thị và giới hạn chunk size nhỏ hơn
            const testIds = lightTests.map((t: any) => t.id);
            if (testIds.length > 0 && !document.hidden) {
                const fetchRichData = async () => {
                    try {
                        const chunkSize = 50; // Tăng lại lên 50 vì query giờ đã siêu nhẹ (chỉ lấy basicInfo)
                        const allRichData: any[] = [];
                        for (let i = 0; i < testIds.length; i += chunkSize) {
                            const chunk = testIds.slice(i, i + chunkSize);
                            const { data } = await supabase.from('tests').select('id, basicInfo:content_json->basicInfo').eq('is_published', true).in('id', chunk);
                            if (data) allRichData.push(...data);
                        }
                        if (allRichData.length > 0) {
                            const contentMap = new Map<string, any>();
                            allRichData.forEach((r: any) => {
                                let basicInfo = r.basicInfo;
                                if (typeof basicInfo === 'string') {
                                    try { basicInfo = JSON.parse(basicInfo); } catch(e) { basicInfo = {}; }
                                }
                                contentMap.set(r.id, { basicInfo: basicInfo || {} });
                            });
                            setAllTests(prev => prev.map(t => ({
                                ...t,
                                content_json: contentMap.has(t.id) ? contentMap.get(t.id) : t.content_json
                            })));
                        }
                    } catch (err) {
                        console.error("Error fetching rich content for tests", err);
                    }
                };
                fetchRichData();
            }
        } else {
            setCourses([]);
            setAllTests([]);
        }

        if (hData) {
            // Lọc dữ liệu: Chỉ giữ bài làm nghiêm túc
            const validHistory = hData.filter((item: any) => {
                let detailsObj = item.details || {};
                if (typeof detailsObj === 'string') {
                    try { detailsObj = JSON.parse(detailsObj); } catch(e) { detailsObj = {}; }
                }
                const sc = parseFloat(item.score || 0);
                const type = String(item.test_type || item.test_title || '').toLowerCase();
                const isIeltsTest = type.includes('ielts') || detailsObj.bandScore !== undefined;
                
                if (isIeltsTest) {
                    const band = parseFloat(detailsObj.bandScore || 0);
                    return band > 3.0;
                }
                return sc > 3.0;
            });

            setHistoryData(validHistory.map((item: any) => {
                let detailsObj = item.details || {};
                if (typeof detailsObj === 'string') {
                    try { detailsObj = JSON.parse(detailsObj); } catch(e) { detailsObj = {}; }
                }
                
                return {
                    id: item.id, 
                    testId: item.test_id || detailsObj.test_id, 
                    name: item.test_title || 'Bài thi không tên', 
                    courseId: item.course_id,
                    scoreObj: { 
                        value: parseFloat(item.score || 0), 
                        total: parseFloat(item.total_score || 0),
                        display: `${item.score || 0} / ${item.total_score || 0}` 
                    },
                    timeSpent: Math.round((item.time_spent || 0) / 60), 
                    date: item.created_at, 
                    details: detailsObj
                };
            }));
        } else {
            setHistoryData([]);
        }
    } catch (err: any) {
        if (retryCount < 3 && (err?.name === 'AbortError' || err?.message?.includes('stole') || err?.message?.includes('Lock'))) {
            console.warn(`Auth lock collision, retrying (${retryCount + 1}/3)...`, err);
            setTimeout(() => checkUserAndFetchData(retryCount + 1), 500);
            return;
        }
        console.error("Lỗi khi load dữ liệu Portal:", err);
    } finally {
        setIsLoading(false);
    }
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
      try {
          localStorage.setItem('tony_target_ielts', newVal);
      } catch (e) {}
      if (userProfile) {
          setUserProfile({ ...userProfile, avatar_url: newVal });
      }
      if (currentUser?.id) {
          await supabase.from('profiles').update({ avatar_url: newVal }).eq('id', currentUser.id);
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

  const handleStartTestClick = async (test: any) => {
    if (!onStartTest) return;
    
    sessionStorage.setItem('portal_scroll_y', window.scrollY.toString());

    // Always fetch full test data (with content_json) for the specific test being started
    const { data: fullTest } = await supabase.from('tests').select('*').eq('id', test.id).single();
    const testData = fullTest || test;
    // Parse content_json if it's a string
    if (typeof testData.content_json === 'string') {
        try { testData.content_json = JSON.parse(testData.content_json); } catch(e) { testData.content_json = {}; }
    }
    
    const category = testData.content_json?.basicInfo?.category;
    if (category === 'game') {
      const theme = testData.content_json?.basicInfo?.gameTheme || 'siege-game';
      onStartTest(theme, testData);
      return; 
    }
    
    const type = String(testData.test_type || '').toLowerCase();
    if (type === 'igcse-direct') {
        onStartTest('igcse-direct', testData);
    } else if (type.includes('igcse')) {
        onStartTest('igcse', testData);
    } else if (type.includes('split-standard')) {
        onStartTest('split-standard', testData);
    } else if (type.includes('standard-reading')) {
        onStartTest('standard-reading', testData);
    } else if (type.includes('splitscreen') && type.includes('standard')) {
        onStartTest('standard-splitscreen', testData);
    } else if (type.includes('standard')) {
        onStartTest('standard', testData);
    } else if (type.includes('case-study') || type.includes('business')) {
        onStartTest('case-study', testData);
    } else if (type === 'ielts-writing') {
        onStartTest('ielts-writing', testData);
    } else if (type === 'ielts-speaking') {
        onStartTest('ielts-speaking', testData);
    } else if (type.includes('mixed-paper')) {
        onStartTest('mixed-paper', testData);
    } else if (type.includes('ielts')) { 
      setTestToStart(testData); 
      setShowModeSelection(true); 
    } else {
        onStartTest('standard', testData);
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

  const selectedCourse = useMemo(() => {
      return courses.find(c => String(c.id) === selectedCourseId) || null;
  }, [courses, selectedCourseId]);

  useEffect(() => {
    if (!isLoading && activeView === 'course' && !selectedCourse) {
      setActiveView('dashboard');
    }
  }, [isLoading, activeView, selectedCourse]);
  
  const courseFolders = useMemo(() => {
      if (!selectedCourse) return [];
      return allFolders.filter(f => f.course_id === selectedCourse.id).sort((a,b) => (a.display_order||0) - (b.display_order||0));
  }, [selectedCourse, allFolders]);

  const completedTestIdsSet = useMemo(() => {
      return new Set(historyData.map(h => String(h.testId || h.details?.test_id)));
  }, [historyData]);

  const courseStats = useMemo(() => {
    const stats: Record<string, { testCount: number, lecCount: number, completedTestIds: Set<string>, completedLecIds: Set<string> }> = {};
    
    courses.forEach(c => {
        stats[c.id] = { testCount: 0, lecCount: 0, completedTestIds: new Set(), completedLecIds: new Set() };
    });

    const folderCourseMap: Record<string, string> = {};
    allFolders.forEach(f => {
        if (f.course_id) folderCourseMap[f.id] = f.course_id;
    });

    const testCourseMap: Record<string, string> = {};
    allTests.forEach(t => {
        let cId = t.course_id || t.content_json?.basicInfo?.courseId || folderCourseMap[t.folder_id];
        if (cId && stats[cId]) {
            stats[cId].testCount++;
            testCourseMap[t.id] = cId;
        }
    });

    const lecCourseMap: Record<string, string> = {};
    allLectures.forEach(l => {
        if (l.course_id && stats[l.course_id]) {
            stats[l.course_id].lecCount++;
            lecCourseMap[l.id] = l.course_id;
        }
    });

    historyData.forEach(h => {
        const tId = String(h.testId || h.details?.test_id);
        const cId = testCourseMap[tId] || String(h.courseId);
        if (cId && stats[cId]) {
            stats[cId].completedTestIds.add(tId);
        }
    });

    lectureProgressData.forEach(lp => {
        if (lp.is_completed) {
            const cId = lecCourseMap[String(lp.lecture_id)];
            if (cId && stats[cId]) {
                stats[cId].completedLecIds.add(String(lp.lecture_id));
            }
        }
    });

    return stats;
  }, [courses, allFolders, allTests, allLectures, historyData, lectureProgressData]);

  const courseTests = useMemo(() => {
      if (!selectedCourse) return [];
      const folderIdsSet = new Set(courseFolders.map(f => f.id));
      return allTests.filter(t => folderIdsSet.has(t.folder_id) || t.content_json?.basicInfo?.courseId === selectedCourse.id);
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
                             if (sortTest === 'name-asc') return (a.title || '').localeCompare(b.title || '', undefined, { numeric: true, sensitivity: 'base' });
                             if (sortTest === 'name-desc') return (b.title || '').localeCompare(a.title || '', undefined, { numeric: true, sensitivity: 'base' });
                             if (sortTest === 'date-desc') return new Date(b.created_at || 0).getTime() - new Date(a.created_at || 0).getTime();
                             return new Date(a.created_at || 0).getTime() - new Date(b.created_at || 0).getTime();
                         });
  }, [currentTests, searchTest, filterType, sortTest]);

  const upcomingDeadlines = useMemo(() => {
    const enrolledCourseIds = new Set(courses.map(c => c.id));
    const validTests = allTests.filter(t => enrolledCourseIds.has(t.course_id) || enrolledCourseIds.has(t.content_json?.basicInfo?.courseId));
    
    return validTests.filter(t => {
        const classDeadlines = t.content_json?.basicInfo?.classDeadlines;
        if (!classDeadlines) return false;
        
        const matchedClassId = userClassIds.find(id => classDeadlines[id]);
        if (!matchedClassId) return false;
        
        if (completedTestIdsSet.has(String(t.id))) return false;
        
        t._deadlineStr = classDeadlines[matchedClassId];
        return true; 
    }).sort((a, b) => new Date(a._deadlineStr).getTime() - new Date(b._deadlineStr).getTime());
  }, [allTests, courses, completedTestIdsSet, userClassIds]);

  const totalFolderPages = Math.ceil(currentSubFolders.length / ITEMS_PER_PAGE);
  const paginatedFolders = useMemo(() => currentSubFolders.slice((folderPage - 1) * ITEMS_PER_PAGE, folderPage * ITEMS_PER_PAGE), [currentSubFolders, folderPage]);
  
  const totalTestPages = Math.ceil(processedTests.length / ITEMS_PER_PAGE);
  const paginatedTests = useMemo(() => processedTests.slice((testPage - 1) * ITEMS_PER_PAGE, testPage * ITEMS_PER_PAGE), [processedTests, testPage]);

  useEffect(() => {
      if (paginatedTests.length > 0 || paginatedFolders.length > 0) {
          const savedScrollY = sessionStorage.getItem('portal_scroll_y');
          if (savedScrollY) {
              setTimeout(() => {
                  window.scrollTo({
                      top: parseInt(savedScrollY, 10),
                      behavior: 'smooth'
                  });
                  sessionStorage.removeItem('portal_scroll_y');
              }, 100);
          }
      }
  }, [paginatedTests, paginatedFolders]);

  const isIeltsCourseSelected = analyticsCourse === 'all' 
      ? courses.some(c => (c.title||'').toLowerCase().includes('ielts') || c.type === 'IELTS')
      : courses.find(c => String(c.id) === String(analyticsCourse))?.title.toLowerCase().includes('ielts');
  const isIeltsContext = isIeltsCourseSelected && analyticsTestType === 'ielts';

  // CHUẨN BỊ DỮ LIỆU BÁO CÁO TỪ HISTORY ĐÃ LỌC
  const processedHistory = useMemo(() => {
      return historyData.filter(h => analyticsCourse === 'all' || String(h.courseId) === String(analyticsCourse)).filter(h => {
         if (analyticsCategory === 'all') return true;
         const ft = allTests.find(t => String(t.id) === String(h.testId));
         return (ft?.content_json?.basicInfo?.category || 'test') === analyticsCategory;
      }).filter(h => {
         if (!isIeltsCourseSelected) return true;
         const type = String(h.details?.test_type || h.name).toLowerCase();
         const isIeltsTest = type.includes('ielts') || h.details?.bandScore !== undefined;
         if (analyticsTestType === 'ielts') return isIeltsTest;
         return !isIeltsTest;
      }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }, [historyData, analyticsCourse, analyticsCategory, allTests, isIeltsContext, analyticsTestType]);

  // TÍNH TOÁN DỮ LIỆU CHO 4 AREA CHART TỔNG QUAN THEO NGÀY
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
          const title = String(h.name).toLowerCase();
          const isIelts = type.includes('ielts') || title.includes('ielts') || h.details?.bandScore !== undefined;
          
          if (isIelts) {
              const band = parseFloat(h.details?.bandScore);
              if (!isNaN(band) && band > 0) {
                  entry.bandSum += band;
                  entry.bandCount += 1;
              }
          } else {
              const p = h.scoreObj.total > 0 ? (h.scoreObj.value / h.scoreObj.total) * 100 : h.scoreObj.value || 0;
              entry.stdScoreSum += p;
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

  const { analyticsTotalTestsDone, analyticsTotalTimeHours, avgScore, avgIelts } = useMemo(() => {
      const total = processedHistory.length;
      const hours = (processedHistory.reduce((acc, curr) => acc + curr.timeSpent, 0) / 60).toFixed(1);
      
      let stdSum = 0, stdCount = 0;
      let bandSum = 0, bandCount = 0;

      processedHistory.forEach(h => {
          const type = String(h.details?.test_type || h.name).toLowerCase();
          const title = String(h.name).toLowerCase();
          const isIeltsTest = type.includes('ielts') || title.includes('ielts') || h.details?.bandScore !== undefined;
          
          if (isIeltsTest) {
              const band = parseFloat(h.details?.bandScore);
              if (!isNaN(band) && band > 0) {
                  bandSum += band;
                  bandCount++;
              }
          } else {
              const p = h.scoreObj.total > 0 ? (h.scoreObj.value / h.scoreObj.total) * 100 : h.scoreObj.value || 0;
              stdSum += p;
              stdCount++;
          }
      });

      const score = stdCount > 0 ? (stdSum / stdCount).toFixed(1) + '%' : '0%';
      const ielts = bandCount > 0 ? (bandSum / bandCount).toFixed(1) : '0.0';
      
      return { analyticsTotalTestsDone: total, analyticsTotalTimeHours: hours, avgScore: score, avgIelts: ielts };
  }, [processedHistory, historyData]);

  // TÍNH TOÁN DỮ LIỆU CHO LINE CHART: 4 KỸ NĂNG IELTS
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

  // TÍNH TOÁN DỮ LIỆU CHO LINE CHART: TỶ LỆ THEO TỪNG DẠNG BÀI THEO NGÀY
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

  const inProgressTestId = Array.from(inProgressIds)[0];
  const inProgressTest = useMemo(() => allTests.find(t => String(t.id) === inProgressTestId), [allTests, inProgressTestId]);

  const hour = new Date().getHours();
  let bannerConfig = { greeting: '', gradient: '', icon: '', subtitle: '' };
  
  if (hour >= 5 && hour < 12) {
      bannerConfig = { greeting: 'Chào buổi sáng', gradient: 'from-[#0ea5e9] to-[#4f46e5]', icon: '🌅', subtitle: 'Bắt đầu ngày mới tràn đầy năng lượng! Một chút nỗ lực hôm nay sẽ mang lại kết quả lớn ngày mai.' };
  } else if (hour >= 12 && hour < 18) {
      bannerConfig = { greeting: 'Chào buổi chiều', gradient: 'from-[#0284c7] to-[#4338ca]', icon: '🌤️', subtitle: 'Tiếp tục hành trình chinh phục mục tiêu nào! Giữ vững sự tập trung nhé.' };
  } else {
      bannerConfig = { greeting: 'Chào buổi tối', gradient: 'from-[#1e1b4b] to-[#312e81]', icon: '🌙', subtitle: 'Thời gian tĩnh lặng tuyệt vời để tập trung ôn tập và nhìn lại những gì đã học.' };
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
      <div className="flex justify-center items-center gap-3 mt-8">
        <button disabled={currentPage === 1} onClick={() => setPage(currentPage - 1)} className="w-10 h-10 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:border-[#0ea5e9] hover:text-[#0ea5e9] hover:bg-sky-50 transition-colors disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 shadow-sm font-black">←</button>
        <span className="text-[13px] font-semibold text-slate-600 bg-white px-5 py-2.5 rounded-full border border-slate-200 shadow-sm">Trang {currentPage} / {totalPages}</span>
        <button disabled={currentPage === totalPages} onClick={() => setPage(currentPage + 1)} className="w-10 h-10 rounded-full flex items-center justify-center bg-white border border-slate-200 text-slate-500 hover:border-[#0ea5e9] hover:text-[#0ea5e9] hover:bg-sky-50 transition-colors disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 shadow-sm font-black">→</button>
      </div>
    );
  };

  return (
    <div className="min-h-[100dvh] bg-[#f8fafc] font-sans text-slate-800 overscroll-none w-full flex flex-col">
      {/* HEADER: Glassmorphism */}
      <header className="bg-white/95 backdrop-blur-md border-b border-slate-200/80 sticky top-0 z-40 shadow-sm">
        <div className="max-w-[1200px] w-full mx-auto px-4 md:px-6 py-3 flex items-center justify-between">
          
          <div className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity" onClick={() => {
              resetWorkspaceAndChat(); 
              onNavigate?.('home');
          }}>
            <div className="w-10 h-10 flex items-center justify-center overflow-hidden shrink-0">
                <img src="/logo-shield.png" alt="Logo" className="w-auto h-full object-contain" />
            </div>
            <div className="flex flex-col items-start mt-1 hidden sm:block">
              <h1 className="font-black text-[22px] text-[#0ea5e9] leading-none tracking-tight">TONY<span className="text-slate-800">ENGLISH</span></h1>
            </div>
          </div>

          <div className="flex items-center gap-3 md:gap-5 ml-auto">
            
            {/* TABS CẢI TIẾN */}
            <div className="hidden md:flex items-center bg-slate-100/80 rounded-full p-1 border border-slate-200/60 shadow-inner">
              <button 
                  onClick={() => { 
                      resetWorkspaceAndChat(); 
                      setActiveTab('library'); 
                      setActiveView('dashboard'); 
                      setSelectedCourseId(null); 
                      setCurrentFolderId(null);
                  }} 
                  className={`flex items-center gap-2 px-5 py-2 rounded-full font-semibold text-[13px] transition-all duration-200 ${activeTab === 'library' ? 'bg-[#0ea5e9] text-white shadow-md' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'}`}
              >
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                  Học tập
              </button>
              <button 
                  onClick={() => {
                      resetWorkspaceAndChat(); 
                      setActiveTab('calendar');
                  }} 
                  className={`flex items-center gap-2 px-5 py-2 rounded-full font-semibold text-[13px] transition-all duration-200 ${activeTab === 'calendar' ? 'bg-[#0ea5e9] text-white shadow-md' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'}`}
              >
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg>
                  Lịch báo bài
              </button>
              <button 
                  onClick={() => {
                      resetWorkspaceAndChat(); 
                      setActiveTab('analytics');
                  }} 
                  className={`flex items-center gap-2 px-5 py-2 rounded-full font-semibold text-[13px] transition-all duration-200 ${activeTab === 'analytics' ? 'bg-[#0ea5e9] text-white shadow-md' : 'text-slate-500 hover:text-slate-800 hover:bg-slate-200/50'}`}
              >
                  <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
                  Báo cáo
              </button>
            </div>

            <div className="hidden lg:flex items-center">
               <button onClick={toggleFullScreen} className="w-9 h-9 rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 border border-transparent hover:border-slate-200 hover:text-[#0ea5e9] transition-colors">
                 {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>}
               </button>
            </div>

            <div className="relative" ref={dropdownRef}>
               <button onClick={() => setIsDropdownOpen(!isDropdownOpen)} className="flex items-center gap-3 bg-white pr-2 pl-4 py-1.5 rounded-full border border-slate-200 shadow-sm hover:border-[#0ea5e9] transition-colors focus:outline-none group">
                 <div className="text-right hidden sm:block">
                   <div className="font-black text-[13px] text-slate-800 group-hover:text-[#0ea5e9] transition-colors">{displayUserName}</div>
                   <div className="text-[10px] font-medium text-slate-500 uppercase tracking-wider">
                       {userProfile?.role === 'admin' ? 'Quản trị' : 'Học viên'}
                   </div>
                 </div>
                 <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 text-white flex items-center justify-center font-black shadow-inner text-[13px] border border-white/20">
                     {displayUserInitial}
                 </div>
               </button>

               {isDropdownOpen && (
                  <div className="absolute right-0 mt-3 w-56 bg-white/95 backdrop-blur-md rounded-xl shadow-xl border border-slate-200 py-2 z-50 animate-in fade-in zoom-in-95 duration-200">
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('library'); 
                         setActiveView('dashboard'); 
                         setSelectedCourseId(null); 
                         setCurrentFolderId(null); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2 transition-colors">
                         <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg> Học tập
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('calendar'); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2 transition-colors">
                         <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg> Lịch báo bài
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('analytics'); 
                         setIsDropdownOpen(false); 
                     }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] flex items-center gap-2 transition-colors">
                         <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg> Báo cáo
                     </button>
                     <button onClick={() => { 
                         resetWorkspaceAndChat(); 
                         setActiveTab('profile'); 
                         setIsDropdownOpen(false); 
                     }} className="w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0ea5e9] transition-colors flex items-center gap-2 md:border-t-0 border-t border-slate-100">
                         👤 Cấu hình tài khoản
                     </button>
                     {userProfile?.role === 'admin' && (
                         <button onClick={() => {
                             resetWorkspaceAndChat();
                             if(onNavigate) onNavigate('admin');
                         }} className="w-full text-left px-5 py-3 text-sm font-black text-purple-600 hover:bg-purple-50 transition-colors">
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

      <main className="flex-1 w-full max-w-[1200px] mx-auto p-4 md:p-8 overflow-y-auto custom-scrollbar" style={{ WebkitOverflowScrolling: 'touch' }}>
        
        {activeTab === 'library' && activeView === 'dashboard' && (
          <div className="animate-in fade-in duration-500">
            {/* 🚀 BANNner HIỆN ĐẠI (Gamified) */}
            <div className={`relative bg-gradient-to-r ${bannerConfig.gradient} rounded-[2rem] p-8 md:p-12 mb-8 md:mb-12 overflow-hidden shadow-lg border border-white/10`}>
              <div className="absolute inset-0 bg-[url('/chat-pattern.png')] bg-repeat bg-[length:300px] opacity-10 mix-blend-overlay"></div>
              <div className="absolute top-0 right-0 w-96 h-96 bg-white/10 blur-[100px] rounded-full -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>
              
              <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8 md:gap-12">
                <div className="text-white flex-1 text-center md:text-left">
                  <h2 className="text-3xl md:text-4xl lg:text-5xl font-black mb-3 md:mb-4 drop-shadow-md tracking-tight">
                      {bannerConfig.greeting}, {displayUserName}! <span className="inline-block animate-bounce">{bannerConfig.icon}</span>
                  </h2>
                  <p className="text-white/80 text-[15px] md:text-[17px] font-medium leading-relaxed max-w-xl">
                      {bannerConfig.subtitle}
                  </p>
                </div>

                {inProgressTest ? (
                   <div className="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-2xl w-full md:w-80 shadow-2xl text-white hover:bg-white/15 transition-all cursor-pointer group hover:-translate-y-1" onClick={() => handleStartTestClick(inProgressTest)}>
                      <div className="flex items-center justify-between mb-4">
                         <div className="flex items-center gap-2">
                            <span className="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse shadow-[0_0_8px_rgba(251,191,36,0.8)]"></span>
                            <span className="text-[11px] font-black uppercase tracking-widest text-amber-300">Đang làm dở</span>
                         </div>
                         <span className="text-white/40 group-hover:text-white transition-colors">↗</span>
                      </div>
                      <h3 className="font-bold text-lg md:text-xl mb-5 line-clamp-2 leading-tight">{inProgressTest.title}</h3>
                      <button className="w-full bg-white text-[#0ea5e9] hover:bg-sky-50 font-black py-3 rounded-xl text-[13px] transition-colors uppercase tracking-wide shadow-md">
                         Tiếp tục ngay
                      </button>
                   </div>
                ) : courses.length > 0 && (
                  <div className="bg-white/10 backdrop-blur-md border border-white/20 p-6 rounded-2xl w-full md:w-80 shadow-2xl text-white hover:bg-white/15 transition-all cursor-pointer group hover:-translate-y-1" onClick={() => {
                      resetWorkspaceAndChat(); 
                      if(onOpenLecture) onOpenLecture(courses[0].id);
                  }}>
                    <div className="flex items-center justify-between mb-4">
                       <span className="text-[11px] font-black uppercase tracking-widest text-white/70 bg-white/10 px-3 py-1 rounded-full">Gợi ý học tập</span>
                       <span className="text-white/40 group-hover:text-white transition-colors">↗</span>
                    </div>
                    <h3 className="font-bold text-lg md:text-xl mb-5 line-clamp-2 leading-tight">{courses[0].title}</h3>
                    <button className="w-full bg-[#0ea5e9] text-white hover:bg-[#0284c7] font-black py-3 rounded-xl text-[13px] transition-colors uppercase tracking-wide shadow-md">
                       Vào học ngay
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* BẢNG CẢNH BÁO DEADLINE (To-do list gamified) */}
            {upcomingDeadlines.length > 0 && (
                <div className="bg-white border border-rose-200 rounded-[2rem] p-6 md:p-8 mb-8 md:mb-12 shadow-[0_8px_30px_rgba(225,29,72,0.08)] flex flex-col md:flex-row items-start gap-6 animate-in slide-in-from-bottom-4 relative overflow-hidden">
                    <div className="absolute top-0 left-0 w-2 h-full bg-rose-500"></div>
                    <div className="w-16 h-16 rounded-2xl bg-rose-50 flex items-center justify-center text-3xl shrink-0 shadow-inner">
                        ⏰
                    </div>
                    <div className="flex-1 min-w-0 w-full">
                        <h3 className="font-black text-slate-800 text-[18px] md:text-xl mb-1 tracking-tight">Nhiệm vụ cần hoàn thành</h3>
                        <p className="text-slate-500 text-sm font-medium mb-4">Bạn có <span className="text-rose-600 font-bold">{upcomingDeadlines.length} bài tập</span> sắp đến hạn nộp.</p>
                        
                        <div className="flex flex-col gap-3">
                            {upcomingDeadlines.slice(0, 3).map(t => {
                                const dDate = new Date(t._deadlineStr);
                                const isOverdue = dDate < new Date();
                                return (
                                    <div key={t.id} onClick={() => handleStartTestClick(t)} className="flex justify-between items-center bg-slate-50 p-4 rounded-xl border border-slate-200 hover:border-[#0ea5e9] cursor-pointer transition-all shadow-sm hover:shadow-md group">
                                        <div className="flex items-center gap-3 min-w-0">
                                            <div className="w-5 h-5 rounded-full border-2 border-slate-300 group-hover:border-[#0ea5e9] transition-colors shrink-0"></div>
                                            <span className="font-semibold text-slate-700 text-[14px] md:text-[15px] truncate group-hover:text-[#0ea5e9] transition-colors">{t.title}</span>
                                        </div>
                                        <span className={`shrink-0 text-[11px] md:text-xs font-black px-3 py-1.5 rounded-lg whitespace-nowrap border ${isOverdue ? 'bg-rose-100 text-rose-700 border-rose-200' : 'bg-orange-50 text-orange-600 border-orange-200'}`}>
                                            {isOverdue ? '⚠️ QUÁ HẠN' : '⏳ ' + formatDate(t._deadlineStr)}
                                        </span>
                                    </div>
                                )
                            })}
                            {upcomingDeadlines.length > 3 && (
                                <button className="text-[13px] font-bold text-slate-400 hover:text-[#0ea5e9] transition-colors self-start mt-1">
                                    Xem thêm {upcomingDeadlines.length - 3} nhiệm vụ khác →
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            )}

            <h2 className="font-black text-2xl md:text-3xl text-slate-800 mb-6 px-2 tracking-tight">Khóa học của tôi</h2>
            
            {isLoading ? (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                 {[1,2].map(i => (
                   <div key={i} className="bg-white rounded-2xl h-[280px] w-full border border-slate-200 p-6 animate-pulse flex flex-col justify-between">
                      <div className="h-40 w-full bg-slate-100 rounded-xl mb-4"></div>
                      <div className="h-6 w-1/2 bg-slate-100 rounded-md"></div>
                      <div className="h-2 w-full bg-slate-100 rounded-full mt-auto"></div>
                   </div>
                 ))}
              </div>
            ) : courses.length === 0 ? (
              <div className="bg-white border border-slate-200 rounded-2xl py-24 text-center shadow-sm mx-2 flex flex-col items-center">
                <div className="w-24 h-24 bg-slate-50 rounded-full flex items-center justify-center text-4xl mb-4 grayscale opacity-50">🔒</div>
                <h3 className="font-bold text-slate-700 text-xl mb-2">Bạn chưa tham gia khóa học nào</h3>
                <p className="text-slate-500 font-medium max-w-sm">Vui lòng liên hệ trung tâm để được cấp quyền truy cập vào các bài giảng nhé!</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 xl:gap-8">
                {courses.map(course => {
                  const cover = getCourseCover(course);
                  const stats = courseStats[course.id] || { testCount: 0, lecCount: 0, completedTestIds: new Set(), completedLecIds: new Set() };
                  
                  const testProgress = stats.testCount > 0 ? Math.min(100, Math.round((stats.completedTestIds.size / stats.testCount) * 100)) : 0;
                  const lecProgress = stats.lecCount > 0 ? Math.min(100, Math.round((stats.completedLecIds.size / stats.lecCount) * 100)) : 0;
                  const overallProgress = Math.round((testProgress + lecProgress) / 2);

                  return (
                    <div key={course.id} className="bg-white rounded-[2rem] border border-slate-200 overflow-hidden shadow-sm hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)] hover:-translate-y-1 transition-all duration-300 flex flex-col mx-2 md:mx-0 group">
                      
                      {/* Image Top Half */}
                      <div className="w-full h-[180px] md:h-[220px] relative overflow-hidden bg-slate-100 cursor-pointer" onClick={() => handleOpenCourse(course)}>
                         <img src={cover.image} loading="lazy" alt={course.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
                         <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                         
                         <div className={`absolute top-4 left-4 bg-white/90 backdrop-blur px-3 py-1.5 rounded-lg text-[10px] font-black uppercase tracking-widest ${cover.color} shadow-sm`}>
                             {cover.badge}
                         </div>
                         <h4 className="absolute bottom-4 left-5 right-5 font-black text-xl md:text-2xl text-white leading-snug drop-shadow-md">
                             {course.title}
                         </h4>
                      </div>
                      
                      {/* Content Bottom Half */}
                      <div className="flex-1 p-6 md:p-8 flex flex-col justify-between bg-white">
                        
                        {/* Overall Progress */}
                        <div className="mb-6">
                            <div className="flex justify-between items-end mb-2">
                                <span className="text-[12px] font-bold text-slate-500 uppercase tracking-widest">Tiến độ chung</span>
                                <span className="text-[18px] font-black text-[#0ea5e9]">{overallProgress}%</span>
                            </div>
                            <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden">
                                <div className="h-full bg-gradient-to-r from-sky-400 to-[#0ea5e9] rounded-full transition-all duration-1000" style={{ width: `${overallProgress}%` }}></div>
                            </div>
                        </div>

                        {/* Detailed Stats */}
                        <div className="flex items-center gap-6 mb-8 bg-slate-50 p-4 rounded-xl border border-slate-100">
                          <div className="flex-1">
                              <span className="flex items-center gap-1.5 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1"><span className="text-emerald-500">📚</span> Lý thuyết</span>
                              <div className="font-black text-slate-700 text-[15px]">{stats.completedLecIds.size} / {stats.lecCount} <span className="text-[11px] font-medium text-slate-400">bài</span></div>
                          </div>
                          <div className="w-px h-10 bg-slate-200"></div>
                          <div className="flex-1">
                              <span className="flex items-center gap-1.5 text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1"><span className="text-blue-500">📝</span> Thực hành</span>
                              <div className="font-black text-slate-700 text-[15px]">{stats.completedTestIds.size} / {stats.testCount} <span className="text-[11px] font-medium text-slate-400">đề</span></div>
                          </div>
                        </div>
                        
                        {/* Actions */}
                        <div className="flex gap-3">
                           <button onClick={() => {
                               resetWorkspaceAndChat(); 
                               if(onOpenLecture) onOpenLecture(course.id);
                           }} className="flex-1 bg-white border-2 border-emerald-500 text-emerald-600 hover:bg-emerald-50 font-bold text-[13px] py-3.5 rounded-xl transition-colors flex items-center justify-center gap-2 uppercase tracking-wide">
                               📖 Lý thuyết
                           </button>
                           <button onClick={() => handleOpenCourse(course)} className="flex-[1.5] bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-bold text-[13px] py-3.5 rounded-xl transition-colors shadow-md shadow-blue-500/20 flex items-center justify-center gap-2 uppercase tracking-wide">
                               📝 Vào làm bài
                           </button>
                        </div>
                      </div>
                    </div>
                  )
                })}
              </div>
            )}
          </div>
        )}

        {/* 🚀 COURSE VIEW (Danh sách Folders & Tests) */}
        {activeTab === 'library' && activeView === 'course' && selectedCourse && (
          <div className="animate-in fade-in slide-in-from-right-8 duration-500">
            {/* Breadcrumb Header */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8 bg-white p-4 md:p-5 rounded-2xl border border-slate-200 shadow-sm mx-2 md:mx-0">
                <div className="flex flex-wrap items-center gap-2 text-[14px] font-semibold text-slate-500">
                    <button onClick={() => { setActiveView('dashboard'); setSelectedCourseId(null); }} className="hover:text-[#0ea5e9] transition-colors p-1 rounded-md hover:bg-sky-50">
                        Khóa học
                    </button>
                    <span className="text-slate-300">/</span>
                    <button onClick={() => { setCurrentFolderId(null); setFolderPage(1); setTestPage(1); }} className={`p-1 rounded-md hover:bg-sky-50 transition-colors ${!currentFolderId ? 'text-[#0ea5e9] font-bold bg-sky-50' : 'hover:text-[#0ea5e9]'}`}>
                        {selectedCourse.title}
                    </button>
                    {breadcrumbs.map((b, i) => (
                      <React.Fragment key={b.id}>
                        <span className="text-slate-300">/</span>
                        <button onClick={() => handleFolderClick(b.id)} className={`p-1 rounded-md hover:bg-sky-50 transition-colors ${i === breadcrumbs.length - 1 ? 'text-[#0ea5e9] font-bold bg-sky-50' : 'hover:text-[#0ea5e9]'}`}>
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
                  className="w-full md:w-auto bg-emerald-50 text-emerald-700 border border-emerald-200 hover:bg-emerald-500 hover:text-white font-bold text-[13px] px-6 py-2.5 rounded-xl transition-all flex items-center justify-center gap-2 shadow-sm uppercase tracking-wide shrink-0"
                >
                  📖 Mở Bài Giảng Lý Thuyết
                </button>
            </div>

            <div className="space-y-8 md:space-y-12 px-2 md:px-0">
              
              {/* Folders Grid */}
              {currentSubFolders.length > 0 && (
                <div>
                  <h3 className="font-black text-xl text-slate-800 mb-5 ml-1 tracking-tight flex items-center gap-2">
                      <span className="text-amber-500">📁</span> Danh mục
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                    {paginatedFolders.map((subFolder, idx) => {
                      const childCount = allFolders.filter(f => f.parent_id === subFolder.id).length;
                      const testCount = allTests.filter(t => t.folder_id === subFolder.id).length;
                      const parentFolder = subFolder.parent_id ? allFolders.find(f => f.id === subFolder.parent_id) : null;
                      const isTopLevel = !subFolder.parent_id || subFolder.parent_id === 'null' || subFolder.parent_id === '';
                      const defaultImage = FOLDER_IMAGES[idx % FOLDER_IMAGES.length];
                      
                      // Inherit parent image if no thumbnail, and apply hue-rotate if it's inherited (to avoid duplicates)
                      const isInherited = !subFolder.thumbnail_url && parentFolder?.thumbnail_url;
                      const displayImage = subFolder.thumbnail_url || (parentFolder ? parentFolder.thumbnail_url : null) || defaultImage;
                      const hueRotate = (!isTopLevel && isInherited) ? `hue-rotate(${(idx * 65) % 360}deg)` : 'none';
                      
                      let badgeText = null;
                      let displayTitle = subFolder.title;
                      
                      if (!isTopLevel) {
                          const prefixMatch = subFolder.title.match(/^([A-Z0-9]+)\s*:/i);
                          if (prefixMatch && prefixMatch[1].length <= 4) {
                              badgeText = prefixMatch[1].toUpperCase();
                              displayTitle = subFolder.title.substring(prefixMatch[0].length).trim();
                          }
                      }

                      return (
                        <div key={subFolder.id} onClick={() => handleFolderClick(subFolder.id)} className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-lg hover:-translate-y-1 hover:border-[#0ea5e9] transition-all duration-300 cursor-pointer flex flex-col group relative">
                          <div className={`h-[120px] relative overflow-hidden bg-slate-800`}>
                            <img src={displayImage} style={{ filter: hueRotate }} loading="lazy" className="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80" alt="folder" />
                            <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent"></div>
                            <div className={`absolute bottom-4 right-4 ${badgeText ? 'left-20' : 'left-5'}`}>
                                <h3 className="text-[16px] font-black leading-snug line-clamp-2 w-full text-white drop-shadow-md">
                                    {displayTitle}
                                </h3>
                            </div>
                          </div>

                          {badgeText && (
                              <div className="absolute top-[96px] left-5 bg-gradient-to-br from-white to-slate-50 text-[#0ea5e9] font-black text-[18px] w-12 h-12 rounded-xl flex items-center justify-center shadow border-2 border-white shrink-0 z-10 ring-1 ring-black/5">
                                  {badgeText}
                              </div>
                          )}

                          <div className="bg-white p-5 pt-4 flex flex-col relative flex-1">
                            {!badgeText && <div className="-mt-1"></div>}
                            <div className="flex justify-between items-center mt-auto">
                              <span className="text-[11px] font-bold text-slate-500 bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200 uppercase tracking-widest">
                                  {childCount > 0 ? `${childCount} thư mục` : `${testCount} bài tập`}
                              </span>
                              <span className="w-8 h-8 rounded-full bg-sky-50 text-[#0ea5e9] flex items-center justify-center group-hover:bg-[#0ea5e9] group-hover:text-white transition-colors">
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

              {/* Tests Grid */}
              {currentTests.length > 0 && (
                <div className="bg-white rounded-[2rem] border border-slate-200 overflow-hidden shadow-sm animate-in fade-in">
                  
                  {/* Test Filters */}
                  <div className="bg-white px-5 md:px-8 py-5 border-b border-slate-100 flex flex-col lg:flex-row justify-between items-center gap-4">
                    <div className="relative w-full lg:w-96">
                      <input type="text" placeholder="Tìm kiếm bài tập..." value={searchTest} onChange={(e) => {setSearchTest(e.target.value); setTestPage(1);}} className="w-full pl-11 pr-4 py-3 rounded-xl bg-slate-50 border border-slate-200 font-semibold text-[14px] outline-none focus:border-[#0ea5e9] focus:ring-4 focus:ring-[#0ea5e9]/10 transition-all shadow-sm" />
                      <span className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-lg">🔍</span>
                    </div>
                    <div className="flex gap-3 w-full lg:w-auto">

                       <select value={sortTest} onChange={(e) => setSortTest(e.target.value)} className="flex-1 lg:flex-none bg-white border border-slate-200 shadow-sm rounded-xl px-4 py-3 font-bold text-[13px] text-slate-600 outline-none cursor-pointer focus:border-[#0ea5e9] focus:ring-4 focus:ring-[#0ea5e9]/10">
                         <option value="name-asc">A-Z</option>
                         <option value="name-desc">Z-A</option>
                         <option value="date-desc">Mới nhất</option>
                         <option value="date-asc">Cũ nhất</option>
                       </select>
                    </div>
                  </div>

                  {/* Tests List */}
                  <div className="p-5 md:p-8 bg-slate-50/50">
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5 md:gap-6">
                      {paginatedTests.map(test => {
                        const inProgress = inProgressIds.has(String(test.id));
                        const isCompleted = completedTestIdsSet.has(String(test.id));
                        const skillConfig = getTestSkillConfig(test);

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

                        let statusConfig = { badge: "Chưa làm", badgeClass: "text-slate-500 bg-slate-100", btnText: "Làm bài ngay", btnClass: "bg-white text-[#0ea5e9] border border-sky-200 hover:bg-[#0ea5e9] hover:text-white" };
                        
                        if (isCompleted) {
                            statusConfig = { badge: "✓ Hoàn thành", badgeClass: "text-emerald-700 bg-emerald-100", btnText: "Làm lại bài", btnClass: "bg-white text-emerald-600 border border-emerald-200 hover:bg-emerald-500 hover:text-white" };
                        }
                        else if (inProgress) {
                            statusConfig = { badge: "⏳ Đang làm dở", badgeClass: "text-amber-700 bg-amber-100", btnText: "Tiếp tục làm", btnClass: "bg-amber-500 text-white shadow-md shadow-amber-500/20 hover:bg-amber-600" };
                        }
                        else if (isOverdue) {
                            statusConfig.btnText = "Nộp muộn";
                            statusConfig.btnClass = "bg-rose-50 text-rose-600 border border-rose-200 hover:bg-rose-600 hover:text-white";
                        }

                        return (
                          <div key={test.id} onClick={() => handleStartTestClick(test)} className={`bg-white border p-5 md:p-6 rounded-2xl shadow-sm hover:shadow-lg transition-all duration-300 cursor-pointer flex flex-col justify-between group relative overflow-hidden ${isCompleted ? 'border-emerald-200' : inProgress ? 'border-amber-300' : 'border-slate-200 hover:border-[#0ea5e9]'}`}>
                            
                            <div>
                              <div className="flex justify-between items-start mb-4">
                                <div className={`w-12 h-12 rounded-xl ${skillConfig.bg} border ${skillConfig.border} flex items-center justify-center text-2xl shadow-inner group-hover:scale-110 transition-transform`}>
                                    {skillConfig.icon}
                                </div>
                                <span className={`text-[10px] font-black px-2.5 py-1 rounded-md uppercase tracking-widest ${statusConfig.badgeClass}`}>
                                    {statusConfig.badge}
                                </span>
                              </div>
                              
                              <h3 className="font-bold text-slate-800 text-[16px] group-hover:text-[#0ea5e9] transition-colors mb-3 line-clamp-2 leading-snug h-12">
                                  {test.title}
                              </h3>
                              
                              <div className="flex flex-wrap items-center gap-2 mb-2">

                                  {matchedClassId && !isCompleted && (
                                      <span className={`text-[10px] px-2 py-0.5 rounded uppercase font-bold tracking-wider ${isOverdue ? 'bg-rose-100 text-rose-600' : 'bg-orange-100 text-orange-600'}`}>
                                          {isOverdue ? 'Quá hạn' : 'Hạn: ' + deadlineLabel}
                                      </span>
                                  )}
                              </div>
                            </div>
                            
                            <button className={`mt-5 w-full font-bold text-[13px] uppercase tracking-wide py-3 rounded-xl transition-all duration-300 ${statusConfig.btnClass}`}>
                                {statusConfig.btnText}
                            </button>
                          </div>
                        );
                      })}
                    </div>
                    
                    {processedTests.length === 0 ? (
                      <div className="text-center py-20 text-slate-400 font-medium flex flex-col items-center justify-center bg-white rounded-2xl border border-dashed border-slate-300">
                        <svg className="w-12 h-12 mb-3 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                        Không tìm thấy bài học nào phù hợp.
                      </div>
                    ) : (
                      renderPagination(testPage, totalTestPages, setTestPage)
                    )}
                  </div>
                </div>
              )}

              {currentSubFolders.length === 0 && currentTests.length === 0 && (
                <div className="text-center py-24 bg-white rounded-2xl border border-slate-200 text-slate-400 font-medium text-base shadow-sm mx-2 md:mx-0 flex flex-col items-center justify-center">
                   <div className="text-5xl mb-4 grayscale opacity-30">📭</div>
                   Thư mục này hiện đang trống.
                </div>
              )}
            </div>
          </div>
        )}

        {/* =====================================================================
            📅 TRANG LỊCH BÁO BÀI (ASSIGNMENT CALENDAR)
            ===================================================================== */}
        {activeTab === 'calendar' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 mx-2 md:mx-0 pb-8">
            <AssignmentCalendar 
              assignments={assignments} 
              completedTestIds={completedTestIdsSet}
              onRefresh={async () => {
                if (!currentUser) return;
                const { data } = await supabase.from('assignments').select('*').eq('user_id', currentUser.id).order('due_date', { ascending: true });
                setAssignments(data || []);
              }}
              onStartTest={(testId) => {
                const test = allTests.find(t => t.id === testId);
                if (test) onStartTest(test.test_type, test);
              }}
            />
          </div>
        )}

        {/* =====================================================================
            🚀 TRANG BÁO CÁO (ANALYTICS) VỚI CÁC AREA CHART TUYỆT ĐẸP VÀ CHUẨN XÁC
            ===================================================================== */}
        {activeTab === 'analytics' && (
          <div className="space-y-6 md:space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
            
            {/* Bộ lọc báo cáo */}
            <div className="bg-white px-6 py-6 rounded-[2rem] border border-slate-200 shadow-sm flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5 mx-2 md:mx-0">
              <div>
                <h2 className="text-[22px] md:text-[24px] font-black text-slate-800 tracking-tight">Hiệu Suất Học Tập</h2>
                <p className="text-[14px] text-slate-500 font-medium mt-1">Phân tích kết quả và biểu đồ kỹ năng</p>
              </div>
              <div className="flex flex-col sm:flex-row items-center gap-3 w-full lg:w-auto">
                {isIeltsCourseSelected && (
                    <div className="flex bg-slate-100/80 p-1 rounded-xl w-full sm:w-fit border border-slate-200/50 backdrop-blur-sm">
                        <button
                            onClick={() => setAnalyticsTestType('ielts')}
                            className={`flex-1 sm:flex-none flex justify-center items-center gap-2 px-5 py-2.5 rounded-lg font-bold text-[13px] transition-all duration-300 ${analyticsTestType === 'ielts' ? 'bg-white text-blue-600 shadow-sm ring-1 ring-slate-200/50' : 'text-slate-500 hover:text-slate-700 hover:bg-slate-200/50'}`}
                        >
                            <span>🎯</span> Luyện thi IELTS
                        </button>
                        <button
                            onClick={() => setAnalyticsTestType('standard')}
                            className={`flex-1 sm:flex-none flex justify-center items-center gap-2 px-5 py-2.5 rounded-lg font-bold text-[13px] transition-all duration-300 ${analyticsTestType === 'standard' ? 'bg-white text-blue-600 shadow-sm ring-1 ring-slate-200/50' : 'text-slate-500 hover:text-slate-700 hover:bg-slate-200/50'}`}
                        >
                            <span>📝</span> Bài Tập Bổ Trợ
                        </button>
                    </div>
                )}
                <div className="relative w-full sm:w-64">
                  <div 
                    onClick={() => setAnalyticsDropdownOpen(!analyticsDropdownOpen)}
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 flex items-center justify-between cursor-pointer hover:border-[#0ea5e9] hover:bg-white transition-all shadow-sm"
                  >
                    <span className="font-bold text-[13px] text-slate-700 truncate pr-2">
                      {analyticsCourse === 'all' ? 'Tất cả khóa học' : courses.find(c => String(c.id) === String(analyticsCourse))?.title || 'Tất cả khóa học'}
                    </span>
                    <span className={`text-slate-400 text-[10px] transition-transform duration-300 ${analyticsDropdownOpen ? 'rotate-180' : ''}`}>▼</span>
                  </div>
                  
                  {analyticsDropdownOpen && (
                    <>
                      <div className="fixed inset-0 z-40" onClick={() => setAnalyticsDropdownOpen(false)}></div>
                      <div className="absolute z-50 mt-2 w-full bg-white border border-slate-200 rounded-xl shadow-xl max-h-72 overflow-y-auto py-2 animate-in fade-in slide-in-from-top-2 duration-200 custom-scrollbar">
                        <div 
                          onClick={() => { setAnalyticsCourse('all'); setAnalyticsDropdownOpen(false); }}
                          className={`px-5 py-3 cursor-pointer text-[13px] font-bold transition-colors ${analyticsCourse === 'all' ? 'bg-[#0ea5e9]/10 text-[#0ea5e9]' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'}`}
                        >
                          Tất cả khóa học
                        </div>
                        {courses.length > 0 && courses.map(course => (
                          <div 
                            key={course.id}
                            onClick={() => { setAnalyticsCourse(course.id); setAnalyticsDropdownOpen(false); }}
                            className={`px-5 py-3 cursor-pointer text-[13px] font-bold truncate transition-colors ${String(analyticsCourse) === String(course.id) ? 'bg-[#0ea5e9]/10 text-[#0ea5e9]' : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'}`}
                            title={course.title}
                          >
                            {course.title}
                          </div>
                        ))}
                      </div>
                    </>
                  )}
                </div>

              </div>
            </div>

            {analyticsTotalTestsDone === 0 ? (
              <div className="bg-white rounded-[2rem] border border-slate-200 py-24 text-center shadow-sm flex flex-col items-center justify-center mx-2 md:mx-0">
                <div className="text-6xl mb-6 opacity-40 grayscale block">📊</div>
                <h3 className="text-xl md:text-2xl font-black text-slate-700 mb-2">Chưa có dữ liệu làm bài hợp lệ</h3>
                <p className="text-slate-500 font-medium text-[14px] md:text-[15px] max-w-md">Hệ thống chỉ tính những bài đạt trên 3.0 điểm (hoặc IELTS Band &gt; 3.0) để đảm bảo phân tích của AI chính xác nhất.</p>
              </div>
            ) : (
              <>
                <div className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 md:gap-6 mx-2 md:mx-0`}>
                  
                  {/* CARD 1: BÀI HOÀN THÀNH */}
                  <div className="bg-white rounded-[2rem] border border-slate-200 shadow-sm p-6 flex flex-col justify-between hover:border-emerald-400 hover:shadow-md transition-all duration-300 group">
                    <div className="flex justify-between items-center mb-4 relative z-10">
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-emerald-400"></span><span className="font-bold text-slate-500 text-[12px] uppercase tracking-widest group-hover:text-emerald-600 transition-colors">Đã làm</span></div>
                      <span className="font-black text-slate-800 text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-20 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorDone" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} bài`, 'Tổng số bài']} contentStyle={{ borderRadius: '12px', fontSize: '13px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                <Area type="monotone" dataKey="cumulativeDone" stroke="#10b981" strokeWidth={3} fill="url(#colorDone)" activeDot={{ r: 6, fill: '#10b981', stroke: '#fff', strokeWidth: 3 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 2: LƯỢT LÀM BÀI */}
                  <div className="bg-white rounded-[2rem] border border-slate-200 shadow-sm p-6 flex flex-col justify-between hover:border-purple-400 hover:shadow-md transition-all duration-300 group">
                    <div className="flex justify-between items-center mb-4 relative z-10">
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-purple-400"></span><span className="font-bold text-slate-500 text-[12px] uppercase tracking-widest group-hover:text-purple-600 transition-colors">Lượt làm</span></div>
                      <span className="font-black text-slate-800 text-2xl">{analyticsTotalTestsDone}</span>
                    </div>
                    <div className="h-20 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorAttempts" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#a855f7" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#a855f7" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} lượt`, 'Trong ngày']} contentStyle={{ borderRadius: '12px', fontSize: '13px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                <Area type="monotone" dataKey="attempts" stroke="#a855f7" strokeWidth={3} fill="url(#colorAttempts)" activeDot={{ r: 6, fill: '#a855f7', stroke: '#fff', strokeWidth: 3 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 3: GIỜ HỌC */}
                  <div className="bg-white rounded-[2rem] border border-slate-200 shadow-sm p-6 flex flex-col justify-between hover:border-orange-400 hover:shadow-md transition-all duration-300 group">
                    <div className="flex justify-between items-center mb-4 relative z-10">
                      <div className="flex items-center gap-2"><span className="w-3 h-3 rounded-full bg-orange-400"></span><span className="font-bold text-slate-500 text-[12px] uppercase tracking-widest group-hover:text-orange-600 transition-colors">Giờ học</span></div>
                      <span className="font-black text-slate-800 text-2xl">{analyticsTotalTimeHours}h</span>
                    </div>
                    <div className="h-20 w-full -mx-2 -mb-2">
                        <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                                <defs>
                                    <linearGradient id="colorTime" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#f97316" stopOpacity={0.3}/>
                                        <stop offset="95%" stopColor="#f97316" stopOpacity={0}/>
                                    </linearGradient>
                                </defs>
                                <XAxis dataKey="name" hide />
                                <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} giờ`, 'Thời gian']} contentStyle={{ borderRadius: '12px', fontSize: '13px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                <Area type="monotone" dataKey="time" stroke="#f97316" strokeWidth={3} fill="url(#colorTime)" activeDot={{ r: 6, fill: '#f97316', stroke: '#fff', strokeWidth: 3 }} />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                  </div>

                  {/* CARD 4: DARK CARD (AVERAGE) */}
                  <div className="bg-slate-900 rounded-[2rem] border border-slate-800 shadow-[0_10px_30px_rgba(15,23,42,0.3)] p-6 flex flex-col justify-center text-center relative overflow-hidden">
                    <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 to-transparent"></div>
                    <h4 className="font-bold text-slate-400 text-[11px] uppercase tracking-widest mb-2 relative z-10">
                        {isIeltsContext ? 'IELTS Average' : 'Điểm Trung Bình'}
                    </h4>
                    <span className="font-black text-white text-4xl relative z-10 drop-shadow-md">
                        {isIeltsContext ? avgIelts : avgScore}
                    </span>
                    <p className="text-[11px] text-slate-500 mt-2 font-medium relative z-10">
                        {isIeltsContext ? '(Dựa trên 4 bài gần nhất)' : '(Toàn bộ hệ thống)'}
                    </p>
                  </div>
                  
                  {/* CARD 5: DARK CARD (TARGET) */}
                  <div className="bg-slate-900 rounded-[2rem] border border-amber-500/50 shadow-[0_10px_30px_rgba(245,158,11,0.15)] p-6 flex flex-col justify-center text-center relative overflow-hidden group hover:border-amber-400 transition-colors">
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-500/20 to-transparent"></div>
                    <div className="absolute -right-2 -bottom-2 text-6xl opacity-10 pointer-events-none group-hover:scale-110 transition-transform">🎯</div>
                    <h4 className="font-bold text-amber-300/80 text-[11px] uppercase tracking-widest mb-2 relative z-10">
                        {isIeltsContext ? 'Mục tiêu IELTS' : 'Mục tiêu Điểm'}
                    </h4>
                    <input 
                        type="number" step="0.5" min="0" max={isIeltsContext ? "9.0" : "100"} 
                        value={targetIelts || ''} 
                        onChange={(e) => handleUpdateTarget(e.target.value)}
                        placeholder="N/A"
                        className="font-black text-amber-400 text-4xl bg-transparent w-full text-center outline-none cursor-pointer placeholder:text-amber-400/30 relative z-10 drop-shadow-md focus:scale-110 transition-transform"
                        title="Click để sửa"
                    />
                    <p className="text-[11px] text-amber-200/50 mt-2 font-medium relative z-10 group-hover:text-amber-200 transition-colors">Click vào số để sửa</p>
                  </div>

                </div>

                {/* KHU VỰC BIỂU ĐỒ IELTS CHI TIẾT */}
                {isIeltsContext && (
                  <div className="mt-8 md:mt-10 bg-white rounded-[2rem] border border-slate-200 shadow-sm overflow-hidden mx-2 md:mx-0 p-6 md:p-10">
                     <div className="flex flex-col xl:flex-row gap-10 xl:gap-16 mb-12">
                        
                        {/* CHART 1: BIỂU ĐỒ 4 KỸ NĂNG IELTS */}
                        <div className="flex-1 w-full">
                           <div className="flex items-center gap-3 mb-6">
                               <div className="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl">📈</div>
                               <h3 className="font-black text-lg md:text-xl text-slate-800 tracking-tight">Biểu đồ 4 Kỹ Năng</h3>
                           </div>
                           <div className="w-full h-[320px] bg-slate-50/50 rounded-2xl p-4 border border-slate-100">
                              <ResponsiveContainer width="100%" height="100%">
                                  <LineChart data={ieltsSkillChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                      <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#64748b', fontWeight: 600 }} dy={10} />
                                      <YAxis domain={[0, 9]} ticks={[0, 3, 5, 7, 9]} axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#64748b', fontWeight: 600 }} />
                                      <Tooltip labelFormatter={(label) => `Ngày ${label}`} contentStyle={{ borderRadius: '12px', fontSize: '13px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                      <Legend iconType="circle" wrapperStyle={{ fontSize: '13px', fontWeight: 'bold', paddingTop: '20px' }} />
                                      
                                      <Line type="monotone" dataKey="Nghe" name="Listening" stroke="#10b981" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Nói" name="Speaking" stroke="#f97316" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Đọc" name="Reading" stroke="#3b82f6" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Viết" name="Writing" stroke="#d946ef" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                  </LineChart>
                              </ResponsiveContainer>
                           </div>
                        </div>
                        
                        {/* CHART 2: BIỂU ĐỒ TỶ LỆ THEO DẠNG BÀI */}
                        <div className="flex-1 w-full">
                           <div className="flex items-center gap-3 mb-6">
                               <div className="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center text-xl">🎯</div>
                               <h3 className="font-black text-lg md:text-xl text-slate-800 tracking-tight">Tỷ Lệ Đúng Từng Dạng (%)</h3>
                           </div>
                           <div className="w-full h-[320px] bg-slate-50/50 rounded-2xl p-4 border border-slate-100">
                              <ResponsiveContainer width="100%" height="100%">
                                  <LineChart data={ieltsTypeChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                      <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#64748b', fontWeight: 600 }} dy={10} />
                                      <YAxis domain={[0, 100]} ticks={[0, 25, 50, 75, 100]} axisLine={false} tickLine={false} tick={{ fontSize: 12, fill: '#64748b', fontWeight: 600 }} />
                                      <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any, name: string) => [`${value}%`, name]} contentStyle={{ borderRadius: '12px', fontSize: '13px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                      <Legend iconType="circle" wrapperStyle={{ fontSize: '13px', fontWeight: 'bold', paddingTop: '20px' }} />
                                      
                                      <Line type="monotone" dataKey="Điền từ" name="Điền từ" stroke="#10b981" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Nhận định" name="T/F/NG" stroke="#f97316" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Trắc nghiệm" name="MCQ/Checkbox" stroke="#3b82f6" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                      <Line type="monotone" dataKey="Matching" name="Matching" stroke="#d946ef" strokeWidth={3} dot={{ r: 4, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 7 }} connectNulls={true} />
                                  </LineChart>
                              </ResponsiveContainer>
                           </div>
                        </div>

                     </div>

                     {/* THANH PROGRESS BAR NẰM NGANG */}
                     <div className="bg-slate-50 rounded-2xl p-6 md:p-8 border border-slate-100">
                         <h3 className="font-black text-[16px] md:text-lg text-slate-800 uppercase tracking-tight mb-6 flex items-center gap-2">
                             <span className="text-emerald-500">🏆</span> Tỷ lệ đúng tích lũy
                         </h3>
                         <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                           {Object.entries(ieltsTypeStats).map(([key, data]) => {
                              const percent = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
                              return (
                                <div key={key} className="bg-white border border-slate-200 rounded-xl p-5 hover:border-[#0ea5e9] hover:shadow-md transition-all duration-300">
                                    <div className="flex justify-between items-end mb-3">
                                        <span className="font-bold text-slate-700 text-[13px]">{key}</span>
                                        <span className="font-black text-[#0ea5e9] text-[18px]">{percent}%</span>
                                    </div>
                                    <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden mb-2 border border-slate-200/50">
                                        <div className="h-full bg-gradient-to-r from-sky-400 to-[#0ea5e9] rounded-full transition-all duration-1000" style={{width: `${percent}%`}}></div>
                                    </div>
                                    <p className="text-[11px] text-slate-400 font-bold text-right tracking-widest">{data.correct} / {data.total} câu</p>
                                </div>
                              );
                           })}
                         </div>
                     </div>
                  </div>
                )}

                {/* BẢNG LỊCH SỬ */}
                <div className="mt-8 md:mt-10 bg-white rounded-[2rem] border border-slate-200 shadow-sm overflow-hidden mx-2 md:mx-0">
                  <div className="px-6 md:px-8 py-5 md:py-6 border-b border-slate-200 flex justify-between items-center bg-white">
                     <h3 className="font-black text-[18px] md:text-xl text-slate-800 tracking-tight flex items-center gap-2">
                         <span className="text-blue-500">📋</span> Lịch sử làm bài
                     </h3>
                  </div>
                  <div className="overflow-x-auto custom-scrollbar bg-slate-50/50" style={{ WebkitOverflowScrolling: 'touch' }}>
                    <table className="w-full text-left border-collapse min-w-[700px]">
                      <thead>
                        <tr className="border-b border-slate-200 text-[12px] text-slate-500 uppercase tracking-widest">
                          <th className="px-6 md:px-8 py-5 font-bold w-2/5">Tên bài kiểm tra</th>
                          <th className="px-6 md:px-8 py-5 font-bold text-center">Ngày làm bài</th>
                          <th className="px-6 md:px-8 py-5 font-bold text-center">Điểm số</th>
                          <th className="px-6 md:px-8 py-5 font-bold text-right">Thao tác</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 bg-white">
                        {paginatedHistory.map(history => {
                          const isHigh = history.scoreObj.value > 60 || parseFloat(history.details?.bandScore) >= 6.0;
                          return (
                          <tr key={history.id} className="hover:bg-slate-50 transition-colors group">
                            <td className="px-6 md:px-8 py-5">
                              <div className="font-bold text-[15px] text-slate-800 mb-2 leading-snug group-hover:text-[#0ea5e9] transition-colors">
                                 {history.name}
                              </div>
                              <div className="flex items-center gap-2">

                              </div>
                            </td>
                            <td className="px-6 md:px-8 py-5 text-center">
                              <div className="font-bold text-[14px] text-slate-700">{formatDate(history.date).split(' ')[0]}</div>
                              <div className="text-[12px] font-medium text-slate-400 mt-1">{formatDate(history.date).split(' ')[1]}</div>
                            </td>
                            <td className="px-6 md:px-8 py-5 text-center">
                              <span className={`inline-flex items-center justify-center px-4 py-2 rounded-lg text-[14px] font-black border ${isHigh ? 'bg-emerald-50 text-emerald-600 border-emerald-200' : 'bg-slate-50 text-slate-700 border-slate-200'}`}>
                                {(() => {
                                   const isIelts = String(history.details?.test_type || history.name).toLowerCase().includes('ielts') || history.details?.bandScore !== undefined;
                                   if (isIelts) {
                                       return `${history.scoreObj.value}/${history.scoreObj.total} - Band ${history.details?.bandScore || '0.0'}`;
                                   } else {
                                       const p = history.scoreObj.total > 0 ? (history.scoreObj.value / history.scoreObj.total) * 100 : 0;
                                       let grade = 'U';
                                       if (p >= 90) grade = 'A*';
                                       else if (p >= 80) grade = 'A';
                                       else if (p >= 70) grade = 'B';
                                       else if (p >= 60) grade = 'C';
                                       else if (p >= 50) grade = 'D';
                                       else if (p >= 40) grade = 'E';
                                       return `${Math.round(p)}% - ${grade}`;
                                   }
                                })()}
                              </span>
                            </td>
                            <td className="px-6 md:px-8 py-5 text-right">
                              <button onClick={() => setViewingHistoryDetail(history)} className="inline-flex items-center bg-white border-2 border-slate-200 text-slate-600 font-bold px-5 py-2.5 rounded-xl hover:border-[#0ea5e9] hover:bg-[#0ea5e9] hover:text-white transition-all text-[12px] uppercase tracking-wider shadow-sm">
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

        {/* =====================================================================
            🚀 TRANG CẤU HÌNH TÀI KHOẢN (PROFILE)
            ===================================================================== */}
        {activeTab === 'profile' && (
          <div className="max-w-xl mx-auto mt-8 md:mt-12 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div className="bg-white p-8 md:p-12 rounded-[2rem] border border-slate-200 shadow-[0_8px_30px_rgba(0,0,0,0.04)] text-center mx-2 md:mx-0">
              
              {/* Avatar */}
              <div className="w-24 h-24 md:w-28 md:h-28 rounded-full bg-gradient-to-tr from-[#0ea5e9] to-indigo-500 text-white flex items-center justify-center font-black text-4xl md:text-5xl mx-auto mb-5 shadow-lg border-4 border-white">
                {displayUserInitial}
              </div>
              <h2 className="text-2xl md:text-3xl font-black text-slate-800 mb-1 tracking-tight">{displayUserName}</h2>
              <p className="text-[#0ea5e9] font-bold mb-8 text-[14px] md:text-[15px] bg-sky-50 inline-block px-4 py-1 rounded-full border border-sky-100 uppercase tracking-widest">
                {userProfile?.role === 'admin' ? 'Quản trị viên' : 'Học viên TonyEnglish'}
              </p>
              
              <div className="space-y-5 border-t border-slate-100 pt-8 text-left">
                <h3 className="font-black text-lg text-slate-800 mb-6">Cài đặt cá nhân</h3>
                
                <div className="space-y-2">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Họ và tên</label>
                  <input type="text" value={newFullName} onChange={e => setNewFullName(e.target.value)} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-5 py-4 font-semibold text-slate-800 focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-[#0ea5e9]/10 outline-none transition-all text-[15px] shadow-sm" placeholder="Nhập họ và tên..." />
                </div>
                
                <div className="space-y-2">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Mục tiêu IELTS</label>
                  <input type="text" value={targetIelts} onChange={e => handleUpdateTarget(e.target.value)} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-5 py-4 font-semibold text-slate-800 focus:border-amber-500 focus:bg-white focus:ring-4 focus:ring-amber-500/10 outline-none transition-all text-[15px] shadow-sm" placeholder="Ví dụ: 7.0" />
                </div>
                
                <div className="space-y-2">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Email đăng nhập</label>
                  <input type="email" defaultValue={currentUser?.email || ""} disabled className="w-full bg-slate-100 border border-slate-200 rounded-xl px-5 py-4 font-semibold text-slate-400 outline-none cursor-not-allowed text-[15px]" />
                </div>
                
                <div className="space-y-2">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Đổi mật khẩu (Tùy chọn)</label>
                  <input type="password" placeholder="••••••••" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} className="w-full bg-slate-50 border border-slate-200 rounded-xl px-5 py-4 font-semibold text-slate-800 focus:border-[#0ea5e9] focus:bg-white focus:ring-4 focus:ring-[#0ea5e9]/10 outline-none transition-all text-[15px] shadow-sm" />
                </div>
                
                <button onClick={handleUpdateProfile} disabled={isUpdatingProfile} className="bg-[#0ea5e9] hover:bg-[#0284c7] disabled:bg-slate-300 text-white font-black px-6 py-4 rounded-xl transition-all w-full mt-6 text-[14px] uppercase tracking-widest shadow-[0_8px_20px_rgba(14,165,233,0.3)] disabled:shadow-none hover:-translate-y-0.5 active:translate-y-0">
                  {isUpdatingProfile ? 'Đang lưu...' : 'Lưu thay đổi'}
                </button>
              </div>
            </div>
          </div>
        )}

      </main>

      {/* POPUP CHI TIẾT LỊCH SỬ */}
      {viewingHistoryDetail && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white rounded-[2rem] w-full max-w-lg shadow-2xl overflow-hidden border border-slate-200 animate-in zoom-in-95">
             <div className="bg-white px-8 py-6 border-b border-slate-100 flex justify-between items-center">
                <h3 className="font-black text-slate-800 text-[14px] uppercase tracking-widest">Bảng Kết Quả</h3>
                <button onClick={() => setViewingHistoryDetail(null)} className="text-slate-400 hover:text-rose-500 w-8 h-8 rounded-full hover:bg-rose-50 flex items-center justify-center transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                </button>
             </div>
             
             <div className="p-8 md:p-10">
                <div className="text-center mb-8 border-b border-slate-100 pb-8">
                   <h2 className="text-2xl font-black text-slate-800 mb-2 leading-tight">{viewingHistoryDetail.name}</h2>
                   <p className="text-slate-500 font-medium text-[13px] mb-8">Nộp lúc: <span className="text-slate-700">{formatDate(viewingHistoryDetail.date)}</span></p>
                   
                   <div className="flex justify-center gap-4">
                      <div className="bg-slate-50 border border-slate-200 px-6 py-5 rounded-2xl flex-1 shadow-sm">
                         <p className="text-[11px] font-bold uppercase text-slate-500 tracking-widest mb-1.5">Thời gian</p>
                         <p className="text-2xl font-black text-slate-800">{viewingHistoryDetail.timeSpent} <span className="text-[13px] font-bold text-slate-500 uppercase">phút</span></p>
                      </div>
                      <div className="bg-emerald-50 border border-emerald-200 px-6 py-5 rounded-2xl flex-1 shadow-sm">
                         <p className="text-[11px] font-bold uppercase text-emerald-600 tracking-widest mb-1.5">Kết quả</p>
                         <p className="text-2xl font-black text-emerald-600">
                           {viewingHistoryDetail.details?.bandScore ? `Band ${viewingHistoryDetail.details.bandScore}` : viewingHistoryDetail.scoreObj.display}
                         </p>
                      </div>
                   </div>
                </div>

                <div className="flex flex-col gap-3">
                    <button onClick={async () => {
                        const testId = viewingHistoryDetail.testId || viewingHistoryDetail.details?.test_id;
                        let foundTest = allTests.find(t => String(t.id) === String(testId));
                        if (!foundTest) foundTest = allTests.find(t => t.title.trim() === viewingHistoryDetail.name.trim());
                        
                        if (foundTest && onStartTest) {
                            // Fetch the FULL test data from the database to guarantee content_json is present
                            const { data: fullTest } = await supabase.from('tests').select('*').eq('id', foundTest.id).single();
                            let testDataToUse = fullTest || foundTest;
                            
                            if (typeof testDataToUse.content_json === 'string') {
                                try { testDataToUse.content_json = JSON.parse(testDataToUse.content_json); } catch(e) { testDataToUse.content_json = {}; }
                            }

                            const type = String(testDataToUse.test_type || '').toLowerCase();
                            let targetMode = 'standard';
                            if (type.includes('igcse-direct')) targetMode = 'igcse-direct';
                            else if (type.includes('igcse')) targetMode = 'igcse';
                            else if (type.includes('split-standard')) targetMode = 'split-standard';
                            else if (type.includes('splitscreen') && type.includes('standard')) targetMode = 'standard-splitscreen';
                            else if (type.includes('standard-reading')) targetMode = 'standard-reading';
                            else if (type.includes('case-study') || type.includes('business')) targetMode = 'case-study';
                            else if (type === 'ielts-writing') targetMode = 'ielts-writing';
                            else if (type === 'ielts-speaking') targetMode = 'ielts-speaking';
                            else if (type.includes('ielts')) targetMode = 'computer';
                            
                            const totalStr = String(viewingHistoryDetail.scoreObj.display).split('/')[1];
                            onStartTest(targetMode, { 
                                ...testDataToUse, 
                                history_id: viewingHistoryDetail.id, 
                                isReview: true,
                                past_answers: viewingHistoryDetail.details?.userAnswers || viewingHistoryDetail.details?.answers || {},
                                past_score: viewingHistoryDetail.scoreObj.value,
                                past_total: totalStr ? totalStr.trim() : 0,
                                past_band: viewingHistoryDetail.details?.bandScore || '0.0',
                                aiFeedback: viewingHistoryDetail.details?.aiFeedback || null
                            });
                            setViewingHistoryDetail(null);
                        } else {
                            alert("Đề thi này không còn tồn tại trên hệ thống.");
                        }
                    }} className="w-full bg-[#0ea5e9] hover:bg-[#0284c7] text-white font-black py-4 rounded-xl transition-colors uppercase tracking-widest text-[13px] shadow-md shadow-blue-500/20">
                        Xem chi tiết chữa bài
                    </button>
                    
                    <button onClick={() => handleRetakeFromHistory(viewingHistoryDetail)} className="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-4 rounded-xl transition-colors uppercase tracking-widest text-[13px]">
                       Làm lại bài này ngay
                    </button>
                </div>
             </div>
          </div>
        </div>
      )}

      {/* POPUP CHỌN CHẾ ĐỘ THI IELTS */}
      {showModeSelection && testToStart && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4 animate-in fade-in duration-200">
          <div className="bg-white w-full max-w-[480px] p-8 md:p-12 rounded-[2rem] shadow-2xl border border-slate-200 animate-in zoom-in-95">
            
            <div className="mb-8 text-center">
              <div className="w-16 h-16 bg-blue-50 rounded-2xl flex items-center justify-center text-3xl mx-auto mb-4 border border-blue-100">
                 🎓
              </div>
              <h2 className="text-[22px] md:text-[24px] font-black text-slate-800 mb-2 leading-tight line-clamp-2" title={testToStart.title}>{testToStart.title}</h2>
              <p className="text-[14px] text-slate-500 font-medium">
                Vui lòng chọn hình thức thi bạn muốn tham gia:
              </p>
            </div>

            <div className="space-y-4">
              <button 
                onClick={() => handleConfirmMode('computer')}
                className="w-full flex items-center p-5 bg-white border-2 border-slate-100 hover:border-[#0ea5e9] hover:shadow-md hover:-translate-y-1 rounded-2xl transition-all duration-300 text-left group cursor-pointer"
              >
                <div className="w-14 h-14 shrink-0 flex items-center justify-center bg-slate-50 text-slate-400 group-hover:bg-[#0ea5e9] group-hover:text-white rounded-xl mr-5 transition-colors duration-300">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-7 h-7">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 17.25v1.007a3 3 0 0 1-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0 1 15 18.257V17.25m6-12V15a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 15V5.25m18 0A2.25 2.25 0 0 0 18.75 3H5.25A2.25 2.25 0 0 0 3 5.25m18 0V12a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 12V5.25" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[16px] font-black text-slate-800 group-hover:text-[#0ea5e9] transition-colors">Thi trên máy tính</h3>
                  <p className="text-[13px] text-slate-500 mt-1 font-medium">Giao diện chuẩn Computer-delivered</p>
                </div>
              </button>

              <button 
                onClick={() => handleConfirmMode('paper')}
                className="w-full flex items-center p-5 bg-white border-2 border-slate-100 hover:border-emerald-500 hover:shadow-md hover:-translate-y-1 rounded-2xl transition-all duration-300 text-left group cursor-pointer"
              >
                <div className="w-14 h-14 shrink-0 flex items-center justify-center bg-slate-50 text-slate-400 group-hover:bg-emerald-500 group-hover:text-white rounded-xl mr-5 transition-colors duration-300">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-7 h-7">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[16px] font-black text-slate-800 group-hover:text-emerald-600 transition-colors">Thi trên giấy</h3>
                  <p className="text-[13px] text-slate-500 mt-1 font-medium">Làm trên giấy, xem đề PDF & nghe Audio</p>
                </div>
              </button>
            </div>

            <div className="mt-8 pt-4 flex justify-center">
              <button 
                onClick={() => setShowModeSelection(false)}
                className="text-[13px] font-black text-slate-400 hover:text-slate-600 hover:bg-slate-100 uppercase tracking-widest transition-colors py-3 px-8 rounded-xl"
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