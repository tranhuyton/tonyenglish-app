import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
import * as XLSX from 'xlsx';
import TestEditorModal from './TestEditorModal';

export default function AdminPanel({ onBack }: { onBack: () => void }) {
  const [dbTests, setDbTests] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [editingTest, setEditingTest] = useState<any>(null);
  
  const [testId, setTestId] = useState('');
  const [title, setTitle] = useState('');
  const [timeLimit, setTimeLimit] = useState('60:00 phút');
  const [examCategory, setExamCategory] = useState<'ielts' | 'standard'>('ielts');
  const [skill, setSkill] = useState<'reading' | 'listening'>('reading');
  const [parsedParts, setParsedParts] = useState<any[]>([]);
  const [totalQ, setTotalQ] = useState(0);
  
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => { fetchTestsFromCloud(); }, []);

  const fetchTestsFromCloud = async () => {
    const { data } = await supabase.from('mock_tests').select('*').order('created_at', { ascending: false });
    if (data) setDbTests(data);
  };

  const handleExcelUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setIsLoading(true);
    const reader = new FileReader();
    reader.onload = (evt) => {
      try {
        const data = new Uint8Array(evt.target?.result as ArrayBuffer);
        const workbook = XLSX.read(data, { type: 'array' });
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const rawJson: any[] = XLSX.utils.sheet_to_json(worksheet);
        if (rawJson.length === 0) throw new Error("File trống!");

        const partsMap = new Map();
        let questionCount = 0;

        rawJson.forEach((row, index) => {
          const partName = row['Part'] || 'Part 1';
          const groupTitle = row['Group Title'] || 'Questions';
          const qType = row['Type']?.toString().toUpperCase() || 'MCQ';

          if (!partsMap.has(partName)) {
            partsMap.set(partName, {
              id: `part_${Date.now()}_${index}`,
              title: partName,
              passageTitle: row['Passage Title'] || '',
              passageContent: row['Passage HTML'] || '',
              audioUrl: row['Audio URL'] || '', 
              imageUrl: row['Image URL'] || '', 
              questionGroups: []
            });
          }

          const currentPart = partsMap.get(partName);
          let group = currentPart.questionGroups.find((g: any) => g.title === groupTitle);
          if (!group) {
            group = { type: qType, title: groupTitle, instruction: row['Instruction'] || '', questions: [] };
            currentPart.questionGroups.push(group);
          }

          questionCount++;
          group.questions.push({
            id: String(row['ID'] || questionCount),
            text: qType !== 'GAP_FILL' ? (row['Question Text'] || '') : '',
            options: [row['A'], row['B'], row['C'], row['D']].filter(Boolean).map((opt, i) => `${String.fromCharCode(65 + i)}. ${opt}`),
            correctAnswer: String(row['Correct Answer'] || '').trim(),
            imageUrl: ''
          });
        });

        setParsedParts(Array.from(partsMap.values()));
        setTotalQ(questionCount);
        alert(`✅ Đã phân tích ${questionCount} câu hỏi!`);
      } catch (error: any) { alert("Lỗi: " + error.message); } 
      finally { setIsLoading(false); }
    };
    reader.readAsArrayBuffer(file);
  };

  const handlePublish = async () => {
    if (!testId || !title) return alert("⚠️ Nhập đầy đủ thông tin!");
    setIsLoading(true);
    const finalTestData = { testId, title, examCategory, skill, timeLimit, totalQuestions: totalQ, parts: parsedParts };
    const { error } = await supabase.from('mock_tests').insert([{ test_id: testId, title, type: examCategory, test_data: finalTestData }]);
    if (error) alert("Lỗi: " + error.message);
    else { alert("🚀 Thành công!"); fetchTestsFromCloud(); }
    setIsLoading(false);
  };

  const handleDelete = async (id: string, testData: any) => {
    if(!window.confirm("Xóa vĩnh viễn?")) return;
    setIsLoading(true);
    try {
      const files: string[] = [];
      testData?.parts?.forEach((p: any) => {
        if (p.audioUrl?.includes('test_assets/')) files.push(p.audioUrl.split('test_assets/').pop()!);
        if (p.imageUrl?.includes('test_assets/')) files.push(p.imageUrl.split('test_assets/').pop()!);
        p.questionGroups?.forEach((g: any) => g.questions?.forEach((q: any) => {
          if (q.imageUrl?.includes('test_assets/')) files.push(q.imageUrl.split('test_assets/').pop()!);
        }));
      });
      if (files.length > 0) await supabase.storage.from('test_assets').remove(files);
      await supabase.from('mock_tests').delete().eq('id', id);
      fetchTestsFromCloud();
    } finally { setIsLoading(false); }
  };

  return (
    <div className="min-h-screen bg-slate-900 p-8 font-sans text-slate-200">
      {editingTest && <TestEditorModal testRecord={editingTest} onClose={() => setEditingTest(null)} onRefresh={fetchTestsFromCloud} />}
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8 border-b border-slate-700 pb-4">
          <h1 className="text-2xl font-bold">⚡ LMS Admin</h1>
          <button onClick={onBack} className="bg-slate-700 px-4 py-2 rounded font-bold">⬅ Thoát</button>
        </div>

        <div className="grid lg:grid-cols-2 gap-8">
          <div className="space-y-6">
            <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-xl">
              <h2 className="text-lg font-bold text-blue-400 mb-4">1. Thông tin đề thi</h2>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <input value={testId} onChange={e => setTestId(e.target.value)} className="bg-slate-900 border border-slate-600 rounded px-3 py-2" placeholder="Mã đề" />
                <input value={title} onChange={e => setTitle(e.target.value)} className="bg-slate-900 border border-slate-600 rounded px-3 py-2" placeholder="Tên hiển thị" />
              </div>
              <div className="flex gap-4 mb-4">
                <button onClick={() => setExamCategory('ielts')} className={`flex-1 p-2 rounded border ${examCategory === 'ielts' ? 'bg-blue-600' : ''}`}>IELTS</button>
                <button onClick={() => setExamCategory('standard')} className={`flex-1 p-2 rounded border ${examCategory === 'standard' ? 'bg-purple-600' : ''}`}>Standard</button>
              </div>
              <div className="flex gap-4 mb-4">
                <button onClick={() => setSkill('reading')} className={`flex-1 p-2 rounded border ${skill === 'reading' ? 'bg-emerald-600' : ''}`}>Reading</button>
                <button onClick={() => setSkill('listening')} className={`flex-1 p-2 rounded border ${skill === 'listening' ? 'bg-amber-600' : ''}`}>Listening</button>
              </div>
              <input type="file" onChange={handleExcelUpload} className="w-full bg-slate-900 p-4 border-2 border-dashed border-slate-600 rounded mb-4" />
              <button onClick={handlePublish} className="w-full bg-blue-600 py-3 rounded-xl font-bold">🚀 XUẤT BẢN</button>
            </div>
          </div>

          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-xl overflow-y-auto max-h-[600px]">
            <h2 className="text-lg font-bold text-amber-400 mb-4">Kho đề & Chỉnh sửa</h2>
            <div className="space-y-3">
              {dbTests.map(test => {
                let parsed = test.test_data;
                if (typeof parsed === 'string') try { parsed = JSON.parse(parsed); } catch (e) {}
                const cat = parsed?.examCategory || 'ielts';
                const sk = parsed?.skill || 'reading';
                return (
                  <div key={test.id} className="bg-slate-900 p-4 rounded border border-slate-700">
                    <div className="flex gap-2 mb-2">
                      <span className="text-[10px] uppercase font-bold bg-blue-900/50 text-blue-300 px-2 py-0.5 rounded">{cat}</span>
                      <span className="text-[10px] uppercase font-bold bg-emerald-900/50 text-emerald-300 px-2 py-0.5 rounded">{sk}</span>
                    </div>
                    <h3 className="font-bold text-sm mb-3">{test.title}</h3>
                    <div className="flex gap-2">
                      <button onClick={() => setEditingTest(test)} className="flex-1 bg-blue-900/30 text-blue-400 py-1.5 rounded border border-blue-800 font-bold text-xs">✏️ SỬA ĐỀ</button>
                      <button onClick={() => handleDelete(test.id, parsed)} className="bg-red-900/30 text-red-400 px-3 py-1.5 rounded border border-red-800 font-bold text-xs">XÓA</button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}