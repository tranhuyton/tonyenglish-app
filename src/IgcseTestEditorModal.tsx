import React, { useState, useEffect, useRef } from 'react';
import { supabase } from './supabase';

interface IgcseTestEditorProps {
    isOpen: boolean;
    onClose: () => void;
    courseId: string;
    moduleId?: string;
    existingTestId?: string | null;
    onSaveSuccess: () => void;
}

export default function IgcseTestEditorModal({ 
    isOpen, 
    onClose, 
    courseId, 
    moduleId, 
    existingTestId, 
    onSaveSuccess 
}: IgcseTestEditorProps) {
    const [title, setTitle] = useState('');
    const [testType, setTestType] = useState('IGCSE-Science');
    const [timeLimit, setTimeLimit] = useState<number>(120);
    const [category, setCategory] = useState('test');
    const [pdfUrl, setPdfUrl] = useState('');
    
    const [questions, setQuestions] = useState<any[]>([]);
    const [isSaving, setIsSaving] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    
    const [editMode, setEditMode] = useState<'visual' | 'json'>('visual');
    const [rawJson, setRawJson] = useState('');
    const [isUploadingPdf, setIsUploadingPdf] = useState(false);
    const pdfInputRef = useRef<HTMLInputElement>(null);
    const [courses, setCourses] = useState<any[]>([]);
    const [selectedCourseId, setSelectedCourseId] = useState(courseId || 'all');

    // Upload PDF to Supabase storage and return public URL
    const uploadPdfFile = async (file: File) => {
        if (!file.type.includes('pdf')) { alert('⚠️ Chỉ hỗ trợ file PDF!'); return; }
        if (file.size > 50 * 1024 * 1024) { alert('⚠️ File quá lớn (tối đa 50MB)!'); return; }
        setIsUploadingPdf(true);
        try {
            const fileName = `igcse_${Date.now()}_${file.name.replace(/\s+/g, '_')}`;
            const { error } = await supabase.storage.from('test_assets').upload(fileName, file, { cacheControl: '3600', upsert: false });
            if (error) throw error;
            const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(fileName);
            if (urlData?.publicUrl) {
                setPdfUrl(urlData.publicUrl);
            }
        } catch (err: any) {
            alert('❌ Lỗi upload: ' + err.message);
        } finally {
            setIsUploadingPdf(false);
            if (pdfInputRef.current) pdfInputRef.current.value = '';
        }
    };

    // Handle paste: file or text URL
    const handlePdfPaste = (e: React.ClipboardEvent) => {
        const items = e.clipboardData?.items;
        if (items) {
            for (let i = 0; i < items.length; i++) {
                if (items[i].type === 'application/pdf' || items[i].kind === 'file') {
                    const file = items[i].getAsFile();
                    if (file && file.type.includes('pdf')) {
                        e.preventDefault();
                        uploadPdfFile(file);
                        return;
                    }
                }
            }
        }
        // If no file found, let default paste behavior handle text URL
    };

    useEffect(() => {
        if (isOpen) {
            supabase.from('courses').select('id, title').order('order_index').then(({ data }) => setCourses(data || []));
            if (existingTestId) {
                fetchTestDetails(existingTestId);
            } else {
                resetForm();
                setSelectedCourseId(courseId || 'all');
            }
        }
    }, [isOpen, existingTestId]);

    const resetForm = () => {
        setTitle('');
        setTestType('IGCSE-Science');
        setTimeLimit(120);
        setCategory('test');
        setPdfUrl('');
        setQuestions([]);
        setRawJson('[\n  {\n    "question_number": "1",\n    "sub_questions": []\n  }\n]');
    };

    const fetchTestDetails = async (id: string) => {
        setIsLoading(true);
        try {
            const { data, error } = await supabase.from('tests').select('*').eq('id', id).single();
            if (error) throw error;
            if (data) {
                setTitle(data.title || '');
                setTestType(data.test_type || 'IGCSE-Science');
                setTimeLimit(data.time_limit || data.json_config?.timeLimit || 120);
                setCategory(data.content_json?.basicInfo?.category || 'test');
                setPdfUrl(data.insert_pdf_url || '');
                setSelectedCourseId(data.course_id || data.content_json?.basicInfo?.courseId || 'all');
                
                const loadedQuestions = data.json_config?.questions || [];
                setQuestions(loadedQuestions);
                setRawJson(JSON.stringify(loadedQuestions, null, 2));
            }
        } catch (err) {
            alert("Không thể tải thông tin đề thi.");
        } finally {
            setIsLoading(false);
        }
    };

    // Question management
    const addQuestion = () => setQuestions(prev => [...prev, { question_number: `${prev.length + 1}`, sub_questions: [] }]);
    const removeQuestion = (qIndex: number) => setQuestions(prev => prev.filter((_, i) => i !== qIndex));
    const updateQuestionNumber = (qIndex: number, value: string) => {
        const newQs = [...questions];
        newQs[qIndex].question_number = value;
        setQuestions(newQs);
    };

    // Sub-question management
    const addSubQuestion = (qIndex: number) => {
        const newQs = [...questions];
        const subCount = newQs[qIndex].sub_questions.length;
        const labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)'];
        const label = subCount < labels.length ? `${labels[subCount]} ` : `(${String.fromCharCode(97 + subCount)}) `;
        const subId = `q${newQs[qIndex].question_number}_${String.fromCharCode(97 + subCount)}`;
        newQs[qIndex].sub_questions.push({
            id: subId, label: label, type: "short_answer", max_marks: 1, marking_scheme: ""
        });
        setQuestions(newQs);
    };

    const updateSubQuestion = (qIndex: number, sqIndex: number, field: string, value: any) => {
        const newQs = [...questions];
        newQs[qIndex].sub_questions[sqIndex][field] = value;
        setQuestions(newQs);
    };

    const removeSubQuestion = (qIndex: number, sqIndex: number) => {
        const newQs = [...questions];
        newQs[qIndex].sub_questions = newQs[qIndex].sub_questions.filter((_:any, i:number) => i !== sqIndex);
        setQuestions(newQs);
    };

    // Total marks calculation
    const totalMarks = questions.reduce((sum, q) => 
        sum + (q.sub_questions || []).reduce((s: number, sq: any) => s + (sq.max_marks || 0), 0), 0
    );
    const totalSubQuestions = questions.reduce((sum, q) => sum + (q.sub_questions?.length || 0), 0);

    // Save handler
    const handleSave = async () => {
        if (!title.trim()) { alert("Vui lòng nhập tên đề thi!"); return; }
        setIsSaving(true);
        try {
            let finalQuestions = questions;
            if (editMode === 'json') {
                try { finalQuestions = JSON.parse(rawJson); } 
                catch (e) { alert("Cấu trúc JSON bị lỗi! Kiểm tra lại."); setIsSaving(false); return; }
            }

            // Validate question IDs are unique
            const allIds = finalQuestions.flatMap((q: any) => (q.sub_questions || []).map((sq: any) => sq.id));
            const uniqueIds = new Set(allIds);
            if (allIds.length !== uniqueIds.size) {
                alert("⚠️ Có ID câu hỏi bị trùng! Kiểm tra lại."); setIsSaving(false); return;
            }

            const jsonConfig = { timeLimit: timeLimit, questions: finalQuestions };
            const contentJson = {
                basicInfo: {
                    title,
                    skill: testType,
                    timeLimit: String(timeLimit),
                    courseId: selectedCourseId || 'all',
                    insert_pdf_url: pdfUrl || '',
                    category: category,
                },
                questions: finalQuestions,
            };
            const assignedCourseId = selectedCourseId && selectedCourseId !== 'all' ? selectedCourseId : null;
            const payload: any = {
                title, 
                test_type: testType, 
                insert_pdf_url: pdfUrl || null, 
                content_json: contentJson,
                json_config: jsonConfig, 
                course_id: assignedCourseId,
                is_published: true,
            };
            if (moduleId) payload.module_id = moduleId;

            if (existingTestId) { 
                const { error } = await supabase.from('tests').update(payload).eq('id', existingTestId); 
                if (error) throw error;
            } else { 
                const { error } = await supabase.from('tests').insert([payload]); 
                if (error) throw error;
            }

            onSaveSuccess();
            onClose();
        } catch (err: any) { alert("Lỗi lưu đề thi: " + err.message); } 
        finally { setIsSaving(false); }
    };

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-[100000] bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in duration-200">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-5xl max-h-[90vh] flex flex-col overflow-hidden ring-1 ring-slate-900/10">
                {/* Header */}
                <div className="px-6 py-4 border-b border-slate-200 bg-slate-50 flex items-center justify-between shrink-0">
                    <div>
                        <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
                            🔬 {existingTestId ? 'Chỉnh sửa Đề thi IGCSE' : 'Tạo Đề thi IGCSE Mới'}
                        </h2>
                        <p className="text-xs text-slate-500 mt-1">Hệ thống Split-Screen cho Cambridge IGCSE Science / Math</p>
                    </div>
                    <button onClick={onClose} className="text-slate-400 hover:text-red-500 w-8 h-8 flex items-center justify-center rounded-full hover:bg-red-50 transition-colors">✕</button>
                </div>

                {isLoading ? (
                    <div className="flex-1 flex items-center justify-center py-20"><div className="w-8 h-8 border-4 border-[#0ea5e9]/30 border-t-[#0ea5e9] rounded-full animate-spin"></div></div>
                ) : (
                    <div className="flex-1 overflow-y-auto p-6 bg-slate-50/50 custom-scrollbar">
                        {/* Basic Info */}
                        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm mb-6 grid grid-cols-1 md:grid-cols-2 gap-5">
                            <div className="col-span-1 md:col-span-2">
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">Tên bài thi <span className="text-red-500">*</span></label>
                                <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Ví dụ: 0654/21 May/June 2024 Paper 2" className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9] focus:ring-1 focus:ring-[#0ea5e9]/20 transition-all"/>
                            </div>
                            <div>
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">Loại bài thi</label>
                                <select value={testType} onChange={(e) => setTestType(e.target.value)} className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9]">
                                    <option value="IGCSE-Science">IGCSE Science (Split Screen)</option>
                                    <option value="IGCSE-Math">IGCSE Math (Split Screen)</option>
                                    <option value="IGCSE-Direct">IGCSE Direct (Draw on PDF)</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">Phân loại</label>
                                <select value={category} onChange={(e) => setCategory(e.target.value)} className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9]">
                                    <option value="test">Đề thi</option>
                                    <option value="exercise">Bài tập</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">Thời gian làm bài (Phút)</label>
                                <input type="number" value={timeLimit} onChange={(e) => setTimeLimit(parseInt(e.target.value) || 0)} className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9]"/>
                            </div>
                            <div className="col-span-1 md:col-span-2">
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">Thuộc Khóa học</label>
                                <select value={selectedCourseId} onChange={(e) => setSelectedCourseId(e.target.value)} className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9]">
                                    <option value="all">-- Dùng chung (không gán khóa học) --</option>
                                    {courses.map(c => <option key={c.id} value={c.id}>{c.title}</option>)}
                                </select>
                            </div>
                            <div className="col-span-1 md:col-span-2">
                                <label className="block text-sm font-bold text-slate-700 mb-1.5">File PDF Đề bài (nửa trái màn hình) 📄</label>
                                <div className="flex gap-2">
                                    <div className="flex-1 relative">
                                        <input 
                                            type="text" 
                                            value={pdfUrl} 
                                            onChange={(e) => setPdfUrl(e.target.value)} 
                                            onPaste={handlePdfPaste}
                                            placeholder="Paste URL hoặc Ctrl+V file PDF..." 
                                            className="w-full px-4 py-2 bg-slate-50 border border-slate-300 rounded-lg outline-none focus:border-[#0ea5e9] font-mono text-sm pr-10"
                                        />
                                        {pdfUrl && (
                                            <button onClick={() => setPdfUrl('')} className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-red-500 text-sm" title="Xóa link">✕</button>
                                        )}
                                    </div>
                                    <input type="file" ref={pdfInputRef} accept="application/pdf" className="hidden" onChange={(e) => { if (e.target.files?.[0]) uploadPdfFile(e.target.files[0]); }} />
                                    <button 
                                        type="button" 
                                        onClick={() => pdfInputRef.current?.click()} 
                                        disabled={isUploadingPdf}
                                        className="px-4 py-2 bg-[#0ea5e9] text-white font-bold text-sm rounded-lg hover:bg-[#0284c7] transition-colors disabled:opacity-50 whitespace-nowrap flex items-center gap-1.5"
                                    >
                                        {isUploadingPdf ? (
                                            <><span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></span> Đang tải...</>
                                        ) : (
                                            <>📤 Upload PDF</>
                                        )}
                                    </button>
                                </div>
                                {pdfUrl && (
                                    <div className="mt-2 flex items-center gap-2">
                                        <span className="text-emerald-600 text-xs font-bold">✅ Đã có PDF</span>
                                        <a href={pdfUrl} target="_blank" rel="noopener noreferrer" className="text-xs text-[#0ea5e9] hover:underline truncate max-w-[400px]">{pdfUrl}</a>
                                    </div>
                                )}
                            </div>
                        </div>

                        {/* Stats bar */}
                        <div className="flex gap-4 mb-4 text-sm">
                            <span className="bg-sky-100 text-sky-800 px-3 py-1 rounded-full font-bold">{questions.length} câu lớn</span>
                            <span className="bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full font-bold">{totalSubQuestions} ý phụ</span>
                            <span className="bg-amber-100 text-amber-800 px-3 py-1 rounded-full font-bold">{totalMarks} điểm tổng</span>
                        </div>

                        {/* Question Editor */}
                        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                            <div className="flex border-b border-slate-200">
                                <button onClick={() => { setEditMode('visual'); if(rawJson) try { setQuestions(JSON.parse(rawJson)); } catch(e){} }} className={`flex-1 py-3 text-sm font-bold transition-colors ${editMode === 'visual' ? 'bg-[#0ea5e9] text-white' : 'bg-slate-100 text-slate-500 hover:bg-slate-200'}`}>🎨 Visual Builder</button>
                                <button onClick={() => { setEditMode('json'); setRawJson(JSON.stringify(questions, null, 2)); }} className={`flex-1 py-3 text-sm font-bold transition-colors ${editMode === 'json' ? 'bg-[#0ea5e9] text-white' : 'bg-slate-100 text-slate-500 hover:bg-slate-200'}`}>{`{ }`} Raw JSON</button>
                            </div>

                            <div className="p-5">
                                {editMode === 'json' ? (
                                    <textarea value={rawJson} onChange={(e) => setRawJson(e.target.value)} className="w-full h-[400px] p-4 bg-slate-900 text-emerald-400 font-mono text-sm rounded-lg outline-none focus:ring-2 focus:ring-[#0ea5e9] resize-y" spellCheck={false} placeholder="Paste JSON cấu trúc câu hỏi vào đây..."/>
                                ) : (
                                    <div className="space-y-6">
                                        {questions.length === 0 ? (
                                            <div className="text-center py-10 border-2 border-dashed border-slate-300 rounded-xl">
                                                <p className="text-slate-400 mb-4">Chưa có câu hỏi nào</p>
                                                <button onClick={addQuestion} className="bg-slate-800 text-white px-4 py-2 rounded-lg text-sm font-bold hover:bg-slate-700 transition-colors">+ Thêm Câu Hỏi Lớn</button>
                                            </div>
                                        ) : (
                                            <>
                                                {questions.map((q, qIndex) => (
                                                    <div key={qIndex} className="border border-slate-300 rounded-xl p-4 bg-slate-50 relative">
                                                        <button onClick={() => removeQuestion(qIndex)} className="absolute top-4 right-4 text-slate-400 hover:text-red-500 transition-colors" title="Xóa câu hỏi">✕</button>
                                                        <div className="flex items-center gap-3 mb-4">
                                                            <span className="font-bold text-slate-800">Câu hỏi số:</span>
                                                            <input type="text" value={q.question_number} onChange={(e) => updateQuestionNumber(qIndex, e.target.value)} className="w-20 px-2 py-1 border border-slate-300 rounded outline-none focus:border-[#0ea5e9] text-center font-bold"/>
                                                        </div>

                                                        <div className="space-y-3 pl-4 border-l-2 border-[#0ea5e9]/30">
                                                            {(q.sub_questions || []).map((sq: any, sqIndex: number) => (
                                                                <div key={sq.id || sqIndex} className="bg-white border border-slate-200 p-4 rounded-lg shadow-sm relative group">
                                                                    <button onClick={() => removeSubQuestion(qIndex, sqIndex)} className="absolute top-2 right-2 text-slate-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-opacity">✕</button>
                                                                    <div className="grid grid-cols-1 md:grid-cols-12 gap-4">
                                                                        <div className="md:col-span-4">
                                                                            <label className="block text-xs font-bold text-slate-500 mb-1">Đề bài (Label)</label>
                                                                            <textarea value={sq.label} onChange={(e) => updateSubQuestion(qIndex, sqIndex, 'label', e.target.value)} className="w-full px-3 py-2 bg-slate-50 border border-slate-300 rounded outline-none focus:border-[#0ea5e9] text-sm h-[80px] resize-y"/>
                                                                        </div>
                                                                        <div className="md:col-span-8 space-y-4">
                                                                            <div className="flex gap-4">
                                                                                <div className="flex-1">
                                                                                    <label className="block text-xs font-bold text-slate-500 mb-1">Loại ô nhập</label>
                                                                                    <select value={sq.type} onChange={(e) => updateSubQuestion(qIndex, sqIndex, 'type', e.target.value)} className="w-full px-3 py-1.5 bg-slate-50 border border-slate-300 rounded outline-none focus:border-[#0ea5e9] text-sm">
                                                                                        <option value="short_answer">Short Answer (1 dòng)</option>
                                                                                        <option value="long_answer">Long Answer (Nhiều dòng)</option>
                                                                                        <option value="image_upload">📸 Image Upload (Chụp ảnh bản vẽ/Đồ thị)</option>
                                                                                    </select>
                                                                                </div>
                                                                                <div className="w-24">
                                                                                    <label className="block text-xs font-bold text-slate-500 mb-1">Điểm</label>
                                                                                    <input type="number" value={sq.max_marks} onChange={(e) => updateSubQuestion(qIndex, sqIndex, 'max_marks', parseInt(e.target.value)||0)} className="w-full px-3 py-1.5 bg-slate-50 border border-slate-300 rounded outline-none text-sm font-bold text-center"/>
                                                                                </div>
                                                                            </div>
                                                                            <div>
                                                                                <label className="block text-xs font-bold text-emerald-600 mb-1">🎯 Marking Scheme (Đáp án chuẩn)</label>
                                                                                <textarea value={sq.marking_scheme} onChange={(e) => updateSubQuestion(qIndex, sqIndex, 'marking_scheme', e.target.value)} className="w-full px-3 py-2 bg-emerald-50 border border-emerald-200 rounded outline-none focus:border-emerald-500 text-sm h-[60px] resize-y" placeholder={sq.type === 'image_upload' ? "Mô tả hình vẽ chuẩn: đồ thị phải đi qua gốc O, dốc dương..." : "Ghi đáp án chuẩn theo Cambridge MS..."}/>
                                                                            </div>
                                                                            <div>
                                                                                <label className="block text-xs font-bold text-slate-400 mb-1">ID (tự động)</label>
                                                                                <input type="text" value={sq.id} onChange={(e) => updateSubQuestion(qIndex, sqIndex, 'id', e.target.value)} className="w-full px-3 py-1.5 bg-slate-100 border border-slate-200 rounded text-xs font-mono text-slate-500"/>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            ))}
                                                            <button onClick={() => addSubQuestion(qIndex)} className="text-[#0ea5e9] font-bold text-sm hover:underline mt-2">+ Thêm ý phụ</button>
                                                        </div>
                                                    </div>
                                                ))}
                                                <button onClick={addQuestion} className="w-full py-3 border-2 border-dashed border-slate-300 text-slate-500 font-bold rounded-xl hover:border-[#0ea5e9] hover:text-[#0ea5e9] transition-colors">+ Thêm Câu Hỏi Lớn</button>
                                            </>
                                        )}
                                    </div>
                                )}
                            </div>
                        </div>
                    </div>
                )}

                {/* Footer */}
                <div className="px-6 py-4 border-t border-slate-200 bg-white flex justify-between items-center shrink-0">
                    <span className="text-xs text-slate-400">{totalSubQuestions} ý • {totalMarks} điểm</span>
                    <div className="flex gap-3">
                        <button onClick={onClose} className="px-6 py-2 rounded-lg font-bold text-slate-600 hover:bg-slate-100 transition-colors">Hủy</button>
                        <button onClick={handleSave} disabled={isSaving || isLoading} className="px-8 py-2 rounded-lg font-bold bg-[#0ea5e9] text-white hover:bg-[#0284c7] disabled:opacity-50 transition-colors">
                            {isSaving ? 'Đang lưu...' : '💾 Lưu Đề Thi'}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}
