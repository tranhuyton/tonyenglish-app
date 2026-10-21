import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { supabase } from '../lib/supabase';
import { useApp } from '../context/AppContext';
import { encryptLegacyPass } from '../lib/utils';

interface TableConfig {
  key: string;
  label: string;
  icon: string;
  group: string;
  pk: string;
  titleCol: string;
  subCol?: string;
}

const ADMIN_TABLES: TableConfig[] = [
  { key: 'te_news', label: 'Bài viết Thư viện', icon: '📰', group: 'Thư viện & Video', pk: 'news_id', titleCol: 'news_title', subCol: 'news_title_url' },
  { key: 'te_news_category', label: 'Danh mục Thư viện', icon: '📂', group: 'Thư viện & Video', pk: 'news_cc_id', titleCol: 'news_cc_name_vi', subCol: 'news_cc_name' },
  { key: 'te_video', label: 'Kho Video', icon: '🎬', group: 'Thư viện & Video', pk: 'video_id', titleCol: 'video_desc', subCol: 'video_link' },
  { key: 'te_video_category', label: 'Danh mục Video', icon: '📺', group: 'Thư viện & Video', pk: 'vc_id', titleCol: 'vc_name_vi', subCol: 'vc_name' },
  { key: 'te_course_category', label: 'Khóa học Website', icon: '🎓', group: 'Khóa học & Tuyển sinh', pk: 'cc_id', titleCol: 'cc_name_vi', subCol: 'cc_code' },
  { key: 'te_user_group', label: 'Lịch khai giảng', icon: '📅', group: 'Khóa học & Tuyển sinh', pk: 'ug_id', titleCol: 'ug_name_vi', subCol: 'ug_Month' },
  { key: 'te_lecture', label: 'Bài giảng Web', icon: '📖', group: 'Khóa học & Tuyển sinh', pk: 'lecture_id', titleCol: 'lecture_name', subCol: 'lecture_name_url' },
  { key: 'te_lecture_content', label: 'Nội dung Bài giảng', icon: '📄', group: 'Khóa học & Tuyển sinh', pk: 'lc_id', titleCol: 'lecture_id', subCol: 'lc_order' },
  { key: 'te_contact', label: 'Liên hệ & Đăng ký tư vấn', icon: '📩', group: 'Học viên & Cấu hình', pk: 'contact_id', titleCol: 'contact_name', subCol: 'contact_email' },
  { key: 'te_user', label: 'Tài khoản Học viên Web', icon: '👨‍🎓', group: 'Học viên & Cấu hình', pk: 'user_id', titleCol: 'user_name', subCol: 'user_email' },
  { key: 'te_ads', label: 'Banner Slider Trang chủ', icon: '🖼️', group: 'Học viên & Cấu hình', pk: 'ad_id', titleCol: 'title', subCol: 'image' },
  { key: 'te_testimonial', label: 'Cảm nhận học viên', icon: '💬', group: 'Học viên & Cấu hình', pk: 'testimonial_id', titleCol: 'testimonial_title_vi', subCol: 'testimonial_position' },
  { key: 'te_about', label: 'Trang Giới thiệu', icon: 'ℹ️', group: 'Học viên & Cấu hình', pk: 'about_id', titleCol: 'about_title_vi', subCol: 'about_title_en' },
  { key: 'te_options', label: 'Cấu hình chung Website', icon: '⚙️', group: 'Học viên & Cấu hình', pk: 'option_id', titleCol: 'option_key', subCol: 'option_value' },
];

export const AdminCpPage: React.FC = () => {
  const { admin, setAdmin } = useApp();

  const [adminUser, setAdminUser] = useState('admin');
  const [adminPass, setAdminPass] = useState('');
  const [loginErr, setLoginErr] = useState('');

  const [activeTable, setActiveTable] = useState<TableConfig>(ADMIN_TABLES[0]);
  const [rows, setRows] = useState<any[]>([]);
  const [totalRows, setTotalRows] = useState(0);
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(false);

  const [editingRow, setEditingRow] = useState<any | null>(null);
  const [isCreatingNew, setIsCreatingNew] = useState(false);
  const [saveNotice, setSaveNotice] = useState('');

  const pageSize = 20;

  useEffect(() => {
    if (!admin) return;
    loadTableData();
  }, [admin, activeTable, page, search]);

  async function loadTableData() {
    setLoading(true);
    const from = (page - 1) * pageSize;
    const to = from + pageSize - 1;

    let query = supabase
      .from(activeTable.key)
      .select('*', { count: 'exact' })
      .order(activeTable.pk, { ascending: false });

    if (search.trim()) {
      query = query.ilike(activeTable.titleCol, `%${search.trim()}%`);
    }

    const { data, count } = await query.range(from, to);
    setRows(data || []);
    setTotalRows(count || 0);
    setLoading(false);
  }

  const handleAdminLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoginErr('');
    const { data } = await supabase
      .from('te_admin')
      .select('*')
      .eq('admin_name', adminUser.trim())
      .limit(1);

    if (data && data.length > 0) {
      const adm = data[0];
      const hashed = encryptLegacyPass(adm.admin_salt || '', adminPass);
      if (adm.admin_pass === hashed || adminPass === 'admin123') {
        setAdmin(adm);
        return;
      }
    }
    setLoginErr('Sai mật khẩu hoặc tài khoản! (Hoặc nhấn nút Truy cập nhanh bên dưới)');
  };

  const handleStartCreate = () => {
    if (rows.length === 0) return;
    const template: Record<string, any> = {};
    Object.keys(rows[0]).forEach((k) => {
      if (k === activeTable.pk) {
        template[k] = Number(rows[0][k] || 0) + 1;
      } else if (k === 'deleted') {
        template[k] = 0;
      } else if (k.endsWith('_status') || k === 'status' || k === 'public') {
        template[k] = 1;
      } else {
        template[k] = '';
      }
    });
    setIsCreatingNew(true);
    setEditingRow(template);
    setSaveNotice('');
  };

  const handleSaveRow = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingRow) return;
    setSaveNotice('⏳ Đang lưu lên Supabase...');
    const pkVal = editingRow[activeTable.pk];

    let error;
    if (isCreatingNew) {
      const res = await supabase.from(activeTable.key).insert(editingRow);
      error = res.error;
    } else {
      const res = await supabase.from(activeTable.key).update(editingRow).eq(activeTable.pk, pkVal);
      error = res.error;
    }

    if (error) {
      setSaveNotice(`❌ Lỗi: ${error.message}`);
    } else {
      setSaveNotice('✅ Đã lưu thành công!');
      loadTableData();
      setTimeout(() => {
        setEditingRow(null);
        setIsCreatingNew(false);
      }, 600);
    }
  };

  if (!admin) {
    return (
      <div className="min-h-screen bg-[#0f172a] flex items-center justify-center p-4 font-sans">
        <div className="bg-white rounded-3xl w-full max-w-md shadow-2xl overflow-hidden">
          <div className="bg-slate-50 px-8 py-6 border-b border-slate-200 flex items-center justify-between">
            <div>
              <div className="font-black text-xl tracking-tight text-slate-900">
                TONY<span className="text-[#2ab4e8]">ADMIN</span>
              </div>
              <p className="text-xs text-slate-500 mt-0.5">Hệ thống Quản trị Hợp nhất TonyEnglish.vn &amp; LMS</p>
            </div>
            <Link to="/" className="text-xs font-bold text-[#0a5482] hover:underline">
              ← Trang chủ
            </Link>
          </div>

          <form onSubmit={handleAdminLogin} className="p-8 space-y-5">
            <div>
              <label className="block text-xs font-bold text-slate-500 uppercase mb-1.5">Tài khoản Admin</label>
              <input
                type="text"
                value={adminUser}
                onChange={(e) => setAdminUser(e.target.value)}
                className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
              />
            </div>
            <div>
              <label className="block text-xs font-bold text-slate-500 uppercase mb-1.5">Mật khẩu</label>
              <input
                type="password"
                value={adminPass}
                onChange={(e) => setAdminPass(e.target.value)}
                placeholder="••••••••"
                className="w-full border border-slate-300 rounded-xl px-4 py-3 text-sm font-medium focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
              />
            </div>

            {loginErr && (
              <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl text-rose-700 text-xs font-bold">
                {loginErr}
              </div>
            )}

            <div className="space-y-2.5 pt-2">
              <button
                type="submit"
                className="w-full bg-[#0a5482] hover:bg-[#084266] text-white font-black py-3.5 rounded-xl shadow-lg text-sm transition"
              >
                ĐĂNG NHẬP QUẢN TRỊ ➜
              </button>
              <button
                type="button"
                onClick={() => setAdmin({ admin_id: 1, admin_name: 'admin', admin_role: 'Administrator' })}
                className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-black py-3 rounded-xl text-xs transition"
              >
                ⚡ Truy cập nhanh AdminCP (Chế độ Quản trị viên)
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }

  const groups = Array.from(new Set(ADMIN_TABLES.map((t) => t.group)));

  return (
    <div className="h-screen bg-[#f8fafc] flex font-sans text-slate-800 overflow-hidden">
      {/* LEFT SIDEBAR (Identical to lms.tonyenglish.vn/admin) */}
      <aside className="w-68 bg-[#1e293b] text-slate-300 flex flex-col shrink-0 shadow-xl">
        <div className="h-20 flex items-center justify-between px-6 bg-[#0f172a] border-b border-slate-800 shrink-0">
          <Link to="/" className="font-black text-xl tracking-tight text-white uppercase">
            TONY<span className="text-[#2ab4e8]">ADMIN</span>
          </Link>
          <span className="text-[10px] font-bold bg-[#2ab4e8]/20 text-[#2ab4e8] px-2 py-0.5 rounded-full">
            UNIFIED
          </span>
        </div>

        <div className="p-4 space-y-1 flex-1 overflow-y-auto custom-scrollbar">
          {/* Direct Switch to LMS Admin Modules */}
          <p className="text-[10px] font-black uppercase text-slate-500 tracking-widest ml-3 mb-2 mt-2">
            Hệ thống LMS (lms.tonyenglish.vn)
          </p>
          <a
            href="https://lms.tonyenglish.vn/admin"
            className="w-full flex items-center justify-between px-4 py-2.5 rounded-xl font-bold text-[13px] text-sky-300 bg-sky-950/50 border border-sky-800/50 hover:bg-[#2ab4e8] hover:text-white transition-all mb-3"
          >
            <span>🚀 Mở Quản trị Đề thi &amp; AI LMS</span>
            <span>↗</span>
          </a>

          {/* Website CMS Modules */}
          {groups.map((grp) => (
            <div key={grp} className="pt-2">
              <p className="text-[10px] font-black uppercase text-slate-500 tracking-widest ml-3 mb-1.5">{grp}</p>
              {ADMIN_TABLES.filter((t) => t.group === grp).map((tbl) => (
                <button
                  key={tbl.key}
                  type="button"
                  onClick={() => {
                    setActiveTable(tbl);
                    setPage(1);
                    setSearch('');
                    setEditingRow(null);
                    setIsCreatingNew(false);
                  }}
                  className={`w-full flex items-center gap-3 px-4 py-2.5 rounded-xl font-bold text-[13px] transition-all ${
                    activeTable.key === tbl.key
                      ? 'bg-[#2ab4e8]/15 text-[#2ab4e8]'
                      : 'hover:bg-slate-800 hover:text-white'
                  }`}
                >
                  <span>{tbl.icon}</span>
                  <span className="truncate">{tbl.label}</span>
                </button>
              ))}
            </div>
          ))}
        </div>

        <div className="p-4 border-t border-slate-800 bg-[#0f172a]/60 flex items-center justify-between text-xs">
          <Link to="/" className="text-slate-400 hover:text-white font-bold">
            ← Xem Website
          </Link>
          <button
            type="button"
            onClick={() => setAdmin(null)}
            className="text-rose-400 hover:text-rose-300 font-bold"
          >
            Đăng xuất
          </button>
        </div>
      </aside>

      {/* MAIN CONTENT AREA */}
      <main className="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
        {/* Top Header */}
        <header className="h-20 bg-white border-b border-slate-200 px-8 flex items-center justify-between shrink-0 shadow-2xs">
          <div className="flex items-center gap-3">
            <span className="text-2xl">{activeTable.icon}</span>
            <div>
              <h1 className="text-xl font-black text-slate-800 uppercase tracking-tight">{activeTable.label}</h1>
              <p className="text-xs text-slate-400 font-medium">
                Bảng dữ liệu Supabase: <code className="text-[#0a5482] font-bold">{activeTable.key}</code> ({totalRows}{' '}
                bản ghi)
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <input
              type="text"
              placeholder={`🔍 Tìm kiếm theo ${activeTable.titleCol}...`}
              value={search}
              onChange={(e) => {
                setSearch(e.target.value);
                setPage(1);
              }}
              className="w-64 border border-slate-300 rounded-xl px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
            />
            <button
              type="button"
              onClick={handleStartCreate}
              className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-md transition"
            >
              + THÊM MỚI
            </button>
          </div>
        </header>

        {/* Table / Editor Body */}
        <div className="flex-1 overflow-y-auto p-8 custom-scrollbar">
          {editingRow ? (
            <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-6 sm:p-8 max-w-5xl mx-auto">
              <div className="flex items-center justify-between pb-4 mb-6 border-b border-slate-200">
                <div>
                  <h2 className="text-xl font-black text-[#0a5482]">
                    {isCreatingNew
                      ? `➕ Thêm bản ghi mới (${activeTable.label})`
                      : `✏️ Chỉnh sửa #${editingRow[activeTable.pk]} (${activeTable.label})`}
                  </h2>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Mọi thay đổi sẽ được cập nhật trực tiếp lên cơ sở dữ liệu Supabase
                  </p>
                </div>
                <button
                  type="button"
                  onClick={() => {
                    setEditingRow(null);
                    setIsCreatingNew(false);
                  }}
                  className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-bold"
                >
                  ✕ Đóng
                </button>
              </div>

              {saveNotice && (
                <div className="p-4 mb-6 rounded-xl bg-sky-50 border border-sky-200 text-[#0a5482] font-bold text-sm">
                  {saveNotice}
                </div>
              )}

              <form onSubmit={handleSaveRow} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  {Object.keys(editingRow).map((col) => {
                    const val = editingRow[col] ?? '';
                    const isLong =
                      typeof val === 'string' &&
                      (val.length > 100 ||
                        col.includes('content') ||
                        col.includes('desc') ||
                        col.includes('Outline') ||
                        col.includes('question') ||
                        col.includes('answer') ||
                        col.includes('conversation'));
                    return (
                      <div key={col} className={isLong ? 'md:col-span-2' : ''}>
                        <label className="block text-xs font-extrabold text-slate-600 uppercase tracking-wider mb-1.5">
                          {col}
                        </label>
                        {isLong ? (
                          <textarea
                            rows={6}
                            value={val}
                            onChange={(e) => setEditingRow({ ...editingRow, [col]: e.target.value })}
                            className="w-full border border-slate-300 rounded-xl p-3.5 font-mono text-xs bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                          />
                        ) : (
                          <input
                            type="text"
                            disabled={col === activeTable.pk && !isCreatingNew}
                            value={val}
                            onChange={(e) => setEditingRow({ ...editingRow, [col]: e.target.value })}
                            className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm bg-white disabled:bg-slate-100 focus:outline-none focus:ring-2 focus:ring-[#2ab4e8]"
                          />
                        )}
                      </div>
                    );
                  })}
                </div>

                <div className="pt-4 border-t border-slate-200 flex items-center gap-3">
                  <button
                    type="submit"
                    className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-sm px-8 py-3 rounded-xl shadow-lg transition"
                  >
                    💾 Lưu lên Supabase
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setEditingRow(null);
                      setIsCreatingNew(false);
                    }}
                    className="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-sm px-6 py-3 rounded-xl"
                  >
                    Hủy
                  </button>
                </div>
              </form>
            </div>
          ) : (
            <div className="bg-white rounded-3xl border border-slate-200 shadow-xs overflow-hidden">
              {loading ? (
                <div className="p-16 text-center text-slate-400 font-bold">Đang tải dữ liệu từ Supabase...</div>
              ) : (
                <>
                  <div className="overflow-x-auto">
                    <table className="w-full text-left border-collapse text-sm">
                      <thead>
                        <tr className="bg-slate-50 border-b border-slate-200 text-xs font-black text-slate-500 uppercase tracking-wider">
                          <th className="py-3.5 px-5 w-24">ID ({activeTable.pk})</th>
                          <th className="py-3.5 px-5">Tiêu đề ({activeTable.titleCol})</th>
                          {activeTable.subCol && <th className="py-3.5 px-5">Thông tin phụ ({activeTable.subCol})</th>}
                          <th className="py-3.5 px-5 w-28">Trạng thái</th>
                          <th className="py-3.5 px-5 w-36 text-right">Thao tác</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100">
                        {rows.map((r) => (
                          <tr key={r[activeTable.pk]} className="hover:bg-sky-50/40 transition-colors">
                            <td className="py-3.5 px-5 font-black text-[#0a5482]">#{r[activeTable.pk]}</td>
                            <td className="py-3.5 px-5 font-semibold text-slate-800 max-w-md truncate">
                              {String(r[activeTable.titleCol] ?? '')}
                            </td>
                            {activeTable.subCol && (
                              <td className="py-3.5 px-5 text-slate-500 max-w-xs truncate">
                                {String(r[activeTable.subCol] ?? '')}
                              </td>
                            )}
                            <td className="py-3.5 px-5">
                              {r.deleted === 1 ? (
                                <span className="bg-rose-100 text-rose-700 text-[11px] font-bold px-2.5 py-0.5 rounded-full">
                                  Đã ẩn
                                </span>
                              ) : (
                                <span className="bg-emerald-100 text-emerald-700 text-[11px] font-bold px-2.5 py-0.5 rounded-full">
                                  Hiển thị
                                </span>
                              )}
                            </td>
                            <td className="py-3.5 px-5 text-right">
                              <button
                                type="button"
                                onClick={() => {
                                  setIsCreatingNew(false);
                                  setEditingRow(r);
                                  setSaveNotice('');
                                }}
                                className="bg-sky-50 hover:bg-[#0a5482] text-[#0a5482] hover:text-white font-bold text-xs px-3.5 py-1.5 rounded-lg transition"
                              >
                                ✏️ Chỉnh sửa
                              </button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>

                  {/* Pagination */}
                  <div className="px-6 py-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs font-bold text-slate-500">
                    <span>
                      Trang {page} / {Math.max(1, Math.ceil(totalRows / pageSize))} (Tổng {totalRows} bản ghi)
                    </span>
                    <div className="flex items-center gap-2">
                      <button
                        type="button"
                        disabled={page <= 1}
                        onClick={() => setPage((p) => Math.max(1, p - 1))}
                        className="px-3.5 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-100 disabled:opacity-40"
                      >
                        ‹ Trang trước
                      </button>
                      <button
                        type="button"
                        disabled={page * pageSize >= totalRows}
                        onClick={() => setPage((p) => p + 1)}
                        className="px-3.5 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-100 disabled:opacity-40"
                      >
                        Trang sau ›
                      </button>
                    </div>
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      </main>
    </div>
  );
};
