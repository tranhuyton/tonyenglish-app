import React, { useState } from 'react';

interface BatchEntry {
  id: string;
  title: string;
  codeBlock: string;
  status?: 'idle' | 'processing' | 'success' | 'error';
  message?: string;
  questionCount?: number;
}

interface Props {
  courses: any[];
  supabase: any;
  onClose: () => void;
  onSuccess: () => void;
}

// Parse pipe-delimited code block into content_json parts structure
function parseCodeBlock(text: string) {
  const lines = text.trim().split('\n').filter(l => l.trim());
  if (lines.length === 0) throw new Error('Code block rỗng');

  // Detect and skip header line
  let startIdx = 0;
  const firstLower = lines[0].toLowerCase();
  if (firstLower.includes('part title') || firstLower.includes('question type') || firstLower.includes('section title')) {
    startIdx = 1;
  }

  const parts: any[] = [];
  let currentPart: any = null;
  let currentSection: any = null;
  let importCount = 0;

  for (let i = startIdx; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    
    const cols = line.split('|').map(c => c.trim());
    // Need at least 20 columns (ID=0..19 for Answer, 20 for Explanation optional)
    if (cols.length < 20) continue;

    const partTitle = cols[0] || '';
    const partContent = (cols[1] || '').replace(/\\n/g, '<br>');
    const secTitle = cols[2] || '';
    const secContent = (cols[3] || '').replace(/\\n/g, '<br>');
    const qTypeRaw = (cols[4] || '').trim();
    const qId = (cols[5] || '').trim();
    const qContent = (cols[6] || '').replace(/\\n/g, '<br>');
    
    const optCols = [];
    for (let c = 7; c <= 18; c++) optCols.push((cols[c] || '').trim());
    const [optA, optB, optC, optD, optE, optF, optG, optH, optI, optJ, optK, optL] = optCols;
    
    const answer = (cols[19] || '').trim();
    const explanation = (cols[20] || '').replace(/\\n/g, '<br>');

    // Map question type
    let qType = 'Trắc nghiệm';
    const upper = qTypeRaw.toUpperCase();
    if (upper.includes('TFNG') || upper.includes('TRUE')) {
      qType = 'TFNG';
    } else if (upper.includes('CHECKBOX') || upper.includes('COMBO') || upper.includes('NHIỀU ĐÁP ÁN')) {
      qType = 'Checkbox';
    } else if (upper.includes('KÉO THẢ') || upper.includes('MATCHING') || upper.includes('DRAG')) {
      qType = 'Kéo thả';
    } else if (upper.includes('DROPLIST') || upper.includes('NỐI')) {
      qType = 'Droplist';
    } else if (upper.includes('ĐIỀN') || upper.includes('FILL') || upper.includes('TỰ LUẬN') || upper.includes('UPLOAD')) {
      qType = 'Điền từ';
    } else if (upper.includes('TRẮC NGHIỆM') || upper.includes('MULTIPLE')) {
      qType = 'Trắc nghiệm';
    } else if (qTypeRaw && currentSection) {
      qType = currentSection.questionType; // inherit from previous
    }

    // Handle Part
    if (partTitle && (!currentPart || currentPart.title !== partTitle)) {
      currentPart = {
        id: Date.now().toString() + Math.random(),
        title: partTitle,
        content: partContent,
        tags: '', audioUrl: '', explanation: '',
        sections: []
      };
      parts.push(currentPart);
      currentSection = null;
    } else if (partContent && currentPart && !currentPart.content) {
      currentPart.content = partContent;
    }

    // Ensure a part exists
    if (!currentPart) {
      currentPart = {
        id: Date.now().toString() + Math.random(),
        title: 'Paper 1', content: '', tags: '', audioUrl: '', explanation: '',
        sections: []
      };
      parts.push(currentPart);
    }

    // Handle Section
    if (secTitle && (!currentSection || currentSection.title !== secTitle)) {
      currentSection = {
        id: Date.now().toString() + Math.random(),
        title: secTitle,
        content: secContent,
        tags: '', questionType: qType, audioUrl: '', explanation: '',
        questions: []
      };
      currentPart.sections.push(currentSection);
    } else if (!currentSection) {
      currentSection = {
        id: Date.now().toString() + Math.random(),
        title: secTitle || 'Section 1',
        content: secContent,
        tags: '', questionType: qType, audioUrl: '', explanation: '',
        questions: []
      };
      currentPart.sections.push(currentSection);
    } else if (secContent && !currentSection.content) {
      currentSection.content = secContent;
    }

    // Build options array
    const options: string[] = [];
    [optA, optB, optC, optD, optE, optF, optG, optH, optI, optJ, optK, optL].forEach(o => { if (o) options.push(o); });

    // Determine if real question
    const isRealQuestion = (qId !== '' && qId !== '0') || answer !== '';
    if (isRealQuestion && currentSection) {
      let finalOptions = options;
      if (options.length === 0) {
        if (qType === 'TFNG') finalOptions = ['TRUE', 'FALSE', 'NOT GIVEN'];
        else if (qType === 'Trắc nghiệm') finalOptions = ['A', 'B', 'C', 'D'];
      }

      // Handle Checkbox with comma-separated answers
      if (qType === 'Checkbox' && answer.includes(',')) {
        const ansArr = answer.split(',').map(x => x.trim()).filter(Boolean);
        const baseMatch = qId.match(/\d+/);
        const baseId = baseMatch ? parseInt(baseMatch[0]) : null;
        
        ansArr.forEach((ans, idx) => {
          let cid = qId;
          if (baseId !== null) cid = String(baseId + idx);
          else if (idx > 0) cid = qId + `_${idx}`;
          
          currentSection.questions.push({
            id: cid,
            content: idx === 0 ? qContent : '',
            tags: '', audioUrl: '',
            explanation: idx === 0 ? explanation : '',
            options: idx === 0 ? finalOptions : [],
            correctAnswer: ans
          });
          importCount++;
        });
      } else {
        currentSection.questions.push({
          id: qId || String(importCount + 1),
          content: qContent,
          tags: '', audioUrl: '',
          explanation: explanation,
          options: finalOptions,
          correctAnswer: answer
        });
        importCount++;
      }
    }
  }

  if (importCount === 0) throw new Error('Không tìm thấy câu hỏi hợp lệ nào');
  return { parts, importCount };
}

export default function BatchImportModal({ courses, supabase, onClose, onSuccess }: Props) {
  const [entries, setEntries] = useState<BatchEntry[]>([
    { id: '1', title: '', codeBlock: '' }
  ]);
  const [courseId, setCourseId] = useState('all');
  const [category, setCategory] = useState('exercise');
  const [skill, setSkill] = useState('Standard-Listening');
  const [timeLimit, setTimeLimit] = useState('40');
  const [isProcessing, setIsProcessing] = useState(false);
  const [isDone, setIsDone] = useState(false);

  const addEntry = () => {
    setEntries(prev => [...prev, { id: Date.now().toString(), title: '', codeBlock: '' }]);
  };

  const removeEntry = (id: string) => {
    if (entries.length <= 1) return;
    setEntries(prev => prev.filter(e => e.id !== id));
  };

  const updateEntry = (id: string, field: 'title' | 'codeBlock', value: string) => {
    setEntries(prev => prev.map(e => e.id === id ? { ...e, [field]: value } : e));
  };

  const handleCreateAll = async () => {
    const validEntries = entries.filter(e => e.title.trim() && e.codeBlock.trim());
    if (validEntries.length === 0) {
      alert('Vui lòng nhập ít nhất 1 đề có Tên và Code Block!');
      return;
    }

    setIsProcessing(true);

    const updatedEntries = [...entries];
    let successCount = 0;

    for (let i = 0; i < updatedEntries.length; i++) {
      const entry = updatedEntries[i];
      if (!entry.title.trim() || !entry.codeBlock.trim()) continue;

      updatedEntries[i] = { ...entry, status: 'processing', message: 'Đang xử lý...' };
      setEntries([...updatedEntries]);

      try {
        const { parts, importCount } = parseCodeBlock(entry.codeBlock);

        const contentJson = {
          basicInfo: {
            title: entry.title.trim(),
            courseId: courseId,
            skill: skill,
            category: category,
            timeLimit: timeLimit,
          },
          parts
        };

        const payload: any = {
          title: entry.title.trim(),
          test_type: skill,
          content_json: contentJson,
          course_id: courseId === 'all' ? null : courseId,
          is_published: false,
          time_limit: parseInt(timeLimit) || 40,
          category: category,
        };

        const { error } = await supabase.from('tests').insert(payload);
        if (error) throw error;

        updatedEntries[i] = {
          ...entry, status: 'success',
          message: `✅ Thành công — ${importCount} câu hỏi`,
          questionCount: importCount
        };
        successCount++;
      } catch (err: any) {
        updatedEntries[i] = {
          ...entry, status: 'error',
          message: `❌ Lỗi: ${err.message || 'Unknown error'}`
        };
      }
      setEntries([...updatedEntries]);
    }

    setIsProcessing(false);
    setIsDone(true);

    if (successCount > 0) {
      onSuccess(); // refresh library
    }
  };

  const totalValid = entries.filter(e => e.title.trim() && e.codeBlock.trim()).length;
  const totalSuccess = entries.filter(e => e.status === 'success').length;

  return (
    <div className="fixed inset-0 bg-black/60 z-[60] flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-[#f0f2f5] rounded-2xl shadow-2xl w-full max-w-[1000px] max-h-[90vh] flex flex-col overflow-hidden">
        
        {/* Header */}
        <div className="bg-white px-6 py-4 border-b border-slate-200 flex justify-between items-center shrink-0">
          <div className="flex items-center gap-3">
            <span className="text-2xl">⚡</span>
            <div>
              <h2 className="font-black text-[16px] text-slate-800 uppercase tracking-tight">Batch Import — Tạo hàng loạt</h2>
              <p className="text-[12px] text-slate-400 font-medium">Paste code block từ Gemini, tạo nhiều đề cùng lúc</p>
            </div>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-700 text-2xl font-bold transition">✕</button>
        </div>

        {/* Settings Bar */}
        <div className="bg-white px-6 py-3 border-b border-slate-200 shrink-0">
          <div className="flex flex-wrap gap-3 items-end">
            <div className="flex-1 min-w-[180px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase tracking-wide">Khóa học</label>
              <select value={courseId} onChange={e => setCourseId(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb]">
                <option value="all">📦 Dùng chung (không gán khóa)</option>
                {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
              </select>
            </div>
            <div className="min-w-[150px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase tracking-wide">Dạng đề</label>
              <select value={skill} onChange={e => setSkill(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb]">
                <option value="Standard-Listening">MCQ (Standard)</option>
                <option value="Standard-Reading">SplitScreen (Standard)</option>
                <option value="IELTS-Listening">Listening (IELTS)</option>
                <option value="IELTS-Reading">Reading (IELTS)</option>
              </select>
            </div>
            <div className="min-w-[140px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase tracking-wide">Phân loại</label>
              <select value={category} onChange={e => setCategory(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb]">
                <option value="exercise">Bài tập (Exercise)</option>
                <option value="test">Đề thi (Test)</option>
              </select>
            </div>
            <div className="w-[80px]">
              <label className="text-[11px] font-bold text-slate-500 block mb-1 uppercase tracking-wide">Phút</label>
              <input type="number" value={timeLimit} onChange={e => setTimeLimit(e.target.value)} className="w-full px-3 py-2 border border-slate-200 rounded-lg text-[13px] font-bold text-slate-700 outline-none bg-white focus:border-[#2bd6eb] text-center" />
            </div>
          </div>
        </div>

        {/* Entries List */}
        <div className="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-4">
          {entries.map((entry, idx) => (
            <div 
              key={entry.id}
              className={`bg-white rounded-xl border-2 shadow-sm overflow-hidden transition-all ${
                entry.status === 'success' ? 'border-emerald-300 bg-emerald-50/30' :
                entry.status === 'error' ? 'border-red-300 bg-red-50/30' :
                entry.status === 'processing' ? 'border-blue-300 bg-blue-50/30 animate-pulse' :
                'border-slate-200 hover:border-[#2bd6eb]'
              }`}
            >
              {/* Entry header */}
              <div className="px-5 py-3 border-b border-slate-100 flex items-center gap-3">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center text-[13px] font-black shrink-0 ${
                  entry.status === 'success' ? 'bg-emerald-100 text-emerald-600' :
                  entry.status === 'error' ? 'bg-red-100 text-red-600' :
                  'bg-slate-100 text-slate-500'
                }`}>
                  {entry.status === 'success' ? '✓' : entry.status === 'error' ? '!' : idx + 1}
                </div>
                <input
                  value={entry.title}
                  onChange={e => updateEntry(entry.id, 'title', e.target.value)}
                  placeholder={`Nhập tên đề #${idx + 1}... (VD: 2.1 Elements PP2)`}
                  className="flex-1 font-bold text-[14px] text-slate-800 outline-none bg-transparent placeholder:text-slate-300"
                  disabled={isProcessing || isDone}
                />
                {entries.length > 1 && !isProcessing && !isDone && (
                  <button onClick={() => removeEntry(entry.id)} className="text-slate-300 hover:text-red-500 font-bold text-lg transition" title="Xóa đề này">✕</button>
                )}
              </div>

              {/* Status message */}
              {entry.status && entry.message && (
                <div className={`px-5 py-2 text-[12px] font-bold ${
                  entry.status === 'success' ? 'text-emerald-600 bg-emerald-50' :
                  entry.status === 'error' ? 'text-red-600 bg-red-50' :
                  'text-blue-600 bg-blue-50'
                }`}>
                  {entry.message}
                </div>
              )}

              {/* Code block textarea */}
              {(!entry.status || entry.status === 'idle') && (
                <div className="p-4">
                  <textarea
                    value={entry.codeBlock}
                    onChange={e => updateEntry(entry.id, 'codeBlock', e.target.value)}
                    placeholder="Paste code block từ Gemini vào đây...&#10;&#10;Part Title | Part Content | Section Title | ..."
                    className="w-full h-[140px] p-3 bg-slate-50 border border-slate-200 rounded-lg text-[12px] font-mono text-slate-700 outline-none focus:border-[#2bd6eb] resize-y transition placeholder:text-slate-300"
                    disabled={isProcessing || isDone}
                    spellCheck={false}
                  />
                  {entry.codeBlock.trim() && (
                    <div className="mt-2 flex items-center gap-2 text-[11px] text-slate-400 font-medium">
                      <span>📊 {entry.codeBlock.trim().split('\n').filter(l => l.trim()).length} dòng</span>
                      <span>•</span>
                      <span>{entry.codeBlock.trim().split('\n').filter(l => l.trim() && (l.split('|').length >= 20)).length} dòng hợp lệ (≥20 cột)</span>
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}

          {/* Add entry button */}
          {!isProcessing && !isDone && (
            <button
              onClick={addEntry}
              className="w-full border-2 border-dashed border-slate-300 hover:border-[#2bd6eb] hover:bg-white text-slate-400 hover:text-[#0a5482] py-4 rounded-xl font-bold text-[14px] transition flex items-center justify-center gap-2"
            >
              <span className="text-xl">+</span> Thêm đề mới
            </button>
          )}
        </div>

        {/* Footer */}
        <div className="bg-white px-6 py-4 border-t border-slate-200 flex justify-between items-center shrink-0">
          <div className="text-[13px] text-slate-500 font-medium">
            {isDone ? (
              <span className="text-emerald-600 font-bold">🎉 Hoàn tất! {totalSuccess}/{entries.filter(e => e.title.trim() && e.codeBlock.trim()).length} đề được tạo thành công</span>
            ) : (
              <span>{totalValid} đề sẵn sàng tạo</span>
            )}
          </div>
          <div className="flex gap-3">
            <button onClick={onClose} className="px-5 py-2.5 text-[13px] font-bold text-slate-500 hover:text-slate-700 transition">
              {isDone ? 'Đóng' : 'Hủy'}
            </button>
            {!isDone && (
              <button
                onClick={handleCreateAll}
                disabled={isProcessing || totalValid === 0}
                className="px-6 py-2.5 bg-[#00a651] hover:bg-[#008f45] text-white text-[13px] font-black rounded-xl shadow-md transition active:scale-95 disabled:opacity-50 disabled:hover:bg-[#00a651] flex items-center gap-2"
              >
                {isProcessing ? (
                  <><span className="animate-spin">⏳</span> Đang tạo...</>
                ) : (
                  <><span>🚀</span> Tạo {totalValid} đề</>
                )}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
