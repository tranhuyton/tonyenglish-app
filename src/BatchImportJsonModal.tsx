import React, { useState, useRef } from 'react';

interface SubQuestion {
  id: string;
  label: string;
  type: 'short_answer' | 'long_answer' | 'image_upload';
  max_marks: number;
  marking_scheme: string;
}

interface Question {
  question_number: string;
  sub_questions: SubQuestion[];
}

interface JsonBatchEntry {
  id: string;
  title: string;
  pdfFile: File | null;
  pdfUrl: string;
  jsonRaw: string;
  timeLimit: number;
  questions: Question[];
  viewMode: 'json' | 'visual';
  status?: 'idle' | 'uploading' | 'processing' | 'success' | 'error';
  message?: string;
}

interface Props {
  courses: any[];
  supabase: any;
  onClose: () => void;
  onSuccess: () => void;
}

function createEmptyEntry(): JsonBatchEntry {
  return {
    id: Date.now().toString() + Math.random(),
    title: '', pdfFile: null, pdfUrl: '', jsonRaw: '', timeLimit: 120,
    questions: [], viewMode: 'json',
  };
}

function generateSubQId(qNum: string, idx: number): string {
  const letters = 'abcdefghijklmnopqrstuvwxyz';
  return `q${qNum}_${letters[idx] || idx}`;
}

function questionsToJson(questions: Question[], timeLimit: number): string {
  const config = { timeLimit, questions };
  return JSON.stringify(config, null, 2);
}

function parseJsonToQuestions(raw: string): { questions: Question[]; timeLimit: number } {
  const obj = JSON.parse(raw);
  // Handle both formats: { questions: [...] } or just [...]
  const questionsArr = Array.isArray(obj) ? obj : (obj.questions || []);
  const tl = Array.isArray(obj) ? 120 : (obj.timeLimit || 120);
  const qs: Question[] = questionsArr.map((q: any) => ({
    question_number: q.question_number || '1',
    sub_questions: (q.sub_questions || []).map((sq: any) => ({
      id: sq.id || '',
      label: sq.label || '',
      type: sq.type || 'short_answer',
      max_marks: sq.max_marks || 1,
      marking_scheme: sq.marking_scheme || '',
    }))
  }));
  return { questions: qs, timeLimit: tl };
}

export default function BatchImportJsonModal({ courses, supabase, onClose, onSuccess }: Props) {
  const [entries, setEntries] = useState<JsonBatchEntry[]>([createEmptyEntry()]);
  const [courseId, setCourseId] = useState('all');
  const [testType, setTestType] = useState('IGCSE-Science');
  const [isProcessing, setIsProcessing] = useState(false);
  const [isDone, setIsDone] = useState(false);
  const fileInputRefs = useRef<Record<string, HTMLInputElement | null>>({});

  const addEntry = () => setEntries(prev => [...prev, createEmptyEntry()]);

  const removeEntry = (id: string) => {
    if (entries.length <= 1) return;
    setEntries(prev => prev.filter(e => e.id !== id));
  };

  const updateEntry = (id: string, patch: Partial<JsonBatchEntry>) => {
    setEntries(prev => prev.map(e => e.id === id ? { ...e, ...patch } : e));
  };

  // Sync JSON raw → visual questions
  const syncJsonToVisual = (id: string, raw: string) => {
    try {
      const { questions, timeLimit } = parseJsonToQuestions(raw);
      updateEntry(id, { jsonRaw: raw, questions, timeLimit });
    } catch {
      updateEntry(id, { jsonRaw: raw });
    }
  };

  // Sync visual → JSON raw
  const syncVisualToJson = (id: string, questions: Question[], timeLimit: number) => {
    const raw = questionsToJson(questions, timeLimit);
    updateEntry(id, { questions, timeLimit, jsonRaw: raw });
  };

  // Add question to entry
  const addQuestion = (entryId: string) => {
    const entry = entries.find(e => e.id === entryId);
    if (!entry) return;
    const nextNum = String((entry.questions.length || 0) + 1);
    const newQ: Question = {
      question_number: nextNum,
      sub_questions: [{
        id: `q${nextNum}_a`, label: `(a) `, type: 'short_answer', max_marks: 1, marking_scheme: ''
      }]
    };
    const updated = [...entry.questions, newQ];
    syncVisualToJson(entryId, updated, entry.timeLimit);
  };

  const removeQuestion = (entryId: string, qIdx: number) => {
    const entry = entries.find(e => e.id === entryId);
    if (!entry) return;
    const updated = entry.questions.filter((_, i) => i !== qIdx);
    syncVisualToJson(entryId, updated, entry.timeLimit);
  };

  const addSubQuestion = (entryId: string, qIdx: number) => {
    const entry = entries.find(e => e.id === entryId);
    if (!entry) return;
    const updated = [...entry.questions];
    const q = { ...updated[qIdx], sub_questions: [...updated[qIdx].sub_questions] };
    const nextIdx = q.sub_questions.length;
    q.sub_questions.push({
      id: generateSubQId(q.question_number, nextIdx),
      label: `(${String.fromCharCode(97 + nextIdx)}) `,
      type: 'short_answer', max_marks: 1, marking_scheme: ''
    });
    updated[qIdx] = q;
    syncVisualToJson(entryId, updated, entry.timeLimit);
  };

  const removeSubQuestion = (entryId: string, qIdx: number, sqIdx: number) => {
    const entry = entries.find(e => e.id === entryId);
    if (!entry) return;
    const updated = [...entry.questions];
    const q = { ...updated[qIdx], sub_questions: updated[qIdx].sub_questions.filter((_, i) => i !== sqIdx) };
    updated[qIdx] = q;
    syncVisualToJson(entryId, updated, entry.timeLimit);
  };

  const updateSubQuestion = (entryId: string, qIdx: number, sqIdx: number, patch: Partial<SubQuestion>) => {
    const entry = entries.find(e => e.id === entryId);
    if (!entry) return;
    const updated = [...entry.questions];
    const q = { ...updated[qIdx], sub_questions: [...updated[qIdx].sub_questions] };
    q.sub_questions[sqIdx] = { ...q.sub_questions[sqIdx], ...patch };
    updated[qIdx] = q;
    syncVisualToJson(entryId, updated, entry.timeLimit);
  };

  const handlePdfSelect = (entryId: string, file: File) => {
    updateEntry(entryId, { pdfFile: file, pdfUrl: file.name });
  };

  const uploadPdf = async (file: File): Promise<string> => {
    const ext = file.name.split('.').pop() || 'pdf';
    const fileName = `igcse_${Date.now()}_${Math.random().toString(36).substr(2, 6)}.${ext}`;
    const { error } = await supabase.storage.from('test_assets').upload(fileName, file, { contentType: file.type });
    if (error) throw new Error(`Upload PDF thất bại: ${error.message}`);
    const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(fileName);
    return urlData.publicUrl;
  };

  const handleCreateAll = async () => {
    const validEntries = entries.filter(e => e.title.trim() && (e.jsonRaw.trim() || e.questions.length > 0));
    if (validEntries.length === 0) {
      alert('Vui lòng nhập ít nhất 1 đề có Tên và JSON/Questions!');
      return;
    }

    setIsProcessing(true);
    const updatedEntries = [...entries];
    let successCount = 0;

    for (let i = 0; i < updatedEntries.length; i++) {
      const entry = updatedEntries[i];
      if (!entry.title.trim() || (!entry.jsonRaw.trim() && entry.questions.length === 0)) continue;

      // Upload PDF phase
      updatedEntries[i] = { ...entry, status: 'uploading', message: '📤 Đang upload PDF...' };
      setEntries([...updatedEntries]);

      try {
        let pdfUrl = entry.pdfUrl;
        
        // Upload PDF file if selected
        if (entry.pdfFile) {
          pdfUrl = await uploadPdf(entry.pdfFile);
        }

        updatedEntries[i] = { ...entry, status: 'processing', message: '⚙️ Đang tạo đề...' };
        setEntries([...updatedEntries]);

        // Parse json_config
        let jsonConfig: any;
        if (entry.jsonRaw.trim()) {
          jsonConfig = JSON.parse(entry.jsonRaw);
        } else {
          jsonConfig = { timeLimit: entry.timeLimit, questions: entry.questions };
        }

        // Count questions
        let totalQ = 0;
        (jsonConfig.questions || []).forEach((q: any) => {
          totalQ += (q.sub_questions || []).length || 1;
        });

        if (testType === 'Case-Study') {
          // Case Study: use handleSaveTestContent style
          const contentJson = {
            basicInfo: {
              title: entry.title.trim(),
              courseId: courseId,
              skill: 'Case-Study',
              category: 'test',
              mode: 'Đề thi',
              timeLimit: String(jsonConfig.timeLimit || 90),
              scoreType: 'IGCSE Grading',
              insert_pdf_url: pdfUrl || null,
            },
            json_config_string: JSON.stringify(jsonConfig),
          };

          const payload: any = {
            title: entry.title.trim(),
            test_type: 'Case-Study',
            content_json: contentJson,
            json_config: jsonConfig,
            course_id: courseId === 'all' ? null : courseId,
            is_published: false,
            insert_pdf_url: pdfUrl || null,
          };

          const { error } = await supabase.from('tests').insert(payload);
          if (error) throw error;
        } else {
          // IGCSE: direct insert
          const contentJson = {
            basicInfo: {
              title: entry.title.trim(),
              skill: testType,
              timeLimit: String(jsonConfig.timeLimit || 120),
              courseId: courseId,
              insert_pdf_url: pdfUrl || null,
              category: 'test',
            },
            questions: jsonConfig.questions || [],
          };

          const payload: any = {
            title: entry.title.trim(),
            test_type: testType,
            insert_pdf_url: pdfUrl || null,
            content_json: contentJson,
            json_config: jsonConfig,
            course_id: courseId === 'all' ? null : courseId,
            is_published: false,
          };

          const { error } = await supabase.from('tests').insert(payload);
          if (error) throw error;
        }

        updatedEntries[i] = {
          ...entry, status: 'success',
          message: `✅ Thành công — ${totalQ} câu hỏi` + (pdfUrl ? ' + PDF' : ''),
        };
        successCount++;
      } catch (err: any) {
        updatedEntries[i] = {
          ...entry, status: 'error',
          message: `❌ ${err.message || 'Unknown error'}`,
        };
      }
      setEntries([...updatedEntries]);
    }

    setIsProcessing(false);
    setIsDone(true);
    if (successCount > 0) onSuccess();
  };

  const totalValid = entries.filter(e => e.title.trim() && (e.jsonRaw.trim() || e.questions.length > 0)).length;
  const totalSuccess = entries.filter(e => e.status === 'success').length;

  return (
    <div className="fixed inset-0 bg-black/60 z-[60] flex items-center justify-center p-4">
      <div className="bg-[#f0f2f5] rounded-2xl shadow-2xl w-full max-w-[1100px] max-h-[92vh] flex flex-col overflow-hidden">

        {/* Header */}
        <div className="bg-white px-6 py-4 border-b border-slate-200 flex justify-between items-center shrink-0">
          <div className="flex items-center gap-3">
            <span className="text-2xl">🧪</span>
            <div>
              <h2 className="font-black text-[16px] text-slate-800 uppercase tracking-tight">Batch Import JSON — IGCSE / Case Study</h2>
              <p className="text-[12px] text-slate-400 font-medium">Upload PDF + Paste JSON hoặc xây dựng câu hỏi trực quan</p>
            </div>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-700 text-2xl font-bold transition">✕</button>
        </div>

        {/* Settings Bar */}
        <div className="bg-white px-6 py-3 border-b border-slate-200 shrink-0">
          <div className="flex flex-wrap gap-3 items-end">
            <div className="flex-1 min-w-[180px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase">Khóa học</label>
              <select value={courseId} onChange={e => setCourseId(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb]">
                <option value="all">📦 Dùng chung</option>
                {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
              </select>
            </div>
            <div className="min-w-[180px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase">Dạng đề</label>
              <select value={testType} onChange={e => setTestType(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb]">
                <option value="IGCSE-Science">🔬 IGCSE Science</option>
                <option value="IGCSE-Math">📐 IGCSE Math</option>
                <option value="IGCSE-Direct">📝 IGCSE Direct</option>
                <option value="Case-Study">💼 Case Study</option>
              </select>
            </div>
          </div>
        </div>

        {/* Entries */}
        <div className="flex-1 overflow-y-auto custom-scrollbar p-5 space-y-5">
          {entries.map((entry, idx) => (
            <div key={entry.id} className={`bg-white rounded-xl border-2 shadow-sm overflow-hidden transition-all ${
              entry.status === 'success' ? 'border-emerald-300' :
              entry.status === 'error' ? 'border-red-300' :
              entry.status === 'uploading' || entry.status === 'processing' ? 'border-blue-300 animate-pulse' :
              'border-slate-200 hover:border-[#2bd6eb]'
            }`}>

              {/* Entry Header */}
              <div className="px-5 py-3 border-b border-slate-100 flex items-center gap-3 bg-slate-50/50">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center text-[13px] font-black shrink-0 ${
                  entry.status === 'success' ? 'bg-emerald-100 text-emerald-600' :
                  entry.status === 'error' ? 'bg-red-100 text-red-600' :
                  'bg-slate-100 text-slate-500'
                }`}>
                  {entry.status === 'success' ? '✓' : entry.status === 'error' ? '!' : idx + 1}
                </div>
                <input
                  value={entry.title}
                  onChange={e => updateEntry(entry.id, { title: e.target.value })}
                  placeholder={`Tên đề #${idx + 1}... (VD: 0654/21 May/June 2024 Paper 2)`}
                  className="flex-1 font-bold text-[14px] text-slate-800 outline-none bg-transparent placeholder:text-slate-300"
                  disabled={isProcessing || isDone}
                />
                {entries.length > 1 && !isProcessing && !isDone && (
                  <button onClick={() => removeEntry(entry.id)} className="text-slate-300 hover:text-red-500 font-bold text-lg transition">✕</button>
                )}
              </div>

              {/* Status */}
              {entry.status && entry.message && (
                <div className={`px-5 py-2 text-[12px] font-bold ${
                  entry.status === 'success' ? 'text-emerald-600 bg-emerald-50' :
                  entry.status === 'error' ? 'text-red-600 bg-red-50' :
                  'text-blue-600 bg-blue-50'
                }`}>
                  {entry.message}
                </div>
              )}

              {/* Content area - only when not yet processed */}
              {(!entry.status || entry.status === 'idle') && (
                <div className="p-4 space-y-4">

                  {/* PDF Upload */}
                  <div>
                    <label className="text-[11px] font-bold text-slate-500 uppercase block mb-1.5">📄 PDF đề thi</label>
                    <div className="flex gap-2 items-center">
                      <input
                        ref={el => { fileInputRefs.current[entry.id] = el; }}
                        type="file" accept=".pdf" className="hidden"
                        onChange={e => { if (e.target.files?.[0]) handlePdfSelect(entry.id, e.target.files[0]); }}
                      />
                      <button
                        onClick={() => fileInputRefs.current[entry.id]?.click()}
                        className="px-4 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-[12px] font-bold text-slate-600 transition flex items-center gap-1.5"
                      >
                        📎 {entry.pdfFile ? entry.pdfFile.name : 'Chọn file PDF'}
                      </button>
                      <span className="text-[11px] text-slate-400">hoặc</span>
                      <div className="flex-1 flex gap-1">
                        <input
                          value={entry.pdfFile ? '' : entry.pdfUrl}
                          onChange={e => updateEntry(entry.id, { pdfUrl: e.target.value, pdfFile: null })}
                          placeholder="Paste URL PDF..."
                          className="flex-1 px-3 py-2 border border-slate-200 rounded-lg text-[12px] text-slate-600 outline-none focus:border-[#2bd6eb]"
                          disabled={!!entry.pdfFile}
                        />
                        <button
                          onClick={async () => {
                            try {
                              const text = await navigator.clipboard.readText();
                              if (text.trim()) updateEntry(entry.id, { pdfUrl: text.trim(), pdfFile: null });
                            } catch { alert('Không thể đọc clipboard. Vui lòng dùng Ctrl+V.'); }
                          }}
                          className="px-2.5 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-[12px] font-bold text-slate-500 transition shrink-0" title="Paste từ clipboard"
                        >📋</button>
                      </div>
                    </div>
                  </div>

                  {/* View mode tabs */}
                  <div className="flex gap-1 bg-slate-100 rounded-lg p-1 w-fit">
                    <button
                      onClick={() => updateEntry(entry.id, { viewMode: 'json' })}
                      className={`px-4 py-1.5 rounded-md text-[12px] font-bold transition ${entry.viewMode === 'json' ? 'bg-white text-slate-800 shadow-sm' : 'text-slate-500 hover:text-slate-700'}`}
                    >{`{ } JSON Raw`}</button>
                    <button
                      onClick={() => {
                        if (entry.viewMode === 'json' && entry.jsonRaw.trim()) {
                          // Combine parse + viewMode change in single update to avoid race condition
                          try {
                            const { questions, timeLimit } = parseJsonToQuestions(entry.jsonRaw);
                            updateEntry(entry.id, { viewMode: 'visual', questions, timeLimit });
                          } catch {
                            updateEntry(entry.id, { viewMode: 'visual' });
                          }
                        } else {
                          updateEntry(entry.id, { viewMode: 'visual' });
                        }
                      }}
                      className={`px-4 py-1.5 rounded-md text-[12px] font-bold transition ${entry.viewMode === 'visual' ? 'bg-white text-slate-800 shadow-sm' : 'text-slate-500 hover:text-slate-700'}`}
                    >🧩 Visual Builder</button>
                  </div>

                  {/* JSON Raw View */}
                  {entry.viewMode === 'json' && (
                    <div>
                      <textarea
                        value={entry.jsonRaw}
                        onChange={e => updateEntry(entry.id, { jsonRaw: e.target.value })}
                        placeholder={`Paste JSON vào đây...\n{\n  "timeLimit": 120,\n  "questions": [\n    {\n      "question_number": "1",\n      "sub_questions": [\n        { "id": "q1_a", "label": "(a)", "type": "short_answer", "max_marks": 1, "marking_scheme": "..." }\n      ]\n    }\n  ]\n}`}
                        className="w-full h-[200px] p-3 bg-slate-50 border border-slate-200 rounded-lg text-[12px] font-mono text-slate-700 outline-none focus:border-[#2bd6eb] resize-y placeholder:text-slate-300"
                        spellCheck={false}
                      />
                      {entry.jsonRaw.trim() && (() => {
                        try {
                          const parsed = JSON.parse(entry.jsonRaw);
                          const questionsArr = Array.isArray(parsed) ? parsed : (parsed.questions || []);
                          const qCount = questionsArr.reduce((acc: number, q: any) => acc + (q.sub_questions?.length || 1), 0);
                          return <p className="mt-1.5 text-[11px] text-emerald-500 font-bold">✅ JSON hợp lệ — {questionsArr.length} câu hỏi chính, {qCount} sub-questions</p>;
                        } catch (e: any) {
                          return <p className="mt-1.5 text-[11px] text-red-500 font-bold">❌ JSON không hợp lệ: {e.message}</p>;
                        }
                      })()}
                    </div>
                  )}

                  {/* Visual Builder View */}
                  {entry.viewMode === 'visual' && (
                    <div className="space-y-3">
                      {/* Time limit */}
                      <div className="flex items-center gap-2">
                        <label className="text-[11px] font-bold text-slate-500">⏱ Thời gian (phút):</label>
                        <input
                          type="number" value={entry.timeLimit}
                          onChange={e => syncVisualToJson(entry.id, entry.questions, parseInt(e.target.value) || 120)}
                          className="w-20 px-2 py-1 border border-slate-200 rounded-lg text-[12px] font-bold text-center outline-none focus:border-[#2bd6eb]"
                        />
                      </div>

                      {/* Questions */}
                      {entry.questions.map((q, qIdx) => (
                        <div key={qIdx} className="border border-slate-200 rounded-xl overflow-hidden">
                          {/* Question header */}
                          <div className="bg-slate-50 px-4 py-2.5 flex items-center justify-between border-b border-slate-200">
                            <div className="flex items-center gap-2">
                              <span className="font-black text-[13px] text-[#0a5482]">Q{q.question_number}</span>
                              <input
                                value={q.question_number}
                                onChange={e => {
                                  const updated = [...entry.questions];
                                  updated[qIdx] = { ...updated[qIdx], question_number: e.target.value };
                                  syncVisualToJson(entry.id, updated, entry.timeLimit);
                                }}
                                className="w-16 px-2 py-0.5 border border-slate-200 rounded text-[11px] font-bold text-center outline-none"
                                placeholder="Số"
                              />
                            </div>
                            <div className="flex gap-1">
                              <button onClick={() => addSubQuestion(entry.id, qIdx)} className="px-2.5 py-1 bg-[#2bd6eb]/10 text-[#0a5482] rounded-md text-[10px] font-bold hover:bg-[#2bd6eb]/20 transition">+ Sub Q</button>
                              <button onClick={() => removeQuestion(entry.id, qIdx)} className="px-2.5 py-1 bg-red-50 text-red-500 rounded-md text-[10px] font-bold hover:bg-red-100 transition">Xóa</button>
                            </div>
                          </div>

                          {/* Sub-questions */}
                          <div className="divide-y divide-slate-100">
                            {q.sub_questions.map((sq, sqIdx) => (
                              <div key={sqIdx} className="px-4 py-2.5 flex gap-2 items-start hover:bg-slate-50/50">
                                <input value={sq.label} onChange={e => updateSubQuestion(entry.id, qIdx, sqIdx, { label: e.target.value })}
                                  className="w-16 px-1.5 py-1 border border-slate-200 rounded text-[11px] font-bold outline-none shrink-0" placeholder="Label" />
                                <select value={sq.type} onChange={e => updateSubQuestion(entry.id, qIdx, sqIdx, { type: e.target.value as any })}
                                  className="px-2 py-1 border border-slate-200 rounded text-[11px] font-bold outline-none bg-white shrink-0">
                                  <option value="short_answer">Trả lời ngắn</option>
                                  <option value="long_answer">Trả lời dài</option>
                                  <option value="image_upload">Upload ảnh</option>
                                </select>
                                <input type="number" value={sq.max_marks} onChange={e => updateSubQuestion(entry.id, qIdx, sqIdx, { max_marks: parseInt(e.target.value) || 1 })}
                                  className="w-14 px-1.5 py-1 border border-slate-200 rounded text-[11px] font-bold text-center outline-none shrink-0" placeholder="Marks" />
                                <input value={sq.marking_scheme} onChange={e => updateSubQuestion(entry.id, qIdx, sqIdx, { marking_scheme: e.target.value })}
                                  className="flex-1 px-2 py-1 border border-slate-200 rounded text-[11px] outline-none" placeholder="Marking scheme / Đáp án..." />
                                {q.sub_questions.length > 1 && (
                                  <button onClick={() => removeSubQuestion(entry.id, qIdx, sqIdx)} className="text-slate-300 hover:text-red-500 text-sm font-bold transition shrink-0">✕</button>
                                )}
                              </div>
                            ))}
                          </div>
                        </div>
                      ))}

                      {entry.questions.length === 0 && (
                        <div className="text-center py-8 text-slate-400">
                          <p className="text-[32px] mb-2">📋</p>
                          <p className="text-[13px] font-bold">Chưa có câu hỏi nào</p>
                          <p className="text-[11px] mt-1">Paste JSON ở tab <strong>JSON Raw</strong> rồi chuyển sang đây để xem preview, hoặc bấm nút bên dưới để tạo câu hỏi mới.</p>
                        </div>
                      )}

                      <button onClick={() => addQuestion(entry.id)} className="w-full border border-dashed border-slate-300 hover:border-[#2bd6eb] py-2.5 rounded-lg text-[12px] font-bold text-slate-400 hover:text-[#0a5482] transition">+ Thêm câu hỏi</button>

                      {entry.questions.length > 0 && (
                        <p className="text-[11px] text-slate-400 font-medium">
                          📊 {entry.questions.length} câu chính, {entry.questions.reduce((a, q) => a + q.sub_questions.length, 0)} sub-questions
                        </p>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}

          {/* Add entry button */}
          {!isProcessing && !isDone && (
            <button onClick={addEntry} className="w-full border-2 border-dashed border-slate-300 hover:border-[#2bd6eb] hover:bg-white text-slate-400 hover:text-[#0a5482] py-4 rounded-xl font-bold text-[14px] transition flex items-center justify-center gap-2">
              <span className="text-xl">+</span> Thêm đề mới
            </button>
          )}
        </div>

        {/* Footer */}
        <div className="bg-white px-6 py-4 border-t border-slate-200 flex justify-between items-center shrink-0">
          <div className="text-[13px] text-slate-500 font-medium">
            {isDone ? (
              <span className="text-emerald-600 font-bold">🎉 Hoàn tất! {totalSuccess}/{entries.filter(e => e.title.trim()).length} đề thành công</span>
            ) : (
              <span>{totalValid} đề sẵn sàng</span>
            )}
          </div>
          <div className="flex gap-3">
            <button onClick={onClose} className="px-5 py-2.5 text-[13px] font-bold text-slate-500 hover:text-slate-700 transition">
              {isDone ? 'Đóng' : 'Hủy'}
            </button>
            {!isDone && (
              <button onClick={handleCreateAll} disabled={isProcessing || totalValid === 0}
                className="px-6 py-2.5 bg-[#00a651] hover:bg-[#008f45] text-white text-[13px] font-black rounded-xl shadow-md transition active:scale-95 disabled:opacity-50 flex items-center gap-2">
                {isProcessing ? <><span className="animate-spin">⏳</span> Đang tạo...</> : <><span>🚀</span> Tạo {totalValid} đề</>}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
