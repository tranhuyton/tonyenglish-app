import React, { useState, useEffect } from 'react';
import { supabase } from './supabase';
import { createClient } from '@supabase/supabase-js';

// TẠO BẢN SAO CLIENT ĐỂ ĐĂNG KÝ HỘ (KHÔNG LƯU PHIÊN ĐỂ TRÁNH VĂNG ACC ADMIN)
const authSupabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
  { auth: { persistSession: false } }
);

export default function StudentManagement() {
  const [students, setStudents] = useState<any[]>([]);
  const [courses, setCourses] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  
  // States cho màn hình Chi tiết
  const [selectedStudent, setSelectedStudent] = useState<any>(null);
  const [studentHistory, setStudentHistory] = useState<any[]>([]);
  const [studentEnrollments, setStudentEnrollments] = useState<any[]>([]);
  const [isLoadingDetails, setIsLoadingDetails] = useState(false);
  const [activeDetailTab, setActiveDetailTab] = useState<'courses' | 'history'>('courses');

  // States Modal Tạo/Gán
  const [showAssignModal, setShowAssignModal] = useState(false);
  const [selectedCourseToAssign, setSelectedCourseToAssign] = useState('');
  const [isAssigning, setIsAssigning] = useState(false);

  // States cho Modal Tạo Tài Khoản Mới
  const [showCreateUserModal, setShowCreateUserModal] = useState(false);
  const [isCreatingUser, setIsCreatingUser] = useState(false);
  const [newUser, setNewUser] = useState({ fullName: '', email: '', password: '', role: 'student' });

  useEffect(() => {
    fetchStudents();
    fetchCourses();
  }, []);

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
    setIsLoadingDetails(true);
    setActiveDetailTab('courses');
    
    try {
      const { data: enrollData } = await supabase.from('enrollments').select('*, courses(title, type)').eq('user_id', student.id).order('enrolled_at', { ascending: false });
      setStudentEnrollments(enrollData || []);

      const { data: historyData } = await supabase.from('test_results').select('*').eq('user_id', student.id).order('created_at', { ascending: false });
      setStudentHistory(historyData || []);
    } catch (err: any) {
      console.error("Lỗi tải chi tiết:", err.message);
    } finally {
      setIsLoadingDetails(false);
    }
  };

  // ==========================================
  // LOGIC TẠO / XÓA TÀI KHOẢN AN TOÀN TRÊN TRÌNH DUYỆT
  // ==========================================
  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsCreatingUser(true);
    try {
      // 1. Dùng client phụ để "Đăng ký" tài khoản mới
      const { data, error } = await authSupabase.auth.signUp({
        email: newUser.email,
        password: newUser.password,
        options: {
          data: {
            full_name: newUser.fullName,
            role: newUser.role
          }
        }
      });

      if (error) throw error;

      // 2. Chờ 1.5 giây để Trigger bên Supabase tự động tạo dòng trong bảng profiles
      await new Promise(resolve => setTimeout(resolve, 1500));

      // 3. Dùng quyền Admin hiện tại update lại thông tin Profile cho chắc chắn
      if (data.user) {
        await supabase.from('profiles').update({
          full_name: newUser.fullName,
          role: newUser.role
        }).eq('id', data.user.id);
      }

      alert(`✅ Đã tạo tài khoản ${newUser.role === 'admin' ? 'Quản trị viên' : 'Học viên'} thành công!`);
      setShowCreateUserModal(false);
      setNewUser({ fullName: '', email: '', password: '', role: 'student' });
      fetchStudents(); 
    } catch (err: any) {
      alert("❌ Lỗi tạo tài khoản: " + err.message);
    } finally {
      setIsCreatingUser(false);
    }
  };

  const handleDeleteUser = async (id: string, name: string) => {
    if (!window.confirm(`Anh có chắc chắn muốn xóa VĨNH VIỄN tài khoản của ${name || 'học viên này'} không? Toàn bộ lịch sử làm bài sẽ bị mất!`)) {
      return;
    }

    try {
      // Gọi hàm siêu quyền lực RPC mình vừa tạo dưới Database để xóa ngầm
      const { error } = await supabase.rpc('delete_admin_user', {
        target_user_id: id
      });

      if (error) throw error;

      alert("🗑️ Đã xóa tài khoản thành công!");
      fetchStudents(); // Cập nhật lại danh sách ngay lập tức
    } catch (err: any) {
      alert("❌ Lỗi xóa tài khoản: " + err.message);
    }
  };

  // --- LOGIC GÁN KHÓA HỌC ---
  const handleAssignCourse = async () => {
    if (!selectedCourseToAssign || !selectedStudent) return;
    setIsAssigning(true);
    try {
      const { data, error } = await supabase.from('enrollments').insert([{
        user_id: selectedStudent.id,
        course_id: selectedCourseToAssign,
        status: 'active'
      }]).select('*, courses(title, type)');

      if (error) {
        if (error.code === '23505') throw new Error("Học viên này đã được gán khóa học này rồi!");
        throw error;
      }
      
      setStudentEnrollments([data[0], ...studentEnrollments]);
      setShowAssignModal(false);
      setSelectedCourseToAssign('');
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

  const formatDate = (isoString: string) => {
    if (!isoString) return '';
    const d = new Date(isoString);
    return `${d.getDate().toString().padStart(2, '0')}/${(d.getMonth() + 1).toString().padStart(2, '0')}/${d.getFullYear()} ${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
  };

  const filteredStudents = students.filter(s => 
    (s.email && s.email.toLowerCase().includes(searchQuery.toLowerCase())) ||
    (s.full_name && s.full_name.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  // ==========================================
  // VIEW 2: CHI TIẾT 1 HỌC VIÊN
  // ==========================================
  if (selectedStudent) {
    const totalTests = studentHistory.length;
    const avgScore = totalTests > 0 ? (studentHistory.reduce((acc, curr) => acc + (curr.score || 0), 0) / totalTests).toFixed(1) : 0;
    const totalTime = studentHistory.reduce((acc, curr) => acc + Math.round((curr.time_spent || 0) / 60), 0);

    return (
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
              {selectedStudent.full_name ? selectedStudent.full_name.charAt(0).toUpperCase() : (selectedStudent.email ? selectedStudent.email.charAt(0).toUpperCase() : 'U')}
            </div>
            <h2 className="text-xl font-black text-slate-800 mb-1">{selectedStudent.full_name || 'Học viên ẩn danh'}</h2>
            <p className="text-slate-500 font-medium text-[14px] mb-4">{selectedStudent.email}</p>
            <div className="w-full border-t border-slate-100 pt-4 flex justify-between text-[13px]">
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
          <div className="bg-slate-50 px-2 pt-2 border-b border-slate-200 flex gap-2">
            <button onClick={() => setActiveDetailTab('courses')} className={`px-6 py-3 font-bold text-sm rounded-t-xl transition-colors ${activeDetailTab === 'courses' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📚 Khóa học ghi danh</button>
            <button onClick={() => setActiveDetailTab('history')} className={`px-6 py-3 font-bold text-sm rounded-t-xl transition-colors ${activeDetailTab === 'history' ? 'bg-white text-[#0a5482] border-t border-x border-slate-200' : 'text-slate-500 hover:bg-slate-100'}`}>📊 Lịch sử & Tiến độ</button>
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
            ) : (
              <div>
                <h3 className="font-black text-slate-700 text-[15px] uppercase tracking-widest mb-6">Lịch sử nộp bài ({studentHistory.length} bài)</h3>
                {studentHistory.length === 0 ? (
                  <div className="py-16 text-center border-2 border-dashed border-slate-200 rounded-xl text-slate-400 font-medium">Học viên này chưa nộp bài thi nào.</div>
                ) : (
                  <div className="border border-slate-200 rounded-xl overflow-hidden">
                    <table className="w-full text-left border-collapse">
                      <thead className="bg-[#f8fafc] text-[11px] font-black uppercase tracking-wider text-slate-500 border-b border-slate-200">
                        <tr>
                          <th className="px-5 py-3">Tên bài thi</th><th className="px-5 py-3 text-center">Dạng</th>
                          <th className="px-5 py-3 text-center">Điểm</th><th className="px-5 py-3 text-center">Thời gian</th><th className="px-5 py-3 text-right">Ngày nộp</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100">
                        {studentHistory.map(h => (
                          <tr key={h.id} className="hover:bg-slate-50 transition-colors">
                            <td className="px-5 py-3 font-bold text-[13px] text-slate-800">{h.test_title}</td>
                            <td className="px-5 py-3 text-center"><span className="bg-slate-100 text-slate-600 px-2 py-1 rounded text-[10px] font-bold border border-slate-200">{h.test_type}</span></td>
                            <td className="px-5 py-3 text-center font-black text-[14px] text-emerald-600">{h.score} / {h.total_score}</td>
                            <td className="px-5 py-3 text-center text-slate-600 text-[12px]">{Math.round((h.time_spent||0)/60)}p</td>
                            <td className="px-5 py-3 text-right text-slate-500 text-[12px]">{formatDate(h.created_at)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Modal Gán Khóa Học */}
        {showAssignModal && (
          <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
              <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4">Gán Khóa Học</h2>
              <div className="space-y-4 mb-8">
                <label className="text-[13px] font-bold text-slate-500 uppercase">Chọn khóa học</label>
                <select value={selectedCourseToAssign} onChange={e => setSelectedCourseToAssign(e.target.value)} className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] font-medium bg-slate-50">
                  <option value="">-- Chọn khóa học --</option>
                  {courses.map(c => <option key={c.id} value={c.id}>[{c.type}] {c.title}</option>)}
                </select>
              </div>
              <div className="flex gap-4">
                <button onClick={() => setShowAssignModal(false)} className="flex-1 font-bold py-3 text-slate-400 hover:bg-slate-50 rounded-xl transition">Hủy</button>
                <button onClick={handleAssignCourse} disabled={isAssigning || !selectedCourseToAssign} className="flex-1 bg-[#0a5482] text-white font-black py-3 rounded-xl shadow-lg transition disabled:opacity-50">GÁN NGAY</button>
              </div>
            </div>
          </div>
        )}
      </div>
    );
  }

  // ==========================================
  // VIEW 1: DANH SÁCH HỌC VIÊN TỔNG
  // ==========================================
  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden animate-in fade-in duration-300">
      <div className="bg-slate-50 px-6 py-5 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-center gap-4">
        <h2 className="font-black text-xl text-[#0a5482]">Quản lý Tài Khoản</h2>
        <div className="relative w-full sm:w-80">
          <input type="text" placeholder="Tìm kiếm theo email hoặc tên..." value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-300 font-medium text-[13px] outline-none focus:border-[#0a5482] focus:ring-1 focus:ring-[#0a5482] bg-white transition-all shadow-sm" />
          <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400">🔍</span>
        </div>
        <button onClick={() => setShowCreateUserModal(true)} className="bg-[#0a5482] hover:bg-[#084266] text-white font-bold px-6 py-2.5 rounded-xl transition shadow-md text-sm whitespace-nowrap">+ Tạo Tài Khoản</button>
      </div>

      <div className="p-0">
        {isLoading ? (
          <div className="p-16 text-center text-slate-500 font-bold text-lg flex items-center justify-center gap-3"><span className="animate-spin text-2xl">⏳</span> Đang tải dữ liệu...</div>
        ) : filteredStudents.length === 0 ? (
          <div className="p-16 text-center text-slate-400 font-medium text-lg border-t border-slate-100">Không tìm thấy tài khoản nào.</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-white border-b border-slate-200 text-[11px] font-black uppercase tracking-wider text-slate-400">
                  <th className="px-6 py-4">Tài Khoản</th>
                  <th className="px-6 py-4">Phân quyền</th>
                  <th className="px-6 py-4 text-center">Ngày tạo</th>
                  <th className="px-6 py-4 text-right">Hành động</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filteredStudents.map((student) => (
                  <tr key={student.id} className="hover:bg-blue-50/50 transition-colors group">
                    <td className="px-6 py-4">
                      <div className="flex items-center gap-3">
                        <div className={`w-10 h-10 rounded-full text-white flex items-center justify-center font-bold text-sm shrink-0 ${student.role === 'admin' ? 'bg-red-500' : 'bg-[#0a5482]'}`}>
                          {student.full_name ? student.full_name.charAt(0).toUpperCase() : (student.email ? student.email.charAt(0).toUpperCase() : 'U')}
                        </div>
                        <div>
                          <div className="font-bold text-[14px] text-slate-800">{student.full_name || 'Người dùng ẩn danh'}</div>
                          <div className="text-[13px] font-medium text-slate-500">{student.email}</div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4">
                      <span className={`px-2.5 py-1 rounded-md text-[10px] font-black uppercase tracking-wider border ${student.role === 'admin' ? 'bg-red-50 text-red-600 border-red-200' : 'bg-emerald-50 text-emerald-600 border-emerald-200'}`}>{student.role || 'Student'}</span>
                    </td>
                    <td className="px-6 py-4 text-slate-600 font-medium text-[13px] text-center">
                      {formatDate(student.created_at).split(' ')[0]}
                    </td>
                    <td className="px-6 py-4 text-right flex items-center justify-end gap-2">
                      <button onClick={() => handleSelectStudent(student)} className="text-[#0a5482] font-bold text-[12px] bg-white hover:bg-[#0a5482] hover:text-white px-4 py-2 rounded-lg transition-all border border-slate-200 shadow-sm uppercase tracking-wider">
                        Cấu hình & Tiến độ
                      </button>
                      <button onClick={() => handleDeleteUser(student.id, student.full_name)} className="text-slate-400 hover:text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors border border-transparent hover:border-red-200" title="Xóa tài khoản">
                        🗑️
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Modal Tạo Tài Khoản Mới */}
      {showCreateUserModal && (
        <div className="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 backdrop-blur-sm">
          <form onSubmit={handleCreateUser} className="bg-white rounded-3xl w-full max-w-md p-8 shadow-2xl animate-in zoom-in-95">
            <h2 className="text-xl font-black text-slate-800 mb-6 uppercase tracking-tight border-b pb-4 text-center">Tạo Tài Khoản Mới</h2>
            
            <div className="space-y-4 mb-8">
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Họ và tên</label>
                <input required type="text" value={newUser.fullName} onChange={e => setNewUser({...newUser, fullName: e.target.value})} placeholder="Nguyễn Văn A" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>
              
              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Email đăng nhập</label>
                <input required type="email" value={newUser.email} onChange={e => setNewUser({...newUser, email: e.target.value})} placeholder="email@tonyenglish.vn" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Mật khẩu</label>
                <input required type="password" minLength={6} value={newUser.password} onChange={e => setNewUser({...newUser, password: e.target.value})} placeholder="Ít nhất 6 ký tự" className="w-full border border-slate-300 rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-[#0a5482] text-sm" />
              </div>

              <div>
                <label className="text-[12px] font-bold text-slate-500 uppercase tracking-wider block mb-1">Phân quyền</label>
                <div className="grid grid-cols-2 gap-3 mt-2">
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUser.role === 'student' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="student" checked={newUser.role === 'student'} onChange={() => setNewUser({...newUser, role: 'student'})} className="hidden" />
                    👨‍🎓 Học viên
                  </label>
                  <label className={`border-2 rounded-xl p-3 flex items-center justify-center cursor-pointer transition-all font-bold text-sm ${newUser.role === 'admin' ? 'border-red-500 bg-red-50 text-red-700' : 'border-slate-200 text-slate-500 hover:bg-slate-50'}`}>
                    <input type="radio" name="role" value="admin" checked={newUser.role === 'admin'} onChange={() => setNewUser({...newUser, role: 'admin'})} className="hidden" />
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
    </div>
  );
}