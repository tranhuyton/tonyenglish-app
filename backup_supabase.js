const fs = require('fs');
const path = require('path');

// Đọc thủ công file .env để không cần cài thêm thư viện
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) {
    return null;
  }
}

const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_SERVICE_ROLE_KEY = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY) {
  console.error("❌ Lỗi: Không tìm thấy VITE_SUPABASE_URL hoặc VITE_SUPABASE_SERVICE_ROLE_KEY trong file .env!");
  process.exit(1);
}

// Các bảng dữ liệu cốt lõi (Kho đề, khóa học, bài giảng)
const tablesToBackup = [
  'courses',
  'folders',
  'tests',
  'lecture_modules',
  'lectures',
  'lecture_pages',
  'classes'
];

async function fetchAllData(tableName) {
  let allData = [];
  let offset = 0;
  const limit = 50; // Mỗi lần tải 1000 dòng để tránh lỗi timeout
  
  while (true) {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/${tableName}?select=*&limit=${limit}&offset=${offset}`, {
      headers: {
        "apikey": SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`
      }
    });
    
    if (!res.ok) {
      console.error(`❌ Lỗi khi tải bảng ${tableName}:`, res.statusText);
      break;
    }
    
    const data = await res.json();
    if (data.length === 0) break;
    
    allData = allData.concat(data);
    offset += limit;
  }
  
  return allData;
}

async function runBackup() {
  console.log("🚀 BẮT ĐẦU SAO LƯU DỮ LIỆU TỪ SUPABASE...");
  const backupData = {};
  let totalRows = 0;
  
  for (const table of tablesToBackup) {
    process.stdout.write(`Đang tải bảng [${table}]... `);
    backupData[table] = await fetchAllData(table);
    totalRows += backupData[table].length;
    console.log(`✅ Đã tải ${backupData[table].length} dòng.`);
  }
  
  const backupDir = path.join(__dirname, 'backups');
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir);
  }
  
  // Format timestamp: YYYY-MM-DD_HH-MM
  const date = new Date();
  const timestamp = date.toISOString().replace(/T/, '_').replace(/:/g, '-').split('.')[0];
  const filename = path.join(backupDir, `supabase_backup_${timestamp}.json`);
  
  fs.writeFileSync(filename, JSON.stringify(backupData, null, 2));
  console.log(`\n🎉 SAO LƯU THÀNH CÔNG!`);
  console.log(`Tổng cộng: ${totalRows} bản ghi được lưu.`);
  console.log(`File backup: ${filename}`);
  console.log("💡 Bạn có thể chạy lại lệnh 'node backup_supabase.js' bất cứ lúc nào để backup bản mới nhất!");
}

runBackup();
