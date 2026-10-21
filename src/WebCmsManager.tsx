import React, { useEffect, useState } from 'react';
import { supabase } from './supabase';

interface TableConfig {
  key: string;
  label: string;
  icon: string;
  group: string;
  pk: string;
  titleCol: string;
  subCol?: string;
}

const CMS_TABLES: TableConfig[] = [
  { key: 'te_news', label: 'Bài viết Thư viện', icon: '📰', group: 'Thư viện & Video', pk: 'news_id', titleCol: 'news_title', subCol: 'news_title_url' },
  { key: 'te_news_category', label: 'Danh mục Thư viện', icon: '📂', group: 'Thư viện & Video', pk: 'news_cc_id', titleCol: 'news_cc_name_vi', subCol: 'news_cc_name' },
  { key: 'te_video', label: 'Kho Video', icon: '🎬', group: 'Thư viện & Video', pk: 'video_id', titleCol: 'video_desc', subCol: 'video_link' },
  { key: 'te_video_category', label: 'Danh mục Video', icon: '📺', group: 'Thư viện & Video', pk: 'vc_id', titleCol: 'vc_name_vi', subCol: 'vc_name' },
  { key: 'te_course_category', label: 'Khóa học (tonyenglish.vn)', icon: '🎓', group: 'Khóa học & Tuyển sinh', pk: 'cc_id', titleCol: 'cc_name_vi', subCol: 'cc_code' },
  { key: 'te_user_group', label: 'Lịch khai giảng', icon: '📅', group: 'Khóa học & Tuyển sinh', pk: 'ug_id', titleCol: 'ug_name_vi', subCol: 'ug_Month' },
  { key: 'te_lecture', label: 'Bài giảng Web cũ', icon: '📖', group: 'Khóa học & Tuyển sinh', pk: 'lecture_id', titleCol: 'lecture_name', subCol: 'lecture_name_url' },
  { key: 'te_contact', label: 'Khách đăng ký tư vấn', icon: '📩', group: 'Học viên & Cấu hình', pk: 'contact_id', titleCol: 'contact_name', subCol: 'contact_email' },
  { key: 'te_user', label: 'Tài khoản Học viên Web', icon: '👨‍🎓', group: 'Học viên & Cấu hình', pk: 'user_id', titleCol: 'user_name', subCol: 'user_email' },
  { key: 'te_ads', label: 'Banner Slider Trang chủ', icon: '🖼️', group: 'Học viên & Cấu hình', pk: 'ad_id', titleCol: 'title', subCol: 'image' },
  { key: 'te_testimonial', label: 'Cảm nhận học viên', icon: '💬', group: 'Học viên & Cấu hình', pk: 'testimonial_id', titleCol: 'testimonial_title_vi', subCol: 'testimonial_position' },
  { key: 'te_about', label: 'Trang Giới thiệu', icon: 'ℹ️', group: 'Học viên & Cấu hình', pk: 'about_id', titleCol: 'about_title_vi', subCol: 'about_title_en' },
  { key: 'te_options', label: 'Cấu hình chung Website', icon: '⚙️', group: 'Học viên & Cấu hình', pk: 'option_id', titleCol: 'option_key', subCol: 'option_value' },
];

export default function WebCmsManager() {
  const [activeTable, setActiveTable] = useState<TableConfig>(CMS_TABLES[0]);
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
    loadTableData();
  }, [activeTable, page, search]);

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
      setSaveNotice('✅ Đã lưu thành công lên trang tonyenglish.vn!');
      loadTableData();
      setTimeout(() => {
        setEditingRow(null);
        setIsCreatingNew(false);
      }, 600);
    }
  };

  return (
    <div className="p-4 md:p-8 space-y-6">
      {/* Top Category Pills for tonyenglish.vn CMS */}
      <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-100">
          <div>
            <h2 className="text-lg font-black text-slate-800 flex items-center gap-2">
              <span>🌐</span>
              <span>Quản trị Nội dung Website Chính (tonyenglish.vn)</span>
            </h2>
            <p className="text-xs text-slate-500">
              Chỉnh sửa trực tiếp bài viết Thư viện, Khóa học, Kho Video, Lịch khai giảng và Liên hệ trên tonyenglish.vn
            </p>
          </div>
          <a
            href="https://tonyenglish.vn"
            target="_blank"
            rel="noreferrer"
            className="bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-200 text-xs font-extrabold px-4 py-2 rounded-xl transition"
          >
            ↗ Xem trang tonyenglish.vn
          </a>
        </div>

        <div className="flex flex-wrap gap-2">
          {CMS_TABLES.map((tbl) => (
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
              className={`px-3.5 py-2 rounded-xl text-xs font-bold flex items-center gap-1.5 transition-all ${
                activeTable.key === tbl.key
                  ? 'bg-[#0a5482] text-white shadow-sm'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              <span>{tbl.icon}</span>
              <span>{tbl.label}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Search & Action Bar */}
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-2">
          <span className="text-xl">{activeTable.icon}</span>
          <h3 className="font-black text-slate-800 text-base">
            {activeTable.label} <span className="text-slate-400 font-bold text-sm">({totalRows} bản ghi)</span>
          </h3>
        </div>

        <div className="flex items-center gap-3">
          <input
            type="text"
            placeholder={`🔍 Tìm theo ${activeTable.titleCol}...`}
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              setPage(1);
            }}
            className="w-60 sm:w-72 bg-white border border-slate-300 rounded-xl px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#2bd6eb]"
          />
          <button
            type="button"
            onClick={handleStartCreate}
            className="bg-[#0a5482] hover:bg-[#084266] text-white font-black text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow-sm transition whitespace-nowrap"
          >
            + THÊM MỚI
          </button>
        </div>
      </div>

      {/* Main Table or Editor */}
      {editingRow ? (
        <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-6 sm:p-8">
          <div className="flex items-center justify-between pb-4 mb-6 border-b border-slate-200">
            <h4 className="text-lg font-black text-[#0a5482]">
              {isCreatingNew
                ? `➕ Thêm mới (${activeTable.label})`
                : `✏️ Chỉnh sửa #${editingRow[activeTable.pk]} (${activeTable.label})`}
            </h4>
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
                        className="w-full border border-slate-300 rounded-xl p-3.5 font-mono text-xs bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#2bd6eb]"
                      />
                    ) : (
                      <input
                        type="text"
                        disabled={col === activeTable.pk && !isCreatingNew}
                        value={val}
                        onChange={(e) => setEditingRow({ ...editingRow, [col]: e.target.value })}
                        className="w-full border border-slate-300 rounded-xl px-3.5 py-2.5 text-sm bg-white disabled:bg-slate-100 focus:outline-none focus:ring-2 focus:ring-[#2bd6eb]"
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
                💾 Lưu thay đổi
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
            <div className="p-16 text-center text-slate-400 font-bold">Đang tải dữ liệu...</div>
          ) : (
            <>
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse text-sm">
                  <thead>
                    <tr className="bg-slate-50 border-b border-slate-200 text-xs font-black text-slate-500 uppercase tracking-wider">
                      <th className="py-3.5 px-5 w-24">ID</th>
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
                            ✏️ Sửa
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              <div className="px-6 py-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs font-bold text-slate-500">
                <span>
                  Trang {page} / {Math.max(1, Math.ceil(totalRows / pageSize))}
                </span>
                <div className="flex items-center gap-2">
                  <button
                    type="button"
                    disabled={page <= 1}
                    onClick={() => setPage((p) => Math.max(1, p - 1))}
                    className="px-3.5 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-100 disabled:opacity-40"
                  >
                    ‹ Trước
                  </button>
                  <button
                    type="button"
                    disabled={page * pageSize >= totalRows}
                    onClick={() => setPage((p) => p + 1)}
                    className="px-3.5 py-1.5 rounded-lg border border-slate-300 bg-white hover:bg-slate-100 disabled:opacity-40"
                  >
                    Sau ›
                  </button>
                </div>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}
