import React, { useEffect, useMemo, useRef, useState } from 'react';

export interface VideoQuizQuestion {
  id: number;
  question: string;
  options: string[];
  correctIndex: number;
  explanation?: string;
}

export function parseVideoQuizData(raw?: string | null): VideoQuizQuestion[] | null {
  if (!raw) return null;
  const trimmed = raw.trim();
  if (!trimmed.startsWith('{') && !trimmed.startsWith('[')) return null;

  try {
    const parsed = JSON.parse(trimmed);
    const list = Array.isArray(parsed)
      ? parsed
      : parsed && Array.isArray(parsed.questions)
      ? parsed.questions
      : null;

    if (!list || list.length === 0) return null;

    const valid: VideoQuizQuestion[] = [];
    for (let i = 0; i < list.length; i++) {
      const item = list[i];
      if (
        !item ||
        typeof item.question !== 'string' ||
        !Array.isArray(item.options) ||
        item.options.length < 2
      ) {
        continue;
      }
      const cIdx = Number(item.correctIndex);
      if (!Number.isInteger(cIdx) || cIdx < 0 || cIdx >= item.options.length) {
        continue;
      }
      valid.push({
        id: Number(item.id) || i + 1,
        question: item.question.trim(),
        options: item.options.map((o: any) => String(o ?? '').trim()),
        correctIndex: cIdx,
        explanation: item.explanation ? String(item.explanation).trim() : '',
      });
    }

    return valid.length > 0 ? valid : null;
  } catch {
    return null;
  }
}

interface VideoInteractiveQuizProps {
  videoId: number | string;
  videoTitle?: string;
  questions: VideoQuizQuestion[];
  lang: 'vi' | 'en';
}

const OPTION_LABELS = ['A', 'B', 'C', 'D', 'E', 'F'];

export const VideoInteractiveQuiz: React.FC<VideoInteractiveQuizProps> = ({
  videoId,
  questions,
  lang,
}) => {
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, number>>({});
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [confirmPartial, setConfirmPartial] = useState(false);
  const [emptyWarning, setEmptyWarning] = useState(false);
  const [filterMode, setFilterMode] = useState<'all' | 'review' | 'correct'>('all');
  const [isCollapsed, setIsCollapsed] = useState(false);

  const quizTopRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    setSelectedAnswers({});
    setIsSubmitted(false);
    setConfirmPartial(false);
    setEmptyWarning(false);
    setFilterMode('all');
    setIsCollapsed(false);
  }, [videoId]);

  const totalQuestions = questions.length;
  const answeredCount = Object.keys(selectedAnswers).length;
  const unansweredCount = totalQuestions - answeredCount;
  const progressPercent = totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;

  const stats = useMemo(() => {
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    questions.forEach((q, idx) => {
      const chosen = selectedAnswers[idx];
      if (chosen === undefined) {
        skipped++;
      } else if (chosen === q.correctIndex) {
        correct++;
      } else {
        wrong++;
      }
    });
    const percent = totalQuestions > 0 ? Math.round((correct / totalQuestions) * 100) : 0;
    return { correct, wrong, skipped, percent };
  }, [questions, selectedAnswers, totalQuestions]);

  const gradeInfo = useMemo(() => {
    const p = stats.percent;
    if (p >= 90) {
      return {
        badge: lang === 'vi' ? '🌟 Xuất sắc!' : '🌟 Excellent!',
        msg:
          lang === 'vi'
            ? 'Bạn nắm bắt nội dung và từ vựng của video cực kỳ vững vàng!'
            : 'Outstanding mastery of the video content and key vocabulary!',
        tone: 'emerald',
      };
    }
    if (p >= 70) {
      return {
        badge: lang === 'vi' ? '👏 Rất tốt!' : '👏 Great Job!',
        msg:
          lang === 'vi'
            ? 'Kết quả rất đáng khen! Hãy xem lại phần giải thích của một vài câu chưa đúng nhé.'
            : 'Great score! Review the explanations below for the few questions you missed.',
        tone: 'sky',
      };
    }
    if (p >= 50) {
      return {
        badge: lang === 'vi' ? '👍 Khá tốt!' : '👍 Good Effort!',
        msg:
          lang === 'vi'
            ? 'Bạn đã nắm được ý chính. Hãy đọc kỹ lời giải thích bên dưới để ghi nhớ từ vựng sâu hơn nhé.'
            : 'Solid effort! Read the detailed explanations below to strengthen your comprehension.',
        tone: 'amber',
      };
    }
    return {
      badge: lang === 'vi' ? '💪 Cố gắng thêm nhé!' : '💪 Keep Practicing!',
      msg:
        lang === 'vi'
          ? 'Hãy xem lại video kết hợp đọc lời giải thích chi tiết bên dưới rồi thử sức lại nhé!'
          : 'Watch the video again, review the explanations below, and give the quiz another try!',
      tone: 'rose',
    };
  }, [stats.percent, lang]);

  const handleSelectOption = (qIdx: number, optIdx: number) => {
    if (isSubmitted) return;
    setEmptyWarning(false);
    setConfirmPartial(false);
    setSelectedAnswers((prev) => ({
      ...prev,
      [qIdx]: optIdx,
    }));
  };

  const finalizeSubmit = () => {
    setIsSubmitted(true);
    setConfirmPartial(false);
    setEmptyWarning(false);
    setFilterMode('all');
    setTimeout(() => {
      quizTopRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  };

  const handleSubmitClick = () => {
    if (answeredCount === 0) {
      setEmptyWarning(true);
      setConfirmPartial(false);
      return;
    }
    if (unansweredCount > 0 && !confirmPartial) {
      setConfirmPartial(true);
      setEmptyWarning(false);
      return;
    }
    finalizeSubmit();
  };

  const handleRetry = () => {
    setSelectedAnswers({});
    setIsSubmitted(false);
    setConfirmPartial(false);
    setEmptyWarning(false);
    setFilterMode('all');
    setTimeout(() => {
      quizTopRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 60);
  };

  const scrollToQuestion = (qIdx: number) => {
    if (filterMode !== 'all') setFilterMode('all');
    setTimeout(() => {
      const el = document.getElementById(`video-quiz-item-${videoId}-${qIdx}`);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 30);
  };

  const visibleEntries = useMemo(() => {
    return questions
      .map((q, idx) => ({ q, idx }))
      .filter(({ q, idx }) => {
        if (!isSubmitted || filterMode === 'all') return true;
        const chosen = selectedAnswers[idx];
        const isRight = chosen === q.correctIndex;
        if (filterMode === 'correct') return isRight;
        return !isRight;
      });
  }, [questions, isSubmitted, filterMode, selectedAnswers]);

  return (
    <div
      ref={quizTopRef}
      className="rounded-2xl sm:rounded-3xl border border-sky-200/90 bg-gradient-to-b from-sky-50/50 via-white to-white shadow-sm overflow-hidden scroll-mt-24"
    >
      {/* QUIZ HEADER BAR */}
      <div className="bg-gradient-to-r from-[#0a5482] via-[#0d6296] to-[#0f172a] px-4 sm:px-6 py-4 text-white flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3 min-w-0">
          <div className="w-10 h-10 rounded-xl bg-white/20 border border-white/20 flex items-center justify-center text-xl shrink-0">
            📝
          </div>
          <div className="min-w-0">
            <div className="text-[11px] font-extrabold uppercase tracking-widest text-[#2ab4e8]">
              {lang === 'vi' ? 'Bài tập tương tác tại trang' : 'Interactive Video Quiz'}
            </div>
            <h3 className="text-base sm:text-lg font-black tracking-tight truncate">
              {lang === 'vi'
                ? `Trắc nghiệm hiểu bài & Từ vựng (${totalQuestions} câu)`
                : `Comprehension & Vocabulary Quiz (${totalQuestions} Questions)`}
            </h3>
          </div>
        </div>

        <div className="flex items-center gap-2.5 ml-auto">
          {!isSubmitted ? (
            <span className="text-xs font-extrabold bg-white/20 border border-white/20 px-3 py-1.5 rounded-full">
              {lang === 'vi'
                ? `Đã chọn: ${answeredCount}/${totalQuestions}`
                : `Answered: ${answeredCount}/${totalQuestions}`}
            </span>
          ) : (
            <span className="text-xs font-extrabold bg-emerald-400/20 text-emerald-200 border border-emerald-300/30 px-3 py-1.5 rounded-full">
              {lang === 'vi'
                ? `Điểm số: ${stats.correct}/${totalQuestions} (${stats.percent}%)`
                : `Score: ${stats.correct}/${totalQuestions} (${stats.percent}%)`}
            </span>
          )}

          <button
            type="button"
            onClick={() => setIsCollapsed((prev) => !prev)}
            className="text-xs font-bold bg-white/10 hover:bg-white/20 border border-white/20 px-3 py-1.5 rounded-xl transition cursor-pointer"
          >
            {isCollapsed
              ? lang === 'vi'
                ? 'Mở Quiz ▼'
                : 'Expand ▼'
              : lang === 'vi'
              ? 'Thu gọn ▲'
              : 'Collapse ▲'}
          </button>
        </div>
      </div>

      {!isCollapsed && (
        <div className="p-4 sm:p-6 space-y-6">
          {/* PROGRESS BAR (BEFORE SUBMIT) OR INSTANT GRADED RESULT DASHBOARD (AFTER SUBMIT) */}
          {!isSubmitted ? (
            <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 space-y-3">
              <div className="flex items-center justify-between text-xs sm:text-sm font-bold text-slate-600">
                <span>
                  {lang === 'vi'
                    ? '💡 Chọn đáp án đúng nhất cho từng câu hỏi rồi nhấn "Nộp bài & Chấm điểm" để xem kết quả ngay.'
                    : '💡 Select the best answer for each question, then click "Submit & Grade" for instant results.'}
                </span>
                <span className="text-[#0a5482] shrink-0 ml-2">{progressPercent}%</span>
              </div>
              <div className="w-full h-2 bg-slate-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-[#0a5482] to-[#2ab4e8] transition-all duration-300 rounded-full"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>

              {/* QUESTION JUMP PILLS */}
              <div className="flex flex-wrap gap-1.5 pt-1">
                {questions.map((_, idx) => {
                  const isDone = selectedAnswers[idx] !== undefined;
                  return (
                    <button
                      key={idx}
                      type="button"
                      onClick={() => scrollToQuestion(idx)}
                      className={`w-7 h-7 rounded-lg text-xs font-extrabold transition cursor-pointer ${
                        isDone
                          ? 'bg-[#0a5482] text-white shadow-sm'
                          : 'bg-white border border-slate-200 text-slate-500 hover:border-[#0a5482] hover:text-[#0a5482]'
                      }`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>
            </div>
          ) : (
            <div
              className={`rounded-2xl border p-4 sm:p-6 space-y-4 ${
                gradeInfo.tone === 'emerald'
                  ? 'bg-emerald-50/70 border-emerald-200'
                  : gradeInfo.tone === 'sky'
                  ? 'bg-sky-50/70 border-sky-200'
                  : gradeInfo.tone === 'amber'
                  ? 'bg-amber-50/70 border-amber-200'
                  : 'bg-rose-50/70 border-rose-200'
              }`}
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div className="flex items-center gap-4">
                  <div className="w-20 h-20 rounded-2xl bg-white border-2 border-[#0a5482]/20 shadow-sm flex flex-col items-center justify-center shrink-0">
                    <span className="text-xl sm:text-2xl font-black text-[#0a5482] leading-none">
                      {stats.correct}/{totalQuestions}
                    </span>
                    <span className="text-[11px] font-extrabold text-slate-500 mt-1">
                      {stats.percent}%
                    </span>
                  </div>
                  <div className="space-y-1">
                    <div className="text-base sm:text-lg font-black text-slate-900">
                      {gradeInfo.badge}
                    </div>
                    <p className="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">
                      {gradeInfo.msg}
                    </p>
                    <div className="flex flex-wrap items-center gap-2 pt-1 text-xs font-extrabold">
                      <span className="px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800">
                        ✅ {lang === 'vi' ? 'Đúng' : 'Correct'}: {stats.correct}
                      </span>
                      <span className="px-2.5 py-1 rounded-full bg-rose-100 text-rose-800">
                        ❌ {lang === 'vi' ? 'Sai' : 'Wrong'}: {stats.wrong}
                      </span>
                      {stats.skipped > 0 && (
                        <span className="px-2.5 py-1 rounded-full bg-slate-200 text-slate-700">
                          ⚪ {lang === 'vi' ? 'Bỏ trống' : 'Skipped'}: {stats.skipped}
                        </span>
                      )}
                    </div>
                  </div>
                </div>

                <button
                  type="button"
                  onClick={handleRetry}
                  className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-sm transition shrink-0 cursor-pointer self-start sm:self-center"
                >
                  🔄 {lang === 'vi' ? 'Làm lại Quiz' : 'Retry Quiz'}
                </button>
              </div>

              {/* GRADED NAVIGATOR + FILTER TABS */}
              <div className="pt-3 border-t border-slate-200/70 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div className="flex flex-wrap gap-1.5">
                  {questions.map((q, idx) => {
                    const chosen = selectedAnswers[idx];
                    const isRight = chosen === q.correctIndex;
                    const isSkipped = chosen === undefined;
                    return (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => scrollToQuestion(idx)}
                        title={
                          isRight
                            ? lang === 'vi'
                              ? `Câu ${idx + 1}: Đúng`
                              : `Q${idx + 1}: Correct`
                            : isSkipped
                            ? lang === 'vi'
                              ? `Câu ${idx + 1}: Chưa chọn`
                              : `Q${idx + 1}: Skipped`
                            : lang === 'vi'
                            ? `Câu ${idx + 1}: Sai`
                            : `Q${idx + 1}: Incorrect`
                        }
                        className={`w-7 h-7 rounded-lg text-xs font-extrabold transition cursor-pointer ${
                          isRight
                            ? 'bg-emerald-600 text-white'
                            : isSkipped
                            ? 'bg-amber-500 text-white'
                            : 'bg-rose-600 text-white'
                        }`}
                      >
                        {idx + 1}
                      </button>
                    );
                  })}
                </div>

                <div className="flex flex-wrap items-center gap-1.5 text-xs font-bold">
                  <button
                    type="button"
                    onClick={() => setFilterMode('all')}
                    className={`px-3 py-1.5 rounded-lg transition cursor-pointer ${
                      filterMode === 'all'
                        ? 'bg-[#0a5482] text-white'
                        : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
                    }`}
                  >
                    {lang === 'vi' ? `Tất cả (${totalQuestions})` : `All (${totalQuestions})`}
                  </button>
                  {stats.wrong + stats.skipped > 0 && (
                    <button
                      type="button"
                      onClick={() => setFilterMode('review')}
                      className={`px-3 py-1.5 rounded-lg transition cursor-pointer ${
                        filterMode === 'review'
                          ? 'bg-rose-600 text-white'
                          : 'bg-white border border-slate-200 text-rose-700 hover:bg-rose-50'
                      }`}
                    >
                      {lang === 'vi'
                        ? `Cần xem lại (${stats.wrong + stats.skipped})`
                        : `Needs Review (${stats.wrong + stats.skipped})`}
                    </button>
                  )}
                  {stats.correct > 0 && (
                    <button
                      type="button"
                      onClick={() => setFilterMode('correct')}
                      className={`px-3 py-1.5 rounded-lg transition cursor-pointer ${
                        filterMode === 'correct'
                          ? 'bg-emerald-600 text-white'
                          : 'bg-white border border-slate-200 text-emerald-700 hover:bg-emerald-50'
                      }`}
                    >
                      {lang === 'vi' ? `Câu đúng (${stats.correct})` : `Correct (${stats.correct})`}
                    </button>
                  )}
                </div>
              </div>
            </div>
          )}

          {/* QUESTIONS LIST */}
          <div className="space-y-4 sm:space-y-5">
            {visibleEntries.map(({ q, idx }) => {
              const chosen = selectedAnswers[idx];
              const isAnswered = chosen !== undefined;
              const isRight = isSubmitted && chosen === q.correctIndex;
              const isWrong = isSubmitted && isAnswered && chosen !== q.correctIndex;
              const isSkipped = isSubmitted && !isAnswered;

              return (
                <div
                  key={q.id || idx}
                  id={`video-quiz-item-${videoId}-${idx}`}
                  className={`rounded-2xl border p-4 sm:p-5 transition-colors scroll-mt-28 ${
                    !isSubmitted
                      ? isAnswered
                        ? 'bg-white border-sky-200/90 shadow-sm'
                        : 'bg-white border-slate-200/80'
                      : isRight
                      ? 'bg-emerald-50/30 border-emerald-200'
                      : isSkipped
                      ? 'bg-amber-50/30 border-amber-200'
                      : 'bg-rose-50/30 border-rose-200'
                  }`}
                >
                  {/* Question Header & Stem */}
                  <div className="flex items-start justify-between gap-3 mb-3.5">
                    <div className="flex items-start gap-2.5 sm:gap-3">
                      <span
                        className={`inline-flex items-center justify-center px-2.5 py-1 rounded-lg text-xs font-black shrink-0 mt-0.5 ${
                          !isSubmitted
                            ? isAnswered
                              ? 'bg-[#0a5482] text-white'
                              : 'bg-slate-100 text-slate-600'
                            : isRight
                            ? 'bg-emerald-600 text-white'
                            : isSkipped
                            ? 'bg-amber-500 text-white'
                            : 'bg-rose-600 text-white'
                        }`}
                      >
                        {lang === 'vi' ? `Câu ${idx + 1}` : `Q${idx + 1}`}
                      </span>
                      <h4 className="text-[15px] sm:text-base font-bold text-slate-800 leading-relaxed">
                        {q.question}
                      </h4>
                    </div>

                    {isSubmitted && (
                      <span
                        className={`text-[11px] font-extrabold px-2.5 py-1 rounded-full shrink-0 ${
                          isRight
                            ? 'bg-emerald-100 text-emerald-800'
                            : isSkipped
                            ? 'bg-amber-100 text-amber-800'
                            : 'bg-rose-100 text-rose-800'
                        }`}
                      >
                        {isRight
                          ? lang === 'vi'
                            ? '✓ Đúng'
                            : '✓ Correct'
                          : isSkipped
                          ? lang === 'vi'
                            ? '⚪ Bỏ trống'
                            : '⚪ Skipped'
                          : lang === 'vi'
                          ? '✕ Sai'
                          : '✕ Wrong'}
                      </span>
                    )}
                  </div>

                  {/* Options Grid */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                    {q.options.map((opt, optIdx) => {
                      const label = OPTION_LABELS[optIdx] || String(optIdx + 1);
                      const isSelected = chosen === optIdx;
                      const isTrueOption = optIdx === q.correctIndex;

                      let btnStyle =
                        'bg-slate-50/70 hover:bg-sky-50/70 border-slate-200 hover:border-sky-300 text-slate-700';
                      let badgeStyle = 'bg-white border border-slate-300 text-slate-600';

                      if (!isSubmitted) {
                        if (isSelected) {
                          btnStyle =
                            'bg-sky-50 border-[#0a5482] ring-2 ring-[#0a5482]/20 text-[#0a5482] font-semibold';
                          badgeStyle = 'bg-[#0a5482] border border-[#0a5482] text-white';
                        }
                      } else {
                        if (isTrueOption) {
                          btnStyle =
                            'bg-emerald-50/90 border-emerald-400 ring-1 ring-emerald-400/30 text-emerald-900 font-semibold';
                          badgeStyle = 'bg-emerald-600 border border-emerald-600 text-white';
                        } else if (isSelected && !isTrueOption) {
                          btnStyle =
                            'bg-rose-50/90 border-rose-400 ring-1 ring-rose-400/30 text-rose-900 font-medium';
                          badgeStyle = 'bg-rose-600 border border-rose-600 text-white';
                        } else {
                          btnStyle = 'bg-slate-50/50 border-slate-200/70 text-slate-500 opacity-80';
                          badgeStyle = 'bg-slate-100 border border-slate-200 text-slate-400';
                        }
                      }

                      return (
                        <button
                          key={optIdx}
                          type="button"
                          disabled={isSubmitted}
                          onClick={() => handleSelectOption(idx, optIdx)}
                          className={`w-full text-left rounded-xl border p-3 sm:p-3.5 flex items-start gap-3 transition-all ${
                            isSubmitted ? 'cursor-default' : 'cursor-pointer'
                          } ${btnStyle}`}
                        >
                          <span
                            className={`w-6 h-6 rounded-lg text-xs font-extrabold flex items-center justify-center shrink-0 mt-0.5 transition-colors ${badgeStyle}`}
                          >
                            {isSubmitted && isTrueOption
                              ? '✓'
                              : isSubmitted && isSelected && !isTrueOption
                              ? '✕'
                              : label}
                          </span>
                          <div className="flex-1 min-w-0 text-sm sm:text-[14.5px] leading-snug">
                            <span>{opt}</span>
                            {isSubmitted && isTrueOption && (
                              <span className="ml-2 inline-block text-[11px] font-extrabold text-emerald-700 bg-emerald-100/90 px-2 py-0.5 rounded-md">
                                {lang === 'vi' ? 'Đáp án đúng' : 'Correct answer'}
                              </span>
                            )}
                            {isSubmitted && isSelected && !isTrueOption && (
                              <span className="ml-2 inline-block text-[11px] font-extrabold text-rose-700 bg-rose-100/90 px-2 py-0.5 rounded-md">
                                {lang === 'vi' ? 'Bạn chọn' : 'Your choice'}
                              </span>
                            )}
                          </div>
                        </button>
                      );
                    })}
                  </div>

                  {/* Detailed Explanation after Submission */}
                  {isSubmitted && q.explanation && (
                    <div className="mt-3.5 rounded-xl bg-amber-50/70 border border-amber-200/90 p-3.5 sm:p-4 text-sm text-slate-700 leading-relaxed">
                      <div className="font-extrabold text-amber-900 text-xs uppercase tracking-wider mb-1 flex items-center gap-1.5">
                        <span>💡</span>
                        <span>{lang === 'vi' ? 'Giải thích chi tiết' : 'Explanation'}</span>
                      </div>
                      <div>{q.explanation}</div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* BOTTOM ACTION / SUBMIT BAR */}
          <div className="pt-2">
            {emptyWarning && !isSubmitted && (
              <div className="mb-3 rounded-xl bg-amber-50 border border-amber-200 px-4 py-3 text-xs sm:text-sm font-bold text-amber-900">
                ⚠️{' '}
                {lang === 'vi'
                  ? 'Bạn hãy chọn ít nhất 1 đáp án trước khi nộp bài chấm điểm nhé!'
                  : 'Please select at least 1 answer before submitting the quiz!'}
              </div>
            )}

            {confirmPartial && !isSubmitted && (
              <div className="mb-3 rounded-xl bg-sky-50 border border-sky-200 px-4 py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div className="text-xs sm:text-sm font-bold text-[#0a5482]">
                  📌{' '}
                  {lang === 'vi'
                    ? `Bạn còn ${unansweredCount} câu chưa chọn đáp án. Bạn có muốn nộp bài và chấm điểm ngay không?`
                    : `You still have ${unansweredCount} unanswered question(s). Submit and grade anyway?`}
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  <button
                    type="button"
                    onClick={finalizeSubmit}
                    className="bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs px-4 py-2 rounded-lg transition cursor-pointer"
                  >
                    ✅ {lang === 'vi' ? 'Chấm điểm ngay' : 'Grade Now'}
                  </button>
                  <button
                    type="button"
                    onClick={() => setConfirmPartial(false)}
                    className="bg-white hover:bg-slate-100 border border-slate-300 text-slate-700 font-bold text-xs px-3.5 py-2 rounded-lg transition cursor-pointer"
                  >
                    {lang === 'vi' ? 'Làm tiếp' : 'Keep Working'}
                  </button>
                </div>
              </div>
            )}

            {!isSubmitted ? (
              <div className="bg-slate-50 border border-slate-200/90 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div className="text-xs sm:text-sm font-bold text-slate-600">
                  {lang === 'vi'
                    ? `Tiến độ: Đã chọn ${answeredCount} / ${totalQuestions} câu hỏi`
                    : `Progress: ${answeredCount} / ${totalQuestions} questions answered`}
                </div>
                <div className="flex items-center gap-2.5">
                  {answeredCount > 0 && (
                    <button
                      type="button"
                      onClick={() => {
                        setSelectedAnswers({});
                        setConfirmPartial(false);
                        setEmptyWarning(false);
                      }}
                      className="px-4 py-2.5 rounded-xl border border-slate-300 bg-white hover:bg-slate-100 text-slate-600 font-bold text-xs sm:text-sm transition cursor-pointer"
                    >
                      {lang === 'vi' ? 'Làm mới' : 'Clear'}
                    </button>
                  )}
                  <button
                    type="button"
                    onClick={handleSubmitClick}
                    className="flex-1 sm:flex-initial bg-gradient-to-r from-[#0a5482] to-[#0d6ca8] hover:from-[#084266] hover:to-[#0a5482] text-white font-black text-sm sm:text-base px-6 py-3 rounded-xl shadow-md hover:shadow-lg transition cursor-pointer flex items-center justify-center gap-2"
                  >
                    <span>🎯</span>
                    <span>
                      {lang === 'vi' ? 'Nộp bài & Chấm điểm' : 'Submit & View Score'}
                    </span>
                  </button>
                </div>
              </div>
            ) : (
              <div className="bg-slate-50 border border-slate-200/90 rounded-2xl p-4 flex flex-wrap items-center justify-between gap-3">
                <div className="text-xs sm:text-sm font-bold text-slate-600">
                  {lang === 'vi'
                    ? `Kết quả: Đúng ${stats.correct}/${totalQuestions} câu (${stats.percent}%)`
                    : `Final Score: ${stats.correct}/${totalQuestions} (${stats.percent}%)`}
                </div>
                <div className="flex items-center gap-2.5">
                  <button
                    type="button"
                    onClick={() =>
                      quizTopRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
                    }
                    className="px-4 py-2.5 rounded-xl border border-slate-300 bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs sm:text-sm transition cursor-pointer"
                  >
                    ↑ {lang === 'vi' ? 'Lên bảng điểm' : 'Back to Score'}
                  </button>
                  <button
                    type="button"
                    onClick={handleRetry}
                    className="bg-[#0a5482] hover:bg-[#084266] text-white font-extrabold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-sm transition cursor-pointer"
                  >
                    🔄 {lang === 'vi' ? 'Làm lại Quiz' : 'Retry Quiz'}
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
