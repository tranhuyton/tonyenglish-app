import React, { useState, useMemo, useEffect } from 'react';
import { supabase } from './supabase';

export interface StudyCoachProps {
  courseId: string;
  courseTitle: string;
  studentName?: string;
  lectures?: any[];
  folders?: any[];
  onOpenLecture: (courseId: string, lectureId?: string) => void;
  onSelectFolder: (folderId: string) => void;
  onNavigate?: (view: string) => void;
  onOpenAIChat?: (initialPrompt?: string) => void;
}

interface CoachStep {
  stepNumber: number;
  title: string;
  description: string;
  tip?: string;
  actions: Array<{
    label: string;
    icon: string;
    variant?: 'primary' | 'secondary' | 'emerald' | 'amber' | 'purple';
    onClick: () => void;
  }>;
}

const cleanTitle = (raw: string) =>
  (raw || '')
    .replace(/\s*\[color:[^\]]*\]/gi, '')
    .replace(/\s*\[bg:[^\]]*\]/gi, '')
    .trim();

export const isCoachSupportedCourse = (courseId?: string | null, courseTitle?: string | null): boolean => {
  if (!courseId && !courseTitle) return false;
  const id = String(courseId || '').toLowerCase();
  const title = String(courseTitle || '').toLowerCase();
  return (
    id === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' ||
    id === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
    title.includes('ielts premium') ||
    title.includes('co-ordinated') ||
    title.includes('0654')
  );
};

export default function CourseStudyCoach({
  courseId,
  courseTitle,
  studentName = '',
  lectures = [],
  folders = [],
  onOpenLecture,
  onSelectFolder,
  onNavigate,
  onOpenAIChat,
}: StudyCoachProps) {
  const [fetchedFolders, setFetchedFolders] = useState<any[]>([]);
  const [fetchedLectures, setFetchedLectures] = useState<any[]>([]);

  useEffect(() => {
    if (!courseId) return;
    if (!Array.isArray(folders) || folders.length === 0) {
      supabase
        .from('folders')
        .select('id, title, parent_id, course_id')
        .eq('course_id', courseId)
        .then(({ data }) => {
          if (data) setFetchedFolders(data);
        });
    }
    if (!Array.isArray(lectures) || lectures.length === 0) {
      supabase
        .from('lectures')
        .select('id, title, module_id, course_id, order_index')
        .eq('course_id', courseId)
        .eq('is_published', true)
        .then(({ data }) => {
          if (data) setFetchedLectures(data);
        });
    }
  }, [courseId, folders?.length, lectures?.length]);

  const effectiveFolders = useMemo(
    () => (Array.isArray(folders) && folders.length > 0 ? folders : fetchedFolders),
    [folders, fetchedFolders]
  );

  const effectiveLectures = useMemo(
    () => (Array.isArray(lectures) && lectures.length > 0 ? lectures : fetchedLectures),
    [lectures, fetchedLectures]
  );
  const isIelts = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return courseId === '239a64f0-c106-40e5-a6e2-4e685a0d70fb' || t.includes('ielts');
  }, [courseId, courseTitle]);

  const isIgcse0654 = useMemo(() => {
    const t = (courseTitle || '').toLowerCase();
    return (
      courseId === 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7' ||
      t.includes('co-ordinated') ||
      t.includes('0654')
    );
  }, [courseId, courseTitle]);

  const [isCollapsed, setIsCollapsed] = useState(false);

  // IELTS states
  const [selectedIeltsSkill, setSelectedIeltsSkill] = useState<
    'listening' | 'reading' | 'writing' | 'speaking' | 'vocab' | null
  >(null);
  const [selectedWritingTask, setSelectedWritingTask] = useState<'task1' | 'task2'>('task2');

  // IGCSE 0654 states
  const [selectedScienceBranch, setSelectedScienceBranch] = useState<
    'biology' | 'chemistry' | 'physics' | 'pastpapers' | null
  >(null);
  const [selectedTopicCode, setSelectedTopicCode] = useState<string>('');

  // Completed step checkboxes persisted in sessionStorage per course
  const [checkedSteps, setCheckedSteps] = useState<Record<string, boolean>>(() => {
    try {
      const saved = sessionStorage.getItem(`tony_coach_checked_${courseId}`);
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  useEffect(() => {
    setSelectedIeltsSkill(null);
    setSelectedScienceBranch(null);
    setSelectedTopicCode('');
  }, [courseId]);

  const toggleStepCheck = (stepKey: string) => {
    setCheckedSteps((prev) => {
      const next = { ...prev, [stepKey]: !prev[stepKey] };
      try {
        sessionStorage.setItem(`tony_coach_checked_${courseId}`, JSON.stringify(next));
      } catch {}
      return next;
    });
  };

  // Helpers to find specific lectures & folders dynamically
  const findLectureByKeyword = (keywords: string[]): any | null => {
    const safeLectures = Array.isArray(effectiveLectures) ? effectiveLectures : [];
    for (const kw of keywords) {
      const lowerKw = kw.toLowerCase();
      const found = safeLectures.find((l) => cleanTitle(l?.title || '').toLowerCase().includes(lowerKw));
      if (found) return found;
    }
    return null;
  };

  const findFolderByKeyword = (keywords: string[], parentId?: string | null): any | null => {
    const safeFolders = Array.isArray(effectiveFolders) ? effectiveFolders : [];
    for (const kw of keywords) {
      const lowerKw = kw.toLowerCase();
      const found = safeFolders.find((f) => {
        if (!f) return false;
        if (parentId !== undefined) {
          if (parentId === null && f.parent_id) return false;
          if (parentId && String(f.parent_id) !== String(parentId)) return false;
        }
        return cleanTitle(f.title || '').toLowerCase().includes(lowerKw);
      });
      if (found) return found;
    }
    return null;
  };

  const scrollToFoldersArea = () => {
    setTimeout(() => {
      const el = document.getElementById('course-folders-section');
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  };

  const openLibraryCategory = (path: string) => {
    window.history.pushState(null, '', path);
    if (onNavigate) {
      onNavigate('home');
    } else {
      window.dispatchEvent(new CustomEvent('tony-navigate', { detail: 'home' }));
    }
  };

  // Extract IGCSE 0654 chapters for the selected science branch (B1..B19, C1..C12, P1..P6)
  const scienceChapters = useMemo(() => {
    if (!isIgcse0654 || !selectedScienceBranch || selectedScienceBranch === 'pastpapers') return [];
    const prefix =
      selectedScienceBranch === 'biology' ? 'B' : selectedScienceBranch === 'chemistry' ? 'C' : 'P';
    const regex = new RegExp(`^${prefix}\\d+\\s*:`, 'i');
    const safeLectures = Array.isArray(effectiveLectures) ? effectiveLectures : [];

    const matchedLectures = safeLectures
      .filter((l) => l && regex.test(cleanTitle(l.title || '')))
      .sort((a, b) => {
        const numA = parseInt(cleanTitle(a.title || '').match(/\d+/)?.[0] || '0', 10);
        const numB = parseInt(cleanTitle(b.title || '').match(/\d+/)?.[0] || '0', 10);
        return numA - numB;
      });

    return matchedLectures.map((l) => {
      const t = cleanTitle(l.title || '');
      const code = (t.match(/^([BCP]\d+)\s*:/i)?.[1] || '').toUpperCase();
      return {
        code,
        title: t,
        lectureId: l.id,
      };
    });
  }, [isIgcse0654, selectedScienceBranch, effectiveLectures]);

  useEffect(() => {
    if (scienceChapters.length > 0 && !scienceChapters.some((ch) => ch.code === selectedTopicCode)) {
      setSelectedTopicCode(scienceChapters[0].code);
    }
  }, [scienceChapters, selectedTopicCode]);

  if (!isIelts && !isIgcse0654) return null;

  // Build steps for IELTS Premium
  const buildIeltsSteps = (): CoachStep[] => {
    if (!selectedIeltsSkill) return [];

    if (selectedIeltsSkill === 'listening') {
      const listenGuideLec = findLectureByKeyword(['hướng dẫn và phân tích luyện nghe', 'luyện nghe']);
      const listenStratFolder = findFolderByKeyword(['listening strategies'], null);
      const camFolder = findFolderByKeyword(['cambridge test'], null);

      return [
        {
          stepNumber: 1,
          title: 'Học chiến thuật & Cách bắt bài người ra đề',
          description:
            'Mở bài giảng "Hướng dẫn và Phân tích Luyện Nghe" trong học phần Luyện thi Nghe. Nắm vững quy tắc gạch chân từ khóa (keywords), dự đoán loại từ cần điền và cách tránh bẫy đổi ý (distractors) trong băng.',
          tip: 'Không bao giờ nghe thụ động khi chưa phân tích kỹ câu hỏi trước khi băng chạy.',
          actions: [
            {
              label: 'Mở bài giảng: Hướng dẫn & Phân tích Luyện Nghe',
              icon: '📖',
              variant: 'primary',
              onClick: () => onOpenLecture(courseId, listenGuideLec?.id),
            },
          ],
        },
        {
          stepNumber: 2,
          title: 'Luyện thuần thục từng dạng câu hỏi (Listening Strategies)',
          description:
            'Vào bộ đề Listening Strategies (gồm 6 Unit chuyên biệt: Unit 1 Letters & Numbers, Unit 2 Form/Table Completion, Unit 3 Description & Location, Unit 4 Multiple Choice, Unit 5 Note Completion, Unit 6 Summary) để rèn kỹ năng bắt chuẩn từng dạng.',
          actions: [
            {
              label: 'Mở bộ đề: Listening Strategies (6 Units)',
              icon: '📂',
              variant: 'emerald',
              onClick: () => {
                onSelectFolder(listenStratFolder?.id || '');
                scrollToFoldersArea();
              },
            },
          ],
        },
        {
          stepNumber: 3,
          title: 'Luyện đề thực chiến chuẩn phòng thi (Cambridge Test)',
          description:
            'Chọn 1 bài Listening trong bộ Cambridge Test (Cam 01 – Cam 21). Làm bài nghiêm túc trong 1 lần nghe duy nhất để rèn sự tập trung và tâm lý phòng thi thật.',
          actions: [
            {
              label: 'Mở kho đề: Cambridge Test (Cam 01 – 21)',
              icon: '📝',
              variant: 'amber',
              onClick: () => {
                onSelectFolder(camFolder?.id || '');
                scrollToFoldersArea();
              },
            },
          ],
        },
        {
          stepNumber: 4,
          title: 'Chữa bài sâu & Đọc Bài Dịch Nghe Cambridge IELTS trong Thư viện (Bắt buộc)',
          description:
            'Sau khi nộp bài, xem giải thích từng câu và đối chiếu Audio Transcript màu vàng. Tiếp theo, BẮT BUỘC mở mục "Bài dịch nghe Cambridge IELTS" trong Thư viện để đọc bản dịch song ngữ và học từ vựng của bài vừa làm (hệ thống tự động lưu vào Tiến độ học).',
          tip: 'Mỗi bài dịch nghe bạn mở đọc trong Thư viện sẽ được tự động đánh dấu hoàn thành trong tab Tiến độ học IELTS Premium.',
          actions: [
            {
              label: '🎧 Mở Thư viện: Bài dịch nghe Cambridge (01 – 21)',
              icon: '📚',
              variant: 'emerald',
              onClick: () => openLibraryCategory('/news/category/cambridge-ielts-listening-translation'),
            },
            {
              label: 'Hỏi Thầy AI phương pháp cải thiện kỹ năng Nghe',
              icon: '🤖',
              variant: 'purple',
              onClick: () =>
                onOpenAIChat?.(
                  'Thầy hướng dẫn chi tiết cho em cách phân tích Audio Transcript và ghi chép Paraphrase sau khi làm bài IELTS Listening nhé!'
                ),
            },
          ],
        },
      ];
    }

    if (selectedIeltsSkill === 'reading') {
      const readVocabLec = findLectureByKeyword(['popular words', 'academic sublist']);
      const readStratFolder = findFolderByKeyword(['reading strategies'], null);
      const crashFolder = findFolderByKeyword(['crash course'], null);
      const cramFolder = findFolderByKeyword(['cram course'], null);
      const camFolder = findFolderByKeyword(['cambridge test'], null);

      return [
        {
          stepNumber: 1,
          title: 'Nạp từ vựng học thuật qua ngữ cảnh (Academic Vocabulary)',
          description:
            'Vào học phần Luyện thi Đọc (1. Popular words, 2. The Five Senses, 3. Academic sublist 1–10). Đọc bài khóa ngữ cảnh và hoàn thành các bài tập tương tác ngay bên dưới bài giảng để nhớ sâu từ vựng.',
          actions: [
            {
              label: 'Mở bài giảng: Luyện thi Đọc & Academic Vocab',
              icon: '📖',
              variant: 'primary',
              onClick: () => onOpenLecture(courseId, readVocabLec?.id),
            },
          ],
        },
        {
          stepNumber: 2,
          title: 'Rèn kỹ thuật xử lý từng dạng câu hỏi (Reading Strategies)',
          description:
            'Luyện kỹ thuật định vị thông tin nhanh (Scanning/Skimming) theo 6 dạng câu hỏi trong thư mục Reading Strategies (Matching, Cloze, Multiple Choice, Summarizing, Yes/No/Not Given, Scanning for Answers).',
          actions: [
            {
              label: 'Mở bộ đề: Reading Strategies (6 Units)',
              icon: '📂',
              variant: 'emerald',
              onClick: () => {
                onSelectFolder(readStratFolder?.id || '');
                scrollToFoldersArea();
              },
            },
          ],
        },
        {
          stepNumber: 3,
          title: 'Nâng cấp tư duy đọc hiểu học thuật (Crash Course & Cram Course)',
          description:
            'Luyện kỹ năng phân tích câu phức, suy luận (Inference) và mục đích tu từ (Rhetorical Purpose) trong bộ Crash Course, kết hợp đọc theo 8 chủ đề học thuật lớn (History, Social Sciences, Natural Sciences...) trong Cram Course.',
          actions: [
            {
              label: 'Mở bộ đề: Crash Course (8 Chapters)',
              icon: '🚀',
              variant: 'secondary',
              onClick: () => {
                onSelectFolder(crashFolder?.id || '');
                scrollToFoldersArea();
              },
            },
            {
              label: 'Mở bộ đề: Cram Course (8 Chủ đề)',
              icon: '📚',
              variant: 'secondary',
              onClick: () => {
                onSelectFolder(cramFolder?.id || '');
                scrollToFoldersArea();
              },
            },
          ],
        },
        {
          stepNumber: 4,
          title: 'Luyện đề Cambridge Test & Đọc Bài Dịch Đọc trong Thư viện (Bắt buộc)',
          description:
            'Làm đề Reading trong bộ Cambridge Test ở chế độ thi máy tính (Computer Test). Sau khi nộp bài và xem giải thích câu sai, BẮT BUỘC mở mục "Bài dịch đọc Cambridge IELTS" trong Thư viện để đọc bản dịch song ngữ và học từ vựng học thuật của Passage vừa làm.',
          tip: 'Mỗi bài dịch đọc bạn mở xem trong Thư viện sẽ được tự động ghi nhận vào Tiến độ học IELTS Premium.',
          actions: [
            {
              label: 'Mở kho đề: Cambridge Test (Cam 01 – 21)',
              icon: '📝',
              variant: 'amber',
              onClick: () => {
                onSelectFolder(camFolder?.id || '');
                scrollToFoldersArea();
              },
            },
            {
              label: '📖 Mở Thư viện: Bài dịch đọc Cambridge (01 – 21)',
              icon: '📚',
              variant: 'emerald',
              onClick: () => openLibraryCategory('/news/category/cambridge-ielts-reading-translation'),
            },
          ],
        },
      ];
    }

    if (selectedIeltsSkill === 'writing') {
      if (selectedWritingTask === 'task1') {
        const task1Lec = findLectureByKeyword(['task 1 : data analysis : dynamic', 'task 1']);
        const task1QuestionsLec = findLectureByKeyword(['task 1 : questions', 'hướng dẫn và phân tích viết task 1']);

        return [
          {
            stepNumber: 1,
            title: 'Học công thức phân tích biểu đồ (Writing Task 1)',
            description:
              'Mở học phần Luyện thi Viết : Task 1 để nắm vững cấu trúc 4 đoạn chuẩn và từ vựng mô tả xu hướng cho 6 dạng bài: Dynamic Chart, Static Chart, Mixed Charts, Process (Nature/Human), và Maps (Indoor/Outdoor/Diagram).',
            actions: [
              {
                label: 'Mở bài giảng: Công thức Luyện thi Viết Task 1',
                icon: '📖',
                variant: 'primary',
                onClick: () => onOpenLecture(courseId, task1Lec?.id),
              },
            ],
          },
          {
            stepNumber: 2,
            title: 'Chọn đề biểu đồ & Nhờ AI phân tích số liệu / Lập dàn ý',
            description:
              'Mở bài "7. Task 1 : Questions" hoặc "8. Hướng dẫn và Phân tích Viết Task 1". Chọn 1 đề biểu đồ và bấm nút nhờ Thầy AI hướng dẫn cách chọn số liệu nổi bật cho phần Overview và chia 2 khổ Body.',
            actions: [
              {
                label: 'Mở danh sách đề: Task 1 Questions',
                icon: '📋',
                variant: 'emerald',
                onClick: () => onOpenLecture(courseId, task1QuestionsLec?.id),
              },
            ],
          },
          {
            stepNumber: 3,
            title: 'Viết bài hoàn chỉnh & Nộp cho Giám khảo AI chấm chữa',
            description:
              'Viết bài hoàn chỉnh trong 20 phút (tối thiểu 150 từ) và nộp vào Phòng Chấm IELTS Writing AI để nhận điểm chi tiết theo 4 tiêu chí (TA, CC, LR, GRA) kèm bản sửa lỗi từng câu.',
            actions: [
              {
                label: 'Vào Phòng Luyện & Chấm IELTS Writing AI',
                icon: '✍️',
                variant: 'amber',
                onClick: () => onNavigate?.('ielts-writing'),
              },
            ],
          },
        ];
      } else {
        const task2Lec = findLectureByKeyword(['task 2 : discussion', 'task 2']);
        const ideasLec = findLectureByKeyword(['1. advertising', '9. genetic', '17. personality']);
        const vocabLec = findLectureByKeyword(['government', 'immigration', 'climate change']);
        const task2QuestionsLec = findLectureByKeyword(['task 2 : questions', 'hướng dẫn và phân tích viết task 2']);

        return [
          {
            stepNumber: 1,
            title: 'Nắm vững cấu trúc 4 dạng bài luận (Writing Task 2)',
            description:
              'Mở học phần Luyện thi Viết : Task 2 và xem kỹ công thức lập luận cho 4 dạng đề: Discussion, Argument, Opinion, và Mixed. Nắm rõ cách viết câu Thesis Statement và câu chủ đề (Topic Sentence) cho từng đoạn.',
            actions: [
              {
                label: 'Mở bài giảng: Công thức Luyện thi Viết Task 2',
                icon: '📖',
                variant: 'primary',
                onClick: () => onOpenLecture(courseId, task2Lec?.id),
              },
            ],
          },
          {
            stepNumber: 2,
            title: 'Tra cứu Ý tưởng (Ideas) & Từ vựng học thuật theo chủ đề',
            description:
              'Trước khi viết, hãy mở học phần Ideas P.I, P.II, P.III (24 chủ đề xã hội lớn) và Luyện thi Viết: Vocabulary để nạp các luận điểm (Pillars) sắc bén và cụm Collocations Band 7.5+.',
            actions: [
              {
                label: 'Mở kho Ý tưởng Task 2 (Ideas P.I – P.III)',
                icon: '💡',
                variant: 'emerald',
                onClick: () => onOpenLecture(courseId, ideasLec?.id),
              },
              {
                label: 'Mở Từ vựng chủ điểm Writing',
                icon: '📚',
                variant: 'secondary',
                onClick: () => onOpenLecture(courseId, vocabLec?.id),
              },
            ],
          },
          {
            stepNumber: 3,
            title: 'Thực hành viết luận & Chấm chữa 24/7 cùng Giám khảo AI',
            description:
              'Chọn 1 đề trong bài "Task 2 : Questions", bấm nút nhờ AI lập dàn ý hoặc gợi ý từ vựng, sau đó viết bài trong 40 phút và nộp vào Phòng Chấm IELTS Writing AI.',
            actions: [
              {
                label: 'Mở danh sách đề: Task 2 Questions',
                icon: '📋',
                variant: 'secondary',
                onClick: () => onOpenLecture(courseId, task2QuestionsLec?.id),
              },
              {
                label: 'Vào Phòng Luyện & Chấm IELTS Writing AI',
                icon: '✍️',
                variant: 'amber',
                onClick: () => onNavigate?.('ielts-writing'),
              },
            ],
          },
        ];
      }
    }

    if (selectedIeltsSkill === 'speaking') {
      const speakBlockLec = findLectureByKeyword(['main block: person', 'main block']);
      const speakFormulaLec = findLectureByKeyword(['part i & iii : formula', 'speaking question']);

      return [
        {
          stepNumber: 1,
          title: 'Học thuộc các khối kịch bản Lego (Main Blocks & Plugin Blocks)',
          description:
            'Mở học phần Luyện thi Nói, nắm vững 6 Main Blocks (1. Person, 2. Place/Service, 3. Historical/Nature, 4. Object/Entity, 5. Action/Experience, 6. Relation/Ceremony) và 3 Plugin Blocks (Food, Plant, Weather) cùng bài "10. Part I & III : Formula".',
          tip: 'Chỉ cần thuộc kỹ các khối Lego này, em có thể xoay chuyển và trả lời trôi chảy hàng chục đề Part 2 khác nhau mà không sợ bí ý!',
          actions: [
            {
              label: 'Mở bài giảng: Luyện thi Nói (Lego Blocks)',
              icon: '📖',
              variant: 'primary',
              onClick: () => onOpenLecture(courseId, speakBlockLec?.id),
            },
          ],
        },
        {
          stepNumber: 2,
          title: 'Lắp ghép kịch bản cho bộ câu hỏi Speaking thực tế',
          description:
            'Mở bài "11. Speaking question" và "12. Hướng dẫn và Phân tích Luyện Nói". Chọn chủ đề em muốn luyện hôm nay và bấm nút nhờ Thầy AI hướng dẫn cách ghép khối Lego + gợi ý Idioms/Collocations ăn điểm.',
          actions: [
            {
              label: 'Mở bộ câu hỏi Speaking & Phân tích',
              icon: '🎙️',
              variant: 'emerald',
              onClick: () => onOpenLecture(courseId, speakFormulaLec?.id),
            },
          ],
        },
        {
          stepNumber: 3,
          title: 'Luyện phản xạ nói trực tiếp với Giám khảo AI',
          description:
            'Vào Phòng Luyện Nói IELTS Speaking AI để ghi âm trả lời trực tiếp các câu hỏi Part 1, Part 2, Part 3 và nhận đánh giá chi tiết về Phát âm, Độ trôi chảy, Từ vựng & Ngữ pháp.',
          actions: [
            {
              label: 'Vào Phòng Luyện IELTS Speaking AI',
              icon: '🗣️',
              variant: 'amber',
              onClick: () => onNavigate?.('ielts-speaking'),
            },
          ],
        },
      ];
    }

    // Vocab & Ideas branch
    const readVocabLec = findLectureByKeyword(['popular words', 'academic sublist']);
    const writeVocabLec = findLectureByKeyword(['government', 'immigration']);
    const ideasLec = findLectureByKeyword(['1. advertising']);

    return [
      {
        stepNumber: 1,
        title: 'Học Từ vựng Học thuật cốt lõi (Academic Word List)',
        description:
          'Mở học phần Luyện thi Đọc (Popular words & Academic sublist 1–10). Đọc từ vựng trong ngữ cảnh bài đọc, tra cứu nghĩa và hoàn thành toàn bộ bài tập + Game từ vựng đi kèm.',
        actions: [
          {
            label: 'Mở bài giảng: Academic Vocabulary (Reading)',
            icon: '📖',
            variant: 'primary',
            onClick: () => onOpenLecture(courseId, readVocabLec?.id),
          },
        ],
      },
      {
        stepNumber: 2,
        title: 'Nạp Từ vựng theo 12 Chủ điểm Writing & Speaking',
        description:
          'Mở học phần Luyện thi Viết: Vocabulary (Government, Immigration, Climate change, Employment, Education, Globalization...) để học các cụm từ học thuật (Collocations) chuyên dùng cho bài viết và nói.',
        actions: [
          {
            label: 'Mở bài giảng: Từ vựng Chủ điểm Writing',
            icon: '📚',
            variant: 'emerald',
            onClick: () => onOpenLecture(courseId, writeVocabLec?.id),
          },
        ],
      },
      {
        stepNumber: 3,
        title: 'Tổng hợp Luận điểm 24 Chủ đề Xã hội (Ideas P.I – P.III)',
        description:
          'Đọc và ghi chép các luận điểm hai chiều (Ưu/Nhược điểm, Nguyên nhân/Giải pháp) cho 24 chủ đề lớn trong Ideas P.I, P.II, P.III để luôn sẵn sàng ý tưởng cho cả Writing Task 2 và Speaking Part 3.',
        actions: [
          {
            label: 'Mở kho Ý tưởng Học thuật (24 Chủ đề)',
            icon: '💡',
            variant: 'amber',
            onClick: () => onOpenLecture(courseId, ideasLec?.id),
          },
        ],
      },
    ];
  };

  // Build steps for IGCSE Co-ordinated Sciences (0654)
  const buildIgcse0654Steps = (): CoachStep[] => {
    if (!selectedScienceBranch) return [];

    if (selectedScienceBranch === 'pastpapers') {
      const pastPaperLec = findLectureByKeyword(['past paper practice', 'podcast ôn tập']);
      const pastPaperFolder = findFolderByKeyword(['past papers'], null);

      return [
        {
          stepNumber: 1,
          title: 'Nghe Podcast Ôn tập & Nắm chiến thuật từng Paper (2, 4, 6)',
          description:
            'Vào học phần "0654 Past Papers", mở bài "1. Past Paper Practice" và nghe "Podcast ôn tập" để nắm rõ cấu trúc & cách phân bổ thời gian cho Paper 2 (40 câu trắc nghiệm), Paper 4 (Tự luận chuyên sâu) và Paper 6 (Kỹ năng thí nghiệm thực hành).',
          actions: [
            {
              label: 'Mở Bài Giảng & Podcast Ôn Tập 0654',
              icon: '🎧',
              variant: 'primary',
              onClick: () => onOpenLecture(courseId, pastPaperLec?.id),
            },
          ],
        },
        {
          stepNumber: 2,
          title: 'Làm đề Past Papers theo năm thi chuẩn Cambridge',
          description:
            'Mở thư mục "Past Papers" trong kho đề bên dưới, chọn 1 mã đề (Paper 2, Paper 4 hoặc Paper 6) và làm bài nghiêm túc theo đúng thời gian quy định.',
          actions: [
            {
              label: 'Mở kho đề: 0654 Past Papers',
              icon: '📝',
              variant: 'emerald',
              onClick: () => {
                onSelectFolder(pastPaperFolder?.id || '');
                scrollToFoldersArea();
              },
            },
          ],
        },
        {
          stepNumber: 3,
          title: 'Phân tích kết quả AI chấm & Lấp lỗ hổng theo chuyên đề',
          description:
            'Sau khi nộp bài, xem điểm quy đổi theo thang Cambridge (A*, A, B, C...). Với những câu bị mất điểm thuộc chương nào (ví dụ B4, C3, hay P2), hãy quay lại đúng chương đó để ôn lại lý thuyết và làm thêm Topic Paper.',
          actions: [
            {
              label: 'Hỏi Thầy AI giải thích câu khó trong Past Paper',
              icon: '🤖',
              variant: 'purple',
              onClick: () =>
                onOpenAIChat?.(
                  'Thầy ơi, hướng dẫn giúp em cách viết câu trả lời tự luận Paper 4 và Paper 6 môn IGCSE Co-ordinated Sciences 0654 sao cho trúng từ khóa Marking Scheme đạt điểm tối đa ạ!'
                ),
            },
          ],
        },
      ];
    }

    // Biology, Chemistry, or Physics branch
    const branchLabel =
      selectedScienceBranch === 'biology'
        ? 'Biology (Sinh học)'
        : selectedScienceBranch === 'chemistry'
        ? 'Chemistry (Hóa học)'
        : 'Physics (Vật lý)';

    const currentChapter =
      scienceChapters.find((ch) => ch.code === selectedTopicCode) || scienceChapters[0] || null;

    const rootTopicFolder = findFolderByKeyword(
      [
        selectedScienceBranch === 'biology'
          ? 'biology: topic papers'
          : selectedScienceBranch === 'chemistry'
          ? 'chemistry: topic papers'
          : 'physics: topic papers',
      ],
      null
    );

    const specificChapterFolder = currentChapter
      ? findFolderByKeyword([`${currentChapter.code}:`], rootTopicFolder?.id) || rootTopicFolder
      : rootTopicFolder;

    return [
      {
        stepNumber: 1,
        title: `Học Lý thuyết Song ngữ & Mô phỏng — ${
          currentChapter ? currentChapter.title : branchLabel
        }`,
        description: `Mở bài giảng lý thuyết của chuyên đề ${
          currentChapter ? `"${currentChapter.title}"` : branchLabel
        }. Đọc kỹ bản tiếng Anh để thuộc các thuật ngữ khoa học (Key Terms & Definitions), bật bản dịch tiếng Việt & nghe Audio giảng bài, đồng thời tương tác với các mô phỏng thí nghiệm ngay trong bài.`,
        tip: 'Chú ý các định nghĩa in đậm chuẩn Syllabus Cambridge — đây chính là các cụm từ ăn điểm trong kỳ thi thật.',
        actions: [
          {
            label: `Mở bài giảng: ${currentChapter ? currentChapter.title : branchLabel}`,
            icon: '📖',
            variant: 'primary',
            onClick: () => onOpenLecture(courseId, currentChapter?.lectureId),
          },
        ],
      },
      {
        stepNumber: 2,
        title: 'Kiểm tra bản chất kiến thức & Hỏi đáp cùng Thầy AI',
        description: `Tự tóm tắt lại các khái niệm cốt lõi, công thức hoặc phương trình phản ứng của chuyên đề ${
          currentChapter ? currentChapter.code : branchLabel
        }. Nếu có hiện tượng khoa học nào chưa hiểu sâu bản chất, hãy bấm nút bên dưới để Thầy AI giải thích cặn kẽ.`,
        actions: [
          {
            label: `Nhờ Thầy AI tóm tắt trọng tâm ${currentChapter ? currentChapter.code : branchLabel}`,
            icon: '🤖',
            variant: 'purple',
            onClick: () =>
              onOpenAIChat?.(
                `Thầy tóm tắt giúp em các khái niệm cốt lõi, công thức và những từ khóa Marking Scheme quan trọng nhất cần nhớ trong chuyên đề "${
                  currentChapter ? currentChapter.title : branchLabel
                }" môn IGCSE Co-ordinated Sciences 0654 nhé!`
              ),
          },
        ],
      },
      {
        stepNumber: 3,
        title: `Làm bài tập theo đúng chuyên đề vừa học (${
          currentChapter ? `${currentChapter.code} Topic Papers` : 'Topic Papers'
        })`,
        description: `Ngay sau khi học xong lý thuyết ${
          currentChapter ? currentChapter.code : ''
        }, em mở ngay thư mục Topic Papers của đúng chuyên đề đó để làm bộ câu hỏi trắc nghiệm (Multiple Choice) và tự luận (Structured Questions) nhằm khóa chặt kiến thức vừa học, tránh học trước quên sau.`,
        actions: [
          {
            label: `Mở bộ đề: ${
              currentChapter ? `Topic Papers — ${currentChapter.title}` : `${branchLabel} Topic Papers`
            }`,
            icon: '📂',
            variant: 'emerald',
            onClick: () => {
              onSelectFolder(specificChapterFolder?.id || '');
              scrollToFoldersArea();
            },
          },
        ],
      },
      {
        stepNumber: 4,
        title: 'Đối chiếu Cambridge Marking Scheme & Ghi chú từ khóa ăn điểm',
        description:
          'Sau khi nộp bài Topic Paper, xem kỹ phần chấm chữa của AI theo chuẩn Marking Scheme của Cambridge. Ghi nhớ các từ khóa bắt buộc (keywords) trong đáp án mẫu để đạt điểm tối đa khi làm bài tự luận Paper 4.',
        actions: [],
      },
    ];
  };

  const activeSteps = isIelts ? buildIeltsSteps() : buildIgcse0654Steps();
  const activeBranchKey = isIelts
    ? `${selectedIeltsSkill || 'none'}_${selectedWritingTask}`
    : `${selectedScienceBranch || 'none'}_${selectedTopicCode}`;

  const getButtonStyle = (variant?: string) => {
    switch (variant) {
      case 'emerald':
        return 'bg-emerald-600 hover:bg-emerald-700 text-white shadow-sm';
      case 'amber':
        return 'bg-amber-500 hover:bg-amber-600 text-slate-950 shadow-sm';
      case 'purple':
        return 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm';
      case 'secondary':
        return 'bg-sky-50 hover:bg-sky-100 text-[#0a5482] border border-sky-200';
      default:
        return 'bg-[#0a5482] hover:bg-[#084266] text-white shadow-sm';
    }
  };

  return (
    <div className="mb-8 rounded-2xl sm:rounded-3xl border-2 border-[#2ab4e8]/40 bg-white shadow-md overflow-hidden transition-all">
      {/* TOP HEADER BAR OF AI STUDY COACH */}
      <div className="bg-gradient-to-r from-[#072f49] via-[#0a5482] to-[#0f172a] px-5 sm:px-7 py-4 sm:py-5 text-white flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3.5 min-w-0">
          <div className="w-11 h-11 sm:w-12 sm:h-12 rounded-2xl bg-gradient-to-br from-[#2ab4e8] to-sky-400 text-slate-950 flex items-center justify-center text-2xl shadow-md shrink-0">
            🤖
          </div>
          <div className="min-w-0">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="bg-emerald-400/20 text-emerald-300 border border-emerald-400/30 text-[10px] sm:text-[11px] font-black uppercase tracking-wider px-2.5 py-0.5 rounded-full flex items-center gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping" />
                <span>Thầy Tony AI Tutor • Hướng dẫn từng bước</span>
              </span>
            </div>
            <h2 className="text-base sm:text-xl font-black tracking-tight text-white mt-0.5 truncate">
              Lộ Trình &amp; Các Việc Cần Làm Hôm Nay — {cleanTitle(courseTitle)}
            </h2>
          </div>
        </div>

        <button
          type="button"
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="bg-white/10 hover:bg-white/20 text-white border border-white/20 text-xs font-extrabold px-3.5 py-2 rounded-xl transition cursor-pointer flex items-center gap-1.5 shrink-0"
        >
          <span>{isCollapsed ? 'Mở hướng dẫn học tập' : 'Thu gọn'}</span>
          <span>{isCollapsed ? '▼' : '▲'}</span>
        </button>
      </div>

      {!isCollapsed && (
        <div className="p-5 sm:p-7 space-y-6 bg-gradient-to-b from-sky-50/40 to-white">
          {/* STEP 1: AI TUTOR QUESTION & BRANCH SELECTION */}
          <div className="flex flex-col sm:flex-row items-start gap-4 bg-white p-4 sm:p-5 rounded-2xl border border-sky-200/80 shadow-2xs">
            <div className="w-10 h-10 rounded-xl bg-sky-100 text-[#0a5482] flex items-center justify-center text-xl shrink-0 font-black">
              👨‍🏫
            </div>
            <div className="flex-1 min-w-0">
              <div className="text-xs font-extrabold uppercase tracking-wider text-[#2ab4e8] mb-1">
                Thầy Tony AI hỏi bạn:
              </div>
              {isIelts ? (
                <p className="text-slate-800 font-bold text-sm sm:text-base leading-relaxed">
                  Chào <span className="text-[#0a5482] font-black">{studentName}</span>! Hôm nay em muốn tập trung rèn
                  luyện kỹ năng nào trong khóa <b>IELTS Premium</b>? Hãy bấm chọn 1 kỹ năng bên dưới để thầy giao các
                  bước cần làm nhé:
                </p>
              ) : (
                <p className="text-slate-800 font-bold text-sm sm:text-base leading-relaxed">
                  Chào <span className="text-[#0a5482] font-black">{studentName}</span>! Hôm nay trong môn{' '}
                  <b>IGCSE Co-ordinated Sciences (0654)</b>, em muốn học phân môn nào hay luyện đề Past Papers? Hãy bấm
                  chọn bên dưới để thầy hướng dẫn từng bước nhé:
                </p>
              )}

              {/* BRANCH BUTTONS FOR IELTS PREMIUM */}
              {isIelts && (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-2.5 mt-4">
                  {[
                    {
                      id: 'listening' as const,
                      icon: '🎧',
                      label: 'Kỹ năng Nghe',
                      sub: 'Listening & Transcript',
                    },
                    {
                      id: 'reading' as const,
                      icon: '📖',
                      label: 'Kỹ năng Đọc',
                      sub: 'Reading & Strategies',
                    },
                    {
                      id: 'writing' as const,
                      icon: '✍️',
                      label: 'Kỹ năng Viết',
                      sub: 'Writing Task 1 & 2',
                    },
                    {
                      id: 'speaking' as const,
                      icon: '🎙️',
                      label: 'Kỹ năng Nói',
                      sub: 'Speaking Lego Blocks',
                    },
                    {
                      id: 'vocab' as const,
                      icon: '📚',
                      label: 'Từ vựng & Ideas',
                      sub: 'Academic Vocab & 24 Chủ đề',
                    },
                  ].map((item) => {
                    const active = selectedIeltsSkill === item.id;
                    return (
                      <button
                        key={item.id}
                        type="button"
                        onClick={() => setSelectedIeltsSkill(item.id)}
                        className={`p-3.5 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between ${
                          active
                            ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-md scale-[1.01]'
                            : 'bg-slate-50/80 hover:bg-sky-50 text-slate-800 border-slate-200/90 hover:border-[#2ab4e8]'
                        }`}
                      >
                        <div className="flex items-center justify-between gap-2 mb-1.5">
                          <span className="text-xl">{item.icon}</span>
                          {active && (
                            <span className="text-[10px] font-black uppercase bg-[#2ab4e8] text-slate-950 px-2 py-0.5 rounded-full">
                              Đang chọn
                            </span>
                          )}
                        </div>
                        <div>
                          <div className="font-black text-sm leading-snug">{item.label}</div>
                          <div className={`text-[11px] font-medium mt-0.5 ${active ? 'text-sky-200' : 'text-slate-500'}`}>
                            {item.sub}
                          </div>
                        </div>
                      </button>
                    );
                  })}
                </div>
              )}

              {/* BRANCH BUTTONS FOR IGCSE CO-ORDINATED SCIENCES (0654) */}
              {isIgcse0654 && (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 mt-4">
                  {[
                    {
                      id: 'biology' as const,
                      icon: '🧬',
                      label: 'Biology (Sinh học)',
                      sub: '19 Chuyên đề (B1 – B19)',
                    },
                    {
                      id: 'chemistry' as const,
                      icon: '🧪',
                      label: 'Chemistry (Hóa học)',
                      sub: '12 Chuyên đề (C1 – C12)',
                    },
                    {
                      id: 'physics' as const,
                      icon: '⚡',
                      label: 'Physics (Vật lý)',
                      sub: '6 Chuyên đề (P1 – P6)',
                    },
                    {
                      id: 'pastpapers' as const,
                      icon: '📄',
                      label: 'Luyện đề Past Papers',
                      sub: 'Paper 2, Paper 4 & Paper 6',
                    },
                  ].map((item) => {
                    const active = selectedScienceBranch === item.id;
                    return (
                      <button
                        key={item.id}
                        type="button"
                        onClick={() => setSelectedScienceBranch(item.id)}
                        className={`p-3.5 rounded-2xl border text-left transition-all cursor-pointer flex flex-col justify-between ${
                          active
                            ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-md scale-[1.01]'
                            : 'bg-slate-50/80 hover:bg-sky-50 text-slate-800 border-slate-200/90 hover:border-[#2ab4e8]'
                        }`}
                      >
                        <div className="flex items-center justify-between gap-2 mb-1.5">
                          <span className="text-xl">{item.icon}</span>
                          {active && (
                            <span className="text-[10px] font-black uppercase bg-[#2ab4e8] text-slate-950 px-2 py-0.5 rounded-full">
                              Đang chọn
                            </span>
                          )}
                        </div>
                        <div>
                          <div className="font-black text-sm leading-snug">{item.label}</div>
                          <div className={`text-[11px] font-medium mt-0.5 ${active ? 'text-sky-200' : 'text-slate-500'}`}>
                            {item.sub}
                          </div>
                        </div>
                      </button>
                    );
                  })}
                </div>
              )}
            </div>
          </div>

          {/* SUB-SELECTORS (Writing Task 1/2 OR IGCSE Chapter Selector B1..B19 / C1..C12 / P1..P6) */}
          {isIelts && selectedIeltsSkill === 'writing' && (
            <div className="bg-white rounded-2xl p-4 border border-slate-200/90 flex flex-wrap items-center justify-between gap-3">
              <div className="text-xs sm:text-sm font-black text-slate-700 flex items-center gap-2">
                <span>✍️</span>
                <span>Chọn phần Writing em muốn luyện hôm nay:</span>
              </div>
              <div className="inline-flex bg-slate-100 p-1 rounded-xl gap-1">
                <button
                  type="button"
                  onClick={() => setSelectedWritingTask('task1')}
                  className={`px-4 py-2 rounded-lg text-xs font-black transition cursor-pointer ${
                    selectedWritingTask === 'task1'
                      ? 'bg-[#0a5482] text-white shadow-xs'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  📊 Writing Task 1 (Biểu đồ / Map / Process)
                </button>
                <button
                  type="button"
                  onClick={() => setSelectedWritingTask('task2')}
                  className={`px-4 py-2 rounded-lg text-xs font-black transition cursor-pointer ${
                    selectedWritingTask === 'task2'
                      ? 'bg-[#0a5482] text-white shadow-xs'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  📝 Writing Task 2 (Viết luận Essay)
                </button>
              </div>
            </div>
          )}

          {isIgcse0654 &&
            selectedScienceBranch &&
            selectedScienceBranch !== 'pastpapers' &&
            scienceChapters.length > 0 && (
              <div className="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 space-y-3">
                <div className="text-xs sm:text-sm font-black text-slate-700 flex items-center justify-between gap-2 flex-wrap">
                  <span>
                    📌 Chọn chuyên đề ({selectedScienceBranch.toUpperCase()}) em đang học hôm nay để mở đúng bài giảng &amp;
                    Topic Paper:
                  </span>
                </div>
                <div className="flex flex-wrap gap-2 max-h-40 overflow-y-auto custom-scrollbar pr-1">
                  {scienceChapters.map((ch) => {
                    const isSelected = ch.code === selectedTopicCode;
                    return (
                      <button
                        key={ch.code}
                        type="button"
                        onClick={() => setSelectedTopicCode(ch.code)}
                        className={`px-3 py-1.5 rounded-xl text-xs font-bold border transition cursor-pointer text-left ${
                          isSelected
                            ? 'bg-[#0a5482] text-white border-[#0a5482] shadow-xs'
                            : 'bg-slate-50 hover:bg-sky-50 text-slate-700 border-slate-200/80'
                        }`}
                      >
                        {ch.title}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}

          {/* STEP 2: NUMBERED STEP-BY-STEP WORKFLOW CHECKLIST */}
          {activeSteps.length > 0 && (
            <div className="space-y-4 animate-in fade-in duration-300">
              <div className="flex items-center justify-between flex-wrap gap-2 px-1">
                <h3 className="font-black text-slate-800 text-sm sm:text-base flex items-center gap-2">
                  <span>📋</span>
                  <span>Các bước thực hiện chuẩn theo quy trình của Thầy Tony:</span>
                </h3>
                <span className="text-xs text-slate-500 font-semibold">
                  Tick chọn vào ô vuông sau khi em hoàn thành từng bước nhé!
                </span>
              </div>

              <div className="grid grid-cols-1 gap-4">
                {activeSteps.map((st) => {
                  const stepKey = `${activeBranchKey}_step_${st.stepNumber}`;
                  const isDone = !!checkedSteps[stepKey];

                  return (
                    <div
                      key={st.stepNumber}
                      className={`rounded-2xl border p-4 sm:p-5 transition-all ${
                        isDone
                          ? 'bg-emerald-50/50 border-emerald-200/90'
                          : 'bg-white border-slate-200/90 hover:border-[#2ab4e8]/70 shadow-2xs'
                      }`}
                    >
                      <div className="flex items-start gap-3.5">
                        {/* Step Number or Checkmark */}
                        <button
                          type="button"
                          onClick={() => toggleStepCheck(stepKey)}
                          title="Đánh dấu hoàn thành bước này"
                          className={`w-9 h-9 rounded-xl font-black text-sm flex items-center justify-center shrink-0 transition cursor-pointer ${
                            isDone
                              ? 'bg-emerald-500 text-white shadow-xs'
                              : 'bg-[#0a5482] text-white hover:bg-[#2ab4e8]'
                          }`}
                        >
                          {isDone ? '✓' : st.stepNumber}
                        </button>

                        <div className="flex-1 min-w-0">
                          <div className="flex items-center justify-between gap-2 flex-wrap mb-1">
                            <h4
                              className={`font-black text-sm sm:text-base ${
                                isDone ? 'line-through text-slate-500' : 'text-slate-900'
                              }`}
                            >
                              Bước {st.stepNumber}: {st.title}
                            </h4>
                            <button
                              type="button"
                              onClick={() => toggleStepCheck(stepKey)}
                              className={`text-[11px] font-bold px-2.5 py-0.5 rounded-lg border cursor-pointer transition ${
                                isDone
                                  ? 'bg-emerald-100 text-emerald-800 border-emerald-300'
                                  : 'bg-slate-100 hover:bg-slate-200 text-slate-600 border-slate-200'
                              }`}
                            >
                              {isDone ? '✓ Đã xong bước này' : '☐ Đánh dấu đã xong'}
                            </button>
                          </div>

                          <p className="text-xs sm:text-[14px] text-slate-600 font-medium leading-relaxed">
                            {st.description}
                          </p>

                          {st.tip && (
                            <div className="mt-2.5 bg-amber-50/90 border border-amber-200/80 text-amber-900 rounded-xl px-3.5 py-2 text-xs font-semibold flex items-start gap-2">
                              <span className="shrink-0">💡</span>
                              <span>
                                <b>Lưu ý từ thầy Tony:</b> {st.tip}
                              </span>
                            </div>
                          )}

                          {st.actions.length > 0 && (
                            <div className="mt-3.5 flex flex-wrap items-center gap-2.5">
                              {st.actions.map((act, idx) => (
                                <button
                                  key={idx}
                                  type="button"
                                  onClick={act.onClick}
                                  className={`text-xs sm:text-[13px] font-extrabold px-4 py-2.5 rounded-xl transition active:scale-95 flex items-center gap-2 cursor-pointer ${getButtonStyle(
                                    act.variant
                                  )}`}
                                >
                                  <span>{act.icon}</span>
                                  <span>{act.label}</span>
                                  <span>→</span>
                                </button>
                              ))}
                            </div>
                          )}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
