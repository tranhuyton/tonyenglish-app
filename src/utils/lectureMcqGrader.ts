/**
 * Interactive MCQ Grading & Review Enhancer for LectureViewer iframes
 * (specifically upgrades Office English listening multiple-choice sections
 * to match SAT lectures & External Library interactive quiz UX).
 */

export const LECTURE_MCQ_GRADER_CSS = `
  /* ==============================================================
     OFFICE ENGLISH INTERACTIVE MCQ GRADER (SAT & Library Parity)
     ============================================================== */
  .oe-quiz-shell {
      border-radius: 18px !important;
      border: 2px solid #bae6fd !important;
      background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 14%, #ffffff 100%) !important;
      overflow: hidden !important;
      margin-bottom: 22px !important;
      box-shadow: 0 10px 26px -10px rgba(10, 84, 130, 0.16) !important;
      font-family: 'Be Vietnam Pro', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  }
  .oe-quiz-header {
      background: linear-gradient(135deg, #0a5482 0%, #0f2942 100%) !important;
      padding: 18px 22px !important;
      color: #ffffff !important;
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 12px !important;
  }
  .oe-quiz-header-left {
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      min-width: 0 !important;
  }
  .oe-quiz-header-icon {
      width: 42px !important;
      height: 42px !important;
      border-radius: 12px !important;
      background: rgba(255, 255, 255, 0.15) !important;
      border: 1px solid rgba(255, 255, 255, 0.24) !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      font-size: 20px !important;
      flex-shrink: 0 !important;
  }
  .oe-quiz-title {
      font-size: 16.5px !important;
      font-weight: 800 !important;
      color: #ffffff !important;
      line-height: 1.3 !important;
      margin: 0 !important;
  }
  .oe-quiz-subtitle {
      font-size: 12.5px !important;
      color: rgba(186, 230, 253, 0.94) !important;
      margin: 3px 0 0 0 !important;
      line-height: 1.45 !important;
  }
  .oe-quiz-counter {
      padding: 6px 14px !important;
      border-radius: 999px !important;
      background: rgba(255, 255, 255, 0.16) !important;
      border: 1px solid rgba(255, 255, 255, 0.25) !important;
      font-size: 12.5px !important;
      font-weight: 800 !important;
      color: #ffffff !important;
      white-space: nowrap !important;
  }
  .oe-quiz-progress-track {
      width: 100% !important;
      height: 4px !important;
      background: #e0f2fe !important;
      overflow: hidden !important;
  }
  .oe-quiz-progress-fill {
      height: 100% !important;
      width: 0%;
      background: linear-gradient(90deg, #0ea5e9 0%, #0284c7 60%, #059669 100%) !important;
      transition: width 0.28s ease !important;
  }
  .oe-quiz-body {
      padding: 20px 22px 22px !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 16px !important;
  }
  .oe-quiz-summary {
      display: none;
      border-radius: 16px !important;
      padding: 16px 18px !important;
      border: 2px solid #6ee7b7 !important;
      background: #ecfdf5 !important;
      color: #064e3b !important;
      align-items: center !important;
      justify-content: space-between !important;
      flex-wrap: wrap !important;
      gap: 14px !important;
  }
  .oe-quiz-summary.is-visible {
      display: flex !important;
  }
  .oe-quiz-summary.is-high {
      background: #ecfdf5 !important;
      border-color: #6ee7b7 !important;
      color: #064e3b !important;
  }
  .oe-quiz-summary.is-mid {
      background: #fffbeb !important;
      border-color: #fcd34d !important;
      color: #78350f !important;
  }
  .oe-quiz-summary.is-low {
      background: #fff1f2 !important;
      border-color: #fda4af !important;
      color: #881337 !important;
  }
  .oe-quiz-summary-left {
      display: flex !important;
      flex-direction: column !important;
      gap: 6px !important;
      flex: 1 1 280px !important;
      min-width: 0 !important;
  }
  .oe-quiz-summary-score {
      display: flex !important;
      align-items: center !important;
      gap: 8px !important;
      font-size: 18px !important;
      font-weight: 900 !important;
      line-height: 1.3 !important;
  }
  .oe-quiz-summary-msg {
      font-size: 13.5px !important;
      font-weight: 600 !important;
      opacity: 0.92 !important;
      line-height: 1.5 !important;
  }
  .oe-quiz-summary-chips {
      display: flex !important;
      flex-wrap: wrap !important;
      gap: 6px !important;
      margin-top: 4px !important;
  }
  .oe-quiz-chip {
      display: inline-flex !important;
      align-items: center !important;
      gap: 4px !important;
      padding: 4px 10px !important;
      border-radius: 8px !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      border: none !important;
      cursor: pointer !important;
      transition: transform 0.12s ease, opacity 0.15s ease !important;
  }
  .oe-quiz-chip:hover {
      transform: translateY(-1px);
      opacity: 0.92;
  }
  .oe-quiz-chip.is-ok {
      background: #059669 !important;
      color: #ffffff !important;
  }
  .oe-quiz-chip.is-bad {
      background: #e11d48 !important;
      color: #ffffff !important;
  }
  .oe-quiz-chip.is-skip {
      background: #d97706 !important;
      color: #ffffff !important;
  }
  .oe-quiz-qcard {
      border-radius: 16px !important;
      border: 1.5px solid #e2e8f0 !important;
      background: #ffffff !important;
      padding: 18px 20px !important;
      transition: border-color 0.18s ease, background-color 0.18s ease, box-shadow 0.18s ease !important;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03) !important;
  }
  .oe-quiz-qcard:hover {
      border-color: #bae6fd !important;
  }
  .oe-quiz-qcard.is-correct {
      background: rgba(236, 253, 245, 0.55) !important;
      border-color: #6ee7b7 !important;
  }
  .oe-quiz-qcard.is-wrong {
      background: rgba(255, 241, 242, 0.52) !important;
      border-color: #fda4af !important;
  }
  .oe-quiz-qcard.is-unanswered {
      background: rgba(255, 251, 235, 0.65) !important;
      border-color: #fcd34d !important;
  }
  .oe-quiz-qhead {
      display: flex !important;
      align-items: flex-start !important;
      justify-content: space-between !important;
      gap: 10px !important;
      margin-bottom: 13px !important;
  }
  .oe-quiz-qhead-left {
      display: flex !important;
      align-items: flex-start !important;
      gap: 10px !important;
      min-width: 0 !important;
      flex: 1 !important;
  }
  .oe-quiz-qnum {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 3px 10px !important;
      border-radius: 8px !important;
      background: #0a5482 !important;
      color: #ffffff !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      flex-shrink: 0 !important;
      margin-top: 2px !important;
      white-space: nowrap !important;
  }
  .oe-quiz-qcard.is-correct .oe-quiz-qnum {
      background: #059669 !important;
  }
  .oe-quiz-qcard.is-wrong .oe-quiz-qnum {
      background: #e11d48 !important;
  }
  .oe-quiz-qcard.is-unanswered .oe-quiz-qnum {
      background: #d97706 !important;
  }
  .oe-quiz-qstem {
      font-size: 16px !important;
      font-weight: 700 !important;
      color: #0f172a !important;
      line-height: 1.55 !important;
      user-select: text !important;
  }
  .oe-quiz-qstatus {
      display: none;
      padding: 4px 10px !important;
      border-radius: 8px !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      flex-shrink: 0 !important;
      white-space: nowrap !important;
  }
  .oe-quiz-qstatus.is-ok {
      display: inline-flex !important;
      background: #d1fae5 !important;
      color: #065f46 !important;
      border: 1px solid #a7f3d0 !important;
  }
  .oe-quiz-qstatus.is-bad {
      display: inline-flex !important;
      background: #ffe4e6 !important;
      color: #9f1239 !important;
      border: 1px solid #fecdd3 !important;
  }
  .oe-quiz-qstatus.is-skip {
      display: inline-flex !important;
      background: #fef3c7 !important;
      color: #92400e !important;
      border: 1px solid #fde68a !important;
  }
  .oe-quiz-opts {
      display: flex !important;
      flex-direction: column !important;
      gap: 8px !important;
  }
  .oe-quiz-opt {
      display: flex !important;
      align-items: flex-start !important;
      justify-content: space-between !important;
      gap: 12px !important;
      padding: 11px 14px !important;
      border-radius: 12px !important;
      border: 1.5px solid #e2e8f0 !important;
      background: #f8fafc !important;
      color: #1e293b !important;
      cursor: pointer !important;
      transition: all 0.15s ease !important;
      outline: none !important;
  }
  .oe-quiz-opt:hover:not(.is-locked) {
      border-color: #38bdf8 !important;
      background: #f0f9ff !important;
  }
  .oe-quiz-opt:focus-visible {
      box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.32) !important;
  }
  .oe-quiz-opt.is-selected {
      border-color: #0a5482 !important;
      background: #e0f2fe !important;
      color: #0a5482 !important;
      box-shadow: 0 0 0 1px rgba(10, 84, 130, 0.2) !important;
  }
  .oe-quiz-opt.is-locked {
      cursor: default !important;
  }
  .oe-quiz-opt.is-opt-correct {
      border-color: #10b981 !important;
      background: #ecfdf5 !important;
      color: #064e3b !important;
      font-weight: 600 !important;
      opacity: 1 !important;
  }
  .oe-quiz-opt.is-opt-wrong {
      border-color: #f43f5e !important;
      background: #fff1f2 !important;
      color: #9f1239 !important;
      opacity: 0.96 !important;
  }
  .oe-quiz-opt.is-opt-wrong .oe-quiz-opt-text {
      text-decoration: line-through !important;
  }
  .oe-quiz-opt.is-opt-dim {
      background: #f8fafc !important;
      border-color: #e2e8f0 !important;
      color: #64748b !important;
      opacity: 0.72 !important;
  }
  .oe-quiz-opt-left {
      display: flex !important;
      align-items: flex-start !important;
      gap: 11px !important;
      min-width: 0 !important;
      flex: 1 !important;
  }
  .oe-quiz-badge {
      width: 26px !important;
      height: 26px !important;
      border-radius: 8px !important;
      border: 1.5px solid #cbd5e1 !important;
      background: #ffffff !important;
      color: #475569 !important;
      font-size: 12.5px !important;
      font-weight: 900 !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
      margin-top: 1px !important;
      transition: all 0.15s ease !important;
  }
  .oe-quiz-opt.is-selected .oe-quiz-badge {
      background: #0a5482 !important;
      border-color: #0a5482 !important;
      color: #ffffff !important;
  }
  .oe-quiz-opt.is-opt-correct .oe-quiz-badge {
      background: #059669 !important;
      border-color: #059669 !important;
      color: #ffffff !important;
  }
  .oe-quiz-opt.is-opt-wrong .oe-quiz-badge {
      background: #e11d48 !important;
      border-color: #e11d48 !important;
      color: #ffffff !important;
  }
  .oe-quiz-opt.is-opt-dim .oe-quiz-badge {
      background: #f1f5f9 !important;
      border-color: #e2e8f0 !important;
      color: #94a3b8 !important;
  }
  .oe-quiz-opt-text {
      font-size: 15.5px !important;
      line-height: 1.55 !important;
      user-select: text !important;
  }
  .oe-quiz-opt-tag {
      display: none;
      padding: 3px 9px !important;
      border-radius: 7px !important;
      font-size: 11.5px !important;
      font-weight: 800 !important;
      flex-shrink: 0 !important;
      white-space: nowrap !important;
      margin-top: 2px !important;
  }
  .oe-quiz-opt-tag.is-correct-tag {
      display: inline-flex !important;
      background: #d1fae5 !important;
      color: #065f46 !important;
      border: 1px solid #a7f3d0 !important;
  }
  .oe-quiz-opt-tag.is-wrong-tag {
      display: inline-flex !important;
      background: #ffe4e6 !important;
      color: #9f1239 !important;
      border: 1px solid #fecdd3 !important;
  }
  .oe-quiz-fb {
      display: none;
      margin-top: 12px !important;
      padding: 12px 15px !important;
      border-radius: 12px !important;
      font-size: 14px !important;
      line-height: 1.6 !important;
  }
  .oe-quiz-fb.is-ok {
      display: block !important;
      background: #ecfdf5 !important;
      border: 1px solid #a7f3d0 !important;
      border-left: 4px solid #10b981 !important;
      color: #065f46 !important;
  }
  .oe-quiz-fb.is-bad {
      display: block !important;
      background: #fff1f2 !important;
      border: 1px solid #fecdd3 !important;
      border-left: 4px solid #e11d48 !important;
      color: #881337 !important;
  }
  .oe-quiz-fb.is-skip {
      display: block !important;
      background: #fffbeb !important;
      border: 1px solid #fde68a !important;
      border-left: 4px solid #f59e0b !important;
      color: #78350f !important;
  }
  .oe-quiz-fb-row {
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 8px !important;
  }
  .oe-quiz-transcript-link {
      display: inline-flex !important;
      align-items: center !important;
      gap: 5px !important;
      padding: 4px 10px !important;
      border-radius: 8px !important;
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      color: #0a5482 !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      cursor: pointer !important;
      transition: all 0.15s ease !important;
      white-space: nowrap !important;
  }
  .oe-quiz-transcript-link:hover {
      background: #f0f9ff !important;
      border-color: #38bdf8 !important;
  }
  .oe-quiz-warning {
      display: none;
      padding: 10px 14px !important;
      border-radius: 10px !important;
      background: #fffbeb !important;
      border: 1px solid #fcd34d !important;
      color: #92400e !important;
      font-size: 13.5px !important;
      font-weight: 700 !important;
  }
  .oe-quiz-warning.is-visible {
      display: block !important;
  }
  .oe-quiz-footer {
      padding-top: 14px !important;
      border-top: 1px dashed #cbd5e1 !important;
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 12px !important;
  }
  .oe-quiz-footer-note {
      font-size: 13.5px !important;
      color: #475569 !important;
      font-weight: 600 !important;
  }
  .oe-quiz-actions {
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      gap: 10px !important;
  }
  .oe-quiz-btn-primary {
      display: inline-flex !important;
      align-items: center !important;
      gap: 7px !important;
      padding: 11px 22px !important;
      border-radius: 12px !important;
      border: none !important;
      background: linear-gradient(135deg, #0a5482 0%, #0284c7 100%) !important;
      color: #ffffff !important;
      font-size: 14.5px !important;
      font-weight: 800 !important;
      cursor: pointer !important;
      box-shadow: 0 6px 16px -4px rgba(10, 84, 130, 0.38) !important;
      transition: transform 0.12s ease, filter 0.15s ease !important;
  }
  .oe-quiz-btn-primary:hover {
      filter: brightness(1.06);
  }
  .oe-quiz-btn-primary:active {
      transform: scale(0.98);
  }
  .oe-quiz-btn-secondary {
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      padding: 9px 16px !important;
      border-radius: 11px !important;
      border: 1.5px solid #cbd5e1 !important;
      background: #ffffff !important;
      color: #1e293b !important;
      font-size: 13.5px !important;
      font-weight: 800 !important;
      cursor: pointer !important;
      transition: all 0.15s ease !important;
  }
  .oe-quiz-btn-secondary:hover {
      background: #f8fafc !important;
      border-color: #94a3b8 !important;
  }
  @media (max-width: 600px) {
      .oe-quiz-header {
          padding: 14px 16px !important;
      }
      .oe-quiz-body {
          padding: 14px 14px 16px !important;
      }
      .oe-quiz-qcard {
          padding: 14px 14px !important;
      }
      .oe-quiz-opt {
          padding: 10px 12px !important;
      }
      .oe-quiz-btn-primary {
          width: 100% !important;
          justify-content: center !important;
      }
  }
`;

export function buildLectureMcqGraderScript(isEn: boolean): string {
  const copy = isEn
    ? {
        title: 'Listening Comprehension Quiz',
        subtitle: 'Choose the best answer for each question, then click Submit for instant grading & review.',
        answeredPrefix: 'Answered:',
        answeredSuffix: '',
        qPrefix: 'Q',
        statusCorrect: '✓ Correct',
        statusWrong: '✗ Incorrect',
        statusSkip: '⚠ Unanswered',
        tagCorrect: '✓ Correct Answer',
        tagWrong: '✗ Your Choice',
        submitBtn: 'Submit & Grade',
        retryBtn: 'Retry Quiz',
        transcriptBtn: 'Open / Close Transcript',
        transcriptJump: 'View Transcript',
        warnEmpty: 'Please select at least one answer before submitting!',
        footerPartial: 'You have answered {done}/{total} questions.',
        footerAll: 'All {total}/{total} questions answered! Click Submit to grade.',
        scoreLine: 'Score: {correct}/{total} correct ({pct}%)',
        msg100: 'Excellent! You mastered every single question in this listening track.',
        msgHigh: 'Great job! Review the detailed answers and transcript below to reinforce key details.',
        msgMid: 'Good effort! Check the missed questions and open the transcript below to compare.',
        msgLow: 'Keep practicing! Replay the audio once more alongside the transcript to catch the keywords.',
        chipOk: '✓ Right',
        fbCorrect: '✅ Correct ({letter})!',
        fbWrong: '❌ Incorrect — Correct answer is {letter}:',
        fbSkip: '⚠️ Unanswered — Correct answer is {letter}:',
      }
    : {
        title: 'Bài tập Trắc nghiệm Nghe hiểu (Listening Quiz)',
        subtitle: 'Chọn đáp án đúng nhất cho từng câu hỏi rồi bấm Nộp bài để chấm điểm & chữa chi tiết.',
        answeredPrefix: 'Đã chọn:',
        answeredSuffix: ' câu',
        qPrefix: 'Câu ',
        statusCorrect: '✓ Chính xác',
        statusWrong: '✗ Chưa đúng',
        statusSkip: '⚠ Chưa chọn',
        tagCorrect: '✓ Đáp án đúng',
        tagWrong: '✗ Bạn chọn',
        submitBtn: 'Nộp bài & Chấm điểm',
        retryBtn: 'Làm lại bài tập',
        transcriptBtn: 'Mở / Thu gọn Transcript',
        transcriptJump: 'Đối chiếu Transcript',
        warnEmpty: 'Bạn chưa chọn đáp án nào — hãy chọn ít nhất 1 câu trước khi nộp bài nhé!',
        footerPartial: 'Bạn đã chọn {done}/{total} câu hỏi.',
        footerAll: 'Bạn đã hoàn thành đủ {total}/{total} câu! Bấm Nộp bài để xem điểm ngay.',
        scoreLine: 'Kết quả: {correct}/{total} câu đúng ({pct}%)',
        msg100: 'Xuất sắc! Bạn đã nghe hiểu chính xác toàn bộ nội dung bài nghe.',
        msgHigh: 'Rất tốt! Xem lại chi tiết đáp án và lời thoại bên dưới để ghi nhớ từ khóa nhé.',
        msgMid: 'Khá tốt! Hãy xem lại các câu chưa đúng và mở Transcript bên dưới để đối chiếu.',
        msgLow: 'Cố gắng lên nhé! Nghe lại audio 1 lần nữa kết hợp xem Transcript để bắt ý chính xác hơn.',
        chipOk: '✓ Đúng',
        fbCorrect: '✅ Chính xác ({letter})!',
        fbWrong: '❌ Chưa đúng — Đáp án đúng là {letter}:',
        fbSkip: '⚠️ Chưa chọn — Đáp án đúng là {letter}:',
      };

  const copyJson = JSON.stringify(copy).replace(/<\/script/gi, '<\\/script');

  return `
          (function initOfficeEnglishMcqGrader() {
            var COPY = ${copyJson};

            function escapeHtml(str) {
              return String(str || '')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
            }

            function cleanText(str) {
              return String(str || '').replace(/\\u00a0/g, ' ').replace(/\\s+/g, ' ').trim();
            }

            function normForMatch(str) {
              return cleanText(str)
                .toLowerCase()
                .replace(/[’‘\`´]/g, "'")
                .replace(/[“”]/g, '"')
                .replace(/[^a-z0-9$%'\\s]/g, ' ')
                .replace(/\\s+/g, ' ')
                .trim();
            }

            function tokenSimilarity(a, b) {
              var ta = normForMatch(a).split(' ').filter(Boolean);
              var tb = normForMatch(b).split(' ').filter(Boolean);
              if (!ta.length || !tb.length) return 0;
              var setB = {};
              for (var i = 0; i < tb.length; i++) setB[tb[i]] = (setB[tb[i]] || 0) + 1;
              var hit = 0;
              for (var j = 0; j < ta.length; j++) {
                if (setB[ta[j]] > 0) {
                  hit++;
                  setB[ta[j]]--;
                }
              }
              return (2 * hit) / (ta.length + tb.length);
            }

            function matchCorrectOption(options, rawAnswer) {
              if (!options || !options.length) return { letter: 'A', text: cleanText(rawAnswer) };
              var ansClean = cleanText(rawAnswer);
              if (!ansClean) return { letter: options[0].letter, text: options[0].text };

              // 1. Single-letter answer like "A" or "B."
              var letterOnly = ansClean.match(/^([A-Da-d])(?:[.)])?$/);
              if (letterOnly) {
                var targetL = letterOnly[1].toUpperCase();
                for (var li = 0; li < options.length; li++) {
                  if (options[li].letter === targetL) return { letter: targetL, text: options[li].text };
                }
              }

              var normAns = normForMatch(ansClean);
              // 2. Exact normalized text match
              for (var i = 0; i < options.length; i++) {
                if (normForMatch(options[i].text) === normAns) {
                  return { letter: options[i].letter, text: options[i].text };
                }
              }

              // 3. Containment match (preferring closest length)
              var bestContain = null;
              var bestLenDiff = 1e9;
              for (var j = 0; j < options.length; j++) {
                var no = normForMatch(options[j].text);
                if (!no || !normAns) continue;
                if (no.indexOf(normAns) !== -1 || normAns.indexOf(no) !== -1) {
                  var diff = Math.abs(no.length - normAns.length);
                  if (diff < bestLenDiff) {
                    bestLenDiff = diff;
                    bestContain = options[j];
                  }
                }
              }
              if (bestContain) return { letter: bestContain.letter, text: bestContain.text };

              // 4. Highest token Dice similarity
              var bestOpt = options[0];
              var bestScore = -1;
              for (var k = 0; k < options.length; k++) {
                var sc = tokenSimilarity(options[k].text, ansClean);
                if (sc > bestScore) {
                  bestScore = sc;
                  bestOpt = options[k];
                }
              }
              return { letter: bestOpt.letter, text: bestOpt.text };
            }

            function parseAnswerKeyMap(answerBox) {
              var map = {};
              var ordered = [];
              if (!answerBox) return { map: map, ordered: ordered };
              var clone = answerBox.cloneNode(true);
              // Remove title header child ("Đáp án chính xác (Answer Key):")
              var childDivs = clone.querySelectorAll('div');
              for (var d = 0; d < childDivs.length; d++) {
                var t = cleanText(childDivs[d].textContent);
                if (/đáp án chính xác|answer key/i.test(t) && !/^\\d+\\s*[.)]/.test(t)) {
                  childDivs[d].parentNode && childDivs[d].parentNode.removeChild(childDivs[d]);
                }
              }
              var brs = clone.querySelectorAll('br');
              for (var b = 0; b < brs.length; b++) {
                brs[b].parentNode.replaceChild(document.createTextNode('\\n'), brs[b]);
              }
              var raw = (clone.textContent || '').replace(/\\r/g, '\\n');
              // Split lines, also handle inline "1. ... 2. ... 3. ..." if ever on one line
              var lines = raw.split('\\n').map(cleanText).filter(Boolean);
              if (lines.length === 1 && /\\b2\\s*[.)]\\s+/.test(lines[0])) {
                lines = lines[0].split(/(?=\\b\\d+\\s*[.)]\\s+)/).map(cleanText).filter(Boolean);
              }
              for (var i = 0; i < lines.length; i++) {
                var ln = lines[i];
                if (/^đáp án chính xác|^answer key/i.test(ln)) continue;
                var m = ln.match(/^(\\d+)\\s*[.)]\\s*(.+)$/);
                if (m) {
                  var num = parseInt(m[1], 10);
                  var val = cleanText(m[2]);
                  map[num] = val;
                  ordered.push({ num: num, text: val });
                } else if (ln) {
                  ordered.push({ num: ordered.length + 1, text: ln });
                }
              }
              return { map: map, ordered: ordered };
            }

            function findTranscriptButton(root) {
              var btns = (root || document).querySelectorAll('button');
              for (var i = 0; i < btns.length; i++) {
                var txt = cleanText(btns[i].textContent);
                if (/transcript|lời thoại bài nghe|dialog/i.test(txt) && btns[i].nextElementSibling) {
                  return btns[i];
                }
              }
              return null;
            }

            function openTranscriptSection(root, toggleMode) {
              var tBtn = findTranscriptButton(root);
              if (!tBtn) return;
              var tBox = tBtn.nextElementSibling;
              if (!tBox) return;
              var isHidden = window.getComputedStyle ? window.getComputedStyle(tBox).display === 'none' : tBox.style.display === 'none';
              if (toggleMode || isHidden) {
                tBtn.click();
              }
              setTimeout(function() {
                if (typeof reportHeight === 'function') reportHeight();
                if (!toggleMode || isHidden) {
                  try { tBtn.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {}
                }
              }, 60);
            }

            function upgradeQuizCard(quizCard, answerBtn, answerBox, root) {
              if (!quizCard || quizCard.getAttribute('data-mcq-enhanced') === '1') return;

              var radios = Array.prototype.slice.call(quizCard.querySelectorAll('input[type="radio"]'));
              if (radios.length < 2) return;

              var answerFooter = answerBtn ? answerBtn.parentElement : null;
              var parsedAns = parseAnswerKeyMap(answerBox);
              if (!parsedAns.ordered.length) return;

              // Determine the container holding questions (either #lib_question or nearest common ancestor of radios)
              var libQ = quizCard.querySelector('#lib_question');
              var bodyEl = libQ || (answerFooter && answerFooter.parentElement) || quizCard;

              // Group radios by name in document order & extract stems cleanly
              var questions = [];
              var qByName = {};

              function getOrCreateQuestion(name) {
                if (!qByName[name]) {
                  var numMatch = String(name || '').match(/(\\d+)/);
                  var qObj = {
                    name: name,
                    num: numMatch ? parseInt(numMatch[1], 10) : questions.length + 1,
                    stem: '',
                    options: []
                  };
                  qByName[name] = qObj;
                  questions.push(qObj);
                }
                return qByName[name];
              }

              // Walk direct children of bodyEl to pair question stems with radio labels / bare radios
              var pendingStem = [];
              var nodes = Array.prototype.slice.call(bodyEl.childNodes);
              for (var idx = 0; idx < nodes.length; idx++) {
                var node = nodes[idx];
                if (answerFooter && (node === answerFooter || (node.contains && node.contains(answerFooter)))) {
                  break;
                }

                // Case 1: <label> wrapping a radio
                if (node.nodeType === 1 && node.tagName === 'LABEL') {
                  var lbRadio = node.querySelector('input[type="radio"]');
                  if (lbRadio) {
                    var qObj = getOrCreateQuestion(lbRadio.getAttribute('name') || ('Q' + (questions.length + 1)));
                    if (!qObj.stem && pendingStem.length) {
                      qObj.stem = cleanText(pendingStem.join(' ')).replace(/^\\d+\\s*[.)]\\s*/, '');
                      pendingStem = [];
                    }
                    var rawOpt = cleanText(node.textContent).replace(/^[A-Da-d]\\s*[.)]\\s*/, '');
                    // Defensive fallback: if option text leaked into immediately following <span> (like $0.75)
                    if (!rawOpt && idx + 1 < nodes.length && nodes[idx + 1].nodeType === 1 && nodes[idx + 1].tagName === 'SPAN') {
                      var nextTxt = cleanText(nodes[idx + 1].textContent);
                      if (nextTxt && !/^\\d+\\s*[.)]/.test(nextTxt)) {
                        rawOpt = nextTxt;
                        idx++;
                      }
                    }
                    var letter = ((lbRadio.getAttribute('value') || '').trim().toUpperCase()) || String.fromCharCode(65 + qObj.options.length);
                    qObj.options.push({ letter: letter, text: rawOpt });
                    continue;
                  }
                }

                // Case 2: bare <input type="radio"> without <label>
                if (node.nodeType === 1 && node.tagName === 'INPUT' && (node.getAttribute('type') || '').toLowerCase() === 'radio') {
                  var qObj2 = getOrCreateQuestion(node.getAttribute('name') || ('Q' + (questions.length + 1)));
                  if (!qObj2.stem && pendingStem.length) {
                    qObj2.stem = cleanText(pendingStem.join(' ')).replace(/^\\d+\\s*[.)]\\s*/, '');
                    pendingStem = [];
                  }
                  var bareParts = [];
                  while (idx + 1 < nodes.length) {
                    var nxt = nodes[idx + 1];
                    if (nxt.nodeType === 1 && (nxt.tagName === 'BR' || nxt.tagName === 'LABEL' || nxt.tagName === 'INPUT' || nxt.tagName === 'DIV')) {
                      break;
                    }
                    bareParts.push(nxt.textContent || '');
                    idx++;
                  }
                  var bareText = cleanText(bareParts.join(' ')).replace(/^[A-Da-d]\\s*[.)]\\s*/, '');
                  var letter2 = ((node.getAttribute('value') || '').trim().toUpperCase()) || String.fromCharCode(65 + qObj2.options.length);
                  qObj2.options.push({ letter: letter2, text: bareText });
                  continue;
                }

                // Case 3: Stem text / inline span / paragraph (skip <br> and empty whitespace)
                if (node.nodeType === 1 && node.tagName === 'BR') continue;
                var txtChunk = cleanText(node.textContent || '');
                if (!txtChunk) continue;
                // Avoid stray trailing duplicate text after the last question's 4 options
                var lastQ = questions.length ? questions[questions.length - 1] : null;
                if (lastQ && lastQ.options.length >= 4 && !/^\\d+\\s*[.)]/.test(txtChunk) && pendingStem.length === 0) {
                  // Only buffer if another radio appears later in nodes
                  var hasLaterRadio = false;
                  for (var look = idx + 1; look < nodes.length; look++) {
                    var ln = nodes[look];
                    if (answerFooter && (ln === answerFooter || (ln.contains && ln.contains(answerFooter)))) break;
                    if (ln.nodeType === 1 && (ln.tagName === 'INPUT' || (ln.querySelector && ln.querySelector('input[type="radio"]')))) {
                      hasLaterRadio = true;
                      break;
                    }
                  }
                  if (!hasLaterRadio) continue;
                }
                pendingStem.push(txtChunk);
              }

              // Validate extracted questions
              questions = questions.filter(function(q) { return q.options.length >= 2; });
              if (!questions.length) return;

              // Attach matched correct answer to each question
              for (var qi = 0; qi < questions.length; qi++) {
                var qItem = questions[qi];
                var rawAns = parsedAns.map[qItem.num] || (parsedAns.ordered[qi] ? parsedAns.ordered[qi].text : '');
                var matched = matchCorrectOption(qItem.options, rawAns);
                qItem.correctLetter = matched.letter;
                qItem.correctText = matched.text || rawAns;
              }

              // Build interactive quiz shell
              var shell = document.createElement('div');
              shell.className = 'oe-quiz-shell';
              shell.setAttribute('data-mcq-enhanced', '1');

              var hasTranscript = !!findTranscriptButton(root);

              var qCardsHtml = questions.map(function(q, qIdx) {
                var optsHtml = q.options.map(function(opt) {
                  return '<div role="button" tabindex="0" class="oe-quiz-opt" data-qidx="' + qIdx + '" data-letter="' + escapeHtml(opt.letter) + '">' +
                    '<div class="oe-quiz-opt-left">' +
                      '<span class="oe-quiz-badge">' + escapeHtml(opt.letter) + '</span>' +
                      '<span class="oe-quiz-opt-text">' + escapeHtml(opt.text) + '</span>' +
                    '</div>' +
                    '<span class="oe-quiz-opt-tag"></span>' +
                  '</div>';
                }).join('');

                return '<div class="oe-quiz-qcard" data-qcard="' + qIdx + '">' +
                  '<div class="oe-quiz-qhead">' +
                    '<div class="oe-quiz-qhead-left">' +
                      '<span class="oe-quiz-qnum">' + escapeHtml(COPY.qPrefix + (qIdx + 1)) + '</span>' +
                      '<div class="oe-quiz-qstem">' + escapeHtml(q.stem || (COPY.qPrefix + (qIdx + 1))) + '</div>' +
                    '</div>' +
                    '<span class="oe-quiz-qstatus" data-qstatus="' + qIdx + '"></span>' +
                  '</div>' +
                  '<div class="oe-quiz-opts">' + optsHtml + '</div>' +
                  '<div class="oe-quiz-fb" data-qfb="' + qIdx + '"></div>' +
                '</div>';
              }).join('');

              shell.innerHTML =
                '<div class="oe-quiz-header">' +
                  '<div class="oe-quiz-header-left">' +
                    '<span class="oe-quiz-header-icon">📝</span>' +
                    '<div>' +
                      '<div class="oe-quiz-title">' + escapeHtml(COPY.title) + '</div>' +
                      '<div class="oe-quiz-subtitle">' + escapeHtml(COPY.subtitle) + '</div>' +
                    '</div>' +
                  '</div>' +
                  '<span class="oe-quiz-counter" data-oe-counter>' +
                    escapeHtml(COPY.answeredPrefix + ' 0/' + questions.length + COPY.answeredSuffix) +
                  '</span>' +
                '</div>' +
                '<div class="oe-quiz-progress-track"><div class="oe-quiz-progress-fill" data-oe-progress></div></div>' +
                '<div class="oe-quiz-body">' +
                  '<div class="oe-quiz-summary" data-oe-summary></div>' +
                  qCardsHtml +
                  '<div class="oe-quiz-warning" data-oe-warning>⚠️ ' + escapeHtml(COPY.warnEmpty) + '</div>' +
                  '<div class="oe-quiz-footer">' +
                    '<div class="oe-quiz-footer-note" data-oe-footer-note>' +
                      escapeHtml(COPY.footerPartial.replace('{done}', '0').replace('{total}', String(questions.length))) +
                    '</div>' +
                    '<div class="oe-quiz-actions" data-oe-actions>' +
                      '<button type="button" class="oe-quiz-btn-primary" data-oe-submit>✅ ' + escapeHtml(COPY.submitBtn) + '</button>' +
                    '</div>' +
                  '</div>' +
                '</div>';

              // Quiz interactive state
              var selected = {};
              var submitted = false;

              var counterEl = shell.querySelector('[data-oe-counter]');
              var progressEl = shell.querySelector('[data-oe-progress]');
              var summaryEl = shell.querySelector('[data-oe-summary]');
              var warningEl = shell.querySelector('[data-oe-warning]');
              var footerNoteEl = shell.querySelector('[data-oe-footer-note]');
              var actionsEl = shell.querySelector('[data-oe-actions]');

              function syncHeaderState() {
                var done = Object.keys(selected).length;
                var total = questions.length;
                if (counterEl) {
                  counterEl.textContent = COPY.answeredPrefix + ' ' + done + '/' + total + COPY.answeredSuffix;
                }
                if (progressEl) {
                  progressEl.style.width = Math.round((done / total) * 100) + '%';
                }
                if (footerNoteEl && !submitted) {
                  var tmpl = done >= total ? COPY.footerAll : COPY.footerPartial;
                  footerNoteEl.textContent = tmpl
                    .replace(/\\{done\\}/g, String(done))
                    .replace(/\\{total\\}/g, String(total));
                }
              }

              function selectOption(qIdx, letter) {
                if (submitted) return;
                selected[qIdx] = letter;
                if (warningEl) warningEl.classList.remove('is-visible');
                var card = shell.querySelector('[data-qcard="' + qIdx + '"]');
                if (card) {
                  var opts = card.querySelectorAll('.oe-quiz-opt');
                  for (var i = 0; i < opts.length; i++) {
                    if (opts[i].getAttribute('data-letter') === letter) {
                      opts[i].classList.add('is-selected');
                    } else {
                      opts[i].classList.remove('is-selected');
                    }
                  }
                }
                syncHeaderState();
              }

              function gradeQuiz() {
                var done = Object.keys(selected).length;
                if (done === 0) {
                  if (warningEl) warningEl.classList.add('is-visible');
                  if (typeof reportHeight === 'function') setTimeout(reportHeight, 30);
                  return;
                }
                if (warningEl) warningEl.classList.remove('is-visible');
                submitted = true;

                var correctCount = 0;
                var chipsHtml = '';

                for (var i = 0; i < questions.length; i++) {
                  var q = questions[i];
                  var picked = selected[i] || '';
                  var isCorrect = picked !== '' && picked === q.correctLetter;
                  var isSkip = picked === '';
                  if (isCorrect) correctCount++;

                  var card = shell.querySelector('[data-qcard="' + i + '"]');
                  var statusEl = shell.querySelector('[data-qstatus="' + i + '"]');
                  var fbEl = shell.querySelector('[data-qfb="' + i + '"]');

                  if (card) {
                    card.classList.remove('is-correct', 'is-wrong', 'is-unanswered');
                    card.classList.add(isCorrect ? 'is-correct' : (isSkip ? 'is-unanswered' : 'is-wrong'));

                    var opts = card.querySelectorAll('.oe-quiz-opt');
                    for (var o = 0; o < opts.length; o++) {
                      var optEl = opts[o];
                      var optL = optEl.getAttribute('data-letter');
                      var tagEl = optEl.querySelector('.oe-quiz-opt-tag');
                      optEl.classList.remove('is-selected', 'is-opt-correct', 'is-opt-wrong', 'is-opt-dim');
                      optEl.classList.add('is-locked');
                      if (tagEl) {
                        tagEl.className = 'oe-quiz-opt-tag';
                        tagEl.textContent = '';
                      }

                      if (optL === q.correctLetter) {
                        optEl.classList.add('is-opt-correct');
                        if (tagEl) {
                          tagEl.className = 'oe-quiz-opt-tag is-correct-tag';
                          tagEl.textContent = COPY.tagCorrect;
                        }
                      } else if (optL === picked) {
                        optEl.classList.add('is-opt-wrong');
                        if (tagEl) {
                          tagEl.className = 'oe-quiz-opt-tag is-wrong-tag';
                          tagEl.textContent = COPY.tagWrong;
                        }
                      } else {
                        optEl.classList.add('is-opt-dim');
                      }
                    }
                  }

                  if (statusEl) {
                    statusEl.className = 'oe-quiz-qstatus ' + (isCorrect ? 'is-ok' : (isSkip ? 'is-skip' : 'is-bad'));
                    statusEl.textContent = isCorrect ? COPY.statusCorrect : (isSkip ? COPY.statusSkip : COPY.statusWrong);
                  }

                  if (fbEl) {
                    fbEl.className = 'oe-quiz-fb ' + (isCorrect ? 'is-ok' : (isSkip ? 'is-skip' : 'is-bad'));
                    var lead = (isCorrect ? COPY.fbCorrect : (isSkip ? COPY.fbSkip : COPY.fbWrong))
                      .replace('{letter}', q.correctLetter);
                    var jumpHtml = (!isCorrect && hasTranscript)
                      ? '<button type="button" class="oe-quiz-transcript-link" data-oe-open-transcript>💬 ' + escapeHtml(COPY.transcriptJump) + '</button>'
                      : '';
                    fbEl.innerHTML =
                      '<div class="oe-quiz-fb-row">' +
                        '<div><strong>' + escapeHtml(lead) + '</strong> ' + escapeHtml(q.correctText) + '</div>' +
                        jumpHtml +
                      '</div>';
                  }

                  var chipCls = isCorrect ? 'is-ok' : (isSkip ? 'is-skip' : 'is-bad');
                  var chipLabel = isCorrect ? COPY.chipOk : ('✗ (' + q.correctLetter + ')');
                  chipsHtml += '<button type="button" class="oe-quiz-chip ' + chipCls + '" data-oe-jump="' + i + '">' +
                    escapeHtml(COPY.qPrefix + (i + 1) + ': ' + chipLabel) +
                  '</button>';
                }

                var pct = Math.round((correctCount / questions.length) * 100);
                var tierCls = pct >= 80 ? 'is-high' : (pct >= 50 ? 'is-mid' : 'is-low');
                var icon = pct >= 80 ? '🏆' : (pct >= 50 ? '🎯' : '💪');
                var msg = pct === 100 ? COPY.msg100 : (pct >= 80 ? COPY.msgHigh : (pct >= 50 ? COPY.msgMid : COPY.msgLow));
                var scoreText = COPY.scoreLine
                  .replace('{correct}', String(correctCount))
                  .replace('{total}', String(questions.length))
                  .replace('{pct}', String(pct));

                if (summaryEl) {
                  summaryEl.className = 'oe-quiz-summary is-visible ' + tierCls;
                  summaryEl.innerHTML =
                    '<div class="oe-quiz-summary-left">' +
                      '<div class="oe-quiz-summary-score"><span>' + icon + '</span><span>' + escapeHtml(scoreText) + '</span></div>' +
                      '<div class="oe-quiz-summary-msg">' + escapeHtml(msg) + '</div>' +
                      '<div class="oe-quiz-summary-chips">' + chipsHtml + '</div>' +
                    '</div>' +
                    '<button type="button" class="oe-quiz-btn-secondary" data-oe-retry>🔄 ' + escapeHtml(COPY.retryBtn) + '</button>';
                }

                if (footerNoteEl) {
                  footerNoteEl.textContent = scoreText;
                }
                if (actionsEl) {
                  actionsEl.innerHTML =
                    (hasTranscript ? '<button type="button" class="oe-quiz-btn-secondary" data-oe-toggle-transcript>💬 ' + escapeHtml(COPY.transcriptBtn) + '</button>' : '') +
                    '<button type="button" class="oe-quiz-btn-primary" data-oe-retry>🔄 ' + escapeHtml(COPY.retryBtn) + '</button>';
                }

                if (typeof reportHeight === 'function') {
                  setTimeout(reportHeight, 40);
                  setTimeout(reportHeight, 220);
                }
                try { shell.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {}
              }

              function resetQuiz() {
                selected = {};
                submitted = false;
                if (warningEl) warningEl.classList.remove('is-visible');
                if (summaryEl) {
                  summaryEl.className = 'oe-quiz-summary';
                  summaryEl.innerHTML = '';
                }

                for (var i = 0; i < questions.length; i++) {
                  var card = shell.querySelector('[data-qcard="' + i + '"]');
                  var statusEl = shell.querySelector('[data-qstatus="' + i + '"]');
                  var fbEl = shell.querySelector('[data-qfb="' + i + '"]');
                  if (card) {
                    card.classList.remove('is-correct', 'is-wrong', 'is-unanswered');
                    var opts = card.querySelectorAll('.oe-quiz-opt');
                    for (var o = 0; o < opts.length; o++) {
                      opts[o].className = 'oe-quiz-opt';
                      var tagEl = opts[o].querySelector('.oe-quiz-opt-tag');
                      if (tagEl) {
                        tagEl.className = 'oe-quiz-opt-tag';
                        tagEl.textContent = '';
                      }
                    }
                  }
                  if (statusEl) {
                    statusEl.className = 'oe-quiz-qstatus';
                    statusEl.textContent = '';
                  }
                  if (fbEl) {
                    fbEl.className = 'oe-quiz-fb';
                    fbEl.innerHTML = '';
                  }
                }

                if (actionsEl) {
                  actionsEl.innerHTML = '<button type="button" class="oe-quiz-btn-primary" data-oe-submit>✅ ' + escapeHtml(COPY.submitBtn) + '</button>';
                }
                syncHeaderState();

                if (typeof reportHeight === 'function') {
                  setTimeout(reportHeight, 40);
                  setTimeout(reportHeight, 200);
                }
                try { shell.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {}
              }

              // Event delegation on the quiz shell
              shell.addEventListener('click', function(e) {
                var t = e.target;
                if (!t || typeof t.closest !== 'function') return;

                var opt = t.closest('.oe-quiz-opt');
                if (opt && !submitted) {
                  var qIdx = parseInt(opt.getAttribute('data-qidx'), 10);
                  var letter = opt.getAttribute('data-letter');
                  if (!isNaN(qIdx) && letter) selectOption(qIdx, letter);
                  return;
                }

                if (t.closest('[data-oe-submit]')) {
                  e.preventDefault();
                  gradeQuiz();
                  return;
                }

                if (t.closest('[data-oe-retry]')) {
                  e.preventDefault();
                  resetQuiz();
                  return;
                }

                if (t.closest('[data-oe-open-transcript]')) {
                  e.preventDefault();
                  openTranscriptSection(root, false);
                  return;
                }

                if (t.closest('[data-oe-toggle-transcript]')) {
                  e.preventDefault();
                  openTranscriptSection(root, true);
                  return;
                }

                var jumpChip = t.closest('[data-oe-jump]');
                if (jumpChip) {
                  e.preventDefault();
                  var targetCard = shell.querySelector('[data-qcard="' + jumpChip.getAttribute('data-oe-jump') + '"]');
                  if (targetCard) {
                    try { targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' }); } catch (err) {}
                  }
                  return;
                }
              });

              shell.addEventListener('keydown', function(e) {
                if (e.key !== 'Enter' && e.key !== ' ') return;
                var opt = e.target && e.target.closest ? e.target.closest('.oe-quiz-opt') : null;
                if (opt && !submitted) {
                  e.preventDefault();
                  var qIdx = parseInt(opt.getAttribute('data-qidx'), 10);
                  var letter = opt.getAttribute('data-letter');
                  if (!isNaN(qIdx) && letter) selectOption(qIdx, letter);
                }
              });

              // Swap legacy Questions Section card cleanly in-place
              if (quizCard.parentNode) {
                quizCard.parentNode.replaceChild(shell, quizCard);
              }

              // Softly update step 2 tip copy ("Xem Đáp Án" -> "Nộp bài & Chấm điểm") if present
              var strongs = (root || document).querySelectorAll('strong');
              for (var s = 0; s < strongs.length; s++) {
                if (cleanText(strongs[s].textContent) === 'Xem Đáp Án') {
                  strongs[s].textContent = COPY.submitBtn;
                }
              }

              if (typeof reportHeight === 'function') {
                setTimeout(reportHeight, 40);
                setTimeout(reportHeight, 220);
              }
            }

            function runUpgrade() {
              var root = document.getElementById('content-wrapper') || document.body;
              if (!root) return;
              var radios = root.querySelectorAll('input[type="radio"]');
              if (!radios.length) return;

              var processedCards = [];
              for (var i = 0; i < radios.length; i++) {
                var r = radios[i];
                if (r.closest && r.closest('[data-mcq-enhanced="1"]')) continue;

                // Walk up to find the card containing both radios and the legacy Answer Key button/box
                var cur = r.parentElement;
                var matchedCard = null;
                var matchedBtn = null;
                var matchedBox = null;

                while (cur && cur !== root && cur !== document.body) {
                  if (cur.querySelector('audio')) break;
                  var btns = cur.querySelectorAll('button');
                  for (var b = 0; b < btns.length; b++) {
                    var bt = cleanText(btns[b].textContent);
                    var sib = btns[b].nextElementSibling;
                    if (
                      sib &&
                      /kiểm tra|xem đáp án|view answer|ẩn đáp án/i.test(bt) &&
                      /đáp án chính xác|answer key/i.test(sib.textContent || '')
                    ) {
                      matchedCard = cur;
                      matchedBtn = btns[b];
                      matchedBox = sib;
                      break;
                    }
                  }
                  if (matchedCard) break;
                  cur = cur.parentElement;
                }

                if (matchedCard && processedCards.indexOf(matchedCard) === -1) {
                  // If matchedCard is the inner body wrapper, promote one level to the full Questions card (with header) if its parent has no audio/transcript
                  var parent = matchedCard.parentElement;
                  if (
                    parent &&
                    parent !== root &&
                    parent !== document.body &&
                    !parent.querySelector('audio') &&
                    /câu hỏi nghe hiểu|listening questions/i.test(parent.textContent || '') &&
                    !/lời thoại bài nghe|audio transcript/i.test(parent.textContent || '')
                  ) {
                    matchedCard = parent;
                  }
                  processedCards.push(matchedCard);
                  upgradeQuizCard(matchedCard, matchedBtn, matchedBox, root);
                }
              }
            }

            runUpgrade();
            if (document.readyState === 'loading') {
              document.addEventListener('DOMContentLoaded', runUpgrade);
            }
            setTimeout(runUpgrade, 80);
          })();
  `;
}
