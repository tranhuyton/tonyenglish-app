import React, { useState, useEffect, useRef, useMemo } from 'react';
import { supabase } from './supabase';
import AssignmentCalendar from './AssignmentCalendar';
import TaskBoard from './TaskBoard';
import { LineChart, Line, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { BoardTheme, DEFAULT_BOARD_THEME, BoardThemeModal, createCustomTheme, loadTheme, saveTheme } from './ThemeModal';

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
const ACTIVITIES_PER_PAGE = 8;

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
  if (t.includes('biology')) return { image: '/images/biology_cover.jpg', badge: 'Biology', color: 'text-emerald-600' };
  if (t.includes('chemistry')) return { image: '/images/chemistry_cover.jpg', badge: 'Chemistry', color: 'text-cyan-600' };
  if (t.includes('physics')) return { image: '/images/physics_cover.jpg', badge: 'Physics', color: 'text-indigo-600' };
  if (t.includes('geography')) return { image: 'https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&q=80&w=800', badge: 'Geography', color: 'text-amber-600' };
  if (t.includes('science')) return { image: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&q=80&w=800', badge: 'Science', color: 'text-teal-600' };
  if (t.includes('math')) return { image: 'https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&q=80&w=800', badge: 'Mathematics', color: 'text-purple-600' };
  if (t.includes('econ')) return { image: 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&q=80&w=800', badge: 'Economics', color: 'text-amber-600' };
  if (t.includes('business')) return { image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800', badge: 'Business', color: 'text-blue-600' };
  if (t.includes('pronunciation') || t.includes('phát âm')) return { image: 'https://images.unsplash.com/photo-1590402494587-44b71d7772f6?auto=format&fit=crop&q=80&w=800', badge: 'Pronunciation', color: 'text-rose-500' };
  if (t.includes('reflex') || t.includes('phản ứng') || t.includes('phản xạ')) return { image: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&q=80&w=800', badge: 'Comm. Reflex', color: 'text-orange-500' };
  if (t.includes('communication') || t.includes('giao tiếp')) return { image: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800', badge: 'Communication', color: 'text-pink-600' };
  if (t.includes('esl') || t.includes('english')) return { image: 'https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&q=80&w=800', badge: 'ESL Program', color: 'text-rose-600' };
  if (t.includes('ielts') || course.type === 'IELTS') return { image: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=800', badge: 'IELTS Mastery', color: 'text-blue-600' };
  return { image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=800', badge: course.type || 'Khóa học', color: 'text-slate-600' };
};

export default function StudentPortal({ onNavigate, onStartTest, onOpenLecture }: any) {
  const [isLoading, setIsLoading] = useState(true);
  
  const [activeTab, setActiveTab] = useState<'library'|'calendar'|'board'|'analytics'|'profile'>(() => {
    const saved = sessionStorage.getItem('lms_portal_tab');
    if (saved === 'library' || saved === 'calendar' || saved === 'board' || saved === 'analytics' || saved === 'profile') {
      return saved as 'library'|'calendar'|'board'|'analytics'|'profile';
    }
    return 'library';
  });

  useEffect(() => {
    sessionStorage.setItem('lms_portal_tab', activeTab);
  }, [activeTab]);
  
  const [activeView, setActiveView] = useState<'dashboard'|'course'>(() => {
      return (sessionStorage.getItem('portal_active_view') as any) || 'dashboard';
  });

  useEffect(() => {
    sessionStorage.setItem('portal_active_view', activeView);
  }, [activeView]);
  
  const [selectedCourseId, setSelectedCourseId] = useState<string | null>(() => {
      return sessionStorage.getItem('portal_selected_course_id') || null;
  });

  useEffect(() => {
    if (selectedCourseId) {
      sessionStorage.setItem('portal_selected_course_id', selectedCourseId);
    } else {
      sessionStorage.removeItem('portal_selected_course_id');
    }
  }, [selectedCourseId]);
  
  const [currentFolderId, setCurrentFolderId] = useState<string | null>(() => {
      return sessionStorage.getItem('portal_current_folder_id') || null;
  });

  useEffect(() => {
    if (currentFolderId) {
      sessionStorage.setItem('portal_current_folder_id', currentFolderId);
    } else {
      sessionStorage.removeItem('portal_current_folder_id');
    }
  }, [currentFolderId]);

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
  
  const [courseTargets, setCourseTargets] = useState<Record<string, string>>(() => {
      try {
          const raw = localStorage.getItem('tony_course_targets');
          if (raw) return JSON.parse(raw);
          // Migrate from legacy single-value format
          const legacy = localStorage.getItem('tony_target_ielts');
          if (legacy) return { ielts: legacy };
          return { ielts: '6.5' };
      } catch (e) {
          return { ielts: '6.5' };
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
  const [activityPage, setActivityPage] = useState(1);

  const [analyticsCourse, setAnalyticsCourse] = useState(() => localStorage.getItem('portal_filter_course') || 'all');
  const [analyticsDropdownOpen, setAnalyticsDropdownOpen] = useState(false);
  const [boardTemplates, setBoardTemplates] = useState<any[]>([]);
  const [dayPlanTaskCourseMap, setDayPlanTaskCourseMap] = useState<Record<string, string>>({});
  const [filterCourse, setFilterCourse] = useState(() => localStorage.getItem('portal_filter_course') || 'all');
  const [filterCourseDropdownOpen, setFilterCourseDropdownOpen] = useState(false);
  
  useEffect(() => {
    localStorage.setItem('portal_filter_course', filterCourse);
    if (analyticsCourse !== filterCourse) {
      setAnalyticsCourse(filterCourse);
    }
    setActivityPage(1);
  }, [filterCourse]);

  useEffect(() => {
    setActivityPage(1);
  }, [analyticsCourse]);

  const [analyticsTestType, setAnalyticsTestType] = useState<'ielts' | 'ielts-standard' | 'standard'>('ielts');
  const [analyticsCategory, setAnalyticsCategory] = useState('all');
  const [viewingHistoryDetail, setViewingHistoryDetail] = useState<any>(null);

  const [analyticsView, setAnalyticsView] = useState<'scores'|'activity'>(() => {
    const saved = sessionStorage.getItem('portal_analytics_view');
    return (saved === 'scores' || saved === 'activity') ? saved : 'scores';
  });
  useEffect(() => {
    sessionStorage.setItem('portal_analytics_view', analyticsView);
  }, [analyticsView]);
  const [analyticsTheme, setAnalyticsTheme] = useState<BoardTheme>(() => loadTheme(`tony_analytics_theme_${currentUser?.id}`, 'tony_analytics_theme'));
  const [isAnalyticsThemeModalOpen, setIsAnalyticsThemeModalOpen] = useState(false);
  const [studentActivities, setStudentActivities] = useState<any[]>([]);

  // Reload theme when currentUser becomes available
  useEffect(() => {
    if (currentUser?.id) {
      setAnalyticsTheme(loadTheme(`tony_analytics_theme_${currentUser.id}`, 'tony_analytics_theme'));
    }
  }, [currentUser?.id]);

  useEffect(() => {
    if ((analyticsView === 'activity' || activeTab === 'analytics') && currentUser?.id) {
      supabase.from('activity_logs').select('*').eq('user_id', currentUser.id).order('created_at', { ascending: false }).limit(200)
        .then(({ data }) => setStudentActivities(data || []));
    }
  }, [analyticsView, activeTab, currentUser?.id]);

  const handleSelectAnalyticsTheme = (theme: BoardTheme) => {
    setAnalyticsTheme(theme);
    saveTheme(`tony_analytics_theme_${currentUser?.id}`, theme, 'tony_analytics_theme');
  };
  const handleApplyCustomAnalyticsColor = (hex: string) => {
    handleSelectAnalyticsTheme(createCustomTheme(hex));
  };
  
  const [showModeSelection, setShowModeSelection] = useState(false);
  const [testToStart, setTestToStart] = useState<any>(null);

  const [newFullName, setNewFullName] = useState('');
  const [isUpdatingProfile, setIsUpdatingProfile] = useState(false);
  const [profileSuccessMsg, setProfileSuccessMsg] = useState('');
  const [profileErrorMsg, setProfileErrorMsg] = useState('');

  // 🔐 Đổi mật khẩu trong trang cá nhân
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showNewPassword, setShowNewPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [isChangingPassword, setIsChangingPassword] = useState(false);
  const [passwordSuccessMsg, setPasswordSuccessMsg] = useState('');
  const [passwordErrorMsg, setPasswordErrorMsg] = useState('');

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
    const handlePortalSync = () => {
      const savedTab = sessionStorage.getItem('lms_portal_tab');
      if (savedTab && (savedTab === 'library' || savedTab === 'calendar' || savedTab === 'board' || savedTab === 'analytics' || savedTab === 'profile')) {
        setActiveTab(savedTab as any);
      }
      const savedCourse = localStorage.getItem('portal_filter_course') || sessionStorage.getItem('portal_filter_course');
      if (savedCourse) {
        setFilterCourse(savedCourse);
      }
    };
    handlePortalSync();
    window.addEventListener('tony-portal-sync', handlePortalSync);
    return () => window.removeEventListener('tony-portal-sync', handlePortalSync);
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

        // Step 1: Fetch user-specific records — each query wrapped to prevent cascading failure
        const safeQuery = async (name: string, queryFn: () => any) => {
            try {
                const result = await queryFn();
                if (result.error) console.warn(`[${name}] error:`, result.error);
                return result;
            } catch (e) { console.error(`[${name}] CRASH:`, e); return { data: null, error: e }; }
        };
        const [profileRes, lpRes, cStudentsRes, enrollsRes, hDataRes, assignRes, boardTempRes, dayPlanTasksRes] = await Promise.all([
            safeQuery('profiles', () => supabase.from('profiles').select('*').eq('id', user.id).single()),
            safeQuery('lecture_progress', () => supabase.from('lecture_progress').select('lecture_id, is_completed').eq('user_id', user.id).limit(5000)),
            safeQuery('class_students', () => supabase.from('class_students').select('class_id').eq('user_id', user.id)),
            safeQuery('enrollments', () => supabase.from('enrollments').select('course_id').eq('user_id', user.id)),
            safeQuery('test_results', () => supabase.from('test_results').select('id, test_title, course_id, score, total_score, time_spent, created_at, test_type, details').eq('user_id', user.id).order('created_at', { ascending: false }).limit(1000)),
            safeQuery('assignments', () => supabase.from('assignments').select('*').eq('user_id', user.id).order('due_date', { ascending: true }).limit(5000)),
            safeQuery('board_templates', () => supabase.from('board_templates').select('id, title, course_id')),
            safeQuery('day_plan_tasks', () => supabase.from('day_plan_tasks').select('title, course_day_plans(course_id)'))
        ]);
        const profile = profileRes.data;
        const isUserAdmin = user.email?.toLowerCase().includes('admin') || profile?.role === 'admin';
        if (profile && !isUserAdmin && profile.status === 'inactive') {
            await supabase.auth.signOut();
            alert("⛔ Tài khoản học của bạn hiện đang ở trạng thái TẠM DỪNG.\nVui lòng liên hệ trung tâm / quản trị viên để được hỗ trợ kích hoạt lại nhé!");
            if (onNavigate) onNavigate('home');
            setIsLoading(false);
            return;
        }
        const lp = lpRes.data;
        const cStudents = cStudentsRes.data;
        const enrolls = enrollsRes.data;
        const hData = hDataRes.data;
        const assignData = assignRes.data;
        setBoardTemplates(boardTempRes.data || []);
        if (dayPlanTasksRes.data) {
          const map: Record<string, string> = {};
          dayPlanTasksRes.data.forEach((item: any) => {
            const cId = item.course_day_plans?.course_id;
            if (cId && item.title) {
              map[item.title.trim()] = String(cId);
            }
          });
          setDayPlanTaskCourseMap(map);
        }
        console.log('[PORTAL INIT] profile:', !!profile, 'lp:', lp?.length, 'enrolls:', enrolls?.length, 'hData:', hData?.length, 'assigns:', assignData?.length);

        setUserProfile(profile);
        if (profile) {
            if (!newFullName) setNewFullName(profile.full_name || '');
            if (profile.avatar_url) {
                try {
                    const parsed = JSON.parse(profile.avatar_url);
                    if (typeof parsed === 'object' && parsed !== null) {
                        setCourseTargets(parsed);
                        try { localStorage.setItem('tony_course_targets', JSON.stringify(parsed)); } catch(e) {}
                    }
                } catch(e) {
                    // Legacy single-value format: treat as IELTS target
                    const legacy = profile.avatar_url.toString();
                    const migrated = { ielts: legacy };
                    setCourseTargets(migrated);
                    try { localStorage.setItem('tony_course_targets', JSON.stringify(migrated)); } catch(e2) {}
                }
            }
        }
        
        setLectureProgressData(lp || []);
        if (cStudents) setUserClassIds(cStudents.map(c => c.class_id));

        let finalAssignments = assignData || [];
        
        if (hData && hData.length > 0 && finalAssignments.length > 0) {
            const passedTestIds = new Set<string>();
            hData.forEach((h: any) => {
                let detailsObj = h.details || {};
                if (typeof detailsObj === 'string') {
                    try { detailsObj = JSON.parse(detailsObj); } catch(e) {}
                }
                const testId = String(h.test_id || detailsObj?.test_id || '');
                if (!testId || testId === 'undefined') return;

                const score = parseFloat(h.score != null ? h.score : 0);
                const total = parseFloat(h.total_score != null ? h.total_score : 0);
                let isPassed = false;
                if (detailsObj?.bandScore != null && !isNaN(parseFloat(detailsObj.bandScore))) {
                    isPassed = parseFloat(detailsObj.bandScore) >= 4.0;
                } else if (total > 0) {
                    isPassed = (score / total) >= 0.5;
                } else {
                    isPassed = score >= 5.0;
                }
                if (isPassed) {
                    passedTestIds.add(testId);
                }
            });
            
            const toUpdate = finalAssignments.filter((a: any) => a.task_type === 'test' && !a.is_completed && a.test_id && passedTestIds.has(String(a.test_id)));
            
            if (toUpdate.length > 0) {
                toUpdate.forEach(async (a: any) => {
                    await supabase.from('assignments')
                        .update({ is_completed: true, updated_at: new Date().toISOString() })
                        .eq('id', a.id);
                });
                
                finalAssignments = finalAssignments.map((a: any) => 
                    toUpdate.some((ua: any) => ua.id === a.id) ? { ...a, is_completed: true } : a
                );
            }
        }

        setAssignments(finalAssignments);

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
                fetchAllPages((from, to) => supabase.from('lectures').select('id, title, course_id, module_id, task_list, order_index, is_published').eq('is_published', true).in('course_id', courseIds).order('id').range(from, to)),
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

            console.log('[REPORT DEBUG] hData raw count:', hData?.length, 'validHistory count:', validHistory.length);
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

  const handleUpdateProfile = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    setIsUpdatingProfile(true);
    setProfileSuccessMsg('');
    setProfileErrorMsg('');
    try {
      if (newFullName.trim() && currentUser?.id) {
        const { error } = await supabase.from('profiles').update({ full_name: newFullName.trim() }).eq('id', currentUser.id);
        if (error) throw error;
        if (userProfile) {
          setUserProfile({ ...userProfile, full_name: newFullName.trim() });
        }
      }
      setProfileSuccessMsg('✓ Đã lưu thông tin cá nhân thành công!');
      setTimeout(() => setProfileSuccessMsg(''), 4000);
    } catch (error: any) { 
      setProfileErrorMsg('Lỗi cập nhật: ' + (error.message || 'Vui lòng thử lại sau.')); 
    } finally { 
      setIsUpdatingProfile(false); 
    }
  };

  const handleChangePassword = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    setPasswordSuccessMsg('');
    setPasswordErrorMsg('');

    if (!newPassword || newPassword.length < 6) {
      setPasswordErrorMsg('Mật khẩu mới phải có tối thiểu 6 ký tự!');
      return;
    }

    if (newPassword !== confirmPassword) {
      setPasswordErrorMsg('Mật khẩu xác nhận không khớp với mật khẩu mới!');
      return;
    }

    setIsChangingPassword(true);
    try {
      const { error } = await supabase.auth.updateUser({ password: newPassword });
      if (error) throw error;
      setNewPassword('');
      setConfirmPassword('');
      setPasswordSuccessMsg('✓ Đổi mật khẩu thành công! Mật khẩu mới đã được cập nhật.');
      setTimeout(() => setPasswordSuccessMsg(''), 5000);
    } catch (error: any) {
      setPasswordErrorMsg('Lỗi đổi mật khẩu: ' + (error.message || 'Vui lòng thử lại sau.'));
    } finally {
      setIsChangingPassword(false);
    }
  };

  // ====== GRADE CONVERSION HELPERS ======
  const GRADE_SCALE = [
    { grade: 'A*', min: 90, color: 'text-emerald-400' },
    { grade: 'A',  min: 80, color: 'text-emerald-300' },
    { grade: 'B',  min: 70, color: 'text-sky-300' },
    { grade: 'C',  min: 60, color: 'text-yellow-300' },
    { grade: 'D',  min: 50, color: 'text-orange-300' },
    { grade: 'E',  min: 40, color: 'text-red-300' },
    { grade: 'U',  min: 0,  color: 'text-slate-400' },
  ];
  const percentToGrade = (p: number): string => {
    for (const g of GRADE_SCALE) { if (p >= g.min) return g.grade; }
    return 'U';
  };
  const gradeToMinPercent = (grade: string): number => {
    return GRADE_SCALE.find(g => g.grade === grade)?.min ?? 0;
  };

  const getTargetForCourse = (courseId: string | null, isIelts: boolean): string => {
    if (isIelts) return courseTargets.ielts || '6.5';
    if (!courseId || courseId === 'all') return '';
    return courseTargets[courseId] || '';
  };

  const handleUpdateTarget = async (courseKey: string, newVal: string) => {
      const updated = { ...courseTargets, [courseKey]: newVal };
      setCourseTargets(updated);
      try { localStorage.setItem('tony_course_targets', JSON.stringify(updated)); } catch(e) {}
      if (userProfile) {
          setUserProfile({ ...userProfile, avatar_url: JSON.stringify(updated) });
      }
      if (currentUser?.id) {
          await supabase.from('profiles').update({ avatar_url: JSON.stringify(updated) }).eq('id', currentUser.id);
      }
  };

  // ====== MOTIVATIONAL COMMENT GENERATOR ======
  const getMotivationalComment = (avgPercent: number, targetGrade: string, isIelts: boolean, ieltsAvg: number, ieltsTarget: number): { emoji: string; text: string; color: string } => {
    if (isIelts) {
      if (ieltsAvg <= 0) return { emoji: '📝', text: 'Hãy hoàn thành thêm bài thi để xem phân tích chi tiết nhé!', color: 'text-slate-400' };
      const diff = ieltsAvg - ieltsTarget;
      if (diff >= 1.0) return { emoji: '🏆', text: `Xuất sắc! Em đã vượt mục tiêu ${ieltsTarget} tận ${diff.toFixed(1)} band! Hãy thử thách bản thân với mục tiêu cao hơn nào!`, color: 'text-emerald-500' };
      if (diff >= 0.5) return { emoji: '🎉', text: `Tuyệt vời! Em đã vượt mục tiêu ${ieltsTarget}! Cứ giữ phong độ này nhé, mục tiêu tiếp theo trong tầm tay rồi!`, color: 'text-emerald-500' };
      if (diff >= 0) return { emoji: '✅', text: `Chúc mừng em đã đạt mục tiêu IELTS ${ieltsTarget}! Hãy tiếp tục ôn luyện để giữ vững phong độ nhé!`, color: 'text-emerald-500' };
      if (diff >= -0.5) return { emoji: '💪', text: `Gần lắm rồi! Chỉ cần thêm ${Math.abs(diff).toFixed(1)} band nữa là chạm mục tiêu ${ieltsTarget}. Cố lên em nhé!`, color: 'text-amber-500' };
      if (diff >= -1.0) return { emoji: '📈', text: `Em đang tiến bộ tốt! Khoảng cách đến mục tiêu ${ieltsTarget} chỉ còn ${Math.abs(diff).toFixed(1)} band. Luyện đều đặn mỗi ngày sẽ đạt thôi!`, color: 'text-amber-500' };
      return { emoji: '🌟', text: `Mục tiêu ${ieltsTarget} là thử thách lớn, nhưng kiên trì là chìa khóa! Hãy tập trung vào từng kỹ năng yếu nhất trước nhé.`, color: 'text-sky-500' };
    }
    // Standard courses
    if (avgPercent <= 0) return { emoji: '📝', text: 'Hãy hoàn thành thêm bài tập để xem phân tích chi tiết nhé!', color: 'text-slate-400' };
    if (!targetGrade) return { emoji: '🎯', text: 'Hãy đặt mục tiêu điểm cho khóa học này để theo dõi tiến độ nhé!', color: 'text-sky-400' };
    const targetMin = gradeToMinPercent(targetGrade);
    const currentGrade = percentToGrade(avgPercent);
    const diff = avgPercent - targetMin;
    const gradeIdx = GRADE_SCALE.findIndex(g => g.grade === currentGrade);
    const targetIdx = GRADE_SCALE.findIndex(g => g.grade === targetGrade);
    if (gradeIdx < targetIdx) return { emoji: '🏆', text: `Xuất sắc! Điểm trung bình ${currentGrade} đã vượt xa mục tiêu ${targetGrade}! Em đang thể hiện rất tốt, hãy giữ phong độ này nhé!`, color: 'text-emerald-500' };
    if (gradeIdx === targetIdx && diff >= 5) return { emoji: '🎉', text: `Tuyệt vời! Em đã đạt và vượt mục tiêu ${targetGrade} rồi! Cứ duy trì đà này là ổn!`, color: 'text-emerald-500' };
    if (gradeIdx === targetIdx) return { emoji: '✅', text: `Chúc mừng! Em đang ở đúng mục tiêu ${targetGrade}. Tiếp tục ôn luyện để giữ vững và nâng cao thêm nhé!`, color: 'text-emerald-500' };
    if (gradeIdx === targetIdx + 1) return { emoji: '💪', text: `Gần lắm rồi! Chỉ cần cải thiện thêm một chút nữa là chạm mục tiêu ${targetGrade}. Cố lên em!`, color: 'text-amber-500' };
    return { emoji: '🌟', text: `Mục tiêu ${targetGrade} đang chờ em phía trước! Hãy tập trung ôn luyện đều đặn, mỗi ngày một chút thôi là sẽ tiến bộ rõ rệt!`, color: 'text-sky-500' };
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
    setFilterCourse(course.id);
    setAnalyticsCourse(course.id);
    setCurrentFolderId(null); 
    setSearchTest(''); 
    setFolderPage(1); 
    setTestPage(1);
    setActiveView('course');
    sessionStorage.setItem('portal_selected_course_id', String(course.id));
    sessionStorage.setItem('portal_active_view', 'course');
    sessionStorage.removeItem('portal_current_folder_id');
  };

  const handleGoToLecture = (courseId?: string, lectureId?: string) => {
    let targetCourseId = courseId;
    if (!targetCourseId || targetCourseId === 'all') {
      if (lectureId && allLectures.length > 0) {
        const found = allLectures.find((l: any) => String(l.id) === String(lectureId));
        if (found?.course_id) targetCourseId = found.course_id;
      }
    }
    if (!targetCourseId || targetCourseId === 'all') {
      targetCourseId = filterCourse !== 'all' ? filterCourse : (selectedCourseId || courses[0]?.id);
    }
    if (targetCourseId && onOpenLecture) {
      resetWorkspaceAndChat();
      onOpenLecture(targetCourseId, lectureId);
    } else {
      setActiveView('dashboard');
      setSelectedCourseId(null);
      setActiveTab('library');
    }
  };

  const handleGoToTestBank = (courseId?: string) => {
    const targetCourseId = courseId || (filterCourse !== 'all' ? filterCourse : (selectedCourseId || courses[0]?.id));
    const targetCourse = courses.find(c => String(c.id) === String(targetCourseId));
    if (targetCourse) {
      handleOpenCourse(targetCourse);
      setActiveTab('library');
    } else {
      setActiveView('dashboard');
      setSelectedCourseId(null);
      setActiveTab('library');
    }
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
        if (!t.folder_id || t.folder_id === 'null' || t.folder_id === '' || !folderCourseMap[t.folder_id]) return;
        let cId = folderCourseMap[t.folder_id] || t.course_id || t.content_json?.basicInfo?.courseId;
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

  // 🛡️ Tự động phát hiện và sửa lỗi folder "lạc trôi" (mismatch giữa các khóa học hoặc folder bị xóa)
  useEffect(() => {
    if (currentFolderId && courseFolders.length > 0) {
      const folderExists = courseFolders.some(f => String(f.id) === String(currentFolderId));
      if (!folderExists) {
        console.warn(`[StudentPortal] Folder ID ${currentFolderId} không tồn tại trong khóa học hiện tại. Đang tự động quay về thư mục gốc.`);
        setCurrentFolderId(null);
        sessionStorage.removeItem('portal_current_folder_id');
      }
    }
  }, [currentFolderId, courseFolders]);

  const courseTests = useMemo(() => {
      if (!selectedCourse) return [];
      const folderIdsSet = new Set(courseFolders.map(f => f.id));
      return allTests.filter(t => t.folder_id && folderIdsSet.has(t.folder_id));
  }, [selectedCourse, allTests, courseFolders]);

  const currentSubFolders = useMemo(() => {
      const validFolderId = (currentFolderId && courseFolders.some(f => String(f.id) === String(currentFolderId))) ? currentFolderId : null;
      return courseFolders.filter(f => validFolderId ? f.parent_id === validFolderId : (!f.parent_id || f.parent_id === 'null' || f.parent_id === '')).sort((a,b) => (a.display_order||0) - (b.display_order||0));
  }, [courseFolders, currentFolderId]);

  const currentTests = useMemo(() => {
      const validFolderId = (currentFolderId && courseFolders.some(f => String(f.id) === String(currentFolderId))) ? currentFolderId : null;
      if (!validFolderId) return [];
      return courseTests.filter(t => t.folder_id === validFolderId);
  }, [courseTests, currentFolderId, courseFolders]);

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
      : (() => {
          const c = courses.find(course => String(course.id) === String(analyticsCourse));
          return (c?.title || '').toLowerCase().includes('ielts') || c?.type === 'IELTS';
        })();
  const isIeltsContext = isIeltsCourseSelected && analyticsTestType === 'ielts';

  // CHUẨN BỊ DỮ LIỆU BÁO CÁO TỪ HISTORY ĐÃ LỌC
  const processedHistory = useMemo(() => {
      return historyData.filter(h => analyticsCourse === 'all' || String(h.courseId) === String(analyticsCourse)).filter(h => {
         if (analyticsCategory === 'all') return true;
         const ft = allTests.find(t => String(t.id) === String(h.testId));
         return (ft?.content_json?.basicInfo?.category || 'test') === analyticsCategory;
      }).filter(h => {
         if (!isIeltsCourseSelected) return true; // Standard only course selected
         
         const course = courses.find(c => String(c.id) === String(h.courseId));
         const isCourseIelts = course ? ((course.title||'').toLowerCase().includes('ielts') || course.type === 'IELTS') : false;
         
         const type = String(h.details?.test_type || h.name).toLowerCase();
         const isIeltsTest = type.includes('ielts') || h.details?.bandScore !== undefined;
         
         if (analyticsTestType === 'ielts') {
            return isCourseIelts && isIeltsTest;
         }
         if (analyticsTestType === 'ielts-standard') {
            return isCourseIelts && !isIeltsTest;
         }
         if (analyticsTestType === 'standard') {
            return !isCourseIelts;
         }
         return true;
      }).sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  }, [historyData, analyticsCourse, analyticsCategory, allTests, isIeltsCourseSelected, analyticsTestType, courses]);

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

  const { analyticsTotalTestsDone, analyticsTotalTimeHours, avgScore, avgScoreRaw, avgIelts, avgIeltsRaw } = useMemo(() => {
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

      const rawStd = stdCount > 0 ? stdSum / stdCount : 0;
      const rawIelts = bandCount > 0 ? bandSum / bandCount : 0;
      const score = stdCount > 0 ? rawStd.toFixed(1) + '%' : '0%';
      const ielts = bandCount > 0 ? rawIelts.toFixed(1) : '0.0';
      
      return { analyticsTotalTestsDone: total, analyticsTotalTimeHours: hours, avgScore: score, avgScoreRaw: rawStd, avgIelts: ielts, avgIeltsRaw: rawIelts };
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

  // LỌC LỊCH SỬ HOẠT ĐỘNG THEO KHÓA HỌC ĐƯỢC CHỌN
  const filteredActivities = useMemo(() => {
    const activeCourseId = filterCourse !== 'all' ? filterCourse : analyticsCourse;
    // Nếu chọn tất cả khóa học thì mới hiện tất cả hoạt động
    if (activeCourseId === 'all') {
      return studentActivities;
    }

    const targetCourseIdStr = String(activeCourseId);

    return studentActivities.filter(act => {
      let details = act.details;
      if (typeof details === 'string') {
        try { details = JSON.parse(details); } catch {}
      }

      // 1. Khớp trực tiếp course_id trong details hoặc act
      if (details?.course_id && String(details.course_id) === targetCourseIdStr) return true;
      if (act.course_id && String(act.course_id) === targetCourseIdStr) return true;

      // 2. Bài giảng (finish_lecture)
      if (act.action_type === 'finish_lecture') {
        const lecId = details?.lecture_id;
        const lecTitle = details?.lecture_title || details?.title || details?.name || (typeof details === 'string' ? details : '');
        if (lecId) {
          const l = allLectures.find(lec => String(lec.id) === String(lecId));
          if (l && String(l.course_id) === targetCourseIdStr) return true;
        }
        if (lecTitle) {
          const clean = String(lecTitle).trim().toLowerCase();
          const exact = allLectures.find(l => l.title && l.title.trim().toLowerCase() === clean);
          if (exact) return String(exact.course_id) === targetCourseIdStr;

          const norm = clean.replace(/[^a-z0-9]/g, '');
          const normMatch = allLectures.find(l => l.title && l.title.toLowerCase().replace(/[^a-z0-9]/g, '') === norm);
          if (normMatch) return String(normMatch.course_id) === targetCourseIdStr;

          const partial = allLectures.find(l => l.title && (l.title.trim().toLowerCase().includes(clean) || clean.includes(l.title.trim().toLowerCase())));
          if (partial) return String(partial.course_id) === targetCourseIdStr;
        }
        return false;
      }

      // 3. Bài kiểm tra (finish_test)
      if (act.action_type === 'finish_test') {
        const testId = details?.test_id;
        const testTitle = details?.test_title || details?.title || details?.name || '';
        if (testId) {
          const t = allTests.find(test => String(test.id) === String(testId));
          if (t && String(t.course_id) === targetCourseIdStr) return true;
        }
        if (testTitle) {
          const clean = String(testTitle).trim().toLowerCase();
          const exact = allTests.find(t => t.title && t.title.trim().toLowerCase() === clean);
          if (exact) return String(exact.course_id) === targetCourseIdStr;

          const norm = clean.replace(/[^a-z0-9]/g, '');
          const normMatch = allTests.find(t => t.title && t.title.toLowerCase().replace(/[^a-z0-9]/g, '') === norm);
          if (normMatch) return String(normMatch.course_id) === targetCourseIdStr;

          const partial = allTests.find(t => t.title && (t.title.trim().toLowerCase().includes(clean) || clean.includes(t.title.trim().toLowerCase())));
          if (partial) return String(partial.course_id) === targetCourseIdStr;

          const hMatch = historyData.find(h => 
            (h.name && h.name.trim().toLowerCase() === clean) ||
            (h.details?.test_title && String(h.details.test_title).trim().toLowerCase() === clean)
          );
          if (hMatch) return String(hMatch.courseId) === targetCourseIdStr;
        }
        return false;
      }

      // 4. Gia sư AI / Luyện nói (call_tutor)
      if (act.action_type === 'call_tutor') {
        const topic = details?.topic || '';
        if (topic) {
          const cleanTopic = String(topic).trim().toLowerCase();
          const selectedCourseObj = courses.find(c => String(c.id) === targetCourseIdStr);
          const isSelectedIelts = selectedCourseObj ? ((selectedCourseObj.title||'').toLowerCase().includes('ielts') || selectedCourseObj.type === 'IELTS') : false;
          if (isSelectedIelts && (cleanTopic.includes('ielts') || cleanTopic.includes('speaking') || cleanTopic.includes('luyện nói') || cleanTopic.includes('voice'))) {
            return true;
          }
          if (selectedCourseObj?.title && cleanTopic.includes(selectedCourseObj.title.toLowerCase())) {
            return true;
          }
        }
        return false;
      }

      return false;
    });
  }, [studentActivities, filterCourse, analyticsCourse, allLectures, allTests, historyData, courses]);

  const totalActivityPages = Math.max(1, Math.ceil(filteredActivities.length / ACTIVITIES_PER_PAGE));
  const paginatedActivities = useMemo(() => filteredActivities.slice((activityPage - 1) * ACTIVITIES_PER_PAGE, activityPage * ACTIVITIES_PER_PAGE), [filteredActivities, activityPage]);

  const inProgressTestId = Array.from(inProgressIds)[0];
  const inProgressTest = useMemo(() => allTests.find(t => String(t.id) === inProgressTestId), [allTests, inProgressTestId]);

  const hour = new Date().getHours();
  let bannerConfig = { greeting: '', gradient: '', icon: '', subtitle: '' };
  
  if (hour >= 5 && hour < 12) {
      bannerConfig = { greeting: 'Chào buổi sáng', gradient: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', icon: '🌅', subtitle: 'Bắt đầu ngày mới tràn đầy năng lượng! Một chút nỗ lực hôm nay sẽ mang lại kết quả lớn ngày mai.' };
  } else if (hour >= 12 && hour < 18) {
      bannerConfig = { greeting: 'Chào buổi chiều', gradient: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', icon: '🌤️', subtitle: 'Tiếp tục hành trình chinh phục mục tiêu nào! Giữ vững sự tập trung nhé.' };
  } else {
      bannerConfig = { greeting: 'Chào buổi tối', gradient: 'from-[#073b5c] via-[#0a5482] to-[#0f172a]', icon: '🌙', subtitle: 'Thời gian tĩnh lặng tuyệt vời để tập trung ôn tập và nhìn lại những gì đã học.' };
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
        <button disabled={currentPage === 1} onClick={() => setPage(currentPage - 1)} className="w-10 h-10 rounded-xl flex items-center justify-center bg-white border border-slate-200/90 text-slate-600 hover:border-[#0a5482] hover:text-[#0a5482] hover:bg-sky-50 transition-colors disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 shadow-2xs font-black cursor-pointer">←</button>
        <span className="text-[13px] font-extrabold text-[#0a5482] bg-white px-5 py-2.5 rounded-xl border border-slate-200/90 shadow-2xs">Trang {currentPage} / {totalPages}</span>
        <button disabled={currentPage === totalPages} onClick={() => setPage(currentPage + 1)} className="w-10 h-10 rounded-xl flex items-center justify-center bg-white border border-slate-200/90 text-slate-600 hover:border-[#0a5482] hover:text-[#0a5482] hover:bg-sky-50 transition-colors disabled:opacity-40 disabled:hover:bg-white disabled:hover:border-slate-200 shadow-2xs font-black cursor-pointer">→</button>
      </div>
    );
  };

  const renderTopControls = (
    <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-end gap-2 sm:gap-2.5 w-full sm:w-auto">
      <div className="grid grid-cols-2 gap-2 sm:flex sm:items-center">
        <button
          type="button"
          onClick={() => handleGoToLecture()}
          className="bg-white hover:bg-emerald-50 text-emerald-700 hover:text-emerald-800 border border-emerald-200/90 hover:border-emerald-400 font-bold text-xs sm:text-[13px] px-3 sm:px-3.5 py-2 rounded-xl shadow-2xs transition-all flex items-center justify-center gap-1.5 hover:shadow hover:-translate-y-0.5 active:scale-95 cursor-pointer shrink-0"
          title="Mở bài giảng lý thuyết"
        >
          <span className="text-base">📖</span> <span className="truncate">Bài giảng</span>
        </button>
        <button
          type="button"
          onClick={() => handleGoToTestBank()}
          className="bg-white hover:bg-sky-50 text-[#0a5482] hover:text-[#084266] border border-sky-200/90 hover:border-[#2ab4e8] font-bold text-xs sm:text-[13px] px-3 sm:px-3.5 py-2 rounded-xl shadow-2xs transition-all flex items-center justify-center gap-1.5 hover:shadow hover:-translate-y-0.5 active:scale-95 cursor-pointer shrink-0"
          title="Mở kho đề"
        >
          <span className="text-base">📚</span> <span>Kho đề</span>
        </button>
      </div>

      {/* DROPDOWN CHỌN KHÓA HỌC */}
      <div className="relative w-full sm:w-64 z-40">
        <div 
          onClick={() => setFilterCourseDropdownOpen(!filterCourseDropdownOpen)}
          className="w-full bg-white hover:bg-sky-50/50 border border-slate-200/90 hover:border-[#2ab4e8] rounded-xl px-4 py-2 flex items-center justify-between cursor-pointer shadow-2xs transition-all"
        >
          <span className="font-bold text-[13px] text-[#0a5482] truncate pr-2">
            {filterCourse === 'all' ? 'Tất cả khóa học' : courses.find(c => String(c.id) === String(filterCourse))?.title || 'Tất cả khóa học'}
          </span>
          <span className={`text-[#2ab4e8] text-[10px] transition-transform duration-300 shrink-0 ${filterCourseDropdownOpen ? 'rotate-180' : ''}`}>▼</span>
        </div>
        
        {filterCourseDropdownOpen && (
          <>
            <div className="fixed inset-0 z-40" onClick={() => setFilterCourseDropdownOpen(false)}></div>
            <div className="absolute top-full right-0 mt-2 w-full min-w-[240px] max-h-72 overflow-y-auto bg-white border border-slate-200 rounded-xl shadow-xl z-50 animate-in fade-in slide-in-from-top-2 custom-scrollbar p-1">
              <div 
                onClick={() => {
                  setFilterCourse('all');
                  setAnalyticsCourse('all');
                  setFilterCourseDropdownOpen(false);
                }}
                className={`px-4 py-2.5 text-[13px] font-medium rounded-lg cursor-pointer transition-colors ${filterCourse === 'all' ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
              >
                🌟 Tất cả khóa học
              </div>
              {courses.map(course => (
                <div 
                  key={course.id}
                  onClick={() => {
                    setFilterCourse(course.id);
                    setAnalyticsCourse(course.id);
                    setFilterCourseDropdownOpen(false);
                  }}
                  className={`px-4 py-2.5 text-[13px] font-medium rounded-lg cursor-pointer transition-colors border-t border-slate-100 ${String(filterCourse) === String(course.id) ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                >
                  📖 {course.title}
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );

  const renderBottomControls = (
    <div className="shrink-0 p-0 flex items-center justify-center z-30">
      <div className="bg-white/95 backdrop-blur-md border border-slate-200/90 shadow-xs rounded-xl px-2.5 py-1 flex flex-wrap items-center justify-center gap-2 transition-all">
        {/* NÚT BÀI GIẢNG */}
        <button
          type="button"
          onClick={() => handleGoToLecture()}
          className="bg-white hover:bg-emerald-50 text-emerald-700 hover:text-emerald-800 border border-emerald-200 hover:border-emerald-400 font-bold text-xs px-3 py-1.5 rounded-lg shadow-2xs transition-all flex items-center gap-1.5 cursor-pointer shrink-0 active:scale-95"
          title="Mở bài giảng lý thuyết"
        >
          <span className="text-sm">📖</span> <span>Bài giảng lý thuyết</span>
        </button>

        {/* NÚT KHO ĐỀ */}
        <button
          type="button"
          onClick={() => handleGoToTestBank()}
          className="bg-white hover:bg-sky-50 text-[#0a5482] hover:text-[#084266] border border-sky-200 hover:border-[#2ab4e8] font-bold text-xs px-3 py-1.5 rounded-lg shadow-2xs transition-all flex items-center gap-1.5 cursor-pointer shrink-0 active:scale-95"
          title="Mở kho đề"
        >
          <span className="text-sm">📚</span> <span>Kho đề</span>
        </button>

        <div className="h-4 w-px bg-slate-200 hidden sm:block"></div>

        {/* DROPDOWN CHỌN KHÓA HỌC */}
        <div className="relative w-44 sm:w-56 z-50">
          <div 
            onClick={() => setFilterCourseDropdownOpen(!filterCourseDropdownOpen)}
            className="w-full bg-white hover:bg-sky-50/50 border border-sky-200 hover:border-[#2ab4e8] rounded-lg px-2.5 py-1.5 flex items-center justify-between cursor-pointer shadow-2xs transition-all"
          >
            <div className="flex items-center gap-1.5 min-w-0 pr-1.5">
              <span className="text-slate-400 text-xs">🎓</span>
              <span className="font-bold text-xs text-[#0a5482] truncate">
                {filterCourse === 'all' ? 'Tất cả khóa học' : courses.find(c => String(c.id) === String(filterCourse))?.title || 'Tất cả khóa học'}
              </span>
            </div>
            <span className={`text-[#2ab4e8] text-[10px] transition-transform duration-300 shrink-0 ${filterCourseDropdownOpen ? 'rotate-180' : ''}`}>▼</span>
          </div>
          
          {filterCourseDropdownOpen && (
            <>
              <div className="fixed inset-0 z-40" onClick={() => setFilterCourseDropdownOpen(false)}></div>
              <div className="absolute top-full right-0 mt-2 w-full min-w-[240px] max-h-72 overflow-y-auto bg-white border border-slate-200 rounded-2xl shadow-2xl z-50 animate-in fade-in slide-in-from-top-2 custom-scrollbar p-1">
                <div 
                  onClick={() => {
                    setFilterCourse('all');
                    setAnalyticsCourse('all');
                    setFilterCourseDropdownOpen(false);
                    if (activeView === 'course') {
                      setActiveView('dashboard');
                      setSelectedCourseId(null);
                    }
                  }}
                  className={`px-3.5 py-2 text-xs rounded-xl font-medium cursor-pointer transition-colors ${filterCourse === 'all' ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                >
                  🌟 Tất cả khóa học
                </div>
                {courses.map(course => (
                  <div 
                    key={course.id}
                    onClick={() => {
                      setFilterCourse(course.id);
                      setAnalyticsCourse(course.id);
                      setFilterCourseDropdownOpen(false);
                      if (activeView === 'course') {
                        handleOpenCourse(course);
                      }
                    }}
                    className={`px-3.5 py-2 text-xs rounded-xl font-medium cursor-pointer transition-colors border-t border-slate-100 ${String(filterCourse) === String(course.id) ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                  >
                    📖 {course.title}
                  </div>
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-[100dvh] bg-slate-50 font-sans text-slate-800 overscroll-none w-full flex flex-col pb-16 md:pb-0">
      {/* 1. TOP UTILITY BAR (Đồng bộ với TonyEnglish.vn Layout) */}
      <div className="bg-[#0f172a] text-slate-300 border-b border-slate-800 text-[12px] sm:text-[13px] shrink-0">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 py-1.5 flex flex-wrap items-center justify-between gap-2">
          <div className="hidden md:flex items-center gap-4 flex-wrap">
            <span className="inline-flex items-center gap-1.5 text-slate-200 font-semibold">
              <span className="text-[#2ab4e8]">📞</span> 0982 042 882
            </span>
            <span className="hidden lg:inline-flex items-center gap-1.5 text-slate-300">
              <span className="text-[#2ab4e8]">✉️</span> contact@tonyenglish.vn
            </span>
            <span className="inline-flex items-center gap-1.5 bg-slate-800/90 text-sky-300 px-3 py-0.5 rounded-full text-xs font-semibold border border-slate-700">
              💡 Click đúp vào từ tiếng Anh bất kỳ để tra từ điển
            </span>
          </div>

          <div className="flex items-center justify-between md:justify-end gap-2 sm:gap-3 w-full md:w-auto ml-auto">
            <div className="flex items-center gap-1.5 sm:gap-2">
              <button
                type="button"
                onClick={() => {
                  resetWorkspaceAndChat();
                  window.history.pushState({}, '', '/');
                  onNavigate?.('home');
                }}
                className="inline-flex items-center gap-1 text-xs font-semibold text-slate-300 hover:text-[#2ab4e8] px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 transition-colors cursor-pointer"
              >
                <span>🏠</span>
                <span>Trang chủ</span>
              </button>
              <a
                href="/news"
                onClick={(e) => {
                  e.preventDefault();
                  resetWorkspaceAndChat();
                  window.history.pushState({}, '', '/news');
                  onNavigate?.('home');
                }}
                className="inline-flex items-center gap-1 text-xs font-semibold text-slate-300 hover:text-[#2ab4e8] px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 transition-colors cursor-pointer"
              >
                <span>📚</span>
                <span>Thư viện bài đọc</span>
              </a>
              <a
                href="/videos"
                onClick={(e) => {
                  e.preventDefault();
                  resetWorkspaceAndChat();
                  window.history.pushState({}, '', '/videos');
                  onNavigate?.('home');
                }}
                className="hidden sm:inline-flex items-center gap-1 text-xs font-semibold text-slate-300 hover:text-[#2ab4e8] px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-800 border border-slate-700/80 transition-colors cursor-pointer"
              >
                <span>🎬</span>
                <span>Kho Video</span>
              </a>
            </div>
            <span className="inline-flex items-center gap-1.5 bg-[#0a5482]/80 text-sky-200 px-2.5 py-0.5 rounded-md text-[11px] font-bold border border-sky-700/50">
              🎓 LMS Portal
            </span>
          </div>
        </div>
      </div>

      {/* 2. MAIN STICKY NAVBAR (Đồng bộ 100% với TonyEnglish.vn) */}
      <header className="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40 shadow-xs shrink-0">
        <div className="max-w-7xl w-full mx-auto px-3 sm:px-6 h-15 sm:h-20 flex items-center justify-between gap-2 sm:gap-4 transition-all">
          
          {/* Brand Logo */}
          <div className="flex items-center gap-2 sm:gap-3 cursor-pointer hover:opacity-90 transition-opacity shrink-0" onClick={() => {
              resetWorkspaceAndChat(); 
              setActiveTab('library');
              setActiveView('dashboard');
              setSelectedCourseId(null);
              setCurrentFolderId(null);
          }}>
            <img
              src="/logo-shield.png"
              onError={(e) => {
                (e.currentTarget as HTMLImageElement).src = '/themes/tony/assets/img/logo khong chu.png';
              }}
              alt="TonyEnglish"
              className="h-8 sm:h-11 w-auto object-contain"
            />
            <div className="flex flex-col items-start leading-none">
              <div className="font-black text-[18px] sm:text-[24px] tracking-tight">
                <span className="text-[#2ab4e8]">TONY</span>
                <span className="text-[#0a5482]">ENGLISH</span>
              </div>
              <span className="text-[10px] sm:text-[11px] font-bold uppercase tracking-widest text-slate-400 mt-0.5 hidden sm:block">
                Student Learning Portal
              </span>
            </div>
          </div>

          {/* Desktop Navigation Tabs (Synchronized with Layout.tsx navItems) */}
          <div className="hidden md:flex items-center gap-1 lg:gap-1.5">
            <button 
              onClick={() => { 
                resetWorkspaceAndChat(); 
                setActiveTab('library'); 
                setActiveView('dashboard'); 
                setSelectedCourseId(null); 
                setCurrentFolderId(null);
              }} 
              className={`px-3.5 lg:px-4 py-2 rounded-xl text-[14px] lg:text-[15px] font-bold transition-all whitespace-nowrap inline-flex items-center gap-2 cursor-pointer ${
                activeTab === 'library'
                  ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-200/80'
                  : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
              }`}
            >
              <svg className={`w-4 h-4 ${activeTab === 'library' ? 'text-[#2ab4e8]' : 'text-slate-400'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
              <span>Học tập &amp; Kho đề</span>
            </button>
            <button 
              onClick={() => {
                resetWorkspaceAndChat(); 
                setActiveTab('calendar');
              }} 
              className={`px-3.5 lg:px-4 py-2 rounded-xl text-[14px] lg:text-[15px] font-bold transition-all whitespace-nowrap inline-flex items-center gap-2 cursor-pointer ${
                activeTab === 'calendar'
                  ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-200/80'
                  : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
              }`}
            >
              <svg className={`w-4 h-4 ${activeTab === 'calendar' ? 'text-[#2ab4e8]' : 'text-slate-400'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg>
              <span>Lịch báo bài</span>
            </button>
            <button 
              onClick={() => { resetWorkspaceAndChat(); setActiveTab('board'); }}
              className={`px-3.5 lg:px-4 py-2 rounded-xl text-[14px] lg:text-[15px] font-bold transition-all whitespace-nowrap inline-flex items-center gap-2 cursor-pointer ${
                activeTab === 'board'
                  ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-200/80'
                  : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
              }`}
            >
              <svg className={`w-4 h-4 ${activeTab === 'board' ? 'text-[#2ab4e8]' : 'text-slate-400'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
              </svg>
              <span>Bảng công việc</span>
            </button>
            <button 
              onClick={() => {
                resetWorkspaceAndChat(); 
                setActiveTab('analytics');
              }} 
              className={`px-3.5 lg:px-4 py-2 rounded-xl text-[14px] lg:text-[15px] font-bold transition-all whitespace-nowrap inline-flex items-center gap-2 cursor-pointer ${
                activeTab === 'analytics'
                  ? 'bg-sky-50 text-[#0a5482] shadow-2xs border border-sky-200/80'
                  : 'text-slate-700 hover:text-[#0a5482] hover:bg-slate-50 border border-transparent'
              }`}
            >
              <svg className={`w-4 h-4 ${activeTab === 'analytics' ? 'text-[#2ab4e8]' : 'text-slate-400'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>
              <span>Báo cáo</span>
            </button>
          </div>

          {/* Right Action Controls */}
          <div className="flex items-center gap-2 sm:gap-3 shrink-0">
            <button
              type="button"
              onClick={() => {
                resetWorkspaceAndChat();
                window.history.pushState({}, '', '/');
                onNavigate?.('home');
              }}
              className="hidden sm:inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-sky-50 text-[#0a5482] border border-slate-200/80 hover:border-sky-200 text-xs sm:text-[13px] font-bold transition-all cursor-pointer shrink-0"
              title="Quay ra Cổng thông tin, Thư viện bài đọc & Kho Video TonyEnglish.vn"
            >
              <span>🌐</span>
              <span>Trang chủ &amp; Thư viện</span>
            </button>

            <div className="hidden lg:flex items-center">
              <button onClick={toggleFullScreen} className="w-9 h-9 rounded-xl flex items-center justify-center text-slate-500 hover:bg-slate-100 border border-transparent hover:border-slate-200 hover:text-[#0a5482] transition-colors cursor-pointer" title="Toàn màn hình">
                {isFullscreen ? <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M9 9V4.5M9 9H4.5M9 9L3.75 3.75M9 15v4.5M9 15H4.5M9 15l-5.25 5.25M15 9h4.5M15 9V4.5M15 9l5.25-5.25M15 15h4.5M15 15v4.5m0-4.5l5.25 5.25" /></svg> : <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75h-4.5m4.5 0v4.5m0-4.5L15 9m5.25 11.25h-4.5m4.5 0v-4.5m0-4.5L15 15" /></svg>}
              </button>
            </div>

            <div className="relative" ref={dropdownRef}>
              <button onClick={() => setIsDropdownOpen(!isDropdownOpen)} className="flex items-center gap-2.5 bg-slate-50 hover:bg-sky-50/60 pr-2 pl-3.5 py-1.5 rounded-xl border border-slate-200/90 shadow-2xs hover:border-[#2ab4e8] transition-all focus:outline-none group cursor-pointer">
                <div className="text-right hidden sm:block">
                  <div className="font-black text-[13px] text-slate-800 group-hover:text-[#0a5482] transition-colors leading-tight">{displayUserName}</div>
                  <div className="text-[10px] font-bold text-[#2ab4e8] uppercase tracking-wider mt-0.5">
                    {userProfile?.role === 'admin' ? 'Quản trị' : 'Học viên'}
                  </div>
                </div>
                <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-lg bg-gradient-to-br from-[#2ab4e8] to-[#0a5482] text-white flex items-center justify-center font-black shadow-xs text-[13px]">
                  {displayUserInitial}
                </div>
              </button>

              {isDropdownOpen && (
                <div className="absolute right-0 mt-2.5 w-60 bg-white rounded-2xl shadow-xl border border-slate-200/90 py-2 z-50 animate-in fade-in zoom-in-95 duration-200">
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    window.history.pushState({}, '', '/');
                    onNavigate?.('home');
                    setIsDropdownOpen(false); 
                  }} className="sm:hidden w-full text-left px-5 py-3 text-sm font-bold text-[#0a5482] hover:bg-sky-50 flex items-center gap-2 transition-colors border-b border-slate-100">
                    <span>🌐</span> Trang chủ &amp; Thư viện
                  </button>
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('library'); 
                    setActiveView('dashboard'); 
                    setSelectedCourseId(null); 
                    setCurrentFolderId(null); 
                    setIsDropdownOpen(false); 
                  }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0a5482] flex items-center gap-2 transition-colors">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg> Học tập &amp; Kho đề
                  </button>
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('calendar'); 
                    setIsDropdownOpen(false); 
                  }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0a5482] flex items-center gap-2 transition-colors">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg> Lịch báo bài
                  </button>
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('board'); 
                    setIsDropdownOpen(false); 
                  }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0a5482] flex items-center gap-2 transition-colors">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" /></svg> Bảng công việc
                  </button>
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('analytics'); 
                    setIsDropdownOpen(false); 
                  }} className="md:hidden w-full text-left px-5 py-3 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0a5482] flex items-center gap-2 transition-colors">
                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg> Báo cáo
                  </button>
                  <button onClick={() => { 
                    resetWorkspaceAndChat(); 
                    setActiveTab('profile'); 
                    setIsDropdownOpen(false); 
                  }} className="w-full text-left px-5 py-2.5 text-sm font-semibold text-slate-700 hover:bg-sky-50 hover:text-[#0a5482] transition-colors flex items-center gap-2 md:border-t-0 border-t border-slate-100 cursor-pointer">
                    👤 Cấu hình tài khoản
                  </button>
                  {userProfile?.role === 'admin' && (
                    <button onClick={() => {
                      resetWorkspaceAndChat();
                      if(onNavigate) onNavigate('admin');
                    }} className="w-full text-left px-5 py-2.5 text-sm font-black text-[#0a5482] hover:bg-sky-50 transition-colors cursor-pointer">
                      ⚙️ Trang Quản Trị
                    </button>
                  )}
                  <div className="h-px bg-slate-100 my-1"></div>
                  <button onClick={handleLogout} className="w-full text-left px-5 py-2.5 text-sm font-bold text-red-600 hover:bg-red-50 transition-colors cursor-pointer">
                    🚪 Đăng xuất
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      <main className="flex-1 w-full min-h-0 max-w-7xl mx-auto px-3.5 sm:px-6 py-5 sm:py-8 overflow-y-auto custom-scrollbar flex flex-col" style={{ WebkitOverflowScrolling: 'touch' }}>
        
        {activeTab === 'library' && activeView === 'dashboard' && (
          <div className="animate-in fade-in duration-500">
            {/* 🚀 HERO BANNER ĐỒNG BỘ TONYENGLISH.VN */}
            <div className={`relative bg-gradient-to-r ${bannerConfig.gradient} rounded-2xl sm:rounded-3xl p-6 sm:p-8 lg:p-10 mb-8 sm:mb-10 overflow-hidden shadow-lg border border-slate-800/30`}>
              <div className="absolute -top-24 -right-24 w-96 h-96 bg-[#2ab4e8]/15 blur-3xl rounded-full pointer-events-none"></div>
              <div className="absolute -bottom-24 -left-24 w-80 h-80 bg-sky-400/10 blur-3xl rounded-full pointer-events-none"></div>
              
              <div className="relative z-10 flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-6 lg:gap-10">
                <div className="text-white flex-1">
                  <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/15 px-3.5 py-1 rounded-full text-[11px] sm:text-xs font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-3.5">
                    <span>🎓</span>
                    <span>TonyEnglish Student Portal • Góc Học Viên</span>
                  </div>
                  <h2 className="text-2xl sm:text-3xl lg:text-4xl font-black mb-2.5 tracking-tight leading-tight">
                    {bannerConfig.greeting}, <span className="text-[#2ab4e8]">{displayUserName}</span>! <span>{bannerConfig.icon}</span>
                  </h2>
                  <p className="text-slate-200/90 text-sm sm:text-[15px] leading-relaxed max-w-2xl mb-6">
                    {bannerConfig.subtitle}
                  </p>

                  {/* Quick Stats Strip (Đồng bộ với HomePage.tsx) */}
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 sm:gap-3 max-w-2xl">
                    <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2.5">
                      <div className="text-[11px] font-bold uppercase tracking-wider text-sky-200/80">Khóa đang học</div>
                      <div className="text-lg sm:text-xl font-black text-white mt-0.5">{courses.length} <span className="text-xs font-semibold text-slate-300">khóa</span></div>
                    </div>
                    <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2.5">
                      <div className="text-[11px] font-bold uppercase tracking-wider text-sky-200/80">Bài hoàn thành</div>
                      <div className="text-lg sm:text-xl font-black text-emerald-300 mt-0.5">{historyData.length} <span className="text-xs font-semibold text-slate-300">đề</span></div>
                    </div>
                    <div className="bg-white/10 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2.5">
                      <div className="text-[11px] font-bold uppercase tracking-wider text-sky-200/80">Giờ luyện tập</div>
                      <div className="text-lg sm:text-xl font-black text-[#2ab4e8] mt-0.5">{analyticsTotalTimeHours}h</div>
                    </div>
                    <div
                      onClick={() => setActiveTab('analytics')}
                      className="bg-white/10 hover:bg-white/15 backdrop-blur-xs border border-white/15 rounded-xl px-3.5 py-2.5 cursor-pointer transition-colors"
                      title="Xem báo cáo chi tiết"
                    >
                      <div className="text-[11px] font-bold uppercase tracking-wider text-amber-300/90">Mục tiêu</div>
                      <div className="text-lg sm:text-xl font-black text-amber-300 mt-0.5">{courseTargets.ielts || '6.5+'} <span className="text-xs font-normal text-white/70">↗</span></div>
                    </div>
                  </div>
                </div>

                {inProgressTest ? (
                   <div className="bg-white/10 backdrop-blur-md border border-white/20 p-5 sm:p-6 rounded-2xl w-full lg:w-80 shadow-xl text-white hover:bg-white/15 transition-all cursor-pointer group hover:-translate-y-0.5 shrink-0 flex flex-col justify-between" onClick={() => handleStartTestClick(inProgressTest)}>
                      <div>
                        <div className="flex items-center justify-between mb-3">
                           <div className="flex items-center gap-2 bg-amber-400/20 border border-amber-300/30 px-2.5 py-1 rounded-full">
                              <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                              <span className="text-[11px] font-extrabold uppercase tracking-wider text-amber-300">Đang làm dở</span>
                           </div>
                           <span className="text-white/50 group-hover:text-white transition-colors">↗</span>
                        </div>
                        <h3 className="font-extrabold text-base sm:text-lg mb-4 line-clamp-2 leading-snug">{inProgressTest.title}</h3>
                      </div>
                      <button className="w-full bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white font-black py-2.5 px-4 rounded-xl text-[13px] transition-colors uppercase tracking-wider shadow-md cursor-pointer">
                         Tiếp tục làm bài →
                      </button>
                   </div>
                ) : courses.length > 0 && (
                  <div className="bg-white/10 backdrop-blur-md border border-white/20 p-5 sm:p-6 rounded-2xl w-full lg:w-80 shadow-xl text-white hover:bg-white/15 transition-all cursor-pointer group hover:-translate-y-0.5 shrink-0 flex flex-col justify-between" onClick={() => handleOpenCourse(courses[0])}>
                    <div>
                      <div className="flex items-center justify-between mb-3">
                         <span className="text-[11px] font-extrabold uppercase tracking-wider text-[#2ab4e8] bg-white/10 border border-white/15 px-3 py-1 rounded-full">Lộ trình trọng tâm</span>
                         <span className="text-white/50 group-hover:text-white transition-colors">↗</span>
                      </div>
                      <h3 className="font-extrabold text-base sm:text-lg mb-2 line-clamp-2 leading-snug">{courses[0].title}</h3>
                      <p className="text-xs text-slate-300 mb-4">Truy cập hệ thống bài giảng lý thuyết &amp; kho đề luyện tập chuẩn quốc tế.</p>
                    </div>
                    <button className="w-full bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white font-black py-2.5 px-4 rounded-xl text-[13px] transition-colors uppercase tracking-wider shadow-md cursor-pointer">
                       Vào học ngay →
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* BẢNG CẢNH BÁO DEADLINE (To-do list) */}
            {upcomingDeadlines.length > 0 && (
                <div className="bg-white border border-rose-200/90 rounded-2xl sm:rounded-3xl p-5 sm:p-7 mb-8 sm:mb-10 shadow-xs flex flex-col md:flex-row items-start gap-5 animate-in slide-in-from-bottom-4 relative overflow-hidden">
                    <div className="absolute top-0 left-0 w-1.5 h-full bg-rose-500"></div>
                    <div className="w-14 h-14 rounded-2xl bg-rose-50 border border-rose-100 flex items-center justify-center text-2xl shrink-0">
                        ⏰
                    </div>
                    <div className="flex-1 min-w-0 w-full">
                        <h3 className="font-black text-slate-800 text-lg sm:text-xl mb-1 tracking-tight">Nhiệm vụ cần hoàn thành</h3>
                        <p className="text-slate-500 text-sm font-medium mb-4">Bạn có <span className="text-rose-600 font-bold">{upcomingDeadlines.length} bài tập</span> sắp đến hạn nộp.</p>
                        
                        <div className="flex flex-col gap-2.5">
                            {upcomingDeadlines.slice(0, 3).map(t => {
                                const dDate = new Date(t._deadlineStr);
                                const isOverdue = dDate < new Date();
                                return (
                                    <div key={t.id} onClick={() => handleStartTestClick(t)} className="flex justify-between items-center bg-slate-50/80 hover:bg-sky-50/40 p-3.5 sm:p-4 rounded-xl border border-slate-200/80 hover:border-[#2ab4e8] cursor-pointer transition-all group">
                                        <div className="flex items-center gap-3 min-w-0">
                                            <div className="w-4 h-4 rounded-full border-2 border-slate-300 group-hover:border-[#0a5482] transition-colors shrink-0"></div>
                                            <span className="font-bold text-slate-700 text-[14px] sm:text-[15px] truncate group-hover:text-[#0a5482] transition-colors">{t.title}</span>
                                        </div>
                                        <span className={`shrink-0 text-[11px] font-black px-3 py-1 rounded-lg whitespace-nowrap border ${isOverdue ? 'bg-rose-100 text-rose-700 border-rose-200' : 'bg-amber-50 text-amber-700 border-amber-200'}`}>
                                            {isOverdue ? '⚠️ QUÁ HẠN' : '⏳ ' + formatDate(t._deadlineStr)}
                                        </span>
                                    </div>
                                )
                            })}
                            {upcomingDeadlines.length > 3 && (
                                <button onClick={() => setActiveTab('calendar')} className="text-[13px] font-bold text-[#0a5482] hover:text-[#2ab4e8] transition-colors self-start mt-1 cursor-pointer">
                                    Xem thêm {upcomingDeadlines.length - 3} nhiệm vụ khác →
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            )}

            {/* SECTION HEADER: KHÓA HỌC CỦA TÔI (Đồng bộ với HomePage.tsx) */}
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
                <div className="flex items-center gap-3">
                    <span className="w-1.5 h-7 bg-[#0a5482] rounded-full"></span>
                    <div>
                        <span className="text-[11px] font-extrabold uppercase tracking-widest text-[#2ab4e8] block">
                            Chương trình đào tạo &amp; Luyện đề
                        </span>
                        <h2 className="font-black text-xl sm:text-2xl md:text-3xl text-slate-900 tracking-tight m-0">Khóa học của tôi</h2>
                    </div>
                </div>
                <div className="relative w-full sm:w-64 z-30">
                    <div 
                        onClick={() => setFilterCourseDropdownOpen(!filterCourseDropdownOpen)}
                        className="w-full bg-white border border-slate-200/90 rounded-xl px-4 py-2.5 flex items-center justify-between cursor-pointer hover:border-[#2ab4e8] shadow-2xs transition-all"
                    >
                        <span className="font-bold text-[13px] text-[#0a5482] truncate pr-2">
                        {filterCourse === 'all' ? 'Tất cả khóa học' : courses.find(c => String(c.id) === String(filterCourse))?.title || 'Tất cả khóa học'}
                        </span>
                        <span className={`text-[#2ab4e8] text-[10px] transition-transform duration-300 ${filterCourseDropdownOpen ? 'rotate-180' : ''}`}>▼</span>
                    </div>
                    
                    {filterCourseDropdownOpen && (
                        <>
                        <div className="fixed inset-0 z-40" onClick={() => setFilterCourseDropdownOpen(false)}></div>
                        <div className="absolute top-full right-0 mt-2 w-full sm:w-64 max-h-72 overflow-y-auto bg-white border border-slate-200 rounded-xl shadow-xl z-50 animate-in fade-in slide-in-from-top-2 custom-scrollbar p-1">
                            <div 
                            onClick={() => { setFilterCourse('all'); setFilterCourseDropdownOpen(false); }}
                            className={`px-4 py-2.5 text-[13px] rounded-lg font-medium cursor-pointer transition-colors ${filterCourse === 'all' ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                            >
                            🌟 Tất cả khóa học
                            </div>
                            {courses.map(course => (
                            <div 
                                key={course.id}
                                onClick={() => { setFilterCourse(course.id); setFilterCourseDropdownOpen(false); }}
                                className={`px-4 py-2.5 text-[13px] rounded-lg font-medium cursor-pointer transition-colors border-t border-slate-100 ${String(filterCourse) === String(course.id) ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                            >
                                📖 {course.title}
                            </div>
                            ))}
                        </div>
                        </>
                    )}
                </div>
            </div>
            
            {isLoading ? (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                 {[1,2].map(i => (
                   <div key={i} className="bg-white rounded-2xl sm:rounded-3xl h-[280px] w-full border border-slate-200/90 p-6 animate-pulse flex flex-col justify-between">
                      <div className="h-40 w-full bg-slate-100 rounded-xl mb-4"></div>
                      <div className="h-6 w-1/2 bg-slate-100 rounded-md"></div>
                      <div className="h-2 w-full bg-slate-100 rounded-full mt-auto"></div>
                   </div>
                 ))}
              </div>
            ) : courses.length === 0 ? (
              <div className="bg-white border border-slate-200/90 rounded-2xl sm:rounded-3xl py-20 text-center shadow-xs flex flex-col items-center">
                <div className="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center text-4xl mb-4 grayscale opacity-50">🔒</div>
                <h3 className="font-bold text-slate-700 text-xl mb-2">Bạn chưa tham gia khóa học nào</h3>
                <p className="text-slate-500 font-medium max-w-sm">Vui lòng liên hệ trung tâm để được cấp quyền truy cập vào các bài giảng nhé!</p>
              </div>
            ) : (
              (() => {
                const filteredCourses = filterCourse === 'all' ? courses : courses.filter(c => String(c.id) === String(filterCourse));
                const isSingle = filteredCourses.length === 1;

                if (filteredCourses.length === 0) {
                  return (
                    <div className="bg-white border border-slate-200/90 rounded-2xl sm:rounded-3xl py-20 text-center shadow-xs flex flex-col items-center">
                      <div className="w-20 h-20 bg-slate-50 rounded-full flex items-center justify-center text-4xl mb-4 grayscale opacity-50">🔍</div>
                      <h3 className="font-bold text-slate-700 text-xl mb-2">Không tìm thấy khóa học</h3>
                      <p className="text-slate-500 font-medium max-w-sm">Không có khóa học nào khớp với lựa chọn của bạn.</p>
                    </div>
                  );
                }

                return (
                  <div className={`grid ${isSingle ? 'grid-cols-1' : 'grid-cols-1 lg:grid-cols-2'} gap-6 xl:gap-8`}>
                    {filteredCourses.map(course => {
                      const cover = getCourseCover(course);
                      const stats = courseStats[course.id] || { testCount: 0, lecCount: 0, completedTestIds: new Set(), completedLecIds: new Set() };
                      
                      const testProgress = stats.testCount > 0 ? Math.min(100, Math.round((stats.completedTestIds.size / stats.testCount) * 100)) : 0;
                      const lecProgress = stats.lecCount > 0 ? Math.min(100, Math.round((stats.completedLecIds.size / stats.lecCount) * 100)) : 0;
                      const overallProgress = Math.round((testProgress + lecProgress) / 2);

                      return (
                        <div key={course.id} className={`bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 overflow-hidden shadow-xs hover:shadow-xl hover:border-[#2ab4e8]/60 hover:-translate-y-1 transition-all duration-300 group flex ${isSingle ? 'flex-col md:flex-row' : 'flex-col'}`}>
                          
                          {/* Image Top/Left Half */}
                          <div className={`relative overflow-hidden bg-slate-900 cursor-pointer ${isSingle ? 'w-full md:w-[44%] h-[230px] md:h-auto min-h-[290px]' : 'w-full h-[190px] sm:h-[215px]'}`} onClick={() => handleOpenCourse(course)}>
                             <img src={cover.image} loading="lazy" alt={course.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
                             <div className="absolute inset-0 bg-gradient-to-t from-[#0f172a]/90 via-[#0f172a]/30 to-transparent"></div>
                             
                             <div className="absolute top-4 left-4 bg-[#0a5482]/90 backdrop-blur-md text-white px-3 py-1 rounded-full text-[11px] font-extrabold uppercase tracking-wider border border-white/15 shadow-sm">
                                 {cover.badge}
                             </div>
                             <div className="absolute bottom-4 left-5 right-5">
                               <span className="text-[11px] font-bold uppercase tracking-widest text-[#2ab4e8] block mb-0.5">TonyEnglish Official Course</span>
                               <h4 className={`font-black ${isSingle ? 'text-2xl md:text-3xl' : 'text-xl md:text-2xl'} text-white leading-snug drop-shadow-sm`}>
                                   {course.title}
                               </h4>
                             </div>
                          </div>
                          
                          {/* Content Bottom/Right Half */}
                          <div className={`flex-1 flex flex-col justify-center bg-white ${isSingle ? 'p-6 sm:p-8 md:p-10' : 'p-5 sm:p-7'}`}>
                            
                            {/* Overall Progress */}
                            <div className="mb-5">
                                <div className="flex justify-between items-end mb-2">
                                    <span className="text-[12px] font-extrabold text-slate-500 uppercase tracking-wider">Tiến độ hoàn thành khóa học</span>
                                    <span className="text-[18px] font-black text-[#0a5482]">{overallProgress}%</span>
                                </div>
                                <div className="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden border border-slate-200/60">
                                    <div className="h-full bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] rounded-full transition-all duration-1000" style={{ width: `${overallProgress}%` }}></div>
                                </div>
                            </div>

                            {/* Detailed Stats */}
                            <div className="flex items-center gap-4 sm:gap-6 mb-6 bg-slate-50/90 p-4 rounded-2xl border border-slate-200/70">
                              <div className="flex-1">
                                  <div className="flex items-center justify-between mb-1">
                                      <span className="flex items-center gap-1.5 text-[11px] font-extrabold text-slate-500 uppercase tracking-wider"><span>📖</span> Bài giảng</span>
                                      <span className="font-black text-emerald-600 text-[12px]">{lecProgress}%</span>
                                  </div>
                                  <div className="font-black text-slate-800 text-[14px] mb-2">{stats.completedLecIds.size} / {stats.lecCount} <span className="text-[11px] font-semibold text-slate-400">bài học</span></div>
                                  <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                                      <div className="h-full bg-emerald-500 rounded-full transition-all duration-1000" style={{ width: `${lecProgress}%` }}></div>
                                  </div>
                              </div>
                              <div className="w-px h-12 bg-slate-200"></div>
                              <div className="flex-1">
                                  <div className="flex items-center justify-between mb-1">
                                      <span className="flex items-center gap-1.5 text-[11px] font-extrabold text-slate-500 uppercase tracking-wider"><span>📝</span> Kho đề thi</span>
                                      <span className="font-black text-[#0a5482] text-[12px]">{testProgress}%</span>
                                  </div>
                                  <div className="font-black text-slate-800 text-[14px] mb-2">{stats.completedTestIds.size} / {stats.testCount} <span className="text-[11px] font-semibold text-slate-400">đề luyện</span></div>
                                  <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                                      <div className="h-full bg-[#2ab4e8] rounded-full transition-all duration-1000" style={{ width: `${testProgress}%` }}></div>
                                  </div>
                              </div>
                            </div>
                            
                            {/* Actions */}
                            <div className={`flex flex-col sm:flex-row gap-3 ${isSingle ? 'mt-2' : 'mt-auto'}`}>
                               <button onClick={() => {
                                   resetWorkspaceAndChat(); 
                                   if(onOpenLecture) onOpenLecture(course.id);
                               }} className="flex-1 bg-sky-50/80 hover:bg-sky-100 text-[#0a5482] border border-sky-200/90 font-extrabold text-[13px] py-3 px-4 rounded-xl transition-all flex items-center justify-center gap-2 uppercase tracking-wider cursor-pointer active:scale-95">
                                   <span>📖</span> <span>Bài giảng lý thuyết</span>
                               </button>
                               <button onClick={() => handleOpenCourse(course)} className="flex-[1.3] bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-[13px] py-3 px-4 rounded-xl transition-all shadow-md shadow-blue-900/15 flex items-center justify-center gap-2 uppercase tracking-wider cursor-pointer active:scale-95">
                                   <span>🚀</span> <span>Vào kho đề &amp; Làm bài</span>
                               </button>
                            </div>
                          </div>
                        </div>
                      )
                    })}
                  </div>
                );
              })()
            )}
          </div>
        )}

        {/* 🚀 COURSE VIEW (Danh sách Folders & Tests - Đồng bộ với Thư viện NewsPage.tsx) */}
        {activeTab === 'library' && activeView === 'course' && selectedCourse && (
          <div className="animate-in fade-in slide-in-from-right-8 duration-500">
            {/* BREADCRUMB BAR (Giống NewsPage.tsx) */}
            <nav className="flex items-center gap-1.5 sm:gap-2 text-xs sm:text-[14px] font-semibold text-slate-500 mb-4 flex-wrap">
              <button
                type="button"
                onClick={() => {
                  setActiveView('dashboard');
                  setSelectedCourseId(null);
                  sessionStorage.removeItem('portal_current_folder_id');
                }}
                className="hover:text-[#0a5482] flex items-center gap-1 cursor-pointer transition-colors"
              >
                <span>🎓</span>
                <span>Góc học viên</span>
              </button>
              <span className="text-slate-300">/</span>
              <button
                type="button"
                onClick={() => {
                  setCurrentFolderId(null);
                  setFolderPage(1);
                  setTestPage(1);
                  sessionStorage.removeItem('portal_current_folder_id');
                }}
                className={`cursor-pointer transition-colors ${
                  !currentFolderId ? 'text-[#0a5482] font-bold' : 'hover:text-[#0a5482]'
                }`}
              >
                {selectedCourse.title}
              </button>
              {breadcrumbs.map((b, i) => (
                <React.Fragment key={b.id}>
                  <span className="text-slate-300">/</span>
                  <button
                    type="button"
                    onClick={() => handleFolderClick(b.id)}
                    className={`cursor-pointer transition-colors ${
                      i === breadcrumbs.length - 1 ? 'text-[#0a5482] font-bold' : 'hover:text-[#0a5482]'
                    }`}
                  >
                    {b.title}
                  </button>
                </React.Fragment>
              ))}
            </nav>

            {/* TONYENGLISH LIBRARY SECTION HEADER BANNER (Giống NewsPage.tsx) */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] rounded-2xl sm:rounded-3xl px-5 sm:px-8 py-5 sm:py-6 text-white mb-6 sm:mb-8 shadow-sm flex flex-col lg:flex-row lg:items-center justify-between gap-4">
              <div className="min-w-0">
                <div className="text-[11px] sm:text-xs font-extrabold uppercase tracking-widest text-[#2ab4e8] mb-1 flex items-center gap-2">
                  <span>📚 TonyEnglish Course &amp; Test Library</span>
                  {(currentSubFolders.length > 0 || currentTests.length > 0) && (
                    <span className="bg-white/15 text-white text-[11px] font-bold px-2.5 py-0.5 rounded-full border border-white/20 normal-case tracking-normal">
                      {currentSubFolders.length > 0 ? `${currentSubFolders.length} danh mục` : ''}
                      {currentSubFolders.length > 0 && currentTests.length > 0 ? ' • ' : ''}
                      {currentTests.length > 0 ? `${currentTests.length} bài tập` : ''}
                    </span>
                  )}
                </div>
                <h1 className="text-xl sm:text-2xl md:text-3xl font-black tracking-tight truncate">
                  {breadcrumbs.length > 0 ? breadcrumbs[breadcrumbs.length - 1].title : selectedCourse.title}
                </h1>
              </div>

              {/* ACTION CONTROLS: QUAY LẠI, CHUYỂN KHÓA HỌC & MỞ BÀI GIẢNG */}
              <div className="flex flex-wrap items-center gap-2.5 shrink-0">
                <button
                  type="button"
                  onClick={() => {
                    if (breadcrumbs.length > 1) {
                      handleFolderClick(breadcrumbs[breadcrumbs.length - 2].id);
                    } else if (breadcrumbs.length === 1) {
                      setCurrentFolderId(null);
                      setFolderPage(1);
                      setTestPage(1);
                      sessionStorage.removeItem('portal_current_folder_id');
                    } else {
                      setActiveView('dashboard');
                      setSelectedCourseId(null);
                      sessionStorage.removeItem('portal_current_folder_id');
                    }
                  }}
                  className="bg-white/10 hover:bg-white/20 text-white border border-white/20 font-bold text-xs sm:text-[13px] px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer"
                >
                  <span>←</span>
                  <span>Quay lại</span>
                </button>

                {/* DROPDOWN CHUYỂN KHÓA HỌC */}
                <div className="relative w-full sm:w-60 z-30">
                  <div 
                    onClick={() => setFilterCourseDropdownOpen(!filterCourseDropdownOpen)}
                    className="w-full bg-white hover:bg-sky-50 border border-white/20 rounded-xl px-3.5 py-2 flex items-center justify-between cursor-pointer shadow-xs transition-all"
                  >
                    <div className="flex items-center gap-2 min-w-0 pr-1.5">
                      <span className="text-[#0a5482] text-xs">🎓</span>
                      <span className="font-bold text-xs text-[#0a5482] truncate">
                        {selectedCourse ? selectedCourse.title : 'Chọn khóa học'}
                      </span>
                    </div>
                    <span className={`text-[#2ab4e8] text-[10px] transition-transform duration-300 shrink-0 ${filterCourseDropdownOpen ? 'rotate-180' : ''}`}>▼</span>
                  </div>
                  
                  {filterCourseDropdownOpen && (
                    <>
                      <div className="fixed inset-0 z-40" onClick={() => setFilterCourseDropdownOpen(false)}></div>
                      <div className="absolute top-full right-0 mt-2 w-full min-w-[240px] max-h-72 overflow-y-auto bg-white text-slate-800 border border-slate-200 rounded-2xl shadow-2xl z-50 animate-in fade-in slide-in-from-top-2 custom-scrollbar p-1">
                        <div 
                          onClick={() => {
                            setFilterCourse('all');
                            setAnalyticsCourse('all');
                            setActiveView('dashboard');
                            setSelectedCourseId(null);
                            setFilterCourseDropdownOpen(false);
                          }}
                          className={`px-3.5 py-2 text-xs rounded-xl font-medium cursor-pointer transition-colors ${filterCourse === 'all' && !selectedCourse ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                        >
                          🌟 Tất cả khóa học (Góc học viên)
                        </div>
                        {courses.map(course => (
                          <div 
                            key={course.id}
                            onClick={() => {
                              setFilterCourse(course.id);
                              setAnalyticsCourse(course.id);
                              setFilterCourseDropdownOpen(false);
                              handleOpenCourse(course);
                            }}
                            className={`px-3.5 py-2 text-xs rounded-xl font-medium cursor-pointer transition-colors border-t border-slate-100 ${String(selectedCourse?.id) === String(course.id) ? 'bg-sky-50 text-[#0a5482] font-bold' : 'text-slate-600 hover:bg-slate-50'}`}
                          >
                            📖 {course.title}
                          </div>
                        ))}
                      </div>
                    </>
                  )}
                </div>

                {/* NÚT MỞ BÀI GIẢNG LÝ THUYẾT */}
                <button 
                  onClick={() => {
                    resetWorkspaceAndChat(); 
                    if(onOpenLecture && selectedCourse) onOpenLecture(selectedCourse.id);
                  }} 
                  className="w-full sm:w-auto bg-[#2ab4e8] hover:bg-[#1fa0d4] text-white font-extrabold text-xs sm:text-[13px] px-4 py-2 rounded-xl transition-all flex items-center justify-center gap-2 shadow-sm uppercase tracking-wider shrink-0 cursor-pointer active:scale-95"
                >
                  <span>📖</span> <span>Bài Giảng Lý Thuyết</span>
                </button>
              </div>
            </div>

            <div className="space-y-8 md:space-y-10">
              
              {/* Folders Grid */}
              {currentSubFolders.length > 0 && (
                <div>
                  <div className="flex items-center gap-2.5 mb-5">
                    <span className="w-1.5 h-6 bg-[#0a5482] rounded-full"></span>
                    <h3 className="font-black text-lg sm:text-xl text-slate-900 tracking-tight m-0">
                      Danh mục chuyên đề &amp; Bộ đề
                    </h3>
                  </div>
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
                        <div key={subFolder.id} onClick={() => handleFolderClick(subFolder.id)} className="bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-xs hover:shadow-xl hover:-translate-y-1 hover:border-[#2ab4e8] transition-all duration-300 cursor-pointer flex flex-col group relative">
                          <div className="h-[125px] relative overflow-hidden bg-slate-900">
                            <img src={displayImage} style={{ filter: hueRotate }} loading="lazy" className="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-85" alt="folder" />
                            <div className="absolute inset-0 bg-gradient-to-t from-[#0f172a]/90 via-[#0f172a]/40 to-transparent"></div>
                            <div className={`absolute bottom-3.5 right-4 ${badgeText ? 'left-20' : 'left-4'}`}>
                                <h3 className="text-[15.5px] font-black leading-snug line-clamp-2 w-full text-white drop-shadow-sm">
                                    {displayTitle}
                                </h3>
                            </div>
                          </div>

                          {badgeText && (
                              <div className="absolute top-[98px] left-4 bg-white text-[#0a5482] font-black text-[16px] w-12 h-12 rounded-xl flex items-center justify-center shadow-md border-2 border-white shrink-0 z-10 ring-1 ring-slate-200">
                                  {badgeText}
                              </div>
                          )}

                          <div className="bg-white p-4 flex flex-col relative flex-1">
                            <div className="flex justify-between items-center mt-auto">
                              <span className="text-[11px] font-extrabold text-[#0a5482] bg-sky-50/90 px-3 py-1 rounded-lg border border-sky-100 uppercase tracking-wider">
                                  {childCount > 0 ? `${childCount} thư mục` : `${testCount} bài tập`}
                              </span>
                              <span className="w-8 h-8 rounded-xl bg-slate-100 text-[#0a5482] flex items-center justify-center font-bold group-hover:bg-[#0a5482] group-hover:text-white transition-colors">
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
                <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 overflow-hidden shadow-xs animate-in fade-in">
                  
                  {/* Test Filters */}
                  <div className="bg-white px-5 sm:px-7 py-4 sm:py-5 border-b border-slate-200/80 flex flex-col lg:flex-row justify-between items-start lg:items-center gap-4">
                    <div className="flex items-center gap-2.5">
                      <span className="w-1.5 h-6 bg-[#2ab4e8] rounded-full"></span>
                      <h3 className="font-black text-base sm:text-lg text-slate-900 tracking-tight m-0">
                        Danh sách bài tập &amp; Đề luyện ({processedTests.length})
                      </h3>
                    </div>

                    <div className="flex flex-col sm:flex-row gap-3 w-full lg:w-auto">
                      <div className="relative flex-1 sm:w-80">
                        <input type="text" placeholder="Tìm kiếm bài tập..." value={searchTest} onChange={(e) => {setSearchTest(e.target.value); setTestPage(1);}} className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200/90 font-semibold text-[13.5px] outline-none focus:border-[#2ab4e8] focus:bg-white focus:ring-2 focus:ring-[#2ab4e8]/20 transition-all" />
                        <span className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm">🔍</span>
                      </div>

                      <select value={sortTest} onChange={(e) => setSortTest(e.target.value)} className="bg-slate-50 border border-slate-200/90 rounded-xl px-3.5 py-2.5 font-bold text-[13px] text-[#0a5482] outline-none cursor-pointer focus:border-[#2ab4e8]">
                        <option value="name-asc">Sắp xếp: A → Z</option>
                        <option value="name-desc">Sắp xếp: Z → A</option>
                        <option value="date-desc">Mới nhất</option>
                        <option value="date-asc">Cũ nhất</option>
                      </select>
                    </div>
                  </div>

                  {/* Tests List */}
                  <div className="p-5 sm:p-7 bg-slate-50/60">
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
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

                        let statusConfig = {
                          badge: "Chưa làm",
                          badgeClass: "text-slate-600 bg-slate-100 border border-slate-200/80",
                          btnText: "Làm bài ngay →",
                          btnClass: "bg-sky-50/90 text-[#0a5482] border border-sky-200/90 group-hover:bg-[#0a5482] group-hover:text-white group-hover:border-[#0a5482]"
                        };
                        
                        if (isCompleted) {
                            statusConfig = {
                              badge: "✓ Hoàn thành",
                              badgeClass: "text-emerald-700 bg-emerald-50 border border-emerald-200",
                              btnText: "Làm lại đề →",
                              btnClass: "bg-emerald-50 text-emerald-700 border border-emerald-200 group-hover:bg-emerald-600 group-hover:text-white"
                            };
                        }
                        else if (inProgress) {
                            statusConfig = {
                              badge: "⏳ Đang làm dở",
                              badgeClass: "text-amber-700 bg-amber-50 border border-amber-200",
                              btnText: "Tiếp tục làm →",
                              btnClass: "bg-amber-500 text-white shadow-sm hover:bg-amber-600"
                            };
                        }
                        else if (isOverdue) {
                            statusConfig.btnText = "Nộp muộn →";
                            statusConfig.btnClass = "bg-rose-50 text-rose-600 border border-rose-200 group-hover:bg-rose-600 group-hover:text-white";
                        }

                        return (
                          <div key={test.id} onClick={() => handleStartTestClick(test)} className={`bg-white border p-5 rounded-2xl shadow-2xs hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300 cursor-pointer flex flex-col justify-between group relative overflow-hidden ${isCompleted ? 'border-emerald-200/90' : inProgress ? 'border-amber-300' : 'border-slate-200/90 hover:border-[#2ab4e8]'}`}>
                            
                            <div>
                              <div className="flex justify-between items-start mb-3.5">
                                <div className={`w-11 h-11 rounded-xl ${skillConfig.bg} border ${skillConfig.border} flex items-center justify-center text-xl group-hover:scale-105 transition-transform`}>
                                    {skillConfig.icon}
                                </div>
                                <span className={`text-[10px] font-extrabold px-2.5 py-1 rounded-full uppercase tracking-wider ${statusConfig.badgeClass}`}>
                                    {statusConfig.badge}
                                </span>
                              </div>
                              
                              <h3 className="font-extrabold text-slate-800 text-[15.5px] group-hover:text-[#0a5482] transition-colors mb-2.5 line-clamp-2 leading-snug min-h-[42px]">
                                  {test.title}
                              </h3>
                              
                              <div className="flex flex-wrap items-center gap-1.5 mb-2">
                                  {(test.content_json?.basicInfo?.guide_video_url || test.content_json?.guide_video_url) && (
                                      <span className="text-[10px] px-2 py-0.5 rounded-md font-bold tracking-wider bg-red-50 text-red-600 border border-red-100 flex items-center gap-1" title="Có video hướng dẫn & giải đề">
                                          🎬 Video giải đề
                                      </span>
                                  )}
                                  {matchedClassId && !isCompleted && (
                                      <span className={`text-[10px] px-2 py-0.5 rounded-md uppercase font-bold tracking-wider ${isOverdue ? 'bg-rose-100 text-rose-600' : 'bg-orange-100 text-orange-600'}`}>
                                          {isOverdue ? 'Quá hạn' : 'Hạn: ' + deadlineLabel}
                                      </span>
                                  )}
                              </div>
                            </div>
                            
                            <button className={`mt-4 w-full font-extrabold text-[12.5px] uppercase tracking-wider py-2.5 rounded-xl transition-all duration-200 cursor-pointer ${statusConfig.btnClass}`}>
                                {statusConfig.btnText}
                            </button>
                          </div>
                        );
                      })}
                    </div>
                    
                    {processedTests.length === 0 ? (
                      <div className="text-center py-16 text-slate-400 font-medium flex flex-col items-center justify-center bg-white rounded-2xl border border-dashed border-slate-300">
                        <svg className="w-10 h-10 mb-3 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                        Không tìm thấy bài học nào phù hợp.
                      </div>
                    ) : (
                      renderPagination(testPage, totalTestPages, setTestPage)
                    )}
                  </div>
                </div>
              )}

              {isLoading ? (
                <div className="text-center py-20 bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col items-center justify-center">
                   <div className="w-10 h-10 border-4 border-sky-100 border-t-[#0a5482] rounded-full animate-spin mb-4"></div>
                   <span className="text-slate-500 font-medium text-sm">Đang tải danh mục và bài tập...</span>
                </div>
              ) : currentSubFolders.length === 0 && currentTests.length === 0 && (
                <div className="text-center py-20 bg-white rounded-2xl border border-slate-200/90 text-slate-400 font-medium text-base shadow-xs flex flex-col items-center justify-center">
                   <div className="text-5xl mb-4 grayscale opacity-30">📭</div>
                   Thư mục này hiện đang trống.
                </div>
              )}
            </div>
          </div>
        )}

        {/* =====================================================================
            📅 TRANG LỊCH BÁO BÀI (ASSIGNMENT CALENDAR) VÀ BẢNG CÔNG VIỆC
            ===================================================================== */}
        {activeTab === 'board' && currentUser && (
          <div className="w-full flex-1 min-h-0 h-full flex flex-col animate-in fade-in duration-500 relative">
            <TaskBoard 
              userId={currentUser.id} 
              filterCourseId={filterCourse}
              courseTitle={filterCourse === 'all' ? undefined : courses.find(c => String(c.id) === String(filterCourse))?.title}
              bottomActions={renderBottomControls}
              lectures={allLectures}
              onOpenLecture={handleGoToLecture}
              onStartTest={(testId: string) => {
                const test = allTests.find(t => String(t.id) === String(testId));
                handleStartTestClick(test || { id: testId });
              }} 
            />
          </div>
        )}

        {activeTab === 'calendar' && (
          <div className="animate-in fade-in slide-in-from-bottom-4 w-full flex-1 flex flex-col pb-2 relative">
            {(() => {
              const calendarAssignments = filterCourse === 'all' ? assignments : assignments.filter(a => {
                if (a.board_template_id) {
                  const tpl = boardTemplates.find(t => String(t.id) === String(a.board_template_id));
                  if (tpl && String(tpl.course_id) === String(filterCourse)) return true;
                }
                if (a.board_template_title) {
                  const tpl = boardTemplates.find(t => t.title === a.board_template_title);
                  if (tpl && String(tpl.course_id) === String(filterCourse)) return true;
                }
                if (a.task_type === 'test') {
                  const test = (a.test_id ? allTests.find(t => String(t.id) === String(a.test_id)) : null) ||
                               (a.title ? allTests.find(t => t.title && t.title.trim().toLowerCase() === a.title.trim().toLowerCase()) : null);
                  if (test && String(test.course_id) === String(filterCourse)) return true;
                }
                if (a.title && dayPlanTaskCourseMap[a.title.trim()] === String(filterCourse)) {
                  return true;
                }
                return false;
              });

              return (
                <div className="flex-1 min-h-0 w-full">
                  <AssignmentCalendar 
                    userId={currentUser?.id}
                    assignments={calendarAssignments} 
                    completedTestIds={completedTestIdsSet}
                    courseTitle={filterCourse === 'all' ? undefined : courses.find(c => String(c.id) === String(filterCourse))?.title}
                    lectures={allLectures}
                    rightActions={<div className="hidden sm:block">{renderBottomControls}</div>}
                    onOpenLecture={handleGoToLecture}
                    onRefresh={async () => {
                      if (!currentUser) return;
                      const { data } = await supabase.from('assignments').select('*').eq('user_id', currentUser.id).order('due_date', { ascending: true });
                      setAssignments(data || []);
                    }}
                    onStartTest={(testId) => {
                      const test = allTests.find(t => String(t.id) === String(testId));
                      if (test) handleStartTestClick(test);
                    }}
                  />
                </div>
              );
            })()}
          </div>
        )}

        {/* =====================================================================
            🚀 TRANG BÁO CÁO (ANALYTICS) ĐỒNG BỘ TONYENGLISH.VN
            ===================================================================== */}
        {activeTab === 'analytics' && (
          <div 
            className={`w-full min-h-[500px] text-slate-800 relative flex-1 flex flex-col space-y-5 md:space-y-6 animate-in fade-in duration-300 ${
              analyticsTheme.id !== 'tony-classic' ? 'p-3 sm:p-4 md:p-5 rounded-3xl' : 'p-0'
            }`}
            style={analyticsTheme.id !== 'tony-classic' ? { backgroundColor: analyticsTheme.boardBg } : undefined}
          >
            {/* TONYENGLISH.VN SYNCHRONIZED HEADER BANNER */}
            <div 
              className="w-full rounded-2xl sm:rounded-3xl p-5 sm:p-6 md:p-7 shadow-md text-white flex flex-col gap-4 transition-all relative overflow-hidden border border-slate-800/20" 
              style={{ background: analyticsTheme.titleBg || 'linear-gradient(135deg, #073b5c 0%, #0a5482 55%, #0f172a 100%)' }}
            >
              {/* Decorative Ambient Glow */}
              <div className="absolute -top-24 -right-24 w-80 h-80 bg-[#2ab4e8]/15 blur-3xl rounded-full pointer-events-none"></div>
              <div className="absolute -bottom-24 -left-24 w-64 h-64 bg-sky-400/10 blur-3xl rounded-full pointer-events-none"></div>

              <div className="relative z-10 flex flex-col xl:flex-row justify-between items-start xl:items-center gap-4">
                {/* CỘT 1 (BÊN TRÁI): TIÊU ĐỀ + 3 NÚT FILTER */}
                <div className="flex flex-col gap-3">
                  <div>
                    <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-xs border border-white/15 px-3 py-1 rounded-full text-[10px] sm:text-[11px] font-extrabold tracking-widest uppercase text-[#2ab4e8] mb-2.5">
                      <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                      TonyEnglish Performance Analytics • Báo Cáo Hiệu Suất
                    </div>
                    <h1 className="text-xl sm:text-2xl md:text-[26px] font-black tracking-tight text-white leading-tight">
                      Báo Cáo Hiệu Suất{filterCourse !== 'all' && courses.find(c => String(c.id) === String(filterCourse))?.title ? ` — ${courses.find(c => String(c.id) === String(filterCourse))?.title}` : ''}
                    </h1>
                    <p className="text-slate-200/85 text-xs sm:text-sm mt-1 font-medium">
                      Phân tích kết quả luyện tập, biểu đồ 4 kỹ năng và nhật ký học tập chi tiết.
                    </p>
                  </div>

                  {/* 3 NÚT FILTER: Luyện thi IELTS, Bài tập bổ trợ, Bài tập khóa khác */}
                  {isIeltsCourseSelected && (
                    <div className="flex flex-wrap bg-white/10 backdrop-blur-xs p-1 rounded-xl border border-white/15 gap-1 w-fit">
                      <button
                        type="button"
                        onClick={() => { setAnalyticsTestType('ielts'); setHistoryPage(1); }}
                        className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg font-extrabold text-xs sm:text-[13px] transition-all cursor-pointer ${analyticsTestType === 'ielts' ? 'bg-white text-[#0a5482] shadow-xs' : 'text-white/85 hover:text-white hover:bg-white/10'}`}
                      >
                        <span>🎯</span> Luyện thi IELTS
                      </button>
                      <button
                        type="button"
                        onClick={() => { setAnalyticsTestType('ielts-standard'); setHistoryPage(1); }}
                        className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg font-extrabold text-xs sm:text-[13px] transition-all cursor-pointer ${analyticsTestType === 'ielts-standard' ? 'bg-white text-[#0a5482] shadow-xs' : 'text-white/85 hover:text-white hover:bg-white/10'}`}
                      >
                        <span>📝</span> Bài Tập Bổ Trợ
                      </button>
                      {analyticsCourse === 'all' && courses.some(c => !((c.title||'').toLowerCase().includes('ielts') || c.type === 'IELTS')) && (
                        <button
                          type="button"
                          onClick={() => { setAnalyticsTestType('standard'); setHistoryPage(1); }}
                          className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg font-extrabold text-xs sm:text-[13px] transition-all cursor-pointer ${analyticsTestType === 'standard' ? 'bg-white text-[#0a5482] shadow-xs' : 'text-white/85 hover:text-white hover:bg-white/10'}`}
                        >
                          <span>📚</span> Bài tập khóa khác
                        </button>
                      )}
                    </div>
                  )}
                </div>

                {/* BÊN PHẢI BANNER: BỘ 3 NÚT (BÀI GIẢNG, KHO ĐỀ, CHỌN KHÓA HỌC) + NÚT ĐỔI MÀU NỀN */}
                <div className="flex flex-wrap items-center gap-2.5 shrink-0 self-start xl:self-center">
                  {renderBottomControls}

                  {/* NÚT ĐỔI MÀU NỀN */}
                  <button 
                    type="button"
                    onClick={() => setIsAnalyticsThemeModalOpen(true)} 
                    className="bg-white/12 hover:bg-white/20 active:scale-95 text-white text-xs sm:text-[13px] font-bold px-3.5 py-2 rounded-xl transition-all shadow-xs flex items-center gap-1.5 cursor-pointer shrink-0 border border-white/20 h-[38px]"
                    title="Đổi giao diện màu nền"
                  >
                    <span>🎨</span> <span className="hidden sm:inline">Giao diện</span>
                  </button>
                </div>
              </div>
            </div>

            {/* 2-COLUMN LAYOUT: CỘT TRÁI PHÂN TÍCH & BIỂU ĐỒ, CỘT PHẢI LỊCH SỬ / NHẬT KÝ */}
            <div className="grid grid-cols-1 xl:grid-cols-12 gap-5 md:gap-6 items-start">
              {/* ========================================================= */}
              {/* CỘT TRÁI (XL:COL-SPAN-7): CÁC BIỂU ĐỒ VÀ PHÂN TÍCH        */}
              {/* ========================================================= */}
              <div className="xl:col-span-7 space-y-5 md:space-y-6">
                {analyticsTotalTestsDone === 0 ? (
                  <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 py-20 text-center shadow-xs flex flex-col items-center justify-center p-6">
                    <div className="text-5xl mb-4 opacity-40 grayscale block">📊</div>
                    <h3 className="text-lg md:text-xl font-black text-slate-800 mb-2">Chưa có dữ liệu làm bài hợp lệ</h3>
                    <p className="text-slate-500 font-medium text-[13px] md:text-[14px] max-w-md">Hệ thống chỉ tính những bài đạt trên 3.0 điểm (hoặc IELTS Band &gt; 3.0) để đảm bảo phân tích của AI chính xác nhất.</p>
                  </div>
                ) : (
                  <>
                    {/* 5 THẺ KPI THỐNG KÊ */}
                    <div className="grid grid-cols-2 sm:grid-cols-3 xl:grid-cols-3 2xl:grid-cols-5 gap-3 sm:gap-4">
                      {/* CARD 1: BÀI HOÀN THÀNH */}
                      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs p-4 sm:p-5 flex flex-col justify-between hover:border-emerald-400 hover:shadow-md transition-all duration-300 group">
                        <div className="flex justify-between items-center mb-3 relative z-10">
                          <div className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-emerald-400"></span><span className="font-bold text-slate-500 text-[11px] uppercase tracking-wider group-hover:text-emerald-600 transition-colors">Đã làm</span></div>
                          <span className="font-black text-slate-800 text-xl sm:text-2xl">{analyticsTotalTestsDone}</span>
                        </div>
                        <div className="h-16 w-full -mx-1 -mb-1">
                          <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                              <defs>
                                <linearGradient id="colorDone" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                                  <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                                </linearGradient>
                              </defs>
                              <XAxis dataKey="name" hide />
                              <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} bài`, 'Tổng số bài']} contentStyle={{ borderRadius: '12px', fontSize: '12px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                              <Area type="monotone" dataKey="cumulativeDone" stroke="#10b981" strokeWidth={2.5} fill="url(#colorDone)" activeDot={{ r: 5, fill: '#10b981', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* CARD 2: LƯỢT LÀM */}
                      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs p-4 sm:p-5 flex flex-col justify-between hover:border-[#2ab4e8] hover:shadow-md transition-all duration-300 group">
                        <div className="flex justify-between items-center mb-3 relative z-10">
                          <div className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-[#2ab4e8]"></span><span className="font-bold text-slate-500 text-[11px] uppercase tracking-wider group-hover:text-[#0a5482] transition-colors">Lượt làm</span></div>
                          <span className="font-black text-slate-800 text-xl sm:text-2xl">{analyticsTotalTestsDone}</span>
                        </div>
                        <div className="h-16 w-full -mx-1 -mb-1">
                          <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                              <defs>
                                <linearGradient id="colorAttempts" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%" stopColor="#2ab4e8" stopOpacity={0.3}/>
                                  <stop offset="95%" stopColor="#2ab4e8" stopOpacity={0}/>
                                </linearGradient>
                              </defs>
                              <XAxis dataKey="name" hide />
                              <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} lượt`, 'Tổng số lượt']} contentStyle={{ borderRadius: '12px', fontSize: '12px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                              <Area type="monotone" dataKey="attempts" stroke="#0a5482" strokeWidth={2.5} fill="url(#colorAttempts)" activeDot={{ r: 5, fill: '#0a5482', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* CARD 3: THỜI GIAN HỌC */}
                      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs p-4 sm:p-5 flex flex-col justify-between hover:border-orange-400 hover:shadow-md transition-all duration-300 group">
                        <div className="flex justify-between items-center mb-3 relative z-10">
                          <div className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-orange-400"></span><span className="font-bold text-slate-500 text-[11px] uppercase tracking-wider group-hover:text-orange-600 transition-colors">Giờ học</span></div>
                          <span className="font-black text-slate-800 text-xl sm:text-2xl">{analyticsTotalTimeHours}h</span>
                        </div>
                        <div className="h-16 w-full -mx-1 -mb-1">
                          <ResponsiveContainer width="99%" height="100%">
                            <AreaChart data={aggregatedByDate} margin={{ top: 5, right: 0, left: 0, bottom: 0 }}>
                              <defs>
                                <linearGradient id="colorTime" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%" stopColor="#f97316" stopOpacity={0.3}/>
                                  <stop offset="95%" stopColor="#f97316" stopOpacity={0}/>
                                </linearGradient>
                              </defs>
                              <XAxis dataKey="name" hide />
                              <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any) => [`${value} giờ`, 'Thời gian học']} contentStyle={{ borderRadius: '12px', fontSize: '12px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                              <Area type="monotone" dataKey="time" stroke="#f97316" strokeWidth={2.5} fill="url(#colorTime)" activeDot={{ r: 5, fill: '#f97316', stroke: '#fff', strokeWidth: 2 }} />
                            </AreaChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* CARD 4: ĐIỂM TRUNG BÌNH */}
                      <div className="bg-gradient-to-br from-[#073b5c] via-[#0a5482] to-[#0f172a] rounded-2xl border border-slate-800/40 shadow-xs p-4 sm:p-5 flex flex-col justify-between text-white relative overflow-hidden group hover:shadow-md transition-all">
                        <div className="relative z-10">
                          <span className="text-[10px] font-extrabold tracking-widest text-[#2ab4e8] uppercase block mb-1">
                            {isIeltsContext ? 'IELTS AVERAGE' : 'ĐIỂM TRUNG BÌNH'}
                          </span>
                          {isIeltsContext ? (
                            <div className="font-black text-2xl sm:text-3xl text-white tracking-tight leading-none mt-1">
                              {avgIelts}
                            </div>
                          ) : (
                            <div className="mt-1">
                              <span className="font-black text-2xl sm:text-3xl text-white tracking-tight leading-none">{avgScore}</span>
                              {avgScoreRaw > 0 && (
                                <span className={`block text-base font-black mt-0.5 ${GRADE_SCALE.find(g => avgScoreRaw >= g.min)?.color || 'text-slate-400'}`}>
                                  {percentToGrade(avgScoreRaw)}
                                </span>
                              )}
                            </div>
                          )}
                          <span className="text-[11px] font-medium text-sky-200/75 mt-2 block">
                            {isIeltsContext ? '(Dựa trên 4 bài gần nhất)' : '(Toàn bộ hệ thống)'}
                          </span>
                        </div>
                        <div className="absolute -right-4 -bottom-4 w-20 h-20 bg-[#2ab4e8]/15 rounded-full blur-xl pointer-events-none"></div>
                      </div>

                      {/* CARD 5: MỤC TIÊU ĐIỂM */}
                      <div className="bg-[#0f172a] rounded-2xl border border-amber-500/40 shadow-xs p-4 sm:p-5 flex flex-col justify-between text-white relative overflow-hidden group hover:border-amber-400 transition-all">
                        <div className="relative z-10 flex-1 flex flex-col justify-between">
                          <span className="text-[10px] font-extrabold tracking-widest text-amber-400 uppercase block mb-1">
                            MỤC TIÊU ĐIỂM
                          </span>
                          <div className="mt-1">
                            {isIeltsContext ? (
                              <input 
                                type="number" step="0.5" min="0" max="9.0" 
                                value={getTargetForCourse(analyticsCourse, true) || ''} 
                                onChange={(e) => handleUpdateTarget('ielts', e.target.value)}
                                placeholder="N/A"
                                className="font-black text-amber-400 text-2xl sm:text-3xl bg-transparent w-full outline-none cursor-pointer placeholder:text-amber-400/30 relative z-10"
                                title="Click để sửa"
                              />
                            ) : analyticsCourse !== 'all' ? (
                              <div className="relative z-10">
                                <div className="relative inline-block w-full">
                                  <select 
                                    value={getTargetForCourse(analyticsCourse, false) || ''} 
                                    onChange={(e) => handleUpdateTarget(analyticsCourse, e.target.value)}
                                    className="font-black text-amber-400 text-2xl sm:text-3xl bg-transparent outline-none cursor-pointer appearance-none relative z-10 border-none pr-6"
                                  >
                                    <option value="" className="bg-slate-800 text-slate-400 text-sm">--</option>
                                    <option value="A*" className="bg-slate-800 text-white text-sm">A*</option>
                                    <option value="A" className="bg-slate-800 text-white text-sm">A</option>
                                    <option value="B" className="bg-slate-800 text-white text-sm">B</option>
                                    <option value="C" className="bg-slate-800 text-white text-sm">C</option>
                                    <option value="D" className="bg-slate-800 text-white text-sm">D</option>
                                    <option value="E" className="bg-slate-800 text-white text-sm">E</option>
                                  </select>
                                  <span className="absolute right-0 top-1/2 -translate-y-1/2 text-amber-400 text-xs pointer-events-none">▼</span>
                                </div>
                              </div>
                            ) : (
                              <div className="relative z-10">
                                <span className="font-black text-amber-400/30 text-2xl sm:text-3xl">--</span>
                                <p className="text-[10px] text-amber-200/40 mt-1">Chọn 1 khóa cụ thể</p>
                              </div>
                            )}
                          </div>
                          <span className="text-[10px] font-medium text-slate-400 mt-2 block">
                            {isIeltsContext ? 'Click số để sửa' : analyticsCourse !== 'all' ? 'Click để đổi' : ''}
                          </span>
                        </div>
                        <div className="absolute right-1 bottom-1 text-4xl opacity-10 pointer-events-none">🎯</div>
                      </div>
                    </div>

                    {/* BANNER KHÍCH LỆ */}
                    {(() => {
                      const currentTarget = isIeltsContext 
                        ? getTargetForCourse(analyticsCourse, true)
                        : getTargetForCourse(analyticsCourse, false);
                      const comment = getMotivationalComment(
                        avgScoreRaw, currentTarget, isIeltsContext, 
                        avgIeltsRaw, parseFloat(currentTarget) || 0
                      );
                      if (!comment.text) return null;
                      return (
                        <div className="bg-white rounded-2xl border border-slate-200/90 shadow-xs px-5 py-3.5 flex items-center justify-center gap-3 text-center animate-in fade-in">
                          <span className="text-2xl shrink-0">{comment.emoji}</span>
                          <p className={`text-[13px] sm:text-[14px] font-semibold ${comment.color} leading-relaxed`}>{comment.text}</p>
                        </div>
                      );
                    })()}

                    {/* KHU VỰC BIỂU ĐỒ IELTS CHI TIẾT */}
                    {isIeltsContext && (
                      <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-xs overflow-hidden p-5 sm:p-6 md:p-7 space-y-6">
                        {/* 2 BIỂU ĐỒ ĐỨNG CẠNH NHAU */}
                        <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 md:gap-6">
                          {/* CHART 1: BIỂU ĐỒ 4 KỸ NĂNG IELTS */}
                          <div className="w-full min-w-0">
                            <div className="flex items-center gap-2.5 mb-3">
                              <span className="w-1.5 h-5 bg-[#0a5482] rounded-full"></span>
                              <div className="w-8 h-8 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center text-base">📈</div>
                              <h3 className="font-black text-sm sm:text-base text-slate-900 tracking-tight">Biểu đồ 4 Kỹ Năng</h3>
                            </div>
                            <div className="w-full bg-slate-50/60 rounded-2xl p-2.5 sm:p-3.5 border border-slate-200/70 flex items-center justify-center" style={{ minHeight: 280 }}>
                              <ResponsiveContainer width="99%" height={260}>
                                <LineChart data={ieltsSkillChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                  <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} dy={10} />
                                  <YAxis domain={[0, 9]} ticks={[0, 3, 5, 7, 9]} axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} />
                                  <Tooltip labelFormatter={(label) => `Ngày ${label}`} contentStyle={{ borderRadius: '12px', fontSize: '11px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                  <Legend iconType="circle" wrapperStyle={{ fontSize: '11px', fontWeight: 'bold', paddingTop: '10px' }} />
                                  
                                  <Line type="monotone" dataKey="Nghe" name="Listening" stroke="#10b981" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Nói" name="Speaking" stroke="#f97316" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Đọc" name="Reading" stroke="#0a5482" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Viết" name="Writing" stroke="#d946ef" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                </LineChart>
                              </ResponsiveContainer>
                            </div>
                          </div>
                          
                          {/* CHART 2: BIỂU ĐỒ TỶ LỆ THEO DẠNG BÀI */}
                          <div className="w-full min-w-0">
                            <div className="flex items-center gap-2.5 mb-3">
                              <span className="w-1.5 h-5 bg-[#2ab4e8] rounded-full"></span>
                              <div className="w-8 h-8 rounded-xl bg-sky-50 border border-sky-200/80 text-[#0a5482] flex items-center justify-center text-base">🎯</div>
                              <h3 className="font-black text-sm sm:text-base text-slate-900 tracking-tight">Tỷ Lệ Đúng Từng Dạng (%)</h3>
                            </div>
                            <div className="w-full bg-slate-50/60 rounded-2xl p-2.5 sm:p-3.5 border border-slate-200/70 flex items-center justify-center" style={{ minHeight: 280 }}>
                              <ResponsiveContainer width="99%" height={260}>
                                <LineChart data={ieltsTypeChartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                                  <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} dy={10} />
                                  <YAxis domain={[0, 100]} ticks={[0, 25, 50, 75, 100]} axisLine={false} tickLine={false} tick={{ fontSize: 10, fill: '#64748b', fontWeight: 600 }} />
                                  <Tooltip labelFormatter={(label) => `Ngày ${label}`} formatter={(value: any, name: string) => [`${value}%`, name]} contentStyle={{ borderRadius: '12px', fontSize: '11px', fontWeight: 'bold', border: 'none', boxShadow: '0 10px 15px -3px rgb(0 0 0 / 0.1)' }} cursor={{ stroke: '#cbd5e1', strokeWidth: 1, strokeDasharray: '3 3' }} />
                                  <Legend iconType="circle" wrapperStyle={{ fontSize: '11px', fontWeight: 'bold', paddingTop: '10px' }} />
                                  
                                  <Line type="monotone" dataKey="Điền từ" name="Điền từ" stroke="#10b981" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Nhận định" name="T/F/NG" stroke="#f97316" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Trắc nghiệm" name="MCQ/Checkbox" stroke="#0a5482" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                  <Line type="monotone" dataKey="Matching" name="Matching" stroke="#d946ef" strokeWidth={2.5} dot={{ r: 3, strokeWidth: 2, fill: '#fff' }} activeDot={{ r: 5 }} connectNulls={true} />
                                </LineChart>
                              </ResponsiveContainer>
                            </div>
                          </div>
                        </div>

                        {/* THANH PROGRESS BAR NẰM NGANG - 4 CARD TRÊN 1 DÒNG */}
                        <div className="bg-slate-50/80 rounded-2xl p-4 sm:p-5 border border-slate-200/80">
                          <h3 className="font-black text-xs sm:text-[13px] text-slate-900 uppercase tracking-tight mb-3 flex items-center gap-2">
                            <span className="text-emerald-500">🏆</span> Tỷ lệ đúng tích lũy theo dạng câu hỏi
                          </h3>
                          <div className="grid grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-3">
                            {Object.entries(ieltsTypeStats).map(([key, data]) => {
                              const percent = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
                              return (
                                <div key={key} className="bg-white border border-slate-200/90 rounded-xl p-3.5 hover:border-[#2ab4e8] hover:shadow-xs transition-all flex flex-col justify-between">
                                  <div className="flex justify-between items-start mb-1.5 gap-1">
                                    <span className="font-bold text-slate-700 text-[11px] sm:text-xs truncate" title={key}>{key}</span>
                                    <span className="font-black text-[#0a5482] text-[13px] sm:text-[14px] shrink-0">{percent}%</span>
                                  </div>
                                  <div className="w-full h-1.5 sm:h-2 bg-slate-100 rounded-full overflow-hidden mb-1 border border-slate-200/50">
                                    <div className="h-full bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] rounded-full transition-all duration-1000" style={{width: `${percent}%`}}></div>
                                  </div>
                                  <p className="text-[10px] text-slate-400 font-bold text-right tracking-wider">{data.correct}/{data.total} câu</p>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      </div>
                    )}
                  </>
                )}
              </div>

              {/* ========================================================= */}
              {/* CỘT PHẢI (XL:COL-SPAN-5): LỊCH SỬ ĐIỂM / NHẬT KÝ TRUY CẬP */}
              {/* ========================================================= */}
              <div className="xl:col-span-5 space-y-4 md:space-y-6">
                <div className="bg-white rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-xs overflow-hidden flex flex-col">
                  {/* CARD HEADER VỚI 2 NÚT CHUYỂN ĐỔI: LỊCH SỬ LÀM BÀI / LỊCH SỬ HOẠT ĐỘNG */}
                  <div className="px-4 sm:px-6 py-4 border-b border-slate-200/80 flex flex-wrap justify-between items-center gap-2 bg-slate-50/70">
                    <div className="flex bg-slate-200/70 p-1 rounded-xl gap-1">
                      <button
                        type="button"
                        onClick={() => setAnalyticsView('scores')}
                        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-extrabold text-xs sm:text-[13px] transition-all cursor-pointer ${
                          analyticsView === 'scores' 
                            ? 'bg-white text-[#0a5482] shadow-xs' 
                            : 'text-slate-600 hover:text-[#0a5482] hover:bg-white/50'
                        }`}
                      >
                        <span>📋</span> Lịch sử làm bài
                      </button>
                      <button
                        type="button"
                        onClick={() => setAnalyticsView('activity')}
                        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-extrabold text-xs sm:text-[13px] transition-all cursor-pointer ${
                          analyticsView === 'activity' 
                            ? 'bg-white text-[#0a5482] shadow-xs' 
                            : 'text-slate-600 hover:text-[#0a5482] hover:bg-white/50'
                        }`}
                      >
                        <span>👀</span> Lịch sử hoạt động
                      </button>
                    </div>

                    <span className="text-xs font-extrabold text-[#0a5482] bg-sky-50 border border-sky-200/80 px-2.5 py-1 rounded-full">
                      {analyticsView === 'scores' ? `${processedHistory.length} bài` : `${filteredActivities.length} hoạt động`}
                    </span>
                  </div>

                  {/* NỘI DUNG CARD: BẢNG LỊCH SỬ HOẶC DÒNG THỜI GIAN HOẠT ĐỘNG */}
                  {analyticsView === 'scores' ? (
                    <>
                      <div className="overflow-x-auto custom-scrollbar bg-slate-50/50" style={{ WebkitOverflowScrolling: 'touch' }}>
                        <table className="w-full text-left border-collapse min-w-[460px]">
                          <thead>
                            <tr className="border-b border-slate-200/80 text-[11px] text-slate-500 uppercase tracking-widest bg-slate-50/80">
                              <th className="px-4 sm:px-5 py-3.5 font-extrabold">Tên bài kiểm tra</th>
                              <th className="px-3 sm:px-4 py-3.5 font-extrabold text-center">Ngày</th>
                              <th className="px-3 sm:px-4 py-3.5 font-extrabold text-center">Điểm số</th>
                              <th className="px-4 sm:px-5 py-3.5 font-extrabold text-right">Chi tiết</th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-100 bg-white">
                            {paginatedHistory.length === 0 ? (
                              <tr>
                                <td colSpan={4} className="text-center py-12 text-slate-400 font-medium text-sm">
                                  Chưa có bài kiểm tra nào được hoàn thành
                                </td>
                              </tr>
                            ) : (
                              paginatedHistory.map(history => {
                                const isHigh = history.scoreObj.value > 60 || parseFloat(history.details?.bandScore) >= 6.0;
                                return (
                                  <tr key={history.id} className="hover:bg-sky-50/30 transition-colors group">
                                    <td className="px-4 sm:px-5 py-3.5">
                                      <div className="font-bold text-[13px] text-slate-800 leading-snug group-hover:text-[#0a5482] transition-colors line-clamp-2">
                                        {history.name}
                                      </div>
                                    </td>
                                    <td className="px-3 sm:px-4 py-3.5 text-center shrink-0">
                                      <div className="font-bold text-[12px] text-slate-700">{formatDate(history.date).split(' ')[0]}</div>
                                      <div className="text-[10px] font-medium text-slate-400 mt-0.5">{formatDate(history.date).split(' ')[1]}</div>
                                    </td>
                                    <td className="px-3 sm:px-4 py-3.5 text-center shrink-0">
                                      <span className={`inline-flex items-center justify-center px-2.5 py-1 rounded-lg text-[12px] font-black border ${isHigh ? 'bg-emerald-50 text-emerald-600 border-emerald-200' : 'bg-sky-50/60 text-[#0a5482] border-sky-200/80'}`}>
                                        {(() => {
                                          const isIelts = String(history.details?.test_type || history.name).toLowerCase().includes('ielts') || history.details?.bandScore !== undefined;
                                          if (isIelts) {
                                            return `${history.scoreObj.value}/${history.scoreObj.total} • Band ${history.details?.bandScore || '0.0'}`;
                                          } else {
                                            const p = history.scoreObj.total > 0 ? (history.scoreObj.value / history.scoreObj.total) * 100 : 0;
                                            let grade = 'U';
                                            if (p >= 90) grade = 'A*';
                                            else if (p >= 80) grade = 'A';
                                            else if (p >= 70) grade = 'B';
                                            else if (p >= 60) grade = 'C';
                                            else if (p >= 50) grade = 'D';
                                            else if (p >= 40) grade = 'E';
                                            return `${Math.round(p)}% • ${grade}`;
                                          }
                                        })()}
                                      </span>
                                    </td>
                                    <td className="px-4 sm:px-5 py-3.5 text-right shrink-0">
                                      <button 
                                        type="button"
                                        onClick={() => setViewingHistoryDetail(history)} 
                                        className="inline-flex items-center bg-sky-50 border border-sky-200/90 text-[#0a5482] font-extrabold px-3 py-1.5 rounded-xl hover:border-[#0a5482] hover:bg-[#0a5482] hover:text-white transition-all text-[11px] uppercase tracking-wider shadow-2xs cursor-pointer"
                                      >
                                        Chi tiết
                                      </button>
                                    </td>
                                  </tr>
                                );
                              })
                            )}
                          </tbody>
                        </table>
                      </div>
                      {renderPagination(historyPage, totalHistoryPages, setHistoryPage)}
                    </>
                  ) : (
                    <>
                      <div className="p-4 sm:p-5">
                        {paginatedActivities.length === 0 ? (
                          <div className="text-center py-16">
                            <p className="text-5xl mb-3">📭</p>
                            <p className="text-slate-500 font-bold text-sm">Chưa có hoạt động nào được ghi nhận</p>
                          </div>
                        ) : (
                          <div className="relative pl-6 space-y-3 before:absolute before:left-2.5 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-200">
                            {paginatedActivities.map((act: any, idx: number) => {
                              let details: any = act.details;
                              if (typeof details === 'string') {
                                try {
                                  details = JSON.parse(details);
                                } catch (e) {
                                  // plain string, keep as is
                                }
                              }

                              let icon = '📖';
                              let title = 'HOÀN THÀNH BÀI GIẢNG';
                              let desc = '';

                              if (act.action_type === 'login') {
                                icon = '🔑';
                                title = 'ĐĂNG NHẬP HỆ THỐNG';
                                desc = details?.message || 'Học sinh đăng nhập thành công vào LMS Tony English.';
                              } else if (act.action_type === 'finish_test') {
                                icon = '📝';
                                title = 'NỘP BÀI KIỂM TRA';
                                const testName = details?.test_title || details?.title || details?.name || 'Bài kiểm tra';
                                const scorePart = (details?.score !== undefined && details?.total !== undefined)
                                  ? ` • Điểm số: ${details.score}/${details.total}`
                                  : details?.score !== undefined
                                    ? ` • Điểm: ${details.score}`
                                    : '';
                                desc = `Đã hoàn thành: "${testName}"${scorePart}`;
                              } else if (act.action_type === 'call_tutor') {
                                icon = '📞';
                                title = 'HỎI ĐÁP GIA SƯ AI / VOICE';
                                const durPart = details?.duration ? `Thời lượng: ${details.duration} giây` : '';
                                const topicPart = details?.topic ? `Chủ đề: "${details.topic}"` : '';
                                desc = [durPart, topicPart].filter(Boolean).join(' • ') || details?.message || 'Đã đàm thoại với gia sư AI.';
                              } else if (act.action_type === 'finish_lecture') {
                                icon = '📖';
                                title = 'HOÀN THÀNH BÀI GIẢNG';
                                const lecName = details?.lecture_title || details?.title || details?.name || (typeof details === 'string' ? details : 'Bài giảng');
                                desc = `Đã học xong: "${lecName}"`;
                              } else {
                                icon = '📌';
                                title = (act.action_type || 'HOẠT ĐỘNG').toUpperCase();
                                if (details && typeof details === 'object') {
                                  desc = details.lecture_title 
                                    ? `Đã học xong: "${details.lecture_title}"`
                                    : details.test_title 
                                      ? `Đã hoàn thành: "${details.test_title}"`
                                      : details.message || details.title || '';
                                } else {
                                  desc = typeof details === 'string' ? details : '';
                                }
                              }

                              const dateStr = new Date(act.created_at).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });
                              return (
                                <div key={act.id || idx} className="relative group">
                                  <div className="absolute -left-[27px] top-1.5 w-6 h-6 rounded-full bg-white border-2 border-sky-400 flex items-center justify-center text-xs shadow-xs group-hover:scale-110 transition-transform">
                                    {icon}
                                  </div>
                                  <div className="bg-slate-50/80 hover:bg-slate-100/80 border border-slate-200/70 rounded-xl p-3.5 transition-all shadow-2xs">
                                    <div className="flex items-center justify-between gap-2 mb-1">
                                      <span className="font-bold text-xs sm:text-[13px] text-slate-800 uppercase tracking-wide">{title}</span>
                                      <span className="text-[11px] font-semibold text-sky-600 bg-sky-50 px-2 py-0.5 rounded-md shrink-0 border border-sky-100">{dateStr}</span>
                                    </div>
                                    {desc && <p className="text-xs text-slate-600 leading-relaxed line-clamp-2" title={desc}>{desc}</p>}
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        )}
                      </div>
                      {renderPagination(activityPage, totalActivityPages, setActivityPage)}
                    </>
                  )}
                </div>
              </div>
            </div>


            <BoardThemeModal
              isOpen={isAnalyticsThemeModalOpen}
              currentTheme={analyticsTheme}
              onSelectTheme={handleSelectAnalyticsTheme}
              onApplyCustomColor={handleApplyCustomAnalyticsColor}
              onClose={() => setIsAnalyticsThemeModalOpen(false)}
            />
          </div>
        )}

        {/* =====================================================================
            🚀 TRANG CẤU HÌNH TÀI KHOẢN (PROFILE)
            ===================================================================== */}
        {activeTab === 'profile' && (
          <div className="max-w-2xl mx-auto mt-4 md:mt-6 mb-12 px-2 sm:px-0 space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
            
            {/* Header Thẻ Cá Nhân */}
            <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] p-6 md:p-8 rounded-2xl sm:rounded-3xl border border-slate-800/40 shadow-md flex flex-col sm:flex-row items-center gap-6 text-center sm:text-left text-white">
              <div className="w-20 h-20 md:w-22 md:h-22 rounded-2xl bg-gradient-to-br from-[#2ab4e8] to-[#0a5482] text-white flex items-center justify-center font-black text-3xl md:text-4xl shadow-lg border-2 border-white/30 shrink-0">
                {displayUserInitial}
              </div>
              <div className="flex-1">
                <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2.5 mb-1.5">
                  <h2 className="text-2xl md:text-3xl font-black text-white tracking-tight">{displayUserName}</h2>
                  <span className="text-[#2ab4e8] font-extrabold text-[11px] bg-white/10 px-3 py-0.5 rounded-full border border-white/15 uppercase tracking-widest">
                    {userProfile?.role === 'admin' ? 'Quản trị viên' : 'Học viên TonyEnglish'}
                  </span>
                </div>
                <p className="text-slate-300 text-[14px] flex items-center justify-center sm:justify-start gap-1.5 font-medium">
                  <svg className="w-4 h-4 text-[#2ab4e8]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  {currentUser?.email || "Chưa có email"}
                </p>
              </div>
            </div>

            {/* Khối 1: Thông tin học viên */}
            <div className="bg-white p-6 md:p-8 rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-xs">
              <div className="flex items-center gap-3 mb-6 pb-4 border-b border-slate-100">
                <div className="w-10 h-10 rounded-xl bg-sky-50 text-[#0a5482] flex items-center justify-center text-xl font-bold border border-sky-100">
                  👤
                </div>
                <div>
                  <h3 className="font-black text-lg text-slate-800 tracking-tight">Thông Tin Cá Nhân</h3>
                  <p className="text-slate-400 text-[13px]">Cập nhật họ tên hiển thị và mục tiêu học tập</p>
                </div>
              </div>

              {profileSuccessMsg && (
                <div className="mb-5 p-3.5 bg-emerald-50 border border-emerald-200 text-emerald-700 text-[14px] font-bold rounded-xl flex items-center gap-2 animate-in fade-in">
                  <span>✓</span>
                  <span>{profileSuccessMsg}</span>
                </div>
              )}
              {profileErrorMsg && (
                <div className="mb-5 p-3.5 bg-rose-50 border border-rose-200 text-rose-700 text-[14px] font-bold rounded-xl flex items-center gap-2 animate-in shake">
                  <span>⚠️</span>
                  <span>{profileErrorMsg}</span>
                </div>
              )}

              <form onSubmit={handleUpdateProfile} className="space-y-4">
                <div className="space-y-1.5">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Họ và tên</label>
                  <input 
                    type="text" 
                    value={newFullName} 
                    onChange={e => setNewFullName(e.target.value)} 
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 font-semibold text-slate-800 focus:border-[#2ab4e8] focus:bg-white focus:ring-4 focus:ring-[#2ab4e8]/10 outline-none transition-all text-[15px]" 
                    placeholder="Nhập họ và tên..." 
                  />
                </div>
                
                <div className="space-y-1.5">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Mục tiêu IELTS / Điểm số</label>
                  <input 
                    type="text" 
                    value={courseTargets.ielts || ''} 
                    onChange={e => handleUpdateTarget('ielts', e.target.value)} 
                    className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 font-semibold text-slate-800 focus:border-amber-500 focus:bg-white focus:ring-4 focus:ring-amber-500/10 outline-none transition-all text-[15px]" 
                    placeholder="Ví dụ: 7.0 hoặc A*" 
                  />
                </div>
                
                <div className="space-y-1.5">
                  <div className="flex justify-between items-center ml-1">
                    <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest">Email đăng nhập</label>
                    <span className="text-[11px] text-slate-400 font-medium flex items-center gap-1">🔒 Cố định</span>
                  </div>
                  <input 
                    type="email" 
                    defaultValue={currentUser?.email || ""} 
                    disabled 
                    className="w-full bg-slate-100 border border-slate-200 rounded-xl px-4 py-3.5 font-semibold text-slate-400 outline-none cursor-not-allowed text-[15px]" 
                  />
                </div>

                <div className="pt-2">
                  <button 
                    type="submit" 
                    disabled={isUpdatingProfile} 
                    className="bg-[#0a5482] hover:bg-[#084266] disabled:bg-slate-300 text-white font-black px-6 py-3.5 rounded-xl transition-all w-full text-[14px] uppercase tracking-wider shadow-md shadow-blue-900/15 hover:shadow-lg disabled:shadow-none active:scale-[0.99] flex items-center justify-center gap-2 cursor-pointer"
                  >
                    {isUpdatingProfile ? (
                      <>
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        <span>Đang lưu...</span>
                      </>
                    ) : (
                      'Lưu Thông Tin Cá Nhân'
                    )}
                  </button>
                </div>
              </form>
            </div>

            {/* Khối 2: Đổi mật khẩu tài khoản */}
            <div className="bg-white p-6 md:p-8 rounded-2xl sm:rounded-3xl border border-slate-200/90 shadow-xs">
              <div className="flex items-center gap-3 mb-6 pb-4 border-b border-slate-100">
                <div className="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl font-bold border border-amber-100">
                  🔐
                </div>
                <div>
                  <h3 className="font-black text-lg text-slate-800 tracking-tight">Đổi Mật Khẩu Tài Khoản</h3>
                  <p className="text-slate-400 text-[13px]">Bảo vệ tài khoản với mật khẩu mới có ít nhất 6 ký tự</p>
                </div>
              </div>

              {passwordSuccessMsg && (
                <div className="mb-5 p-3.5 bg-emerald-50 border border-emerald-200 text-emerald-700 text-[14px] font-bold rounded-xl flex items-center gap-2 animate-in fade-in">
                  <span>✓</span>
                  <span>{passwordSuccessMsg}</span>
                </div>
              )}
              {passwordErrorMsg && (
                <div className="mb-5 p-3.5 bg-rose-50 border border-rose-200 text-rose-700 text-[14px] font-bold rounded-xl flex items-center gap-2 animate-in shake">
                  <span>⚠️</span>
                  <span>{passwordErrorMsg}</span>
                </div>
              )}

              <form onSubmit={handleChangePassword} className="space-y-4">
                <div className="space-y-1.5">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Mật khẩu mới</label>
                  <div className="relative">
                    <input 
                      type={showNewPassword ? 'text' : 'password'}
                      placeholder="Nhập mật khẩu mới (tối thiểu 6 ký tự)..." 
                      value={newPassword} 
                      onChange={(e) => {
                        setNewPassword(e.target.value);
                        setPasswordErrorMsg('');
                      }} 
                      className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 pr-12 font-semibold text-slate-800 focus:border-[#2ab4e8] focus:bg-white focus:ring-4 focus:ring-[#2ab4e8]/10 outline-none transition-all text-[15px]" 
                    />
                    <button 
                      type="button" 
                      onClick={() => setShowNewPassword(!showNewPassword)}
                      className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1"
                    >
                      {showNewPassword ? (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />
                        </svg>
                      ) : (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                        </svg>
                      )}
                    </button>
                  </div>
                </div>

                <div className="space-y-1.5">
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-widest ml-1">Xác nhận mật khẩu mới</label>
                  <div className="relative">
                    <input 
                      type={showConfirmPassword ? 'text' : 'password'}
                      placeholder="Nhập lại mật khẩu mới..." 
                      value={confirmPassword} 
                      onChange={(e) => {
                        setConfirmPassword(e.target.value);
                        setPasswordErrorMsg('');
                      }} 
                      className="w-full bg-slate-50 border border-slate-200 rounded-xl px-4 py-3.5 pr-12 font-semibold text-slate-800 focus:border-[#2ab4e8] focus:bg-white focus:ring-4 focus:ring-[#2ab4e8]/10 outline-none transition-all text-[15px]" 
                    />
                    <button 
                      type="button" 
                      onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                      className="absolute right-3.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 p-1"
                    >
                      {showConfirmPassword ? (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />
                        </svg>
                      ) : (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                        </svg>
                      )}
                    </button>
                  </div>
                  {confirmPassword && newPassword && confirmPassword !== newPassword && (
                    <p className="text-[12px] text-rose-500 font-semibold ml-1">Mật khẩu xác nhận không khớp!</p>
                  )}
                  {confirmPassword && newPassword && confirmPassword === newPassword && (
                    <p className="text-[12px] text-emerald-600 font-semibold ml-1 flex items-center gap-1">✓ Mật khẩu khớp</p>
                  )}
                </div>

                <div className="pt-2">
                  <button 
                    type="submit" 
                    disabled={isChangingPassword || !newPassword || newPassword.length < 6 || newPassword !== confirmPassword} 
                    className="bg-amber-600 hover:bg-amber-700 disabled:bg-slate-300 text-white font-black px-6 py-3.5 rounded-xl transition-all w-full text-[14px] uppercase tracking-wider shadow-md hover:shadow-lg disabled:shadow-none active:scale-[0.99] flex items-center justify-center gap-2 cursor-pointer"
                  >
                    {isChangingPassword ? (
                      <>
                        <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        <span>Đang cập nhật mật khẩu...</span>
                      </>
                    ) : (
                      'Cập Nhật Mật Khẩu Mới ➔'
                    )}
                  </button>
                </div>
              </form>
            </div>

          </div>
        )}

      </main>

      {/* UNIFIED COMPACT FOOTER (Đồng bộ với TonyEnglish.vn) */}
      <footer className="bg-[#0f172a] text-slate-400 py-8 border-t border-slate-800 mt-12 shrink-0">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <img
              src="/logo-shield.png"
              onError={(e) => {
                (e.currentTarget as HTMLImageElement).src = '/themes/tony/assets/img/logo khong chu.png';
              }}
              alt="TonyEnglish"
              className="h-7 w-auto object-contain"
            />
            <div>
              <div className="font-black text-base tracking-tight text-white">
                <span className="text-[#2ab4e8]">TONY</span>ENGLISH <span className="text-xs font-semibold text-slate-400">• Student Portal</span>
              </div>
              <p className="text-xs text-slate-500">
                © 2013–2026 TonyEnglish.vn — Hệ sinh thái đào tạo Tiếng Anh &amp; Luyện thi thông minh tích hợp AI.
              </p>
            </div>
          </div>

          <div className="flex flex-wrap items-center justify-center gap-4 text-xs font-semibold text-slate-400">
            <button
              type="button"
              onClick={() => {
                resetWorkspaceAndChat();
                window.history.pushState({}, '', '/');
                onNavigate?.('home');
              }}
              className="hover:text-[#2ab4e8] transition-colors cursor-pointer"
            >
              🏠 Trang chủ
            </button>
            <span>•</span>
            <a
              href="/courses"
              onClick={(e) => {
                e.preventDefault();
                resetWorkspaceAndChat();
                window.history.pushState({}, '', '/courses');
                onNavigate?.('home');
              }}
              className="hover:text-[#2ab4e8] transition-colors cursor-pointer"
            >
              🎓 Các khóa học
            </a>
            <span>•</span>
            <a
              href="/news"
              onClick={(e) => {
                e.preventDefault();
                resetWorkspaceAndChat();
                window.history.pushState({}, '', '/news');
                onNavigate?.('home');
              }}
              className="hover:text-[#2ab4e8] transition-colors cursor-pointer"
            >
              📚 Thư viện bài đọc
            </a>
            <span>•</span>
            <a
              href="/videos"
              onClick={(e) => {
                e.preventDefault();
                resetWorkspaceAndChat();
                window.history.pushState({}, '', '/videos');
                onNavigate?.('home');
              }}
              className="hover:text-[#2ab4e8] transition-colors cursor-pointer"
            >
              🎬 Kho Video
            </a>
          </div>
        </div>
      </footer>

      {/* POPUP CHI TIẾT LỊCH SỬ */}
      {viewingHistoryDetail && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-[100] flex items-center justify-center p-4 animate-in fade-in duration-200">
          <div className="bg-white rounded-3xl w-full max-w-lg shadow-2xl overflow-hidden border border-slate-200 animate-in zoom-in-95">
             <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-7 py-5 text-white flex justify-between items-center">
                <h3 className="font-black text-[13px] uppercase tracking-widest text-[#2ab4e8]">Bảng Kết Quả Làm Bài</h3>
                <button onClick={() => setViewingHistoryDetail(null)} className="text-white/70 hover:text-white w-8 h-8 rounded-full hover:bg-white/10 flex items-center justify-center transition-colors cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2.5} stroke="currentColor" className="w-5 h-5"><path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                </button>
             </div>
             
             <div className="p-7 md:p-9">
                <div className="text-center mb-7 border-b border-slate-100 pb-7">
                   <h2 className="text-xl sm:text-2xl font-black text-slate-800 mb-2 leading-tight">{viewingHistoryDetail.name}</h2>
                   <p className="text-slate-500 font-medium text-[13px] mb-6">Nộp lúc: <span className="text-slate-700">{formatDate(viewingHistoryDetail.date)}</span></p>
                   
                   <div className="flex justify-center gap-4">
                      <div className="bg-slate-50 border border-slate-200 px-6 py-4 rounded-2xl flex-1 shadow-2xs">
                         <p className="text-[11px] font-bold uppercase text-slate-500 tracking-widest mb-1">Thời gian</p>
                         <p className="text-2xl font-black text-slate-800">{viewingHistoryDetail.timeSpent} <span className="text-[13px] font-bold text-slate-500 uppercase">phút</span></p>
                      </div>
                      <div className="bg-emerald-50 border border-emerald-200 px-6 py-4 rounded-2xl flex-1 shadow-2xs">
                         <p className="text-[11px] font-bold uppercase text-emerald-600 tracking-widest mb-1">Kết quả</p>
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
                    }} className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-3.5 rounded-xl transition-colors uppercase tracking-wider text-[13px] shadow-md shadow-blue-900/15 cursor-pointer">
                        Xem chi tiết chữa bài
                    </button>
                    
                    <button onClick={() => handleRetakeFromHistory(viewingHistoryDetail)} className="w-full bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-3.5 rounded-xl transition-colors uppercase tracking-wider text-[13px] cursor-pointer">
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
          <div className="bg-white w-full max-w-[480px] p-7 md:p-10 rounded-3xl shadow-2xl border border-slate-200 animate-in zoom-in-95">
            
            <div className="mb-7 text-center">
              <div className="w-16 h-16 bg-sky-50 rounded-2xl flex items-center justify-center text-3xl mx-auto mb-4 border border-sky-100">
                 🎓
              </div>
              <span className="text-[11px] font-extrabold uppercase tracking-widest text-[#2ab4e8] block mb-1">TonyEnglish IELTS Testing</span>
              <h2 className="text-[20px] md:text-[22px] font-black text-slate-800 mb-2 leading-tight line-clamp-2" title={testToStart.title}>{testToStart.title}</h2>
              <p className="text-[14px] text-slate-500 font-medium">
                Vui lòng chọn hình thức thi bạn muốn tham gia:
              </p>
            </div>

            <div className="space-y-3.5">
              <button 
                onClick={() => handleConfirmMode('computer')}
                className="w-full flex items-center p-4.5 bg-white border-2 border-slate-200/80 hover:border-[#0a5482] hover:shadow-md hover:-translate-y-0.5 rounded-2xl transition-all duration-300 text-left group cursor-pointer"
              >
                <div className="w-13 h-13 shrink-0 flex items-center justify-center bg-sky-50 text-[#0a5482] group-hover:bg-[#0a5482] group-hover:text-white rounded-xl mr-4 transition-colors duration-300">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 17.25v1.007a3 3 0 0 1-.879 2.122L7.5 21h9l-.621-.621A3 3 0 0 1 15 18.257V17.25m6-12V15a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 15V5.25m18 0A2.25 2.25 0 0 0 18.75 3H5.25A2.25 2.25 0 0 0 3 5.25m18 0V12a2.25 2.25 0 0 1-2.25 2.25H5.25A2.25 2.25 0 0 1 3 12V5.25" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[15.5px] font-black text-slate-800 group-hover:text-[#0a5482] transition-colors">Thi trên máy tính (Computer-delivered)</h3>
                  <p className="text-[12.5px] text-slate-500 mt-0.5 font-medium">Giao diện chia đôi màn hình, highlight &amp; chấm điểm tự động</p>
                </div>
              </button>

              <button 
                onClick={() => handleConfirmMode('paper')}
                className="w-full flex items-center p-4.5 bg-white border-2 border-slate-200/80 hover:border-emerald-600 hover:shadow-md hover:-translate-y-0.5 rounded-2xl transition-all duration-300 text-left group cursor-pointer"
              >
                <div className="w-13 h-13 shrink-0 flex items-center justify-center bg-emerald-50 text-emerald-600 group-hover:bg-emerald-600 group-hover:text-white rounded-xl mr-4 transition-colors duration-300">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-[15.5px] font-black text-slate-800 group-hover:text-emerald-600 transition-colors">Thi trên giấy (Paper-based)</h3>
                  <p className="text-[12.5px] text-slate-500 mt-0.5 font-medium">Làm trên giấy, xem đề PDF &amp; nghe Audio</p>
                </div>
              </button>
            </div>

            <div className="mt-6 pt-3 flex justify-center">
              <button 
                onClick={() => setShowModeSelection(false)}
                className="text-[13px] font-black text-slate-400 hover:text-slate-600 hover:bg-slate-100 uppercase tracking-widest transition-colors py-2.5 px-8 rounded-xl cursor-pointer"
              >
                Hủy bỏ
              </button>
            </div>

          </div>
        </div>
      )}

      {/* 📱 STICKY MOBILE BOTTOM NAVIGATION BAR */}
      <nav 
        aria-label="Mobile Navigation"
        className="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-lg border-t border-slate-200/90 shadow-[0_-4px_20px_rgba(0,0,0,0.06)] px-2 py-1 flex items-center justify-around"
        style={{ paddingBottom: 'calc(env(safe-area-inset-bottom, 0px) + 6px)' }}
      >
        <button
          type="button"
          onClick={() => {
            resetWorkspaceAndChat();
            setActiveTab('library');
            setActiveView('dashboard');
            setSelectedCourseId(null);
            setCurrentFolderId(null);
          }}
          className={`flex flex-col items-center justify-center py-1 px-3 rounded-2xl transition-all duration-200 min-w-[64px] ${
            activeTab === 'library'
              ? 'text-[#0a5482] font-bold scale-105'
              : 'text-slate-400 hover:text-slate-600 font-medium'
          }`}
        >
          <div className={`p-1 rounded-xl transition-colors ${activeTab === 'library' ? 'bg-sky-50 text-[#0a5482]' : ''}`}>
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={activeTab === 'library' ? 2.5 : 2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <span className="text-[10px] tracking-tight mt-0.5">Học tập</span>
        </button>

        <button
          type="button"
          onClick={() => {
            resetWorkspaceAndChat();
            setActiveTab('calendar');
          }}
          className={`flex flex-col items-center justify-center py-1 px-3 rounded-2xl transition-all duration-200 min-w-[64px] ${
            activeTab === 'calendar'
              ? 'text-[#0a5482] font-bold scale-105'
              : 'text-slate-400 hover:text-slate-600 font-medium'
          }`}
        >
          <div className={`p-1 rounded-xl transition-colors ${activeTab === 'calendar' ? 'bg-sky-50 text-[#0a5482]' : ''}`}>
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={activeTab === 'calendar' ? 2.5 : 2} d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" />
            </svg>
          </div>
          <span className="text-[10px] tracking-tight mt-0.5">Lịch báo bài</span>
        </button>

        <button
          type="button"
          onClick={() => {
            resetWorkspaceAndChat();
            setActiveTab('board');
          }}
          className={`flex flex-col items-center justify-center py-1 px-3 rounded-2xl transition-all duration-200 min-w-[64px] ${
            activeTab === 'board'
              ? 'text-[#0a5482] font-bold scale-105'
              : 'text-slate-400 hover:text-slate-600 font-medium'
          }`}
        >
          <div className={`p-1 rounded-xl transition-colors ${activeTab === 'board' ? 'bg-sky-50 text-[#0a5482]' : ''}`}>
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={activeTab === 'board' ? 2.5 : 2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
            </svg>
          </div>
          <span className="text-[10px] tracking-tight mt-0.5">Bảng việc</span>
        </button>

        <button
          type="button"
          onClick={() => {
            resetWorkspaceAndChat();
            setActiveTab('analytics');
          }}
          className={`flex flex-col items-center justify-center py-1 px-3 rounded-2xl transition-all duration-200 min-w-[64px] ${
            activeTab === 'analytics'
              ? 'text-[#0a5482] font-bold scale-105'
              : 'text-slate-400 hover:text-slate-600 font-medium'
          }`}
        >
          <div className={`p-1 rounded-xl transition-colors ${activeTab === 'analytics' ? 'bg-sky-50 text-[#0a5482]' : ''}`}>
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={activeTab === 'analytics' ? 2.5 : 2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
          </div>
          <span className="text-[10px] tracking-tight mt-0.5">Báo cáo</span>
        </button>
      </nav>
    </div>
  );
}