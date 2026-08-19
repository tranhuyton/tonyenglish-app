import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';
import { createClient } from '@supabase/supabase-js';

const authSupabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
  { auth: { persistSession: false } }
);

let studentSearchTimer: any;

export default function StudentManagement({ onStartTest, autoSelectUserId, autoTab, onAutoSelectDone }: { onStartTest?: any, autoSelectUserId?: string | null, autoTab?: 'courses' | 'history' | 'activity' | null, onAutoSelectDone?: () => void }) {
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
  const [activeDetailTab, setActiveDetailTab] = useState<'courses' | 'history' | 'activity'>('courses');
  const [studentActivities, setStudentActivities] = useState<any[]>([]);

  const [showAssignModal, setShowAssignModal] = useState(false);
  const [isAssigning, setIsAssigning] = useState(false);

  const [showCreateUserModal, setShowCreateUserModal] = useState(false);
  const [isCreatingUser, setIsCreatingUser] = useState(false);
  const [newUserRole, setNewUserRole] = useState('student');

  const [editingUser, setEditingUser] = useState<any>(null);
  const [isUpdatingUser, setIsUpdatingUser] = useState(false);

  // 🚀 KHO ĐỀ THI ĐỂ MỞ TÍNH NĂNG XEM LẠI BÀI
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
      console.error("Lỗi tải học viên:", err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchCourses = async () => {
    const { data } = await supabase.from('courses').select('id, title, type').order('created_at', { ascending: false });
    setCourses(data || []);
  };

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

      // 🚀 FETCH NHẬT KÝ HOẠT ĐỘNG
      const { data: actData } = await supabase.from('activity_logs').select('*').eq('user_id', student.id).order('created_at', { ascending: false });
      setStudentActivities(actData || []);
      
    } catch (err: any) {
      console.error("Lỗi tải chi tiết:", err.message);
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

      alert(`✅ Đã tạo tài khoản ${newUserRole === 'admin' ? 'Quản trị viên' : 'Học viên'} thành công!`);
      setShowCreateUserModal(false);
      setNewUserRole('student');
      fetchStudents(); 
    } catch (err: any) {
      alert("❌ Lỗi tạo tài khoản: " + err.message);
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
      
      alert("✅ Đã cập nhật thông tin thành công!");
      
      if (selectedStudent && selectedStudent.id === editingUser.id) {
         setSelectedStudent({ ...selectedStudent, full_name: fullName, role: role, phone: phone });
      }
      
      setEditingUser(null);
      fetchStudents();
    } catch (err: any) {
      alert("❌ Lỗi cập nhật: " + err.message);
    } finally {
      setIsUpdatingUser(false);
    }
  };

  const handleDeleteUser = async (id: string, name: string) => {
    if (!window.confirm(`Anh có chắc chắn muốn xóa VĨNH VIỄN tài khoản của ${name || 'học viên này'} không? Toàn bộ lịch sử làm bài sẽ bị mất!\n\n💡 Gợi ý: Nên dùng nút "Tạm dừng" thay vì xóa để giữ lại lịch sử.`)) return;

    try {
      const { error } = await supabase.rpc('delete_admin_user', { target_user_id: id });
      if (error) throw error;
      alert("🗑️ Đã xóa tài khoản thành công!");
      fetchStudents(); 
    } catch (err: any) {
      alert("❌ Lỗi xóa tài khoản: " + err.message);
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
        if (error.code === '23505') throw new Error("Học viên này đã được gán khóa học này rồi!");
        throw error;
      }
      
      setStudentEnrollments([data[0], ...studentEnrollments]);
      setShowAssignModal(false);
      alert("✅ Đã gán khóa học thành công!");
    } catch (err: any) {
      alert("❌ Lỗi: " + err.message);
    } finally {
      setIsAssigning(false);
    }
  };

  const handleRemoveCourse = async (enrollmentId: string) => {
    if (!window.confirm("Xóa quyền truy cập khóa học này của học viên?")) return;
    try {
      await supabase.from('enrollments').delete().eq('id', enrollmentId);
      setStudentEnrollments(studentEnrollments.filter(e => e.id !== enrollmentId));
    } catch (err: any) {
      alert("Lỗi khi xóa: " + err.message);
    }
  };

  // 🚀 HÀM MỞ BÀI THI CHI TIẾT TỪ ADMIN
  const handleReviewTest = async (h: any) => {
    const testId = h.details?.test_id || h.test_id;
    
    // Tìm test ID từ cache nhẹ (chỉ để lấy test_type nếu cần)
    let cachedTest = allTests.find(t => String(t.id) === String(testId));
    if (!cachedTest) cachedTest = allTests.find(t => t.title?.trim() === h.test_title?.trim());
    
    // Luôn fetch đầy đủ dữ liệu từ DB (bao gồm json_config, insert_pdf_url...)
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
        // 🔒 Lưu context để khi quay lại admin sẽ tự mở đúng profile học viên + tab lịch sử
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
        alert("Đề thi này không còn tồn tại trên hệ thống.");
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
    const action = isCurrentlyActive ? 'TẠM DỪNG' : 'KÍCH HOẠT LẠI';
    
    if (!window.confirm(`${action} tài khoản của ${student.full_name || student.email}?${isCurrentlyActive ? '\n\nHọc viên sẽ không thể đăng nhập cho đến khi được kích hoạt lại. Toàn bộ lịch sử được giữ nguyên.' : ''}`)) return;
    
    try {
      const { error } = await supabase.from('profiles').update({ status: newStatus }).eq('id', student.id);
      if (error) throw error;
      
      alert(`✅ Đã ${action.toLowerCase()} tài khoản thành công!`);
      
      // Update local state
      setStudents(prev => prev.map(s => s.id === student.id ? { ...s, status: newStatus } : s));
      if (selectedStudent?.id === student.id) {
        setSelectedStudent({ ...selectedStudent, status: newStatus });
      }
    } catch (err: any) {
      alert('❌ Lỗi: ' + err.message);
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
  // VIEW CHI TIẾT HỌC VIÊN
  // ==========================================
  if (selectedStudent) {
    const totalTests = studentHistory.length;
    const avgScore = totalTests > 0 ? (studentHistory.reduce((acc, curr) => acc + (curr.score || 0), 0) / totalTests).toFixed(1) : 0;
    const totalTime = studentHistory.reduce((acc, curr) => acc + Math.round((curr.time_spent || 0) / 60), 0);

    return (
      <>
        <div className="animate-in slide-in-from-right-4 duration-300">
          <button onClick={() => setSelectedStudent(null)} className="mb-6 flex items-center gap-2 text-slate-500 hover:text-[#0a5482] font-bold transition-colors bg-white px-4 py-2 rounded-lg border border-slate-200 shadow-sm w-fit">
            <span>←</span> Quay lại danh sách
          </button>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col items-center text-center relative overflow-hidden">
              <span className={`absolute top-0 w-full py-1 text-[10px] font-black uppercase tracking-widest text-white ${selectedStudent.role === 'admin' ? 'bg-red-500' : 'bg-emerald-500'}`}>
                {selectedStudent.role === 'admin' ? 'Quản trị viên' : 'Học viên'}
              </span>
              <div className="w-20 h-20 rounded-full bg-[#0a5482] text-white flex items-center justify-center font-black text-3xl mb-4 shadow-inner mt-4">
                {selectedStudent.full_name ? selectedStudent.full_name.trim().split(/\s+/).pop()?.charAt(0).toUpperCase() : (selectedStudent.email ? selectedStudent.email.charAt(0).toUpperCase() : 'U')}
              </div>
              
              <h2 className="text-xl font-black text-slate-800 mb-1 flex items-center justify-center gap-2">
                 {selectedStudent.full_name || <span className="text-orange-500 italic text-lg">[Chưa cập nhật Tên]</span>}
                 <button onClick={() => setEditingUser(selectedStudent)} className="text-sm bg-slate-100 hover:bg-[#0a5482] hover:text-white text-slate-400 p-1.5 rounded-md transition-colors" title="Sửa thông tin">✏️</button>
              </h2>
              
              <p className="text-slate-500 font-medium text-[14px] mb-1">{selectedStudent.email}</p>
              {selectedStudent.phone && <p className="text-slate-500 font-bold text-[13px] mb-4 bg-slate-50 px-3 py-1 rounded-full border border-slate-100">📞 {selectedStudent.phone}</p>}
              
              <div className="w-full border-t border-slate-100 pt-4 flex justify-between text-[13px] mt-auto">
                <span className="text-slate-500 font-medium">Ngày tham gia:</span>
                <span className="font-bold text-slate-700">{formatDate(selectedStudent.created_at).split(' ')[0]}</span>
              </div>
            </div>

            <div className="lg:col-span-2 grid grid-cols-3 gap-4">
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-emerald-500 text-lg">📝</span> Tổng bài làm</div>
                <div className="text-4xl font-black text-slate-800">{totalTests}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-blue-500 text-lg">📊</span> Điểm trung bình</div>
                <div className="text-4xl font-black text-slate-800">{avgScore}</div>
              </div>
              <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-center">
                <div className="text-slate-500 font-bold text-[13px] uppercase tracking-wider mb-2 flex items-center gap-2"><span className="text-amber-500 text-lg">⏱️</span> Tổng giờ học</div>
                <div className="text-4xl font-black text-slate-800">{Math.round(totalTime/60)} <span className="text-base text-slate-400 font-medium">giờ</span></div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col min-h-[400px]">
            <div className="bg-slate-50 px-2 pt-2 border-b border-slate-200 flex gap-2 overflow-x-auto custom-scrollbar">
              <button onClick={() => setActiveDetailTab('courses')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'courses' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📚 Khóa học</button>
              <button onClick={() => setActiveDetailTab('history')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'history' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📊 Lịch sử Điểm</button>
              <button onClick={() => setActiveDetailTab('activity')} className={`px-4 md:px-6 py-3 font-bold text-[13px] md:text-sm rounded-t-xl transition-colors whitespace-nowrap ${activeDetailTab === 'activity' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>👀 Nhật ký Truy cập</button>
            </div>
            
            <div className="p-6 flex-1 bg-white">
              {isLoadingDetails ? (
                <div className="py-20 text-center text-slate-400 font-bold">⏳ Đang tải dữ liệu...</div>
              ) : activeDetailTab === 'courses' ? (
                <div>
                  <div className="flex justify-between items-center mb-6">
                    <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest">Danh sách khóa học được phép truy cập</h3>
                    <button onClick={() => setShowAssignModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white px-5 py-2.5 rounded-lg font-bold text-xs shadow-sm transition">+ GÁN KHÓA HỌC</button>
                  </div>
                  
                  {studentEnrollments.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Học viên này chưa được gán khóa học nào.</div>
                  ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4">
                      {studentEnrollments.map(e => (
                        <div key={e.id} className="border border-slate-200 p-5 rounded-xl bg-slate-50 flex flex-col relative group">
                          <span className="bg-blue-100 text-blue-700 font-black uppercase text-[10px] px-2 py-1 rounded w-fit mb-3">{e.courses?.type || 'Khóa học'}</span>
                          <h4 className="font-bold text-slate-800 text-[15px] mb-2">{e.courses?.title || 'Khóa học đã xóa'}</h4>
                          <p className="text-[12px] text-slate-500 font-medium">Gán ngày: {formatDate(e.enrolled_at).split(' ')[0]}</p>
                          <button onClick={() => handleRemoveCourse(e.id)} className="absolute top-4 right-4 text-red-400 hover:text-red-600 font-bold text-xs opacity-0 group-hover:opacity-100 transition-opacity">Gỡ bỏ ✖</button>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

              ) : activeDetailTab === 'history' ? (
                <div>
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-6">Lịch sử nộp bài ({studentHistory.length} bài)</h3>
                  {studentHistory.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Học viên này chưa nộp bài thi nào.</div>
                  ) : (
                    <div className="border border-slate-200 rounded-xl overflow-hidden">
                      <table className="w-full text-left border-collapse">
                        <thead className="bg-[#f8fafc] text-[11px] font-black uppercase tracking-wider text-slate-500 border-b border-slate-200">
                          <tr>
                            <th className="px-5 py-3">Tên bài thi</th>
                            <th className="px-5 py-3 text-center">Dạng</th>
                            <th className="px-5 py-3 text-center">Điểm</th>
                            <th className="px-5 py-3 text-center">Ngày nộp</th>
                            <th className="px-5 py-3 text-right">Thao tác</th>
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
                                    👁️ Xem bài làm
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
                  <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-8">Nhật ký truy cập & hành vi</h3>
                  {studentActivities.length === 0 ? (
                    <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Chưa có hoạt động nào được ghi nhận.</div>
                  ) : (
                    <div className="space-y-6 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-slate-200 before:to-transparent">
                      {studentActivities.map((act) => (
                         <div key={act.id} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                            <div className="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white bg-[#0a5482] text-white font-bold shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 shadow-sm z-10 text-[14px]">
                               {act.action_type === 'login' ? '🔑' : act.action_type === 'finish_test' ? '📝' : act.action_type === 'call_tutor' ? '📞' : '📖'}
                            </div>
                            <div className="w-[calc(100%-4rem)] md:w-[calc(50%-3rem)] bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-[#2bd6eb] transition-colors">
                               <div className="flex justify-between items-start mb-2">
                                  <h4 className="font-black text-[#0a5482] text-[13px] md:text-[15px] uppercase tracking-tight">
                                     {act.action_type === 'login' && 'Đăng nhập hệ thống'}
                                     {act.action_type === 'finish_test' && 'Nộp bài kiểm tra'}
                                     {act.action_type === 'call_tutor' && 'Hỏi đáp AI / Voice'}
                                     {act.action_type === 'finish_lecture' && 'Hoàn thành bài giảng'}
                                  </h4>
                                  <span className="text-[11px] font-bold text-slate-400 whitespace-nowrap ml-2 bg-slate-50 px-2 py-1 rounded border border-slate-100">{formatDate(act.created_at)}</span>
                               </div>
                               <p className="text-[13px] text-slate-600 font-medium leading-relaxed">
                                  {act.action_type === 'login' && 'Học sinh đăng nhập thành công vào LMS.'}
                                  {act.action_type === 'finish_test' && `Đã nộp bài: "${act.details?.test_title || 'IELTS'}" với số điểm: ${act.details?.score || 0}`}
                                  {act.action_type === 'call_tutor' && `Thời lượng đàm thoại / hỏi AI: ${act.details?.duration || 0} giây.`}
                                  {act.action_type === 'finish_lecture' && `Học xong bài giảng: "${act.details?.lecture_title || 'Lecture'}"`}
                               </p>
                            </div>
                         </div>
                      ))}
                    </div>
                  )}
                </div>
              ) : null}

            </div>
          </div>
        </div>

        {/* MODAL EDIT TÀI KHOẢN KHI ĐANG XEM CHI TIẾT */}
        {editingUser && (
          <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
            <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sửa Thông Tin</h2>
              
              <div className="space-y-4 mb-8">
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                  <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Trần Huy Tôn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>
                
                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                  <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                  <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                  <p className="text-[10px] text-slate-400 mt-1 italic">* Không thể sửa email từ Admin Panel.</p>
                </div>

                <div>
                  <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                  <div className="grid grid-cols-2 gap-3 mt-2">
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                      👨‍🎓 Học viên
                    </label>
                    <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                      <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                      👑 Quản trị
                    </label>
                  </div>
                </div>
              </div>

              <div className="flex gap-4">
                <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                  {isUpdatingUser ? 'ĐANG LƯU...' : 'LƯU THAY ĐỔI'}
                </button>
              </div>
            </form>
          </div>
        )}

        {/* MODAL GÁN KHÓA HỌC */}
        {showAssignModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <form onSubmit={handleAssignCourse} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4">Gán Khóa Học</h2>
              <div className="space-y-4 mb-8">
                <label className="text-[13px] font-bold text-slate-500 uppercase">Chọn khóa học</label>
                <select name="courseId" required defaultValue="" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] font-medium bg-slate-50">
                  <option value="" disabled>-- Chọn khóa học --</option>
                  {availableCourses.length === 0 ? (
                     <option value="" disabled>Học viên đã gán tất cả khóa học</option>
                  ) : (
                     availableCourses.map(c => <option key={c.id} value={c.id}>[{c.type}] {c.title}</option>)
                  )}
                </select>
              </div>
              <div className="flex gap-4">
                <button type="button" onClick={() => setShowAssignModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button type="submit" disabled={isAssigning} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition disabled:opacity-50">GÁN NGAY</button>
              </div>
            </form>
          </div>
        )}
      </>
    );
  }

  // ==========================================
  // VIEW DANH SÁCH HỌC VIÊN TỔNG
  // ==========================================
  return (
    <>
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden animate-in fade-in duration-300 flex flex-col h-[calc(100vh-120px)]">
        <div className="bg-slate-50 px-6 py-5 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-4 shrink-0">
          <div className="flex items-center gap-4">
            <h2 className="font-black text-xl text-[#0a5482]">Quản lý Tài Khoản</h2>
            <div className="flex bg-white border border-slate-200 rounded-lg overflow-hidden shadow-sm">
              <button onClick={() => { setStatusFilter('active'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors ${statusFilter === 'active' ? 'bg-emerald-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Đang học ({students.filter(s => s.status !== 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('inactive'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'inactive' ? 'bg-slate-500 text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Tạm dừng ({students.filter(s => s.status === 'inactive').length})
              </button>
              <button onClick={() => { setStatusFilter('all'); setCurrentPage(1); }} className={`px-3 py-1.5 text-[11px] font-bold uppercase tracking-wider transition-colors border-l border-slate-200 ${statusFilter === 'all' ? 'bg-[#0a5482] text-white' : 'text-slate-500 hover:bg-slate-50'}`}>
                Tất cả
              </button>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <div className="relative w-full sm:w-72">
              <input 
                type="text" 
                placeholder="Tìm kiếm theo email, tên, SĐT..." 
                defaultValue={searchQuery}
                onChange={(e) => {
                  clearTimeout(studentSearchTimer);
                  studentSearchTimer = setTimeout(() => setSearchQuery(e.target.value), 350);
                }} 
                className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 font-medium text-[13px] outline-none focus:border-[#0a5482] focus:ring-1 focus:ring-[#0a5482] bg-white transition-all shadow-sm" 
              />
              <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">🔍</span>
            </div>
            <button onClick={() => setShowCreateUserModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-6 py-2.5 rounded-xl transition shadow-md text-sm whitespace-nowrap">+ Tạo Tài Khoản</button>
          </div>
        </div>

        <div className="flex-1 flex flex-col overflow-hidden">
          {isLoading ? (
            <div className="p-16 text-center text-slate-500 font-bold text-lg flex items-center justify-center gap-3"><span className="animate-spin text-2xl">⏳</span> Đang tải dữ liệu...</div>
          ) : filteredStudents.length === 0 ? (
            <div className="p-16 text-center text-slate-400 font-medium text-lg border-t border-slate-100">Không tìm thấy tài khoản nào.</div>
          ) : (
            <>
              <div className="flex-1 overflow-y-auto custom-scrollbar">
                <table className="w-full text-left border-collapse min-w-[900px]">
                  <thead className="sticky top-0 bg-white shadow-[0_1px_2px_rgba(0,0,0,0.05)] z-10">
                    <tr className="text-[11px] font-black uppercase tracking-wider text-slate-400">
                      <th className="px-6 py-4 text-center w-16">STT</th>
                      <th className="px-6 py-4">Tài Khoản (Email)</th>
                      <th className="px-6 py-4">Số Điện Thoại</th>
                      <th className="px-6 py-4">Họ và Tên</th>
                      <th className="px-6 py-4">Trạng thái</th>
                      <th className="px-6 py-4 text-center">Ngày tạo</th>
                      <th className="px-6 py-4 text-right">Hành động</th>
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
                             {student.full_name || '[Chưa cập nhật]'}
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex flex-col gap-1">
                            <span className={`px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-wider border w-fit ${student.role === 'admin' ? 'bg-red-50 text-red-600 border-red-200' : 'bg-emerald-50 text-emerald-600 border-emerald-200'}`}>{student.role || 'Student'}</span>
                            {student.status === 'inactive' && <span className="px-2 py-0.5 rounded text-[9px] font-bold uppercase bg-slate-100 text-slate-500 border border-slate-200 w-fit">⏸ Tạm dừng</span>}
                          </div>
                        </td>
                        <td className="px-6 py-4 text-slate-600 font-medium text-[13px] text-center">
                          {formatDate(student.created_at).split(' ')[0]}
                        </td>
                        <td className="px-6 py-4 text-right flex items-center justify-end gap-1.5">
                          <button onClick={() => handleSelectStudent(student)} className="text-[#0a5482] font-bold text-[12px] bg-white hover:bg-[#0a5482] hover:text-white px-4 py-2 rounded-lg transition-all border border-slate-200 shadow-sm uppercase tracking-wider">
                            Cấu hình & Tiến độ
                          </button>
                          
                          <button onClick={() => setEditingUser(student)} className="text-blue-500 hover:text-blue-600 hover:bg-blue-50 p-2 rounded-lg transition-colors border border-transparent hover:border-blue-200" title="Sửa thông tin">
                            ✏️
                          </button>

                          <button onClick={() => handleToggleStatus(student)} className={`p-2 rounded-lg transition-colors border border-transparent ${student.status === 'inactive' ? 'text-emerald-500 hover:text-emerald-600 hover:bg-emerald-50 hover:border-emerald-200' : 'text-amber-500 hover:text-amber-600 hover:bg-amber-50 hover:border-amber-200'}`} title={student.status === 'inactive' ? 'Kích hoạt lại' : 'Tạm dừng'}>
                            {student.status === 'inactive' ? '▶️' : '⏸️'}
                          </button>
    
                          <button onClick={() => handleDeleteUser(student.id, student.full_name)} className="text-slate-400 hover:text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors border border-transparent hover:border-red-200" title="Xóa vĩnh viễn">
                            🗑️
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
                      ← Trang trước
                   </button>
                   <span className="text-[13px] font-black text-slate-500">
                      Trang {currentPage} <span className="font-medium text-slate-400">/ {totalPages}</span>
                   </span>
                   <button disabled={currentPage === totalPages} onClick={() => setCurrentPage(p => p + 1)} className="px-4 py-2 bg-white border border-slate-200 text-slate-600 hover:text-[#0a5482] hover:border-[#0a5482] rounded-lg disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-600 font-bold text-[13px] transition-colors shadow-sm">
                      Trang sau →
                   </button>
                </div>
              )}
            </>
          )}
        </div>
      </div>

      {/* MODAL TẠO TÀI KHOẢN MỚI */}
      {showCreateUserModal && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleCreateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Tạo Tài Khoản Mới</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                <input name="fullName" required type="text" defaultValue="" autoComplete="off" placeholder="Nguyễn Văn A" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                <input name="phone" type="text" defaultValue="" autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                <input name="email" required type="email" defaultValue="" autoComplete="off" placeholder="email@tonyenglish.vn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Mật khẩu</label>
                <input name="password" required type="password" minLength={6} defaultValue="123456" autoComplete="off" placeholder="Ít nhất 6 ký tự" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold text-[#0a5482]" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'student' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" checked={newUserRole === 'student'} onChange={() => setNewUserRole('student')} className="hidden" />
                    👨‍🎓 Học viên
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUserRole === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" checked={newUserRole === 'admin'} onChange={() => setNewUserRole('admin')} className="hidden" />
                    👑 Quản trị viên
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setShowCreateUserModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
              <button type="submit" disabled={isCreatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isCreatingUser ? 'ĐANG TẠO...' : 'TẠO TÀI KHOẢN'}
              </button>
            </div>
          </form>
        </div>
      )}
      
      {/* MODAL EDIT TÀI KHOẢN NGOÀI DANH SÁCH TỔNG */}
      {editingUser && !selectedStudent && (
        <div className="fixed inset-0 bg-slate-900/60 z-[100] flex items-center justify-center p-4">
          <form onSubmit={handleUpdateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Sửa Thông Tin</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                <input name="fullName" required type="text" defaultValue={editingUser.full_name || ''} autoComplete="off" placeholder="VD: Trần Huy Tôn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Số điện thoại</label>
                <input name="phone" type="text" defaultValue={editingUser.phone || ''} autoComplete="off" placeholder="VD: 0987654321" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm font-bold" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                <input type="email" defaultValue={editingUser.email} disabled className="w-full border border-slate-200 bg-slate-50 rounded-xl px-4 py-3 outline-none text-slate-400 text-sm cursor-not-allowed" />
                <p className="text-[10px] text-slate-400 mt-1 italic">* Không thể sửa email từ Admin Panel.</p>
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'student' || !editingUser.role ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" defaultChecked={editingUser.role === 'student' || !editingUser.role} onChange={(e) => setEditingUser({...editingUser, role: 'student'})} className="hidden" />
                    👨‍🎓 Học viên
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${editingUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" defaultChecked={editingUser.role === 'admin'} onChange={(e) => setEditingUser({...editingUser, role: 'admin'})} className="hidden" />
                    👑 Quản trị
                  </label>
                </div>
              </div>
            </div>

            <div className="flex gap-4">
              <button type="button" onClick={() => setEditingUser(null)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
              <button type="submit" disabled={isUpdatingUser} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition hover:bg-[#084266] disabled:opacity-50">
                {isUpdatingUser ? 'ĐANG LƯU...' : 'LƯU THAY ĐỔI'}
              </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
}