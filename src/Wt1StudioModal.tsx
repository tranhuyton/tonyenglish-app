import React, { useState, useEffect, useMemo, useRef } from 'react';
import { supabase } from './supabase';
import {
  Wt1FrameworkId,
  WT1_STRUCTURES,
  WT1_FRAMEWORK_ORDER,
  WT1_TREND_ITEMS,
  WT1_DEGREE_MODIFIERS,
  WT1_STATIC_SHARE_CHIPS,
  WT1_APPROX_FRACTION_CHIPS,
  WT1_PROCESS_MAP_CHIPS,
  detectWt1PromptGuide
} from './wt1Data';

export interface Wt1StudioOpenPayload {
  topic: string;
  imageUrl?: string;
  label?: string;
  frameworkHint?: Wt1FrameworkId | 'auto';
  pageHint?: string;
}

interface Wt1AiEvaluation {
  overall: number;
  formulaScore: number;
  formulaReview: {
    structureCheck: string;
    dataAndUnitCheck: string;
    vocabCollocationCheck: string;
  };
  criteria: Array<{
    name: string;
    score: number;
    comment: string;
  }>;
  correctedHtml: string;
  modelUpgradeParagraph?: string;
  generalFeedback: string;
}

// ============================================================================
// 1. MODAL BẢNG TỪ VỰNG XU HƯỚNG & CẤP ĐỘ TASK 1 (ĐỘC LẬP HOẶC MỞ TỪ STUDIO)
// ============================================================================
interface Wt1VocabBankModalProps {
  isOpen: boolean;
  initialTab?: 'trends' | 'degrees' | 'static' | 'process_map';
  onClose: () => void;
  onSelectPhrase?: (phrase: string) => void;
}

export const Wt1VocabBankModal: React.FC<Wt1VocabBankModalProps> = ({
  isOpen,
  initialTab = 'trends',
  onClose,
  onSelectPhrase
}) => {
  const [activeTab, setActiveTab] = useState<'trends' | 'degrees' | 'static' | 'process_map'>(initialTab);
  const [copiedPhrase, setCopiedPhrase] = useState<string | null>(null);

  // Interactive Phrase Combiner state (Verb + Adverb vs Adj + Noun)
  const [combDir, setCombDir] = useState<'up' | 'down'>('up');
  const [combVerbId, setCombVerbId] = useState<string>('up_climb');
  const [combDegId, setCombDegId] = useState<string>('deg_dramatic');
  const [combTense, setCombTense] = useState<'past' | 'present' | 'future'>('past');

  useEffect(() => {
    if (isOpen) setActiveTab(initialTab);
  }, [isOpen, initialTab]);

  useEffect(() => {
    setCombVerbId(combDir === 'up' ? 'up_climb' : 'down_decline');
  }, [combDir]);

  const combinableTrends = useMemo(
    () => WT1_TREND_ITEMS.filter((t) => t.group === combDir && !t.isExtreme && t.nounForm),
    [combDir]
  );

  const selectedTrend = useMemo(
    () => combinableTrends.find((t) => t.id === combVerbId) || combinableTrends[0],
    [combinableTrends, combVerbId]
  );

  const selectedDeg = useMemo(
    () => WT1_DEGREE_MODIFIERS.find((d) => d.id === combDegId) || WT1_DEGREE_MODIFIERS[0],
    [combDegId]
  );

  const generatedFormula1 = useMemo(() => {
    if (!selectedTrend || !selectedDeg) return '';
    if (combTense === 'past') return `${selectedTrend.verbPast} ${selectedDeg.adverb} to`;
    if (combTense === 'present') return `${selectedTrend.verbPresent} ${selectedDeg.adverb} to`;
    return `is projected to ${selectedTrend.verbBase} ${selectedDeg.adverb} to`;
  }, [selectedTrend, selectedDeg, combTense]);

  const generatedFormula2 = useMemo(() => {
    if (!selectedTrend || !selectedDeg || !selectedTrend.nounForm) return '';
    const leadVerb =
      combTense === 'past'
        ? 'experienced'
        : combTense === 'present'
        ? 'experiences'
        : 'is expected to experience';
    return `${leadVerb} ${selectedDeg.article} ${selectedDeg.adjective} ${selectedTrend.nounForm} to`;
  }, [selectedTrend, selectedDeg, combTense]);

  const handleUseOrCopy = (phrase: string) => {
    if (onSelectPhrase) {
      onSelectPhrase(phrase);
      onClose();
      return;
    }
    navigator.clipboard?.writeText(phrase);
    setCopiedPhrase(phrase);
    setTimeout(() => setCopiedPhrase(null), 1600);
  };

  if (!isOpen) return null;

  const trendSections: Array<{
    group: 'up' | 'down' | 'stable' | 'fluctuate' | 'peak_low' | 'future';
    title: string;
    badgeBg: string;
    borderCol: string;
  }> = [
    { group: 'up', title: '📈 1. Xu hướng ĐI LÊN (Tăng)', badgeBg: 'bg-emerald-600', borderCol: 'border-emerald-200' },
    { group: 'down', title: '📉 2. Xu hướng ĐI XUỐNG (Giảm)', badgeBg: 'bg-rose-600', borderCol: 'border-rose-200' },
    { group: 'stable', title: '➖ 3. GIỮ NGUYÊN / ĐI NGANG (Ổn định)', badgeBg: 'bg-sky-600', borderCol: 'border-sky-200' },
    { group: 'fluctuate', title: '〰️ 4. DAO ĐỘNG LÊN XUỐNG (Biến động)', badgeBg: 'bg-amber-600', borderCol: 'border-amber-200' },
    { group: 'peak_low', title: '⛰️ 5. CHẠM ĐỈNH & CHẠM ĐÁY (Peaks & Lows)', badgeBg: 'bg-violet-600', borderCol: 'border-violet-200' },
    { group: 'future', title: '🔮 6. CẤU TRÚC DỰ BÁO TƯƠNG LAI (2030, 2050...)', badgeBg: 'bg-indigo-600', borderCol: 'border-indigo-200' }
  ];

  const degreeSections: Array<{
    intensity: 'rapid_huge' | 'moderate_steady' | 'slight_small';
    title: string;
    subtitle: string;
    headerClass: string;
  }> = [
    {
      intensity: 'rapid_huge',
      title: '🔥 Cấp độ 1: Thay đổi MẠNH / ĐỘT NGỘT / RÕ RỆT (Rapid & Huge Change)',
      subtitle: 'Dùng khi đường biểu đồ dựng đứng, lao dốc hoặc chênh lệch rất lớn',
      headerClass: 'bg-rose-50 border-rose-200 text-rose-900'
    },
    {
      intensity: 'moderate_steady',
      title: '⚖️ Cấp độ 2: Thay đổi ĐỀU ĐẶN / TỪ TỪ / VỪA PHẢI (Moderate & Steady Change)',
      subtitle: 'Dùng khi số liệu nhích lên/xuống ổn định qua từng mốc năm',
      headerClass: 'bg-amber-50 border-amber-200 text-amber-900'
    },
    {
      intensity: 'slight_small',
      title: '🪶 Cấp độ 3: Thay đổi NHẸ / KHÔNG ĐÁNG KỂ (Slight & Minimal Change)',
      subtitle: 'Dùng khi chênh lệch chỉ 1%–5% hoặc đường gần như thoải nhẹ',
      headerClass: 'bg-sky-50 border-sky-200 text-sky-900'
    }
  ];

  return (
    <div className="fixed inset-0 z-[135] bg-slate-900/75 backdrop-blur-xs flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-white w-full max-w-5xl rounded-2xl shadow-2xl border border-slate-200 flex flex-col max-h-[92vh] overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-emerald-700 via-teal-600 to-cyan-700 text-white px-4 sm:px-6 py-4 flex items-center justify-between gap-3 shrink-0">
          <div>
            <h2 className="font-extrabold text-base sm:text-lg flex items-center gap-2">
              <span>📊</span>
              <span>Bảng Từ Vựng Xu Hướng, Cấp Độ &amp; So Sánh (Writing Task 1)</span>
            </h2>
            <p className="text-xs text-emerald-100 mt-0.5">
              {onSelectPhrase
                ? 'Bấm vào bất kỳ cụm từ nào để ĐIỀN THẲNG vào ô đang chọn trong Khung bất biến!'
                : 'Kho từ đồng nghĩa Đi lên / Đi xuống / Giữ nguyên + Trạng từ & Tính từ cấp độ để điền mượt mọi chỗ [...]'}
            </p>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/30 flex items-center justify-center text-white font-bold text-lg cursor-pointer shrink-0"
            title="Đóng"
          >
            ✕
          </button>
        </div>

        {/* Navigation Tabs */}
        <div className="bg-slate-100 px-3 sm:px-6 py-2.5 border-b border-slate-200 flex flex-wrap gap-1.5 shrink-0">
          {[
            { id: 'trends' as const, label: '📈 Đi lên / Đi xuống / Giữ nguyên' },
            { id: 'degrees' as const, label: '⚡ Trạng-Tính từ Cấp độ & Máy Ghép Cụm' },
            { id: 'static' as const, label: '🥧 Tỷ trọng Tĩnh & Xấp xỉ' },
            { id: 'process_map' as const, label: '⚙️🗺️ Process & Maps' }
          ].map((t) => (
            <button
              key={t.id}
              onClick={() => setActiveTab(t.id)}
              className={`px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold transition-all cursor-pointer ${
                activeTab === t.id
                  ? 'bg-emerald-600 text-white shadow-xs'
                  : 'bg-white text-slate-700 hover:bg-emerald-50 border border-slate-200'
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>

        {/* Body */}
        <div className="p-4 sm:p-6 overflow-y-auto space-y-5 flex-1 bg-slate-50">
          {copiedPhrase && (
            <div className="fixed bottom-6 right-6 z-[150] bg-slate-900 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow-lg">
              ✅ Đã copy: "{copiedPhrase}"
            </div>
          )}

          {/* TAB 1: TRENDS */}
          {activeTab === 'trends' && (
            <div className="space-y-5">
              <div className="bg-emerald-50 border border-emerald-200 rounded-xl p-3.5 text-xs sm:text-sm text-emerald-950">
                <strong>💡 Quy tắc chống lặp từ Band 7.5+:</strong> Trong 1 bài Dynamic, em hãy xoay vòng ít nhất{' '}
                <strong>3–4 động từ khác nhau</strong> (VD: câu 1 dùng <em>stood at ... climbed up steadily</em>, câu 2 đổi sang{' '}
                <em>experienced a dramatic surge</em>, sang Body 2 dùng <em>declined gradually</em> và <em>remained unchanged at</em>).
              </div>

              {trendSections.map((sec) => {
                const items = WT1_TREND_ITEMS.filter((i) => i.group === sec.group);
                return (
                  <div key={sec.group} className={`bg-white rounded-xl border ${sec.borderCol} overflow-hidden shadow-2xs`}>
                    <div className="px-4 py-2.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
                      <span className={`text-xs font-extrabold text-white px-2.5 py-1 rounded-lg ${sec.badgeBg}`}>
                        {sec.title}
                      </span>
                      <span className="text-[11px] text-slate-500 font-medium">
                        {onSelectPhrase ? 'Click cụm mẫu để chèn ngay' : 'Click để copy'}
                      </span>
                    </div>
                    <div className="overflow-x-auto">
                      <table className="w-full text-left border-collapse text-xs sm:text-sm">
                        <thead>
                          <tr className="bg-slate-50/70 text-slate-600 border-b border-slate-200">
                            <th className="py-2 px-3 font-bold">Động từ (Quá khứ / Hiện tại)</th>
                            <th className="py-2 px-3 font-bold">Danh từ tương ứng</th>
                            <th className="py-2 px-3 font-bold">Nghĩa &amp; Lưu ý</th>
                            <th className="py-2 px-3 font-bold">Cụm mẫu ăn điểm (Click dùng ngay)</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100">
                          {items.map((item) => (
                            <tr key={item.id} className="hover:bg-emerald-50/40 transition-colors">
                              <td className="py-2.5 px-3 font-bold text-slate-800 whitespace-nowrap">
                                <button
                                  onClick={() => handleUseOrCopy(item.verbPast)}
                                  className="text-emerald-700 hover:underline cursor-pointer font-extrabold"
                                >
                                  {item.verbPast}
                                </button>
                                <span className="text-slate-400 font-normal text-xs ml-1.5">/ {item.verbPresent}</span>
                              </td>
                              <td className="py-2.5 px-3 text-indigo-700 font-semibold whitespace-nowrap">
                                {item.nounForm ? `a/an ... ${item.nounForm}` : '—'}
                              </td>
                              <td className="py-2.5 px-3 text-slate-600">
                                {item.vi}
                                {item.isExtreme && (
                                  <span className="ml-1.5 inline-block bg-rose-100 text-rose-700 text-[10px] font-extrabold px-1.5 py-0.5 rounded">
                                    CẤM + dramatically
                                  </span>
                                )}
                              </td>
                              <td className="py-2.5 px-3">
                                <button
                                  onClick={() => handleUseOrCopy(item.sampleCollocation)}
                                  className="text-left px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-emerald-100 text-slate-800 hover:text-emerald-900 font-medium text-xs transition-colors cursor-pointer"
                                >
                                  {item.sampleCollocation}
                                </button>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB 2: DEGREES & INTERACTIVE COLLOCATION COMBINER */}
          {activeTab === 'degrees' && (
            <div className="space-y-5">
              {/* Interactive Combiner Box */}
              <div className="bg-gradient-to-br from-indigo-50 via-white to-emerald-50 rounded-2xl border-2 border-indigo-200 p-4 sm:p-5 shadow-xs">
                <div className="flex flex-wrap items-center justify-between gap-2 mb-3">
                  <h3 className="font-extrabold text-sm sm:text-base text-indigo-950 flex items-center gap-2">
                    <span>🧪</span>
                    <span>Máy Ghép Cụm Tự Động Vào Chỗ [...] (2 Công Thức Vàng Task 1)</span>
                  </h3>
                  <span className="text-[11px] font-bold bg-indigo-100 text-indigo-800 px-2.5 py-0.5 rounded-full">
                    Đổi qua lại 2 công thức = Tự động 7.5+ Lexical &amp; Grammar!
                  </span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-4 gap-2.5 mb-4">
                  <div>
                    <label className="block text-[11px] font-bold text-slate-600 mb-1">1. Chiều xu hướng</label>
                    <select
                      value={combDir}
                      onChange={(e) => setCombDir(e.target.value as 'up' | 'down')}
                      className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                    >
                      <option value="up">📈 Đi lên (Tăng)</option>
                      <option value="down">📉 Đi xuống (Giảm)</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-600 mb-1">2. Từ gốc Xu hướng</label>
                    <select
                      value={combVerbId}
                      onChange={(e) => setCombVerbId(e.target.value)}
                      className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                    >
                      {combinableTrends.map((t) => (
                        <option key={t.id} value={t.id}>
                          {t.verbPast} ({t.vi.split('(')[0].trim()})
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-600 mb-1">3. Cấp độ mạnh/nhẹ</label>
                    <select
                      value={combDegId}
                      onChange={(e) => setCombDegId(e.target.value)}
                      className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                    >
                      {WT1_DEGREE_MODIFIERS.map((d) => (
                        <option key={d.id} value={d.id}>
                          {d.adverb} / {d.adjective} ({d.vi.split(',')[0]})
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label className="block text-[11px] font-bold text-slate-600 mb-1">4. Thì của biểu đồ</label>
                    <select
                      value={combTense}
                      onChange={(e) => setCombTense(e.target.value as 'past' | 'present' | 'future')}
                      className="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs font-bold text-slate-800"
                    >
                      <option value="past">Quá khứ (1995–2010)</option>
                      <option value="present">Hiện tại</option>
                      <option value="future">Dự báo Tương lai (2030)</option>
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <div className="bg-white rounded-xl border border-emerald-200 p-3 flex items-center justify-between gap-2">
                    <div>
                      <div className="text-[11px] font-extrabold text-emerald-700 uppercase">
                        Công thức 1: S + Động từ + Trạng từ (-ly)
                      </div>
                      <div className="text-sm font-extrabold text-slate-900 mt-0.5">{generatedFormula1} [Data]</div>
                    </div>
                    <button
                      onClick={() => handleUseOrCopy(generatedFormula1)}
                      className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold shrink-0 cursor-pointer"
                    >
                      {onSelectPhrase ? 'Chèn ô này' : 'Copy'}
                    </button>
                  </div>
                  <div className="bg-white rounded-xl border border-indigo-200 p-3 flex items-center justify-between gap-2">
                    <div>
                      <div className="text-[11px] font-extrabold text-indigo-700 uppercase">
                        Công thức 2: S + experienced + a/an + Tính từ + Danh từ
                      </div>
                      <div className="text-sm font-extrabold text-slate-900 mt-0.5">{generatedFormula2} [Data]</div>
                    </div>
                    <button
                      onClick={() => handleUseOrCopy(generatedFormula2)}
                      className="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shrink-0 cursor-pointer"
                    >
                      {onSelectPhrase ? 'Chèn ô này' : 'Copy'}
                    </button>
                  </div>
                </div>
              </div>

              {/* Degree Tables */}
              {degreeSections.map((sec) => {
                const items = WT1_DEGREE_MODIFIERS.filter((d) => d.intensity === sec.intensity);
                return (
                  <div key={sec.intensity} className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-2xs">
                    <div className={`px-4 py-2.5 border-b ${sec.headerClass}`}>
                      <div className="font-extrabold text-xs sm:text-sm">{sec.title}</div>
                      <div className="text-[11px] opacity-80">{sec.subtitle}</div>
                    </div>
                    <div className="overflow-x-auto">
                      <table className="w-full text-left border-collapse text-xs sm:text-sm">
                        <thead>
                          <tr className="bg-slate-50 text-slate-600 border-b border-slate-200">
                            <th className="py-2 px-3 font-bold">Tính từ (đi trước Danh từ)</th>
                            <th className="py-2 px-3 font-bold">Trạng từ (đi sau Động từ)</th>
                            <th className="py-2 px-3 font-bold">Nghĩa tiếng Việt</th>
                            <th className="py-2 px-3 font-bold">Ví dụ ghép sẵn (Click dùng ngay)</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100">
                          {items.map((deg) => (
                            <tr key={deg.id} className="hover:bg-slate-50">
                              <td className="py-2.5 px-3 font-bold text-indigo-700 whitespace-nowrap">
                                {deg.article} {deg.adjective}
                              </td>
                              <td className="py-2.5 px-3 font-extrabold text-emerald-700 whitespace-nowrap">
                                <button
                                  onClick={() => handleUseOrCopy(deg.adverb)}
                                  className="hover:underline cursor-pointer"
                                >
                                  {deg.adverb}
                                </button>
                              </td>
                              <td className="py-2.5 px-3 text-slate-600">{deg.vi}</td>
                              <td className="py-2.5 px-3 space-y-1">
                                <button
                                  onClick={() => handleUseOrCopy(deg.exampleVerbAdv)}
                                  className="block text-left px-2 py-0.5 rounded bg-emerald-50 hover:bg-emerald-100 text-emerald-900 text-xs font-medium cursor-pointer"
                                >
                                  1) {deg.exampleVerbAdv}
                                </button>
                                <button
                                  onClick={() => handleUseOrCopy(deg.exampleAdjNoun)}
                                  className="block text-left px-2 py-0.5 rounded bg-indigo-50 hover:bg-indigo-100 text-indigo-900 text-xs font-medium cursor-pointer"
                                >
                                  2) {deg.exampleAdjNoun}
                                </button>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB 3: STATIC & APPROXIMATIONS */}
          {activeTab === 'static' && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-white rounded-xl border border-emerald-200 p-4 space-y-3">
                <h3 className="font-extrabold text-sm text-emerald-900">
                  🥧 1. Động từ Tỷ trọng &amp; Xếp hạng (Thay cho từ Tăng/Giảm ở bài Static)
                </h3>
                <div className="space-y-2">
                  {WT1_STATIC_SHARE_CHIPS.map((c, idx) => (
                    <div
                      key={idx}
                      onClick={() => handleUseOrCopy(c.phrase)}
                      className="p-2.5 rounded-xl border border-slate-200 hover:border-emerald-400 hover:bg-emerald-50/50 transition-all cursor-pointer"
                    >
                      <div className="font-extrabold text-xs sm:text-sm text-emerald-800">{c.phrase}</div>
                      <div className="text-xs text-slate-600">{c.vi}</div>
                      {c.note && <div className="text-[11px] text-amber-700 font-medium mt-0.5">💡 {c.note}</div>}
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-white rounded-xl border border-indigo-200 p-4 space-y-3">
                <h3 className="font-extrabold text-sm text-indigo-900">
                  🔢 2. Từ chỉ Xấp xỉ &amp; Quy đổi Phân số (Ăn điểm Lexical Resource)
                </h3>
                <div className="space-y-2">
                  {WT1_APPROX_FRACTION_CHIPS.map((c, idx) => (
                    <div
                      key={idx}
                      onClick={() => handleUseOrCopy(c.phrase)}
                      className="p-2.5 rounded-xl border border-slate-200 hover:border-indigo-400 hover:bg-indigo-50/50 transition-all cursor-pointer"
                    >
                      <div className="font-extrabold text-xs sm:text-sm text-indigo-800">{c.phrase}</div>
                      <div className="text-xs text-slate-600">{c.vi}</div>
                      {c.note && <div className="text-[11px] text-slate-500 mt-0.5">📌 {c.note}</div>}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* TAB 4: PROCESS & MAPS */}
          {activeTab === 'process_map' && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white rounded-xl border border-violet-200 p-4 space-y-2.5">
                <h3 className="font-extrabold text-sm text-violet-900">⚙️ Quy trình (Process)</h3>
                {WT1_PROCESS_MAP_CHIPS.process.map((c, i) => (
                  <div
                    key={i}
                    onClick={() => handleUseOrCopy(c.phrase)}
                    className="p-2.5 rounded-lg border border-slate-200 hover:bg-violet-50 cursor-pointer"
                  >
                    <div className="font-bold text-xs text-violet-800">{c.phrase}</div>
                    <div className="text-[11px] text-slate-600">{c.vi}</div>
                  </div>
                ))}
              </div>
              <div className="bg-white rounded-xl border border-emerald-200 p-4 space-y-2.5">
                <h3 className="font-extrabold text-sm text-emerald-900">🗺️ Bản đồ Ngoài trời (Outdoor Map)</h3>
                {WT1_PROCESS_MAP_CHIPS.outdoor_map.map((c, i) => (
                  <div
                    key={i}
                    onClick={() => handleUseOrCopy(c.phrase)}
                    className="p-2.5 rounded-lg border border-slate-200 hover:bg-emerald-50 cursor-pointer"
                  >
                    <div className="font-bold text-xs text-emerald-800">{c.phrase}</div>
                    <div className="text-[11px] text-slate-600">{c.vi}</div>
                  </div>
                ))}
              </div>
              <div className="bg-white rounded-xl border border-teal-200 p-4 space-y-2.5">
                <h3 className="font-extrabold text-sm text-teal-900">🏢 Sơ đồ Mặt bằng (Indoor Map)</h3>
                {WT1_PROCESS_MAP_CHIPS.indoor_map.map((c, i) => (
                  <div
                    key={i}
                    onClick={() => handleUseOrCopy(c.phrase)}
                    className="p-2.5 rounded-lg border border-slate-200 hover:bg-teal-50 cursor-pointer"
                  >
                    <div className="font-bold text-xs text-teal-800">{c.phrase}</div>
                    <div className="text-[11px] text-slate-600">{c.vi}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// ============================================================================
// 2. MODAL PHÒNG LUYỆN GHÉP KHUNG BẤT BIẾN + TỪ VỰNG XU HƯỚNG & CHẤM AI TASK 1
// ============================================================================
interface Wt1StudioModalProps {
  isOpen: boolean;
  payload: Wt1StudioOpenPayload | null;
  courseId?: string;
  onClose: () => void;
}

export const Wt1StudioModal: React.FC<Wt1StudioModalProps> = ({
  isOpen,
  payload,
  courseId,
  onClose
}) => {
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [selectedFrameworkId, setSelectedFrameworkId] = useState<Wt1FrameworkId>('dynamic');
  const [hasConfirmedFramework, setHasConfirmedFramework] = useState<boolean>(false);
  const [slotValues, setSlotValues] = useState<Record<string, string>>({});
  const [activeVocabSlotKey, setActiveVocabSlotKey] = useState<string | null>(null);

  // Step 2 editor state
  const [essayDraft, setEssayDraft] = useState<string>('');
  const textareaRef = useRef<HTMLTextAreaElement | null>(null);

  // Image zoom state
  const [isImageZoomed, setIsImageZoomed] = useState<boolean>(false);
  const [isLightboxOpen, setIsLightboxOpen] = useState<boolean>(false);

  // Vocab modal inside Studio
  const [vocabModalState, setVocabModalState] = useState<{
    open: boolean;
    tab: 'trends' | 'degrees' | 'static' | 'process_map';
    forSlotKey?: string | null;
  }>({ open: false, tab: 'trends', forSlotKey: null });

  // Step 3 AI grading state
  const [isGrading, setIsGrading] = useState<boolean>(false);
  const [gradeError, setGradeError] = useState<string | null>(null);
  const [aiEvaluation, setAiEvaluation] = useState<Wt1AiEvaluation | null>(null);

  const promptGuide = useMemo(
    () => detectWt1PromptGuide(payload?.topic || '', payload?.pageHint),
    [payload?.topic, payload?.pageHint]
  );

  useEffect(() => {
    if (!isOpen || !payload) return;
    setStep(1);
    setSlotValues({});
    setActiveVocabSlotKey(null);
    setEssayDraft('');
    setAiEvaluation(null);
    setGradeError(null);
    setIsImageZoomed(false);
    setIsLightboxOpen(false);

    if (payload.frameworkHint && payload.frameworkHint !== 'auto') {
      setSelectedFrameworkId(payload.frameworkHint);
      setHasConfirmedFramework(true);
    } else {
      setSelectedFrameworkId(promptGuide.detectedFramework);
      setHasConfirmedFramework(false);
    }
  }, [isOpen, payload, promptGuide.detectedFramework]);

  const frameworkDef = WT1_STRUCTURES[selectedFrameworkId];

  const allSlotsCount = useMemo(() => {
    let total = 0;
    let filled = 0;
    frameworkDef.paragraphs.forEach((p) =>
      p.tokens.forEach((t) => {
        if (t.type !== 'text' && t.slotKey) {
          total += 1;
          if ((slotValues[t.slotKey] || '').trim()) filled += 1;
        }
      })
    );
    return { total, filled };
  }, [frameworkDef, slotValues]);

  const buildAssembledReport = (): string => {
    return frameworkDef.paragraphs
      .map((para) => {
        const raw = para.tokens
          .map((tok) => {
            if (tok.type === 'text') return tok.text || '';
            if (tok.slotKey) {
              const val = (slotValues[tok.slotKey] || '').trim();
              return val || `[${tok.label || tok.placeholder || '...'}]`;
            }
            return '';
          })
          .join('');
        return raw.replace(/\s+\./g, '.').replace(/\s+,/g, ',').replace(/\s{2,}/g, ' ').trim();
      })
      .join('\n\n');
  };

  const handleProceedToStep2 = () => {
    if (!hasConfirmedFramework) {
      setHasConfirmedFramework(true);
    }
    const assembled = buildAssembledReport();
    if (!essayDraft.trim() || window.confirm('Cập nhật lại bản nháp Bước 2 theo các ô em vừa điền ở Bước 1?')) {
      setEssayDraft(assembled);
    }
    setStep(2);
  };

  const wordCount = useMemo(() => {
    const trimmed = essayDraft.trim();
    if (!trimmed) return 0;
    return trimmed.split(/\s+/).length;
  }, [essayDraft]);

  const bracketWarnings = useMemo(() => {
    const matches = essayDraft.match(/\[[^\]]+\]/g);
    return matches ? Array.from(new Set(matches)) : [];
  }, [essayDraft]);

  // Task 1 Fatal Pitfall Radar
  const task1PitfallWarnings = useMemo(() => {
    const low = essayDraft.toLowerCase();
    const warnings: string[] = [];
    if (!low) return warnings;

    if (/\b(in conclusion|to sum up|in summary|to conclude)\b/.test(low)) {
      warnings.push(
        'Cảnh báo cấu trúc: Writing Task 1 KHÔNG viết đoạn kết "In conclusion / To sum up" (đã có Overview rồi)!'
      );
    }
    if (/\b(i think|i believe|in my opinion|from my perspective|we should|governments should)\b/.test(low)) {
      warnings.push(
        'Cảnh báo Task Achievement: Task 1 chỉ báo cáo khách quan dữ liệu trên hình, TUYỆT ĐỐI không nêu ý kiến cá nhân (I think / in my opinion / should)!'
      );
    }
    if (
      selectedFrameworkId === 'static' &&
      /\b(increased|decreased|climbed|rose|dropped|declined|fluctuated|surged|soared|plunged|plummeted|upward trend|downward trend)\b/.test(
        low
      )
    ) {
      warnings.push(
        'Lỗi kinh điển bài Static: Biểu đồ tĩnh 1 thời điểm KHÔNG có biến thiên thời gian — em hãy thay các từ tăng/giảm (increased/dropped/rose...) bằng từ tỷ trọng (accounted for, made up, stood at, ranked first)!'
      );
    }
    if (
      /\b(surged|soared|rocketed|plunged|plummeted)\s+(dramatically|sharply|rapidly|steeply)\b/.test(low)
    ) {
      warnings.push(
        'Lỗi thừa nghĩa (Redundancy): Các động từ cực mạnh (surged, soared, plunged, plummeted) bản thân đã chứa nghĩa "mạnh/vọt" — không đi kèm dramatically/sharply!'
      );
    }
    if (
      selectedFrameworkId === 'indoor_map' &&
      /\b(in the north|in the south|in the east|in the west|northern|southern|eastern|western)\b/.test(low)
    ) {
      warnings.push(
        'Lưu ý Indoor Map: Sơ đồ phòng ốc trong nhà thường KHÔNG dùng Đông/Tây/Nam/Bắc — hãy ưu tiên on the left/right-hand side, in the top-right corner, along the back wall!'
      );
    }
    return warnings;
  }, [essayDraft, selectedFrameworkId]);

  const highlightBracketInEditor = (tag: string) => {
    const el = textareaRef.current;
    if (!el) return;
    const idx = essayDraft.indexOf(tag);
    if (idx >= 0) {
      el.focus();
      el.setSelectionRange(idx, idx + tag.length);
    }
  };

  const insertPhraseAtCursor = (phrase: string) => {
    const el = textareaRef.current;
    if (!el) {
      setEssayDraft((prev) => `${prev} ${phrase}`.trim());
      return;
    }
    const start = el.selectionStart ?? essayDraft.length;
    const end = el.selectionEnd ?? essayDraft.length;
    const needSpaceBefore = start > 0 && !/\s/.test(essayDraft[start - 1]);
    const insertText = (needSpaceBefore ? ' ' : '') + phrase;
    const next = essayDraft.slice(0, start) + insertText + essayDraft.slice(end);
    setEssayDraft(next);
    setTimeout(() => {
      el.focus();
      el.setSelectionRange(start + insertText.length, start + insertText.length);
    }, 10);
  };

  const handleSubmitToAiGrader = async () => {
    if (wordCount < 60) {
      alert('Bài viết còn quá ngắn. Em hãy hoàn thiện 4 đoạn (mục tiêu tối thiểu 150 từ) trước khi nộp chấm AI nhé!');
      return;
    }
    setStep(3);
    setIsGrading(true);
    setGradeError(null);

    try {
      const prompt = `
Bạn là Giám khảo IELTS Writing Task 1 chấm bài kiêm Thầy giáo hướng dẫn phương pháp "Khung Cấu Trúc Bất Biến + Bảng Từ Vựng Xu Hướng & Cấp Độ" của hệ thống TonyEnglish.
QUY TẮC XƯNG HÔ BẮT BUỘC: Xưng "Thầy" và gọi học viên là "em" (TUYỆT ĐỐI KHÔNG xưng "tôi/bạn" hay "con"). Nhận xét ân cần, sắc sảo, chỉ rõ số liệu đúng/sai so với hình biểu đồ đính kèm.

1. ĐỀ BÀI IELTS WRITING TASK 1:
"""
${payload?.topic || ''}
"""
${payload?.imageUrl ? '(Đã đính kèm hình ảnh biểu đồ/bản đồ/quy trình gốc để Thầy đối chiếu trực tiếp số liệu, đơn vị và xu hướng!)' : ''}

2. KHUNG BẤT BIẾN TONYENGLISH HỌC VIÊN ĐANG ÁP DỤNG:
- Dạng khung học viên chọn: ${frameworkDef.name} (${frameworkDef.viSubtitle})
- Dạng khung hệ thống gợi ý cho đề này: ${WT1_STRUCTURES[promptGuide.detectedFramework].name}

3. BÀI LÀM CỦA HỌC VIÊN (${wordCount} từ — chuẩn IELTS Task 1 yêu cầu ≥ 150 từ):
"""
${essayDraft}
"""

Hãy quan sát kỹ HÌNH ẢNH BIỂU ĐỒ (nếu có) và chấm kép bài làm trên theo cả chuẩn IELTS Task 1 lẫn phương pháp Khung bất biến + Từ vựng Xu hướng/Cấp độ của TonyEnglish. Trả về ĐÚNG ĐỊNH DẠNG JSON THUẦN TÚY SAU (KHÔNG bọc markdown \`\`\`json):
{
  "overall": 7.0,
  "formulaScore": 8.5,
  "formulaReview": {
    "structureCheck": "Nhận xét xem em chọn dạng khung (${frameworkDef.shortBadge}) đã chuẩn với biểu đồ chưa, bố cục 4 đoạn (Intro - Overview - Body 1 - Body 2) và Khung bất biến đã chuẩn xác chưa (có bị viết nhầm kết bài hay thiếu Overview không)...",
    "dataAndUnitCheck": "Đối chiếu trực tiếp với hình ảnh biểu đồ: Số liệu, mốc năm, thì của động từ (Quá khứ / Hiện tại / Dự báo tương lai) và ĐƠN VỊ (%, million, tonnes...) em trích xuất đã chính xác chưa, có bỏ sót đặc điểm nổi bật nhất nào không...",
    "vocabCollocationCheck": "Nhận xét cách em kết hợp Bảng Từ Vựng Xu hướng (climbed up, rose, declined, remained stable, accounted for...) + Trạng từ/Tính từ cấp độ (dramatically, steadily, slightly...) hoặc từ vựng Map/Process đã đa dạng và tự nhiên chưa..."
  },
  "criteria": [
    { "name": "Task Achievement", "score": 7.0, "comment": "Nhận xét chi tiết tiếng Việt..." },
    { "name": "Coherence & Cohesion", "score": 7.5, "comment": "Nhận xét chi tiết tiếng Việt..." },
    { "name": "Lexical Resource", "score": 7.0, "comment": "Nhận xét chi tiết tiếng Việt..." },
    { "name": "Grammatical Range & Accuracy", "score": 7.0, "comment": "Nhận xét chi tiết tiếng Việt..." }
  ],
  "correctedHtml": "Toàn bộ bài làm của học viên giữ nguyên chia 4 đoạn bằng <br/><br/>, trong đó mọi chỗ sai số liệu/đơn vị/thì/ngữ pháp hoặc còn sót ngoặc [...] được bọc bằng <span class='bg-red-100 text-red-700 line-through px-1 rounded'>cụm chưa chuẩn</span> kèm ngay kế bên là <span class='bg-emerald-100 text-emerald-800 font-bold px-1 rounded'>cụm sửa mượt chuẩn Band 8.0+</span>.",
  "modelUpgradeParagraph": "Viết tặng em 1 đoạn Overview + 1 đoạn Body mẫu chuẩn Band 8.0+ áp dụng đúng Khung bất biến TonyEnglish và số liệu thật từ hình ảnh của đề này để em đối chiếu học tập.",
  "generalFeedback": "Lời dặn dò tổng kết ngắn gọn 2-3 câu của Thầy giúp em ghi nhớ công thức và bứt phá điểm Task 1."
}
      `.trim();

      const { data, error } = await supabase.functions.invoke('ai-grader', {
        body: {
          prompt,
          imageUrls: payload?.imageUrl ? [payload.imageUrl] : [],
          model: 'gemini-2.5-flash'
        }
      });

      if (error) throw new Error(error.message);
      if (data?.error) throw new Error(data.error);

      const cleaned = String(data.result || '')
        .replace(/```(json)?/gi, '')
        .trim();
      const parsed: Wt1AiEvaluation = JSON.parse(cleaned);
      setAiEvaluation(parsed);

      // Save practice record to test_results
      const {
        data: { user }
      } = await supabase.auth.getUser();
      if (user) {
        await supabase.from('test_results').insert([
          {
            user_id: user.id,
            course_id: courseId || null,
            test_title: `[WT1 Studio] ${payload?.label || frameworkDef.shortBadge}`,
            test_type: 'IELTS-Writing',
            score: parsed.overall || 0,
            total_score: 9,
            time_spent: 0,
            details: {
              mode: 'wt1_studio',
              topic: payload?.topic,
              imageUrl: payload?.imageUrl,
              frameworkId: selectedFrameworkId,
              essay: essayDraft,
              wordCount,
              aiFeedback: parsed
            }
          }
        ]);
      }
    } catch (err: any) {
      console.error('WT1 Studio AI Grader error:', err);
      setGradeError(err?.message || 'Không thể kết nối máy chủ chấm bài AI. Em vui lòng bấm thử lại nhé!');
    } finally {
      setIsGrading(false);
    }
  };

  if (!isOpen || !payload) return null;

  return (
    <>
      <div className="fixed inset-0 z-[120] bg-slate-900/75 backdrop-blur-xs flex items-center justify-center p-1.5 sm:p-3 overflow-y-auto">
        <div className="bg-slate-50 w-full max-w-[1380px] rounded-2xl shadow-2xl border border-slate-200 flex flex-col h-[95vh] overflow-hidden">
          {/* ==================== STICKY HEADER ==================== */}
          <div className="bg-gradient-to-r from-emerald-800 via-teal-700 to-cyan-700 text-white px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-2.5 shrink-0">
            <div className="flex items-center gap-2.5 min-w-0">
              <span className="text-xl">📊</span>
              <div className="min-w-0">
                <div className="flex items-center gap-2 flex-wrap">
                  <h2 className="font-extrabold text-sm sm:text-base tracking-tight truncate">
                    Phòng Luyện Ghép Khung Bất Biến &amp; Chấm AI Mắt Thần (Task 1)
                  </h2>
                  {payload.label && (
                    <span className="bg-white/20 text-white text-[11px] font-bold px-2.5 py-0.5 rounded-full">
                      {payload.label}
                    </span>
                  )}
                </div>
                <p className="text-[11px] text-emerald-100 hidden md:block">
                  Nhìn biểu đồ bên trái → Chọn Khung &amp; Lắp Từ Vựng Xu Hướng/Cấp Độ + Số Liệu bên phải → AI đối chiếu ảnh chấm điểm
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2 flex-wrap">
              {/* Quick Open Vocab Table Button */}
              <button
                onClick={() =>
                  setVocabModalState({
                    open: true,
                    tab: frameworkDef.recommendedVocabTab,
                    forSlotKey: activeVocabSlotKey
                  })
                }
                className="px-3 py-1.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-900 font-extrabold text-xs shadow-xs flex items-center gap-1.5 cursor-pointer transition-all"
              >
                <span>📚</span>
                <span>Bảng Từ Vựng Xu Hướng &amp; Cấp Độ</span>
              </button>

              {/* Stepper Pills */}
              <div className="flex items-center gap-1 bg-slate-950/25 p-1 rounded-xl">
                {[
                  { n: 1 as const, label: '1. Ghép Khung & Số Liệu' },
                  { n: 2 as const, label: '2. Tự Edit (150+ từ)' },
                  { n: 3 as const, label: '3. Chấm AI Mắt Thần' }
                ].map((s) => (
                  <button
                    key={s.n}
                    onClick={() => {
                      if (s.n === 1) setStep(1);
                      if (s.n === 2) {
                        setHasConfirmedFramework(true);
                        if (!essayDraft.trim()) setEssayDraft(buildAssembledReport());
                        setStep(2);
                      }
                      if (s.n === 3 && aiEvaluation) setStep(3);
                    }}
                    className={`px-2.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                      step === s.n
                        ? 'bg-white text-emerald-900 shadow-xs'
                        : s.n === 3 && !aiEvaluation
                        ? 'text-white/45 cursor-not-allowed'
                        : 'text-white/90 hover:bg-white/15'
                    }`}
                  >
                    {s.label}
                  </button>
                ))}
              </div>

              <button
                onClick={onClose}
                className="w-8 h-8 rounded-full bg-white/15 hover:bg-white/30 flex items-center justify-center text-white font-bold text-lg cursor-pointer"
                title="Đóng"
              >
                ✕
              </button>
            </div>
          </div>

          {/* ==================== SPLIT WORKSPACE ==================== */}
          <div className="flex-1 overflow-y-auto lg:overflow-hidden flex flex-col lg:flex-row divide-y lg:divide-y-0 lg:divide-x divide-slate-200">
            {/* LEFT PANE: CHART / PROCESS / MAP VIEWER */}
            <div className="lg:w-[43%] xl:w-[44%] bg-white flex flex-col lg:h-full lg:overflow-y-auto shrink-0">
              <div className="p-4 border-b border-slate-100 bg-slate-50/70">
                <div className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-700 mb-1">
                  📌 Đề bài Writing Task 1
                </div>
                <p className="text-xs sm:text-sm font-bold text-slate-800 leading-relaxed">{payload.topic}</p>
              </div>

              {payload.imageUrl ? (
                <div className="p-3 sm:p-4 flex-1 flex flex-col">
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <span className="text-[11px] font-semibold text-slate-500">
                      🔍 Quan sát kỹ ĐƠN VỊ trục tung/chú thích &amp; MỐC NĂM
                    </span>
                    <div className="flex items-center gap-1.5">
                      <button
                        onClick={() => setIsImageZoomed((z) => !z)}
                        className="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-bold cursor-pointer"
                      >
                        {isImageZoomed ? 'Thu vừa khung' : 'Phóng to 150%'}
                      </button>
                      <button
                        onClick={() => setIsLightboxOpen(true)}
                        className="px-2.5 py-1 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-800 text-[11px] font-bold cursor-pointer"
                      >
                        ⛶ Xem toàn màn hình
                      </button>
                    </div>
                  </div>

                  <div className="border border-slate-200 rounded-xl bg-white p-2 overflow-auto max-h-[340px] lg:max-h-none lg:flex-1 flex items-start justify-center">
                    <img
                      src={payload.imageUrl}
                      alt="IELTS Writing Task 1 Visual"
                      onClick={() => setIsLightboxOpen(true)}
                      className={`transition-all rounded-lg cursor-zoom-in ${
                        isImageZoomed ? 'w-[150%] max-w-none' : 'max-w-full h-auto object-contain'
                      }`}
                    />
                  </div>
                </div>
              ) : (
                <div className="p-6 text-center text-slate-400 text-sm">Đề bài không đính kèm ảnh biểu đồ.</div>
              )}

              {/* Quick Reminder Footer on Left Pane */}
              <div className="p-3.5 bg-amber-50/90 border-t border-amber-200 text-xs text-amber-950 space-y-1">
                <div className="font-extrabold">⚡ Mẹo đọc biểu đồ 15 giây trước khi viết:</div>
                <div>• Kiểm tra <strong>Mốc năm</strong>: Nhiều năm (Dynamic) hay 1 thời điểm (Static)? Có năm tương lai (2030) không?</div>
                <div>• Kiểm tra <strong>Đơn vị</strong>: %, million, billion minutes, hay tonnes?</div>
              </div>
            </div>

            {/* RIGHT PANE: 3-STEP INTERACTIVE STUDIO */}
            <div className="lg:w-[57%] xl:w-[56%] flex-1 lg:h-full lg:overflow-y-auto p-4 sm:p-5 space-y-4 bg-slate-50">
              {/* ==================== STEP 1 ==================== */}
              {step === 1 && (
                <div className="space-y-4">
                  {/* Step 1A: Choose 1 of 8 Task 1 Frameworks */}
                  <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-2xs space-y-3">
                    <div className="flex flex-wrap items-center justify-between gap-2">
                      <div>
                        <span className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-700">
                          Bước 1A • Nhận diện dạng biểu đồ &amp; Mở Khung Bất Biến
                        </span>
                        <h3 className="font-extrabold text-sm sm:text-base text-slate-900">
                          Đề bài bên trái thuộc dạng nào trong 8 dạng Task 1 của Thầy Tony?
                        </h3>
                      </div>
                      <button
                        onClick={() => {
                          setSelectedFrameworkId(promptGuide.detectedFramework);
                          setHasConfirmedFramework(true);
                        }}
                        className="text-xs font-bold text-emerald-700 hover:text-emerald-800 underline cursor-pointer"
                      >
                        ✨ Gợi ý tự động cho đề này
                      </button>
                    </div>

                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                      {WT1_FRAMEWORK_ORDER.map((fid) => {
                        const def = WT1_STRUCTURES[fid];
                        const isSelected = selectedFrameworkId === fid && hasConfirmedFramework;
                        const isRecommended = promptGuide.detectedFramework === fid && hasConfirmedFramework;
                        return (
                          <button
                            key={fid}
                            onClick={() => {
                              setSelectedFrameworkId(fid);
                              setHasConfirmedFramework(true);
                              setActiveVocabSlotKey(null);
                            }}
                            className={`text-left p-2.5 rounded-xl border text-xs transition-all cursor-pointer relative ${
                              isSelected
                                ? 'bg-emerald-600 text-white border-emerald-700 shadow-sm ring-2 ring-emerald-200'
                                : 'bg-slate-50 hover:bg-emerald-50/70 text-slate-800 border-slate-200'
                            }`}
                          >
                            <div className="font-extrabold leading-snug">{def.shortBadge}</div>
                            {isRecommended && (
                              <span
                                className={`inline-block mt-1 text-[10px] font-extrabold px-1.5 py-0.5 rounded ${
                                  isSelected ? 'bg-white/25 text-white' : 'bg-emerald-100 text-emerald-800'
                                }`}
                              >
                                Chuẩn nhất
                              </span>
                            )}
                          </button>
                        );
                      })}
                    </div>

                    {/* Smart Coaching Feedback Box */}
                    {hasConfirmedFramework && (
                      <div
                        className={`rounded-xl p-3.5 border text-xs space-y-1.5 ${
                          selectedFrameworkId === promptGuide.detectedFramework
                            ? 'bg-emerald-50 border-emerald-200 text-emerald-950'
                            : 'bg-amber-50 border-amber-300 text-amber-950'
                        }`}
                      >
                        <div className="font-extrabold flex items-center justify-between gap-2">
                          <span>
                            {selectedFrameworkId === promptGuide.detectedFramework
                              ? `✅ Chính xác! ${promptGuide.detectedConfidenceNote}`
                              : `💡 Gợi ý từ Thầy Tony: Em đang chọn "${frameworkDef.shortBadge}". Với đề này, ${promptGuide.detectedConfidenceNote}`}
                          </span>
                          {selectedFrameworkId !== promptGuide.detectedFramework && (
                            <button
                              onClick={() => setSelectedFrameworkId(promptGuide.detectedFramework)}
                              className="px-2.5 py-1 rounded-lg bg-amber-600 text-white font-bold shrink-0 cursor-pointer"
                            >
                              Đổi sang khung chuẩn
                            </button>
                          )}
                        </div>
                        <div className="text-slate-700">
                          <strong>🕒 Quy tắc chia Thì cho đề này:</strong> {promptGuide.detectedTenseTip}
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Step 1B: Fill the 4-Paragraph Invariant Skeleton */}
                  <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-2xs space-y-4">
                    <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                      <div>
                        <span className="text-[11px] font-extrabold uppercase tracking-wider text-indigo-700">
                          Bước 1B • Điền Từ Vựng Xu Hướng/Cấp Độ &amp; Số Liệu Vào Khung Bất Biến
                        </span>
                        <h3 className="font-extrabold text-sm sm:text-base text-slate-900">{frameworkDef.name}</h3>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold bg-slate-100 text-slate-700 px-2.5 py-1 rounded-full">
                          Đã điền {allSlotsCount.filled}/{allSlotsCount.total} ô
                        </span>
                      </div>
                    </div>

                    {/* Golden Tips of Current Framework */}
                    <div className="bg-indigo-50/70 border border-indigo-100 rounded-xl p-3 text-xs text-indigo-950 space-y-1">
                      {frameworkDef.goldenTips.map((tip, idx) => (
                        <div key={idx}>• {tip}</div>
                      ))}
                    </div>

                    {/* 4 Paragraphs Interactive Fill */}
                    <div className="space-y-4">
                      {frameworkDef.paragraphs.map((para) => (
                        <div
                          key={para.key}
                          className="rounded-xl border border-slate-200 bg-slate-50/60 p-3.5 space-y-2.5"
                        >
                          <div className="flex flex-wrap items-center justify-between gap-1">
                            <span className="font-extrabold text-xs sm:text-sm text-slate-900">{para.title}</span>
                            <span className="text-[11px] text-slate-500 italic">{para.viHint}</span>
                          </div>

                          <div className="text-sm text-slate-800 leading-[2.35] bg-white rounded-xl p-3.5 border border-slate-200/80">
                            {para.tokens.map((tok, tIdx) => {
                              if (tok.type === 'text') {
                                return (
                                  <span key={tIdx} className="font-medium text-slate-700">
                                    {tok.text}
                                  </span>
                                );
                              }

                              const key = tok.slotKey || `slot_${tIdx}`;
                              const val = slotValues[key] || '';
                              const isVocab = tok.type === 'vocab_slot';
                              const isFocused = activeVocabSlotKey === key;

                              return (
                                <span key={key} className="inline-block align-middle mx-1 my-0.5">
                                  <span className="inline-flex items-center gap-1">
                                    <input
                                      type="text"
                                      value={val}
                                      onFocus={() => setActiveVocabSlotKey(key)}
                                      onChange={(e) =>
                                        setSlotValues((prev) => ({ ...prev, [key]: e.target.value }))
                                      }
                                      placeholder={tok.label || tok.placeholder}
                                      style={{
                                        width: `${Math.min(
                                          Math.max((val || tok.label || '1234567890').length + 4, 15),
                                          44
                                        )}ch`
                                      }}
                                      className={`px-2.5 py-1 rounded-lg text-xs sm:text-sm font-bold border transition-all outline-none max-w-full ${
                                        isVocab
                                          ? val
                                            ? 'bg-emerald-50 border-emerald-400 text-emerald-900'
                                            : 'bg-violet-50 border-violet-300 text-violet-900 placeholder:text-violet-500'
                                          : val
                                          ? 'bg-sky-50 border-sky-400 text-sky-900'
                                          : 'bg-sky-50/60 border-sky-300 border-dashed text-slate-800 placeholder:text-sky-600/80'
                                      } ${isFocused ? 'ring-2 ring-emerald-400' : ''}`}
                                    />
                                    {isVocab && (
                                      <button
                                        type="button"
                                        onClick={() => {
                                          setActiveVocabSlotKey(key);
                                          setVocabModalState({
                                            open: true,
                                            tab:
                                              selectedFrameworkId === 'dynamic' || selectedFrameworkId === 'mixed'
                                                ? 'degrees'
                                                : selectedFrameworkId === 'static'
                                                ? 'static'
                                                : 'process_map',
                                            forSlotKey: key
                                          });
                                        }}
                                        title="Mở Bảng Từ Vựng & Máy Ghép Cụm để điền vào ô này"
                                        className="px-1.5 py-1 rounded-md bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-extrabold cursor-pointer shrink-0"
                                      >
                                        +Từ
                                      </button>
                                    )}
                                  </span>

                                  {/* Inline Quick Chips when focused */}
                                  {isFocused && tok.quickChips && tok.quickChips.length > 0 && (
                                    <span className="flex flex-wrap gap-1 mt-1 p-1.5 rounded-lg bg-slate-100 border border-slate-200">
                                      <span className="text-[10px] font-bold text-slate-500 self-center mr-1">
                                        Chọn nhanh:
                                      </span>
                                      {tok.quickChips.map((chip, cIdx) => (
                                        <button
                                          key={cIdx}
                                          type="button"
                                          onClick={() => {
                                            setSlotValues((prev) => ({ ...prev, [key]: chip }));
                                            setActiveVocabSlotKey(null);
                                          }}
                                          className="px-2 py-0.5 rounded-md bg-white hover:bg-emerald-600 hover:text-white text-slate-700 border border-slate-300 text-[11px] font-bold transition-colors cursor-pointer"
                                        >
                                          {chip}
                                        </button>
                                      ))}
                                      {isVocab && (
                                        <button
                                          type="button"
                                          onClick={() =>
                                            setVocabModalState({
                                              open: true,
                                              tab: 'degrees',
                                              forSlotKey: key
                                            })
                                          }
                                          className="px-2 py-0.5 rounded-md bg-amber-100 hover:bg-amber-200 text-amber-900 text-[11px] font-extrabold cursor-pointer"
                                        >
                                          🧪 Mở Máy Ghép Động từ + Cấp độ...
                                        </button>
                                      )}
                                    </span>
                                  )}
                                </span>
                              );
                            })}
                          </div>
                        </div>
                      ))}
                    </div>

                    {/* Step 1 Action Footer */}
                    <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
                      <span className="text-xs text-slate-500">
                        💡 Không sao nếu còn vài ô chưa điền hết — sang Bước 2 em có thể gõ tự do và mài mượt toàn bài!
                      </span>
                      <button
                        onClick={handleProceedToStep2}
                        className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-sm shadow-md cursor-pointer transition-all"
                      >
                        Sang Bước 2: Tự Biên Tập &amp; Hoàn Thiện Bài ➔
                      </button>
                    </div>
                  </div>
                </div>
              )}

              {/* ==================== STEP 2 ==================== */}
              {step === 2 && (
                <div className="space-y-4">
                  <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-2xs space-y-3">
                    <div className="flex flex-wrap items-center justify-between gap-2">
                      <div>
                        <span className="text-[11px] font-extrabold uppercase tracking-wider text-emerald-700">
                          Bước 2 • Tự Biên Tập, Bổ Sung Số Liệu &amp; Kiểm Lỗi Task 1
                        </span>
                        <h3 className="font-extrabold text-sm sm:text-base text-slate-900">
                          Gọt mượt câu chữ &amp; đảm bảo đạt tối thiểu 150 từ chuẩn phòng thi
                        </h3>
                      </div>

                      <div className="flex items-center gap-2">
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-extrabold ${
                            wordCount >= 150
                              ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                              : 'bg-amber-100 text-amber-800 border border-amber-300'
                          }`}
                        >
                          📝 {wordCount} / 150+ từ {wordCount >= 150 ? '✅ Đạt chuẩn' : '(Cần thêm từ)'}
                        </span>
                        <button
                          onClick={() => {
                            if (window.confirm('Lấy lại bản ghép mới nhất từ các ô ở Bước 1?')) {
                              setEssayDraft(buildAssembledReport());
                            }
                          }}
                          className="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold cursor-pointer"
                        >
                          ↺ Đồng bộ lại từ Bước 1
                        </button>
                      </div>
                    </div>

                    {/* Quick Insert Synonym Chips at Cursor */}
                    <div className="bg-slate-50 border border-slate-200 rounded-xl p-2.5 space-y-1.5">
                      <div className="flex items-center justify-between">
                        <span className="text-[11px] font-bold text-slate-600">
                          ⚡ Chèn nhanh cụm đồng nghĩa tại con trỏ:
                        </span>
                        <button
                          onClick={() =>
                            setVocabModalState({
                              open: true,
                              tab: frameworkDef.recommendedVocabTab,
                              forSlotKey: '__editor__'
                            })
                          }
                          className="text-[11px] font-extrabold text-emerald-700 hover:underline cursor-pointer"
                        >
                          📚 Mở toàn bộ Bảng Từ Vựng &amp; Máy Ghép Cụm
                        </button>
                      </div>
                      <div className="flex flex-wrap gap-1.5">
                        {[
                          'climbed up steadily to',
                          'experienced a dramatic surge to',
                          'declined gradually to',
                          'remained relatively stable at',
                          'fluctuated mildly around',
                          'peaked at',
                          'accounted for',
                          'approximately',
                          'respectively',
                          'is projected to reach'
                        ].map((chip) => (
                          <button
                            key={chip}
                            type="button"
                            onClick={() => insertPhraseAtCursor(chip)}
                            className="px-2 py-1 rounded-lg bg-white hover:bg-emerald-600 hover:text-white border border-slate-300 text-[11px] font-bold text-slate-700 transition-colors cursor-pointer"
                          >
                            + {chip}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Unfilled Brackets Radar */}
                    {bracketWarnings.length > 0 && (
                      <div className="bg-amber-50 border border-amber-300 rounded-xl p-3 text-xs text-amber-950 space-y-1.5">
                        <div className="font-extrabold">
                          ⚠️ Còn {bracketWarnings.length} chỗ ngoặc vuông [...] chưa thay bằng dữ liệu thật (Click để nhảy tới sửa):
                        </div>
                        <div className="flex flex-wrap gap-1.5">
                          {bracketWarnings.map((b) => (
                            <button
                              key={b}
                              onClick={() => highlightBracketInEditor(b)}
                              className="px-2 py-0.5 rounded bg-amber-200/80 hover:bg-amber-300 text-amber-950 font-bold cursor-pointer"
                            >
                              {b}
                            </button>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Task 1 Pitfall Warnings */}
                    {task1PitfallWarnings.length > 0 && (
                      <div className="bg-rose-50 border border-rose-300 rounded-xl p-3 text-xs text-rose-900 space-y-1">
                        {task1PitfallWarnings.map((w, i) => (
                          <div key={i} className="font-bold">
                            🚨 {w}
                          </div>
                        ))}
                      </div>
                    )}

                    {/* Editable Textarea */}
                    <textarea
                      ref={textareaRef}
                      value={essayDraft}
                      onChange={(e) => setEssayDraft(e.target.value)}
                      rows={13}
                      placeholder="Bài báo cáo 4 đoạn (Introduction, Overview, Body 1, Body 2) của em sẽ hiển thị tại đây..."
                      className="w-full rounded-xl border border-slate-300 focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200 p-4 text-sm text-slate-800 leading-relaxed font-medium outline-none bg-white resize-y"
                    />

                    {/* Step 2 Action Buttons */}
                    <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                      <button
                        onClick={() => setStep(1)}
                        className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs sm:text-sm cursor-pointer"
                      >
                        ← Quay lại Bước 1
                      </button>

                      <button
                        onClick={handleSubmitToAiGrader}
                        disabled={isGrading}
                        className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 via-teal-600 to-indigo-600 hover:opacity-95 text-white font-extrabold text-sm shadow-lg cursor-pointer flex items-center gap-2"
                      >
                        <span>🤖</span>
                        <span>Nộp Bài Cho Giám Khảo AI Mắt Thần Chấm Kép</span>
                      </button>
                    </div>
                  </div>
                </div>
              )}

              {/* ==================== STEP 3 ==================== */}
              {step === 3 && (
                <div className="space-y-4">
                  {isGrading && (
                    <div className="bg-white rounded-2xl border border-slate-200 p-8 text-center space-y-3 shadow-2xs">
                      <div className="w-12 h-12 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin mx-auto" />
                      <div className="font-extrabold text-base text-slate-800">
                        Giám khảo AI Mắt Thần đang quét biểu đồ &amp; chấm bài của em...
                      </div>
                      <p className="text-xs text-slate-500 max-w-md mx-auto">
                        Đang đối chiếu trực tiếp từng con số, đơn vị, thì động từ và cách lắp Khung bất biến + Từ vựng Xu hướng/Cấp độ (khoảng 5–10 giây).
                      </p>
                    </div>
                  )}

                  {!isGrading && gradeError && (
                    <div className="bg-rose-50 border border-rose-200 rounded-2xl p-5 text-center space-y-3">
                      <div className="font-extrabold text-rose-800 text-sm">⚠️ {gradeError}</div>
                      <div className="flex justify-center gap-2">
                        <button
                          onClick={() => setStep(2)}
                          className="px-4 py-2 rounded-xl bg-white border border-slate-300 text-slate-700 text-xs font-bold cursor-pointer"
                        >
                          ← Quay lại bản nháp
                        </button>
                        <button
                          onClick={handleSubmitToAiGrader}
                          className="px-4 py-2 rounded-xl bg-emerald-600 text-white text-xs font-bold cursor-pointer"
                        >
                          🔄 Thử chấm lại
                        </button>
                      </div>
                    </div>
                  )}

                  {!isGrading && aiEvaluation && (
                    <div className="space-y-4">
                      {/* Dual Score Banner */}
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div className="bg-gradient-to-br from-emerald-600 to-teal-700 text-white rounded-2xl p-4 shadow-sm flex items-center justify-between">
                          <div>
                            <div className="text-xs uppercase font-bold text-emerald-100">
                              Điểm IELTS Writing Task 1
                            </div>
                            <div className="text-xs text-emerald-50 mt-0.5">Chuẩn 4 tiêu chí khảo thí quốc tế</div>
                          </div>
                          <div className="text-3xl font-black bg-white/20 px-4 py-2 rounded-xl">
                            {aiEvaluation.overall}
                          </div>
                        </div>

                        <div className="bg-gradient-to-br from-indigo-600 to-violet-700 text-white rounded-2xl p-4 shadow-sm flex items-center justify-between">
                          <div>
                            <div className="text-xs uppercase font-bold text-indigo-100">
                              Độ Chuẩn Khung &amp; Số Liệu
                            </div>
                            <div className="text-xs text-indigo-50 mt-0.5">Khung bất biến + Từ vựng Xu hướng</div>
                          </div>
                          <div className="text-3xl font-black bg-white/20 px-4 py-2 rounded-xl">
                            {aiEvaluation.formulaScore}/10
                          </div>
                        </div>
                      </div>

                      {/* TonyEnglish Formula & Chart Verification Review */}
                      <div className="bg-white rounded-2xl border border-emerald-200 p-4 space-y-3 shadow-2xs">
                        <h4 className="font-extrabold text-sm text-emerald-900 flex items-center gap-1.5">
                          <span>🎯</span>
                          <span>Nhận xét Chuyên sâu theo Phương pháp Thầy Tony &amp; Đối chiếu Ảnh Biểu Đồ</span>
                        </h4>
                        <div className="space-y-2 text-xs sm:text-sm text-slate-700">
                          <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                            <strong className="text-slate-900">1. Bố cục &amp; Khung bất biến:</strong>{' '}
                            {aiEvaluation.formulaReview?.structureCheck}
                          </div>
                          <div className="p-3 rounded-xl bg-emerald-50/60 border border-emerald-200">
                            <strong className="text-emerald-950">2. Đối chiếu Số liệu, Đơn vị &amp; Thì trên biểu đồ:</strong>{' '}
                            {aiEvaluation.formulaReview?.dataAndUnitCheck}
                          </div>
                          <div className="p-3 rounded-xl bg-indigo-50/60 border border-indigo-200">
                            <strong className="text-indigo-950">3. Từ vựng Xu hướng &amp; Trạng-Tính từ cấp độ:</strong>{' '}
                            {aiEvaluation.formulaReview?.vocabCollocationCheck}
                          </div>
                        </div>
                      </div>

                      {/* 4 Official Criteria */}
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        {(aiEvaluation.criteria || []).map((c, idx) => (
                          <div key={idx} className="bg-white rounded-xl border border-slate-200 p-3.5 space-y-1">
                            <div className="flex items-center justify-between">
                              <span className="font-extrabold text-xs sm:text-sm text-slate-900">{c.name}</span>
                              <span className="px-2 py-0.5 rounded-lg bg-emerald-100 text-emerald-800 font-extrabold text-xs">
                                Band {c.score}
                              </span>
                            </div>
                            <p className="text-xs text-slate-600 leading-relaxed">{c.comment}</p>
                          </div>
                        ))}
                      </div>

                      {/* Inline Corrected Essay */}
                      <div className="bg-white rounded-2xl border border-slate-200 p-4 space-y-2.5">
                        <h4 className="font-extrabold text-sm text-slate-900">
                          ✍️ Bài làm đã được Thầy sửa chi tiết (Đỏ = Cần sửa • Xanh = Nâng cấp Band 8.0+)
                        </h4>
                        <div
                          className="text-xs sm:text-sm text-slate-800 leading-relaxed bg-slate-50 p-4 rounded-xl border border-slate-200"
                          dangerouslySetInnerHTML={{ __html: aiEvaluation.correctedHtml || '' }}
                        />
                      </div>

                      {/* Model Upgrade Reference */}
                      {aiEvaluation.modelUpgradeParagraph && (
                        <div className="bg-amber-50/80 rounded-2xl border border-amber-200 p-4 space-y-2">
                          <h4 className="font-extrabold text-sm text-amber-950">
                            🌟 Đoạn mẫu Band 8.0+ chuẩn Khung bất biến TonyEnglish cho đề này
                          </h4>
                          <p className="text-xs sm:text-sm text-slate-800 whitespace-pre-line leading-relaxed">
                            {aiEvaluation.modelUpgradeParagraph}
                          </p>
                        </div>
                      )}

                      {/* Teacher Final Advice */}
                      <div className="bg-emerald-900 text-white rounded-2xl p-4 text-xs sm:text-sm leading-relaxed">
                        <strong>💬 Lời dặn của Thầy Tony:</strong> {aiEvaluation.generalFeedback}
                      </div>

                      <div className="flex justify-between items-center pt-1">
                        <button
                          onClick={() => setStep(2)}
                          className="px-4 py-2 rounded-xl bg-white border border-slate-300 hover:bg-slate-100 text-slate-800 font-bold text-xs sm:text-sm cursor-pointer"
                        >
                          ← Sửa lại bài &amp; Chấm lại để nâng Band
                        </button>
                        <button
                          onClick={onClose}
                          className="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs sm:text-sm cursor-pointer"
                        >
                          Hoàn thành bài luyện ✓
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Fullscreen Image Lightbox */}
      {isLightboxOpen && payload.imageUrl && (
        <div
          onClick={() => setIsLightboxOpen(false)}
          className="fixed inset-0 z-[145] bg-black/85 flex items-center justify-center p-4 cursor-zoom-out"
        >
          <img
            src={payload.imageUrl}
            alt="Zoomed Task 1 Chart"
            className="max-w-[96vw] max-h-[92vh] object-contain bg-white p-2 rounded-xl shadow-2xl"
          />
          <button
            onClick={() => setIsLightboxOpen(false)}
            className="fixed top-4 right-4 px-3.5 py-1.5 rounded-full bg-white text-slate-900 font-extrabold text-sm shadow-lg cursor-pointer"
          >
            ✕ Đóng ảnh phóng to
          </button>
        </div>
      )}

      {/* Embedded Vocab Modal for 1-Click Slot / Editor Insertion */}
      <Wt1VocabBankModal
        isOpen={vocabModalState.open}
        initialTab={vocabModalState.tab}
        onClose={() => setVocabModalState((prev) => ({ ...prev, open: false }))}
        onSelectPhrase={(phrase) => {
          if (vocabModalState.forSlotKey === '__editor__' || step === 2) {
            insertPhraseAtCursor(phrase);
          } else if (vocabModalState.forSlotKey) {
            setSlotValues((prev) => ({ ...prev, [vocabModalState.forSlotKey!]: phrase }));
          }
        }}
      />
    </>
  );
};
