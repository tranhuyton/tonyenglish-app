import React, { useEffect } from 'react';
import { Columns2, PenTool } from 'lucide-react';

export const hasIgcsePaperPdf = (testData: any): boolean => {
  if (!testData) return false;
  const cj = typeof testData.content_json === 'string'
    ? (() => { try { return JSON.parse(testData.content_json); } catch { return {}; } })()
    : (testData.content_json || {});
  const pdfUrl =
    testData.insert_pdf_url ||
    testData.pdf_url ||
    cj?.basicInfo?.insert_pdf_url ||
    cj?.basicInfo?.pdf_url ||
    cj?.pdf_url ||
    testData.json_config?.insert_pdf_url ||
    testData.json_config?.pdf_url ||
    null;
  return Boolean(pdfUrl && String(pdfUrl).trim());
};

const detectIgcseSubjectBadge = (test: any, isEn: boolean): string => {
  const hay = `${test?.title || ''} ${test?.test_type || ''} ${test?.content_json?.basicInfo?.tags || ''}`.toLowerCase();
  if (hay.includes('0580')) return 'Cambridge IGCSE Mathematics 0580';
  if (hay.includes('0606')) return 'Cambridge IGCSE Additional Maths 0606';
  if (hay.includes('0654') || hay.includes('co-ord')) return 'Cambridge IGCSE Co-ordinated Sciences 0654';
  if (hay.includes('0610') || hay.includes('biology')) return 'Cambridge IGCSE Biology 0610';
  if (hay.includes('0620') || hay.includes('chemistry')) return 'Cambridge IGCSE Chemistry 0620';
  if (hay.includes('0625') || hay.includes('physics')) return 'Cambridge IGCSE Physics 0625';
  if (hay.includes('math')) return 'Cambridge IGCSE Mathematics';
  return isEn ? 'TonyEnglish IGCSE Testing' : 'Hệ thống luyện đề Cambridge IGCSE';
};

interface IgcseModeSelectionModalProps {
  test: any | null;
  isEn: boolean;
  onSelect: (mode: 'igcse' | 'igcse-direct') => void;
  onClose: () => void;
}

export default function IgcseModeSelectionModal({
  test,
  isEn,
  onSelect,
  onClose,
}: IgcseModeSelectionModalProps) {
  useEffect(() => {
    if (!test) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, [test, onClose]);

  if (!test) return null;

  const isTouchTablet =
    typeof navigator !== 'undefined' &&
    ((navigator.maxTouchPoints && navigator.maxTouchPoints > 1) ||
      /ipad|tablet|android/i.test(navigator.userAgent || ''));

  const hasTypedDraft = (() => {
    if (!test?.id || typeof localStorage === 'undefined') return false;
    try {
      const saved = localStorage.getItem(`igcse_ans_${test.id}`);
      if (!saved) return false;
      const parsed = JSON.parse(saved);
      return parsed && typeof parsed === 'object' && Object.values(parsed).some((v: any) => String(v || '').trim().length > 0);
    } catch {
      return false;
    }
  })();

  const subjectLabel = detectIgcseSubjectBadge(test, isEn);

  return (
    <div
      className="fixed inset-0 z-[130] flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4 animate-in fade-in duration-200"
      onClick={onClose}
    >
      <div
        className="bg-white w-full max-w-[520px] p-6 sm:p-8 rounded-3xl shadow-2xl border border-slate-200 animate-in zoom-in-95"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="mb-6 text-center">
          <div className="w-15 h-15 bg-gradient-to-br from-sky-50 to-violet-50 rounded-2xl flex items-center justify-center mx-auto mb-3.5 border border-indigo-100 shadow-2xs">
            <PenTool className="w-7 h-7 text-[#0a5482]" />
          </div>
          <span className="text-[11px] font-extrabold uppercase tracking-widest text-[#0284c7] block mb-1">
            {subjectLabel}
          </span>
          <h2
            className="text-[18px] sm:text-[20px] font-black text-slate-800 mb-2 leading-snug line-clamp-2"
            title={test.title}
          >
            {test.title}
          </h2>
          <p className="text-[13.5px] text-slate-500 font-medium">
            {isEn
              ? 'Choose how you want to complete this Cambridge exam paper:'
              : 'Chọn chế độ làm bài phù hợp với thiết bị của bạn:'}
          </p>
        </div>

        <div className="space-y-3.5">
          {/* Option 1: Fill-in Answer Sheet + Upload (Laptop / PC) */}
          <button
            type="button"
            onClick={() => onSelect('igcse')}
            className="w-full flex items-start p-4 sm:p-4.5 bg-white border-2 border-slate-200/90 hover:border-[#0a5482] hover:shadow-md hover:-translate-y-0.5 rounded-2xl transition-all duration-200 text-left group cursor-pointer"
          >
            <div className="w-12 h-12 shrink-0 flex items-center justify-center bg-sky-50 text-[#0a5482] group-hover:bg-[#0a5482] group-hover:text-white rounded-xl mr-4 mt-0.5 transition-colors duration-200">
              <Columns2 className="w-6 h-6" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex flex-wrap items-center gap-1.5 mb-0.5">
                <h3 className="text-[15px] font-black text-slate-800 group-hover:text-[#0a5482] transition-colors">
                  {isEn ? 'Fill-in Answer Sheet (Laptop / PC)' : 'Điền vào ô & Chụp ảnh bài làm'}
                </h3>
                {!isTouchTablet && (
                  <span className="text-[10px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full bg-sky-50 text-[#0a5482] border border-sky-200">
                    {isEn ? 'Best for PC' : 'Tối ưu Laptop'}
                  </span>
                )}
              </div>
              <p className="text-[12.5px] text-slate-500 font-medium leading-relaxed">
                {isEn
                  ? 'Split screen: Cambridge PDF paper on the left, type answers (LaTeX formulas) or paste working photos on the right.'
                  : 'Chia đôi màn hình: xem đề PDF bên trái, điền đáp án (hỗ trợ công thức) hoặc dán ảnh bài nháp bên phải.'}
              </p>
              {hasTypedDraft && (
                <span className="inline-flex items-center gap-1 mt-2 text-[11px] font-bold text-amber-700 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
                  ⏳ {isEn ? 'You have a saved answer draft in this mode' : 'Đang có bản nháp bài làm ở chế độ này'}
                </span>
              )}
            </div>
          </button>

          {/* Option 2: Direct Draw / Write on PDF (iPad / Stylus / Mouse) */}
          <button
            type="button"
            onClick={() => onSelect('igcse-direct')}
            className="w-full flex items-start p-4 sm:p-4.5 bg-white border-2 border-slate-200/90 hover:border-violet-600 hover:shadow-md hover:-translate-y-0.5 rounded-2xl transition-all duration-200 text-left group cursor-pointer"
          >
            <div className="w-12 h-12 shrink-0 flex items-center justify-center bg-violet-50 text-violet-600 group-hover:bg-violet-600 group-hover:text-white rounded-xl mr-4 mt-0.5 transition-colors duration-200">
              <PenTool className="w-6 h-6" />
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex flex-wrap items-center gap-1.5 mb-0.5">
                <h3 className="text-[15px] font-black text-slate-800 group-hover:text-violet-700 transition-colors">
                  {isEn ? 'Write & Draw Directly on PDF (iPad / Stylus)' : 'Viết / Vẽ trực tiếp trên giấy PDF'}
                </h3>
                <span className="text-[10px] font-extrabold uppercase tracking-wider px-2 py-0.5 rounded-full bg-violet-50 text-violet-700 border border-violet-200">
                  {isTouchTablet
                    ? (isEn ? 'Recommended' : 'Khuyên dùng')
                    : (isEn ? 'iPad / Apple Pencil' : 'iPad / Bút cảm ứng')}
                </span>
              </div>
              <p className="text-[12.5px] text-slate-500 font-medium leading-relaxed">
                {isEn
                  ? 'Handwrite workings, equations, and diagrams directly on the exam pages with Apple Pencil, stylus, or mouse — AI grades every part.'
                  : 'Dùng Apple Pencil, bút cảm ứng hoặc chuột viết thẳng lời giải & vẽ hình lên tờ đề như thi giấy thật, AI chấm chi tiết từng câu.'}
              </p>
            </div>
          </button>
        </div>

        <div className="mt-5 pt-2 flex justify-center">
          <button
            type="button"
            onClick={onClose}
            className="text-[13px] font-black text-slate-400 hover:text-slate-600 hover:bg-slate-100 uppercase tracking-widest transition-colors py-2.5 px-8 rounded-xl cursor-pointer"
          >
            {isEn ? 'Cancel' : 'Hủy bỏ'}
          </button>
        </div>
      </div>
    </div>
  );
}
