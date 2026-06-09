const fs = require('fs');
const file = 'src/AITutorSidebar.tsx';
let content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');

const t = `      case 'task1':
      case 'task2':
        return {
          headerBg: 'from-[#8b5cf6] to-[#6d28d9]',`;

const r = `      case 'task1':
        return {
          headerBg: 'from-[#10b981] to-[#0d9488]', 
          title: \`IELTS Assessor (TASK 1)\`,
          subtitle: 'Chấm điểm & Sửa lỗi chuyên sâu', 
          icon: '📝',
          userBg: 'bg-gradient-to-br from-[#10b981] to-[#0d9488]', 
          aiBorder: 'border-emerald-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#10b981] hover:bg-[#059669]', 
          focusRing: 'focus-within:border-[#10b981] focus-within:ring-4 focus-within:ring-[#10b981]/10', 
          width: 'md:w-[500px]'
        };
      case 'task2':
        return {
          headerBg: 'from-[#8b5cf6] to-[#6d28d9]',`;

if (content.includes(t)) {
  content = content.replace(t, r);
  console.log('Fixed task1 and task2');
} else {
  console.log('t1 not found');
}

const t2 = `      case 'ESL':
        return {
          headerBg: 'from-[#0284c7] to-[#0369a1]',`;

const r2 = `      case 'speaking':
        return {
          headerBg: 'from-[#f43f5e] to-[#e11d48]', 
          title: 'Speaking Assistant',
          subtitle: 'Lên ý tưởng & Bẻ lõi Part 2', 
          icon: '🎙️',
          userBg: 'bg-gradient-to-br from-[#f43f5e] to-[#e11d48]', 
          aiBorder: 'border-rose-100', 
          aiBg: 'bg-white',
          btnColor: 'bg-[#f43f5e] hover:bg-[#e11d48]', 
          focusRing: 'focus-within:border-[#f43f5e] focus-within:ring-4 focus-within:ring-[#f43f5e]/10', 
          width: 'md:w-[500px]'
        };
      case 'ESL':
        return {
          headerBg: 'from-[#0284c7] to-[#0369a1]',`;

if (content.includes(t2)) {
  content = content.replace(t2, r2);
  console.log('Fixed speaking theme');
} else {
  console.log('t2 not found');
}

fs.writeFileSync(file, content);
