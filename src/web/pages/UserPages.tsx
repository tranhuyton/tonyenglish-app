import React, { useEffect, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { unserializePhpIds, fixLegacyHtmlContent, encryptLegacyPass, resolveUploadUrl } from '../lib/utils';

/* 1. LOGIN PAGE (/user/login) */
export const LoginPage: React.FC = () => {
  const { t, loginUser } = useApp();
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    const res = await loginUser(username, password);
    setLoading(false);
    if (res.ok) {
      navigate('/user/lecture');
    } else {
      setError(res.error || 'Login failed');
    }
  };

  return (
    <div className="max-w-md mx-auto px-4 py-16">
      <div className="bg-white rounded-3xl border border-slate-200 shadow-xl overflow-hidden">
        <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-8 py-6 text-white">
          <h2 className="text-2xl font-black">{t('Sign in')}</h2>
          <p className="text-xs text-sky-200 mt-1">Đăng nhập tài khoản học viên TonyEnglish</p>
        </div>
        <form onSubmit={handleSubmit} className="p-8 space-y-5">
          <div>
            <label className="block text-xs font-bold text-slate-500 uppercase mb-1.5">
              {t('Enter your Email')} / Username
            </label>
            <input
              type="text"
              required
              placeholder={t('Enter your Email')}
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
            />
          </div>
          <div>
            <label className="block text-xs font-bold text-slate-500 uppercase mb-1.5">
              {t('Enter your password')}
            </label>
            <input
              type="password"
              required
              placeholder={t('Enter your password')}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
            />
          </div>
          {error && <div className="p-3 bg-rose-50 text-rose-700 rounded-xl text-xs font-bold">{error}</div>}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-3.5 rounded-xl shadow-lg transition"
          >
            {loading ? '...' : `${t('Sign in')} ➜`}
          </button>
          <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold">
            <Link to="/courses" className="text-[#0a5482] hover:underline">
              {t('Register')}
            </Link>
            <a href="https://lms.tonyenglish.vn" className="text-[#2ab4e8] hover:underline">
              🎓 Cổng LMS mới →
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

/* 2. LECTURE & TRIAL COURSE VIEWER (/user/lecture & /trial/:courseSlug) */
export const LecturePage: React.FC<{ isTrial?: boolean }> = ({ isTrial = false }) => {
  const { courseSlug, lectureSlug } = useParams<{ courseSlug?: string; lectureSlug?: string }>();
  const { lang, t, selectedCourseId } = useApp();

  const [classes, setClasses] = useState<any[]>([]);
  const [selectedClass, setSelectedClass] = useState<any | null>(null);
  const [lecturesByClass, setLecturesByClass] = useState<Record<number, any[]>>({});
  const [currentLecture, setCurrentLecture] = useState<any | null>(null);
  const [lecturePages, setLecturePages] = useState<any[]>([]);
  const [curPageIdx, setCurPageIdx] = useState(0);

  const [showQuestion, setShowQuestion] = useState(false);
  const [showAnswer, setShowAnswer] = useState(false);
  const [showDialog, setShowDialog] = useState(false);
  const [showVocab, setShowVocab] = useState(false);
  const [showQuiz, setShowQuiz] = useState(false);
  const [mobileCateOpen, setMobileCateOpen] = useState(false);

  useEffect(() => {
    async function loadClassesAndLectures() {
      let targetCourseId = selectedCourseId;

      if (isTrial && courseSlug) {
        const { data: cRows } = await supabase
          .from('te_course_category')
          .select('*')
          .eq('deleted', 0)
          .eq('cc_name_url', courseSlug.replace(/\.html$/i, ''))
          .limit(1);
        if (cRows && cRows.length > 0) {
          targetCourseId = cRows[0].cc_id;
        }
      }

      let classQuery = supabase
        .from('te_class_category')
        .select('*')
        .eq('deleted', 0)
        .eq('cl_status', 1)
        .order('cl_order', { ascending: true });

      if (targetCourseId) {
        classQuery = classQuery.eq('c_id', targetCourseId);
      }

      const { data: clRows } = await classQuery;
      let activeClasses = clRows || [];

      if (activeClasses.length === 0) {
        const { data: allCls } = await supabase
          .from('te_class_category')
          .select('*')
          .eq('deleted', 0)
          .eq('cl_status', 1)
          .order('cl_order', { ascending: true })
          .limit(30);
        activeClasses = allCls || [];
      }

      setClasses(activeClasses);

      const allLecIds = new Set<number>();
      const classLecMap: Record<number, number[]> = {};
      activeClasses.forEach((cls) => {
        const ids = unserializePhpIds(cls.lec_id);
        classLecMap[cls.cl_id] = ids;
        ids.forEach((id) => allLecIds.add(id));
      });

      let fetchedLectures: any[] = [];
      if (allLecIds.size > 0) {
        const { data: lRows } = await supabase
          .from('te_lecture')
          .select('*')
          .eq('deleted', 0)
          .eq('lecture_status', 1)
          .in('lecture_id', Array.from(allLecIds))
          .order('lecture_order', { ascending: true });
        fetchedLectures = lRows || [];
      } else if (targetCourseId) {
        const { data: lRows } = await supabase
          .from('te_lecture')
          .select('*')
          .eq('deleted', 0)
          .eq('lecture_status', 1)
          .eq('cc_id', targetCourseId)
          .order('lecture_order', { ascending: true });
        fetchedLectures = lRows || [];
      }

      const byClass: Record<number, any[]> = {};
      activeClasses.forEach((cls) => {
        const ids = classLecMap[cls.cl_id] || [];
        byClass[cls.cl_id] = fetchedLectures.filter(
          (l) => ids.includes(Number(l.lecture_id)) || Number(l.cc_id) === Number(cls.c_id)
        );
      });
      setLecturesByClass(byClass);

      const firstClsWithLec = activeClasses.find((c) => (byClass[c.cl_id] || []).length > 0) || activeClasses[0];
      setSelectedClass(firstClsWithLec || null);

      if (lectureSlug) {
        const foundLec = fetchedLectures.find((l) => l.lecture_name_url === lectureSlug);
        if (foundLec) {
          setCurrentLecture(foundLec);
          return;
        }
      }

      if (firstClsWithLec && (byClass[firstClsWithLec.cl_id] || []).length > 0) {
        setCurrentLecture(byClass[firstClsWithLec.cl_id][0]);
      } else if (fetchedLectures.length > 0) {
        setCurrentLecture(fetchedLectures[0]);
      } else {
        setCurrentLecture(null);
      }
    }

    loadClassesAndLectures();
  }, [isTrial, courseSlug, lectureSlug, selectedCourseId]);

  useEffect(() => {
    async function loadLectureContentPages() {
      setCurPageIdx(0);
      setShowQuestion(false);
      setShowAnswer(false);
      setShowDialog(false);
      setShowVocab(false);
      setShowQuiz(false);

      if (!currentLecture) {
        setLecturePages([]);
        return;
      }

      const { data } = await supabase
        .from('te_lecture_content')
        .select('*')
        .eq('lecture_id', currentLecture.lecture_id)
        .eq('lc_status', 1)
        .order('lc_order', { ascending: true });

      setLecturePages(data || []);
    }

    loadLectureContentPages();
  }, [currentLecture]);

  const currentPageContent = lecturePages[curPageIdx] || null;
  const classTitle = selectedClass
    ? lang === 'vi'
      ? selectedClass.cl_name_vi || selectedClass.cl_name
      : selectedClass.cl_name
    : t('Lecture');

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
      {/* Banner connecting to new LMS */}
      <div className="mb-6 bg-gradient-to-r from-[#0a5482] to-[#0f172a] rounded-2xl p-4 sm:px-6 flex flex-wrap items-center justify-between gap-4 text-white shadow-md">
        <div className="flex items-center gap-3">
          <span className="text-2xl">🚀</span>
          <div>
            <div className="font-black text-sm sm:text-base">Hệ thống Bài giảng &amp; Luyện thi thế hệ mới</div>
            <div className="text-xs text-sky-200">
              Tích hợp Gia sư AI, chấm chữa Writing/Speaking và bài tập tương tác tại lms.tonyenglish.vn
            </div>
          </div>
        </div>
        <a
          href="https://lms.tonyenglish.vn"
          className="bg-[#2ab4e8] hover:bg-[#1d9ad1] text-white font-black text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-md transition whitespace-nowrap"
        >
          Chuyển sang LMS mới ➜
        </a>
      </div>

      <div className="flex flex-col lg:flex-row gap-4 sm:gap-8 xl:gap-12 items-start">
        {/* LEFT SIDEBAR */}
        <aside className="w-full lg:w-[260px] xl:w-[270px] shrink-0 bg-white rounded-2xl border border-slate-200/80 shadow-2xs overflow-hidden lg:sticky lg:top-24">
          <button
            type="button"
            onClick={() => setMobileCateOpen((prev) => !prev)}
            className="w-full bg-slate-100/80 px-4 py-3 border-b border-slate-200/70 flex items-center justify-between lg:pointer-events-none cursor-pointer text-left"
          >
            <h2 className="text-slate-600 lg:text-slate-500 font-bold text-xs uppercase tracking-widest flex items-center gap-2 min-w-0">
              <span className="opacity-80 shrink-0">📖</span>
              <span className="truncate">{isTrial ? 'Khóa học thử' : classTitle}</span>
            </h2>
            <span className="lg:hidden text-[11px] font-bold text-[#0a5482] bg-white px-2.5 py-1 rounded-lg border border-slate-200/80 shadow-2xs flex items-center gap-1 shrink-0 ml-2">
              <span>{mobileCateOpen ? 'Thu gọn' : 'Danh sách bài'}</span>
              <span>{mobileCateOpen ? '▲' : '▼'}</span>
            </span>
          </button>
          <ul className={`divide-y divide-slate-100 text-[14.5px] p-1.5 ${mobileCateOpen ? 'block' : 'hidden'} lg:block`}>
            {classes.map((cls) => {
              const isOpen = selectedClass && selectedClass.cl_id === cls.cl_id;
              const cName = lang === 'vi' ? cls.cl_name_vi || cls.cl_name : cls.cl_name;
              const lecs = lecturesByClass[cls.cl_id] || [];

              return (
                <li key={cls.cl_id}>
                  <button
                    type="button"
                    onClick={() => {
                      setSelectedClass(cls);
                      if (lecs.length > 0) setCurrentLecture(lecs[0]);
                    }}
                    className={`w-full text-left px-3.5 py-2.5 rounded-xl flex items-center justify-between ${
                      isOpen
                        ? 'bg-sky-50/90 text-[#0a5482] font-semibold'
                        : 'text-slate-600 font-medium hover:bg-slate-50'
                    }`}
                  >
                    <span>{cName}</span>
                    <span className="text-xs">{isOpen ? '▾' : '▸'}</span>
                  </button>

                  {isOpen && lecs.length > 0 && (
                    <ul className="mt-0.5 mb-1 ml-2 pl-2 border-l border-slate-200/80 space-y-0.5">
                      {lecs.map((lec) => (
                        <li key={lec.lecture_id}>
                          <button
                            type="button"
                            onClick={() => {
                              setCurrentLecture(lec);
                              setMobileCateOpen(false);
                            }}
                            className={`w-full text-left px-3 py-2 rounded-lg text-[13.5px] transition ${
                              currentLecture && currentLecture.lecture_id === lec.lecture_id
                                ? 'bg-sky-50 text-[#0a5482] font-semibold border-l-2 border-[#2ab4e8]'
                                : 'text-slate-500 font-normal hover:bg-slate-50 hover:text-slate-800'
                            }`}
                          >
                            {lec.lecture_name}
                          </button>
                        </li>
                      ))}
                    </ul>
                  )}
                </li>
              );
            })}
          </ul>
        </aside>

        {/* RIGHT LECTURE CONTENT */}
        <div className="flex-1 min-w-0 w-full">
          <div className="bg-white rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
            <div className="bg-slate-50 border-b border-slate-200 px-6 sm:px-8 py-5 flex items-center justify-between flex-wrap gap-3">
              <h1 className="text-xl sm:text-2xl font-black text-[#0a5482]">
                {currentLecture ? currentLecture.lecture_name : classTitle}
              </h1>
              {lecturePages.length > 1 && (
                <span className="text-xs font-bold bg-sky-100 text-[#0a5482] px-3 py-1 rounded-full">
                  Trang {curPageIdx + 1} / {lecturePages.length}
                </span>
              )}
            </div>

            <div className="p-6 sm:p-8 space-y-6">
              {currentLecture ? (
                <>
                  {currentPageContent ? (
                    <div
                      className="legacy-prose"
                      dangerouslySetInnerHTML={{
                        __html: fixLegacyHtmlContent(currentPageContent.lc_content),
                      }}
                    />
                  ) : (
                    currentLecture.lecture_question && (
                      <div
                        className="legacy-prose"
                        dangerouslySetInnerHTML={{
                          __html: fixLegacyHtmlContent(currentLecture.lecture_question),
                        }}
                      />
                    )
                  )}

                  {/* Interactive Vocabulary / Quiz / Q&A / Dialog */}
                  {currentPageContent && (
                    <div className="space-y-3 pt-4 border-t border-slate-200">
                      {currentPageContent.lc_vocabulary && currentPageContent.lc_vocabulary.trim() !== '' && (
                        <div className="bg-slate-50 rounded-2xl border border-slate-200 overflow-hidden">
                          <button
                            type="button"
                            onClick={() => setShowVocab(!showVocab)}
                            className="w-full px-5 py-3.5 text-left font-black text-sm text-[#0a5482] flex justify-between"
                          >
                            <span>📝 View Note / Vocabulary</span>
                            <span>{showVocab ? '▲' : '▼'}</span>
                          </button>
                          {showVocab && (
                            <div
                              className="p-5 border-t border-slate-200 legacy-prose text-sm"
                              dangerouslySetInnerHTML={{
                                __html: fixLegacyHtmlContent(currentPageContent.lc_vocabulary),
                              }}
                            />
                          )}
                        </div>
                      )}

                      {currentPageContent.lc_link_quiz && currentPageContent.lc_link_quiz.trim() !== '' && (
                        <div className="bg-slate-50 rounded-2xl border border-slate-200 overflow-hidden">
                          <button
                            type="button"
                            onClick={() => setShowQuiz(!showQuiz)}
                            className="w-full px-5 py-3.5 text-left font-black text-sm text-[#0a5482] flex justify-between"
                          >
                            <span>🎯 Start Quiz</span>
                            <span>{showQuiz ? '▲' : '▼'}</span>
                          </button>
                          {showQuiz && (
                            <div className="p-4 border-t border-slate-200">
                              <iframe
                                width="100%"
                                height="550px"
                                src={currentPageContent.lc_link_quiz}
                                title="Quiz"
                                className="rounded-xl border border-slate-200"
                              />
                            </div>
                          )}
                        </div>
                      )}

                      {currentPageContent.lc_question && currentPageContent.lc_question.trim() !== '' && (
                        <div className="bg-slate-50 rounded-2xl border border-slate-200 overflow-hidden">
                          <button
                            type="button"
                            onClick={() => setShowQuestion(!showQuestion)}
                            className="w-full px-5 py-3.5 text-left font-black text-sm text-[#0a5482] flex justify-between"
                          >
                            <span>❓ {t('View Question')}</span>
                            <span>{showQuestion ? '▲' : '▼'}</span>
                          </button>
                          {showQuestion && (
                            <div className="p-5 border-t border-slate-200 space-y-3">
                              <div
                                className="legacy-prose text-sm"
                                dangerouslySetInnerHTML={{
                                  __html: fixLegacyHtmlContent(currentPageContent.lc_question),
                                }}
                              />
                              {currentPageContent.lc_answer && currentPageContent.lc_answer.trim() !== '' && (
                                <div>
                                  <button
                                    type="button"
                                    onClick={() => setShowAnswer(!showAnswer)}
                                    className="bg-emerald-600 text-white font-bold text-xs px-4 py-2 rounded-xl"
                                  >
                                    ✅ {t('View Answer')}
                                  </button>
                                  {showAnswer && (
                                    <div
                                      className="mt-3 p-4 bg-emerald-50 border border-emerald-200 rounded-xl legacy-prose text-sm"
                                      dangerouslySetInnerHTML={{
                                        __html: fixLegacyHtmlContent(currentPageContent.lc_answer),
                                      }}
                                    />
                                  )}
                                </div>
                              )}
                            </div>
                          )}
                        </div>
                      )}

                      {currentPageContent.lc_conversation && currentPageContent.lc_conversation.trim() !== '' && (
                        <div className="bg-slate-50 rounded-2xl border border-slate-200 overflow-hidden">
                          <button
                            type="button"
                            onClick={() => setShowDialog(!showDialog)}
                            className="w-full px-5 py-3.5 text-left font-black text-sm text-[#0a5482] flex justify-between"
                          >
                            <span>💬 {t('View Conversation Dialog')}</span>
                            <span>{showDialog ? '▲' : '▼'}</span>
                          </button>
                          {showDialog && (
                            <div
                              className="p-5 border-t border-slate-200 legacy-prose text-sm"
                              dangerouslySetInnerHTML={{
                                __html: fixLegacyHtmlContent(currentPageContent.lc_conversation),
                              }}
                            />
                          )}
                        </div>
                      )}
                    </div>
                  )}

                  {currentLecture.lecture_attach && currentLecture.lecture_attach.trim() !== '' && (
                    <div className="pt-2">
                      <a
                        href={resolveUploadUrl(currentLecture.lecture_attach, '#')}
                        target="_blank"
                        rel="noreferrer"
                        className="inline-flex items-center gap-2 bg-sky-50 hover:bg-sky-100 text-[#0a5482] font-bold text-xs px-4 py-2.5 rounded-xl border border-sky-200"
                      >
                        📎 Tải tài liệu đính kèm (Download)
                      </a>
                    </div>
                  )}

                  {/* Multi-page lecture pagination */}
                  {lecturePages.length > 1 && (
                    <div className="pt-6 border-t border-slate-200 flex items-center justify-center gap-2">
                      <button
                        type="button"
                        disabled={curPageIdx <= 0}
                        onClick={() => setCurPageIdx((p) => Math.max(0, p - 1))}
                        className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-bold disabled:opacity-40"
                      >
                        {t('< PREV')}
                      </button>
                      {lecturePages.map((lp, idx) => (
                        <button
                          key={lp.lc_id || idx}
                          type="button"
                          onClick={() => setCurPageIdx(idx)}
                          className={`w-9 h-9 rounded-xl text-xs font-black ${
                            idx === curPageIdx ? 'bg-[#0a5482] text-white' : 'border border-slate-200 text-slate-600'
                          }`}
                        >
                          {idx + 1}
                        </button>
                      ))}
                      <button
                        type="button"
                        disabled={curPageIdx >= lecturePages.length - 1}
                        onClick={() => setCurPageIdx((p) => Math.min(lecturePages.length - 1, p + 1))}
                        className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-bold disabled:opacity-40"
                      >
                        {t('NEXT >')}
                      </button>
                    </div>
                  )}
                </>
              ) : (
                <div className="py-16 text-center text-slate-500 font-bold">{t('No lecture is posted!')}</div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

/* 3. PROFILE PAGE (/user/profile) */
export const ProfilePage: React.FC = () => {
  const { lang, t, user, setUser, selectedCourseId, setSelectedCourseId, userCoursesList, logoutUser } = useApp();
  const navigate = useNavigate();

  const [fullName, setFullName] = useState(user?.user_fullname || user?.user_name || '');
  const [birthday, setBirthday] = useState(user?.user_birthday || '');
  const [gender, setGender] = useState(String(user?.user_gender ?? 1));
  const [job, setJob] = useState(user?.user_job || '');
  const [aboutMe, setAboutMe] = useState(user?.user_about || '');
  const [saveMsg, setSaveMsg] = useState('');

  const [newPass, setNewPass] = useState('');
  const [confPass, setConfPass] = useState('');
  const [passMsg, setPassMsg] = useState('');

  if (!user) {
    return <LoginPage />;
  }

  const handleSaveProfile = async (e: React.FormEvent) => {
    e.preventDefault();
    const fields = {
      user_fullname: fullName,
      user_birthday: birthday,
      user_gender: parseInt(gender, 10),
      user_job: job,
      user_about: aboutMe,
    };
    const { error } = await supabase.from('te_user').update(fields).eq('user_id', user.user_id);
    if (!error) {
      setUser({ ...user, ...fields });
      setSaveMsg('Đã lưu thông tin hồ sơ!');
      setTimeout(() => setSaveMsg(''), 3000);
    }
  };

  const handlePassChange = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newPass || newPass !== confPass) {
      setPassMsg(t('New password does not match!'));
      return;
    }
    const newEncrypted = encryptLegacyPass(user.user_salt || '', newPass);
    await supabase.from('te_user').update({ user_pass: newEncrypted }).eq('user_id', user.user_id);
    setUser({ ...user, user_pass: newEncrypted });
    setNewPass('');
    setConfPass('');
    setPassMsg(t('You did change password complete!'));
  };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      <div className="bg-white rounded-3xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-8 py-6 text-white flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-black">{t('Profile')}</h1>
            <p className="text-xs text-sky-200 mt-0.5">{user.user_email || user.user_name}</p>
          </div>
          <button
            type="button"
            onClick={() => {
              logoutUser();
              navigate('/');
            }}
            className="bg-rose-500 hover:bg-rose-600 text-white text-xs font-black px-4 py-2 rounded-xl"
          >
            {t('Logout')}
          </button>
        </div>

        <div className="p-6 sm:p-8 grid grid-cols-1 md:grid-cols-2 gap-8">
          <form onSubmit={handleSaveProfile} className="space-y-4">
            <h3 className="font-black text-base text-[#0a5482] border-b border-slate-200 pb-2">{t('Basic info')}</h3>
            {saveMsg && <div className="p-3 bg-emerald-50 text-emerald-700 rounded-xl text-xs font-bold">{saveMsg}</div>}
            <div>
              <label className="block text-xs font-bold text-slate-500 mb-1">{t('Full Name')}</label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-500 mb-1">{t('Birthday')}</label>
              <input
                type="text"
                value={birthday}
                onChange={(e) => setBirthday(e.target.value)}
                className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-500 mb-1">{t('Gender')}</label>
              <select
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
              >
                <option value="1">{t('Male')}</option>
                <option value="0">{t('Female')}</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-500 mb-1">{t('Work')}</label>
              <input
                type="text"
                value={job}
                onChange={(e) => setJob(e.target.value)}
                className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-500 mb-1">Giới thiệu bản thân</label>
              <textarea
                rows={3}
                value={aboutMe}
                onChange={(e) => setAboutMe(e.target.value)}
                className="w-full border border-slate-300 rounded-xl p-3 text-sm"
              />
            </div>
            <button type="submit" className="bg-[#0a5482] text-white font-black text-xs px-6 py-2.5 rounded-xl">
              {t('Save')}
            </button>
          </form>

          <div className="space-y-6">
            <div>
              <h3 className="font-black text-base text-[#0a5482] border-b border-slate-200 pb-2 mb-3">
                {t('My Courses')}
              </h3>
              <select
                value={selectedCourseId || ''}
                onChange={(e) => setSelectedCourseId(parseInt(e.target.value, 10))}
                className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm"
              >
                {userCoursesList.map((cc: any) => (
                  <option key={cc.cc_id} value={cc.cc_id}>
                    {lang === 'vi' ? cc.cc_name_vi || cc.cc_name : cc.cc_name}
                  </option>
                ))}
              </select>
            </div>

            <form onSubmit={handlePassChange} className="space-y-4">
              <h3 className="font-black text-base text-[#0a5482] border-b border-slate-200 pb-2">
                {t('Do you want change your password?')}
              </h3>
              {passMsg && <div className="p-3 bg-sky-50 text-[#0a5482] rounded-xl text-xs font-bold">{passMsg}</div>}
              <div>
                <label className="block text-xs font-bold text-slate-500 mb-1">{t('New Pass')}</label>
                <input
                  type="password"
                  value={newPass}
                  onChange={(e) => setNewPass(e.target.value)}
                  className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
                />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-500 mb-1">{t('Confirm New Pass')}</label>
                <input
                  type="password"
                  value={confPass}
                  onChange={(e) => setConfPass(e.target.value)}
                  className="w-full border border-slate-300 rounded-xl px-3.5 py-2 text-sm"
                />
              </div>
              <button type="submit" className="bg-slate-800 text-white font-black text-xs px-6 py-2.5 rounded-xl">
                Đổi mật khẩu
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

/* 4. MESSAGE PAGE (/user/message) */
export const MessagePage: React.FC = () => {
  const { t, user } = useApp();
  const [messages, setMessages] = useState<any[]>([]);

  useEffect(() => {
    if (!user) return;
    supabase
      .from('te_message')
      .select('*')
      .eq('deleted', 0)
      .order('msg_id', { ascending: false })
      .limit(30)
      .then(({ data }) => {
        if (data) setMessages(data);
      });
  }, [user]);

  if (!user) return <LoginPage />;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
      <div className="bg-white rounded-3xl border border-slate-200 shadow-xs overflow-hidden">
        <div className="bg-gradient-to-r from-[#0a5482] to-[#0f172a] px-8 py-6 text-white">
          <h1 className="text-2xl font-black">✉️ {t('Message')}</h1>
        </div>
        <div className="p-6 sm:p-8 divide-y divide-slate-100">
          {messages.length > 0 ? (
            messages.map((m) => (
              <div key={m.msg_id} className="py-4 first:pt-0 last:pb-0">
                <h4 className="font-bold text-slate-800 text-sm">{m.msg_title || 'Thông báo từ TonyEnglish'}</h4>
                <div
                  className="text-xs text-slate-600 mt-1 legacy-prose"
                  dangerouslySetInnerHTML={{ __html: fixLegacyHtmlContent(m.msg_content) }}
                />
              </div>
            ))
          ) : (
            <p className="text-sm text-slate-500">Chưa có tin nhắn nào.</p>
          )}
        </div>
      </div>
    </div>
  );
};
