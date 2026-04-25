import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';
// Import thư viện đọc Excel vừa cài
import * as XLSX from 'xlsx';

export default function AdminPanel({ onBack }: { onBack: () => void }) {
  const [dbTests, setDbTests] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  
  // Các trường thông tin của bài test
  const [testId, setTestId] = useState('');
  const [title, setTitle] = useState('');
  const [timeLimit, setTimeLimit] = useState('60:00 phút');
  const [audioUrl, setAudioUrl] = useState('');
  const [questionsData, setQuestionsData] = useState<any[]>([]);
  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    fetchTestsFromCloud();
  }, []);

  const fetchTestsFromCloud = async () => {
    const { data, error } = await supabase.from('mock_tests').select('*').order('created_at', { ascending: false });
    if (data) setDbTests(data);
    if (error) console.error("Lỗi tải data:", error);
  };

  // HÀM MA THUẬT: ĐỌC FILE EXCEL VÀ TỰ ĐỘNG DỊCH SANG JSON
  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsLoading(true);
    const reader = new FileReader();
    
    reader.onload = async (evt) => {
      try {
        const data = new Uint8Array(evt.target?.result as ArrayBuffer);
        const workbook = XLSX.read(data, { type: 'array' });
        
        // Lấy dữ liệu từ Sheet đầu tiên của file Excel
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];
        
        // Chuyển đổi Excel thành mảng Object
        const rawJson: any[] = XLSX.utils.sheet_to_json(worksheet);

        if (rawJson.length === 0) throw new Error("File Excel trống!");

        // Vòng lặp: Chuyển đổi từng hàng Excel thành chuẩn dữ liệu hệ thống cần
        const formattedQuestions = rawJson.map((row: any, index: number) => {
          const options = [];
          
          // Gộp các đáp án lại. Nếu người dùng nhập thẳng "A. Hello" thì lấy luôn, nếu nhập "Hello" thì tự thêm "A. "
          if (row['A']) options.push(String(row['A']).startsWith('A.') ? row['A'] : `A. ${row['A']}`);
          if (row['B']) options.push(String(row['B']).startsWith('B.') ? row['B'] : `B. ${row['B']}`);
          if (row['C']) options.push(String(row['C']).startsWith('C.') ? row['C'] : `C. ${row['C']}`);
          if (row['D']) options.push(String(row['D']).startsWith('D.') ? row['D'] : `D. ${row['D']}`);

          let correct = String(row['Đáp án đúng'] || '').trim();
          
          // SỰ THÔNG MINH CỦA CODE: Nếu GV chỉ gõ chữ "A" vào cột Đáp án, hệ thống tự động tìm đoạn "A. ..." để khớp vào.
          if (correct.length === 1 && options.length > 0) {
            const found = options.find(o => o.toUpperCase().startsWith(correct.toUpperCase() + '.'));
            if (found) correct = found;
          }

          return {
            id: row['ID'] || index + 1,
            text: row['Câu hỏi'] || "",
            options: options, // Nếu file Excel không có cột ABCD (Dạng điền từ) thì mảng này sẽ tự động rỗng []
            correctAnswer: correct,
            explanation: row['Giải thích'] || ""
          };
        });

        setQuestionsData(formattedQuestions);
        alert(`✅ Xử lý thành công! Tìm thấy ${formattedQuestions.length} câu hỏi. Hãy bấm "XUẤT BẢN" để đẩy lên máy chủ.`);
      } catch (error: any) {
        alert("❌ Lỗi đọc file Excel. Vui lòng kiểm tra lại cấu trúc cột. Chi tiết: " + error.message);
      } finally {
        setIsLoading(false);
      }
    };
    reader.readAsArrayBuffer(file);
  };

  // HÀM ĐẨY ĐỀ LÊN ĐÁM MÂY SUPABASE
  const handlePublish = async () => {
    if (!testId || !title) return alert("⚠️ Vui lòng nhập Mã đề và Tên bài thi!");
    if (questionsData.length === 0) return alert("⚠️ Bạn chưa tải file Excel câu hỏi lên!");
    
    setIsLoading(true);
    
    // Gom dữ liệu Form và dữ liệu Excel thành 1 cục hoàn chỉnh
    const finalTestData = {
      testId: testId,
      title: title,
      type: 'paper',
      timeLimit: timeLimit,
      audioUrl: audioUrl,
      partName: "Nội dung bài thi:",
      instructions: ["Đề thi này được tạo tự động từ file Excel."],
      totalQuestions: questionsData.length,
      questions: questionsData
    };

    const { error } = await supabase.from('mock_tests').insert([{
      test_id: testId,
      title: title,
      type: 'paper',
      test_data: finalTestData
    }]);

    if (error) {
      alert("Lỗi tải lên Đám mây: " + error.message);
    } else {
      alert("🚀 Đã xuất bản lên Máy chủ Cloud thành công!");
      // Reset form cho sạch sẽ
      setTestId(''); setTitle(''); setAudioUrl(''); setQuestionsData([]);
      if (fileInputRef.current) fileInputRef.current.value = '';
      fetchTestsFromCloud();
    }
    setIsLoading(false);
  };

  const handleDelete = async (id: string) => {
    if(window.confirm("Xóa vĩnh viễn đề thi này khỏi Máy chủ?")) {
      await supabase.from('mock_tests').delete().eq('id', id);
      fetchTestsFromCloud();
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 p-8 font-sans text-slate-200">
      <div className="max-w-6xl mx-auto">
        <div className="flex justify-between items-center mb-8 border-b border-slate-700 pb-4">
          <h1 className="text-2xl font-bold text-white flex items-center gap-3">
            <span className="text-emerald-400">📊</span> Quản trị Đề thi (Upload bằng Excel)
          </h1>
          <button onClick={onBack} className="bg-slate-700 hover:bg-slate-600 px-4 py-2 rounded text-sm font-bold text-white transition">
            ⬅ Thoát về Trang chủ
          </button>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* CỘT TRÁI: FORM UPLOAD */}
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-xl flex flex-col gap-4 h-fit">
            <h2 className="text-lg font-bold text-blue-400 mb-2 border-b border-slate-700 pb-2">1. Thông tin chung</h2>
            
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-400 mb-1">Mã đề thi (VD: test_01)</label>
                <input value={testId} onChange={e => setTestId(e.target.value)} className="w-full bg-slate-900 border border-slate-600 rounded px-3 py-2 text-white focus:border-blue-500 outline-none text-sm" placeholder="Mã đề viết liền không dấu" />
              </div>
              <div>
                <label className="block text-xs font-bold text-slate-400 mb-1">Thời gian làm bài</label>
                <input value={timeLimit} onChange={e => setTimeLimit(e.target.value)} className="w-full bg-slate-900 border border-slate-600 rounded px-3 py-2 text-white focus:border-blue-500 outline-none text-sm" placeholder="VD: 60:00 phút" />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-400 mb-1">Tên bài thi hiển thị</label>
              <input value={title} onChange={e => setTitle(e.target.value)} className="w-full bg-slate-900 border border-slate-600 rounded px-3 py-2 text-white focus:border-blue-500 outline-none text-sm" placeholder="VD: Đề thi IELTS Tháng 10" />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-400 mb-1">Link Audio (Phần Listening - Tùy chọn)</label>
              <input value={audioUrl} onChange={e => setAudioUrl(e.target.value)} className="w-full bg-slate-900 border border-slate-600 rounded px-3 py-2 text-white focus:border-blue-500 outline-none text-sm" placeholder="Dán link file .mp3 vào đây" />
            </div>

            <h2 className="text-lg font-bold text-emerald-400 mt-4 border-b border-slate-700 pb-2">2. Upload Câu hỏi (File Excel)</h2>
            <div className="bg-slate-900 border-2 border-dashed border-slate-600 rounded-lg p-6 text-center hover:border-emerald-500 hover:bg-slate-800 transition relative">
              <input 
                type="file" 
                accept=".xlsx, .xls"
                onChange={handleFileUpload}
                ref={fileInputRef}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
              />
              <div className="text-4xl mb-2">📑</div>
              <p className="text-sm font-bold text-emerald-400 mb-1">Kéo thả hoặc Bấm vào đây để tải file Excel</p>
              <p className="text-xs text-slate-500">
                {questionsData.length > 0 ? <span className="text-emerald-400 font-bold">Đã tải lên sẵn sàng {questionsData.length} câu hỏi!</span> : "Chưa có file nào được chọn (.xlsx)"}
              </p>
            </div>

            <button 
              onClick={handlePublish} 
              disabled={isLoading || questionsData.length === 0}
              className={`w-full text-white font-bold py-3.5 rounded-lg mt-4 transition shadow-lg ${isLoading || questionsData.length === 0 ? 'bg-slate-600 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-500'}`}
            >
              {isLoading ? "⏳ Đang xử lý..." : "🚀 TẠO ĐỀ & ĐẨY LÊN CLOUD"}
            </button>

            <div className="mt-2 bg-slate-950 p-4 rounded border border-slate-800">
              <p className="text-[11px] text-emerald-400 font-bold mb-2">💡 QUY CÁCH FILE EXCEL (HÀNG SỐ 1):</p>
              <code className="text-[10px] text-slate-400 block break-all">
                ID | Câu hỏi | A | B | C | D | Đáp án đúng | Giải thích
              </code>
            </div>
          </div>

          {/* CỘT PHẢI: KHO MÁY CHỦ */}
          <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-xl flex flex-col h-fit">
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-lg font-bold text-emerald-400">3. Kho đề Máy chủ Supabase</h2>
              <span className="text-xs bg-emerald-900 text-emerald-300 px-2 py-1 rounded border border-emerald-700">Online</span>
            </div>
            
            <div className="space-y-3 flex-1 overflow-y-auto pr-2 custom-scrollbar" style={{ maxHeight: '600px' }}>
              {dbTests.length === 0 ? (
                <div className="text-slate-500 italic text-center py-10 border border-dashed border-slate-700 rounded">Kho Máy chủ trống.</div>
              ) : (
                dbTests.map((test) => (
                  <div key={test.id} className="bg-slate-900 border border-slate-700 p-4 rounded flex justify-between items-center hover:border-slate-500 transition">
                    <div className="overflow-hidden pr-4">
                      <h3 className="font-bold text-white text-sm truncate">{test.title}</h3>
                      <p className="text-xs text-slate-400 mt-1 truncate">Mã: {test.test_id}</p>
                    </div>
                    <button onClick={() => handleDelete(test.id)} className="bg-red-900/30 hover:bg-red-900 text-red-400 text-xs px-2.5 py-1.5 rounded border border-red-800 transition shrink-0">Xóa</button>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}