const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const baseDir = 'F:\\Downloads\\Chrome\\Geo Podcast\\Final';
const enDir = path.join(baseDir, 'English podcast', 'Audio');
const viDir = path.join(baseDir, 'Vietnamese podcast');

const rawMapping = [
  {
    episode: 1,
    code: '1.1',
    group: 'Physical geography',
    topic: 'Changing river environments',
    syllabusTitle: 'The main hydrological characteristics and processes that operate in rivers and drainage basins',
    viOld: '07-Cách dòng sông điêu khắc Trái Đất.mp3',
    enOld: '30-Why Calm Rivers Flow Faster Than Rapids.mp3'
  },
  {
    episode: 2,
    code: '1.2',
    group: 'Physical geography',
    topic: 'Changing river environments',
    syllabusTitle: 'The main landforms associated with these processes',
    viOld: '09-Dòng sông kiến tạo địa hình.mp3',
    enOld: '25-How Rivers Carve Mountains into Deltas.mp3'
  },
  {
    episode: 3,
    code: '1.3',
    group: 'Physical geography',
    topic: 'Changing river environments',
    syllabusTitle: 'Rivers present opportunities and hazards for people',
    viOld: '01-Trả lại không gian cho dòng sông.mp3',
    enOld: '02-Why Living Near Rivers Is Dangerous.mp3'
  },
  {
    episode: 4,
    code: '2.1',
    group: 'Physical geography',
    topic: 'Changing coastal environments',
    syllabusTitle: 'The physical processes that shape the coast',
    viOld: '03-Đại dương điêu khắc bờ biển.mp3',
    enOld: '29-How Waves Carve and Build Coastlines.mp3'
  },
  {
    episode: 5,
    code: '2.2',
    group: 'Physical geography',
    topic: 'Changing coastal environments',
    syllabusTitle: 'The main landforms associated with these processes',
    viOld: '10-Sóng biển định hình bờ biển.mp3',
    enOld: '07-How Waves Destroy and Rebuild Coastlines.mp3'
  },
  {
    episode: 6,
    code: '2.3',
    group: 'Physical geography',
    topic: 'Changing coastal environments',
    syllabusTitle: 'Coasts present opportunities and hazards for people',
    viOld: '02-Cuộc chiến giữ đất ven biển.mp3',
    enOld: '01-Concrete Sea Walls Versus Natural Defenses.mp3'
  },
  {
    episode: 7,
    code: '3.1',
    group: 'Physical geography',
    topic: 'Changing ecosystems',
    syllabusTitle: 'The characteristics of the Antarctic ecosystem',
    viOld: '08-Nghịch lý sự sống Nam Cực.mp3',
    enOld: '27-Antarctica\'s Extreme Biology and Climate Engine.mp3'
  },
  {
    episode: 8,
    code: '3.2',
    group: 'Physical geography',
    topic: 'Changing ecosystems',
    syllabusTitle: 'The threats to the Antarctic ecosystem and how they can be managed',
    viOld: '10-Bom hẹn giờ sinh thái Nam Cực.mp3',
    enOld: '10-Why It Is Raining in Antarctica.mp3'
  },
  {
    episode: 9,
    code: '3.3',
    group: 'Physical geography',
    topic: 'Changing ecosystems',
    syllabusTitle: 'The characteristics of the tropical rainforest ecosystem',
    viOld: '13-Nghịch lý đất cằn ở rừng mưa.mp3',
    enOld: '06-How Rainforests Thrive on Infertile Soil.mp3'
  },
  {
    episode: 10,
    code: '3.4',
    group: 'Physical geography',
    topic: 'Changing ecosystems',
    syllabusTitle: 'The threats to the tropical rainforest ecosystem and how they can be managed',
    viOld: '14-Vì sao rừng mưa Amazon biến mất.mp3',
    enOld: '21-Rainforest Deforestation and the Borneo Blueprint.mp3'
  },
  {
    episode: 11,
    code: '4.1',
    group: 'Physical geography',
    topic: 'Tectonic hazards',
    syllabusTitle: 'The structure of the Earth and the distribution of earthquakes and volcanoes',
    viOld: '14-Lòng Trái Đất và mảng kiến tạo.mp3',
    enOld: '28-How Gravity and Heat Move Continents.mp3'
  },
  {
    episode: 12,
    code: '4.2',
    group: 'Physical geography',
    topic: 'Tectonic hazards',
    syllabusTitle: 'The processes and features associated with earthquakes and volcanoes',
    viOld: '19-Cơ chế động đất và núi lửa.mp3',
    enOld: '15-What Drives Earthquakes and Volcanoes.mp3'
  },
  {
    episode: 13,
    code: '4.3',
    group: 'Physical geography',
    topic: 'Tectonic hazards',
    syllabusTitle: 'The impact of tectonic hazards',
    viOld: '04-Giàu nghèo trước thảm họa kiến tạo.mp3',
    enOld: '14-Why Millions Settle on Active Fault Lines.mp3'
  },
  {
    episode: 14,
    code: '4.4',
    group: 'Physical geography',
    topic: 'Tectonic hazards',
    syllabusTitle: 'Managing the impacts of tectonic hazards',
    viOld: '03-Sinh tồn trước thảm họa địa chất.mp3',
    enOld: '04-Engineering Survival Against Earthquakes and Volcanoes.mp3'
  },
  {
    episode: 15,
    code: '5.1',
    group: 'Physical geography',
    topic: 'Climate change',
    syllabusTitle: 'The natural and human causes of climate change',
    viOld: '12-Cơ chế làm Trái Đất nóng lên.mp3',
    enOld: '12-The Physics of Human Climate Change.mp3'
  },
  {
    episode: 16,
    code: '5.2',
    group: 'Physical geography',
    topic: 'Climate change',
    syllabusTitle: 'The impacts of climate change at a range of geographic scales',
    viOld: '02-Trái Đất sốt và đại dương dâng.mp3',
    enOld: '26-How Extreme Heat Destroys Coasts and Crops.mp3'
  },
  {
    episode: 17,
    code: '5.3',
    group: 'Physical geography',
    topic: 'Climate change',
    syllabusTitle: 'The responses to climate change',
    viOld: '09-Giảm thiểu và thích ứng khí hậu.mp3',
    enOld: '31-Global Climate Treaties and Bangladesh Adaptation.mp3'
  },
  {
    episode: 18,
    code: '6.1',
    group: 'Human geography',
    topic: 'Changing populations',
    syllabusTitle: 'Populations grow and decline',
    viOld: '11-Bùng nổ và suy giảm dân số.mp3',
    enOld: '13-From Eight Billion to Population Collapse.mp3'
  },
  {
    episode: 19,
    code: '6.2',
    group: 'Human geography',
    topic: 'Changing populations',
    syllabusTitle: 'Population structures change over time',
    viOld: '18-Tháp dân số định hình kinh tế.mp3',
    enOld: '24-How Population Pyramids Dictate Economic Destiny.mp3'
  },
  {
    episode: 20,
    code: '6.3',
    group: 'Human geography',
    topic: 'Changing populations',
    syllabusTitle: 'The causes and impacts of international migration',
    viOld: '12-Đằng sau 281 triệu người di cư.mp3',
    enOld: '05-The Hidden Mechanics of Global Migration.mp3'
  },
  {
    episode: 21,
    code: '7.1',
    group: 'Human geography',
    topic: 'Changing towns and cities',
    syllabusTitle: 'Where people live',
    viOld: '05-Nghịch lý phân bố dân số.mp3',
    enOld: '32-Why People Are Abandoning Cities.mp3'
  },
  {
    episode: 22,
    code: '7.2',
    group: 'Human geography',
    topic: 'Changing towns and cities',
    syllabusTitle: 'The opportunities and challenges of urbanisation',
    viOld: '15-Cái giá của đô thị hóa.mp3',
    enOld: '34-Is the Modern City Broken.mp3'
  },
  {
    episode: 23,
    code: '7.3',
    group: 'Human geography',
    topic: 'Changing towns and cities',
    syllabusTitle: 'The management of urban growth',
    viOld: '06-Phát triển đô thị bền vững.mp3',
    enOld: '19-How Cities Manage Rapid Urban Growth.mp3'
  },
  {
    episode: 24,
    code: '8.1',
    group: 'Human geography',
    topic: 'Development',
    syllabusTitle: 'Measuring development',
    viOld: '20-Điểm mù chỉ số phát triển.mp3',
    enOld: '16-How Global Development Is Actually Measured.mp3'
  },
  {
    episode: 25,
    code: '8.2',
    group: 'Human geography',
    topic: 'Development',
    syllabusTitle: 'The world is developing unevenly',
    viOld: '06-Vì sao nước nghèo khó vươn lên.mp3',
    enOld: '33-Why Global Development Is So Uneven.mp3'
  },
  {
    episode: 26,
    code: '8.3',
    group: 'Human geography',
    topic: 'Development',
    syllabusTitle: 'Achieving sustainable development',
    viOld: '01-Cái bẫy viện trợ quốc tế.mp3',
    enOld: '23-Why Wealth Protects Local Nature But Destroys Climate.mp3'
  },
  {
    episode: 27,
    code: '9.1',
    group: 'Human geography',
    topic: 'Changing economies',
    syllabusTitle: 'Changing employment structures',
    viOld: '16-Tương lai bốn khu vực kinh tế.mp3',
    enOld: '20-How Global Employment Structures Shift.mp3'
  },
  {
    episode: 28,
    code: '9.2',
    group: 'Human geography',
    topic: 'Changing economies',
    syllabusTitle: 'The impact of globalisation and the role of transnational corporations',
    viOld: '17-Bên trong cỗ máy toàn cầu hóa.mp3',
    enOld: '11-How Transnational Corporations Control Sovereign Nations.mp3'
  },
  {
    episode: 29,
    code: '9.3',
    group: 'Human geography',
    topic: 'Changing economies',
    syllabusTitle: 'Tourism is a growing industry',
    viOld: '15-Cái giá của du lịch đại chúng.mp3',
    enOld: '18-Where Your Vacation Money Really Goes.mp3'
  },
  {
    episode: 30,
    code: '10.1',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'How our food is produced',
    viOld: '08-Cỗ máy nông nghiệp vận hành thế nào.mp3',
    enOld: '17-The Mechanics of Food Production.mp3'
  },
  {
    episode: 31,
    code: '10.2',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'The global patterns of food supply and demand',
    viOld: '05-Nghịch lý hệ thống lương thực toàn cầu.mp3',
    enOld: '22-Why We Are Actually Eating Oil.mp3'
  },
  {
    episode: 32,
    code: '10.3',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'The challenges of food supply',
    viOld: '11-Nghịch lý nạn đói toàn cầu.mp3',
    enOld: '08-Why Food Abundance Leaves Millions Hungry.mp3'
  },
  {
    episode: 33,
    code: '10.4',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'How our energy is produced',
    viOld: '07-Thực tế cuộc chuyển dịch năng lượng.mp3',
    enOld: '09-Why We Burn More Oil Than Ever.mp3'
  },
  {
    episode: 34,
    code: '10.5',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'The global patterns of energy supply and demand',
    viOld: '04-Bàn cờ an ninh năng lượng.mp3',
    enOld: '35-Energy Poverty and the Renewable Transition.mp3'
  },
  {
    episode: 35,
    code: '10.6',
    group: 'Human geography',
    topic: 'Resource provision',
    syllabusTitle: 'The impacts of energy production',
    viOld: '13-Cái giá của chuyển dịch năng lượng.mp3',
    enOld: '03-Rebuilding the Global Power Grid.mp3'
  }
];

function getDuration(filePath) {
  try {
    const out = execSync(`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${filePath}"`, { encoding: 'utf-8' });
    const sec = parseFloat(out.trim());
    return Math.round(sec);
  } catch (err) {
    console.error('Duration probe failed for', filePath, err.message);
    return 1200;
  }
}

function formatDuration(sec) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${m}:${s < 10 ? '0' : ''}${s}`;
}

function cleanBaseTitle(oldFilename) {
  // Removes leading digits and hyphen, e.g. "07-Cách dòng..." -> "Cách dòng..."
  return oldFilename.replace(/^\d+[-_]?\s*/, '').replace(/\.mp3$/i, '').trim();
}

console.log('Probing durations and constructing manifest...');

const manifest = rawMapping.map(item => {
  const viOldPath = path.join(viDir, item.viOld);
  const enOldPath = path.join(enDir, item.enOld);

  if (!fs.existsSync(viOldPath)) throw new Error('Missing VI: ' + viOldPath);
  if (!fs.existsSync(enOldPath)) throw new Error('Missing EN: ' + enOldPath);

  const durVi = getDuration(viOldPath);
  const durEn = getDuration(enOldPath);

  const titleVi = cleanBaseTitle(item.viOld);
  const titleEn = cleanBaseTitle(item.enOld);

  const viNewFile = `${item.code}-${titleVi}.mp3`;
  const enNewFile = `${item.code}-${titleEn}.mp3`;

  const epStr = item.episode < 10 ? `0${item.episode}` : `${item.episode}`;
  const storageFileName = `ep_${epStr}.mp3`;

  return {
    episode: item.episode,
    code: item.code,
    group: item.group,
    topic: item.topic,
    syllabusTitle: item.syllabusTitle,
    titleVi: titleVi,
    titleEn: titleEn,
    viOldFile: item.viOld,
    enOldFile: item.enOld,
    newViFile: viNewFile,
    newEnFile: enNewFile,
    storageFileName: storageFileName,
    audioUrlVi: `https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/podcast/geography-0460/${storageFileName}`,
    audioUrlEn: `https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets/audio/podcast/geography-0460-en/${storageFileName}`,
    durationViSec: durVi,
    durationEnSec: durEn,
    durationViStr: formatDuration(durVi),
    durationEnStr: formatDuration(durEn)
  };
});

fs.writeFileSync('scripts/geography_0460_podcast_manifest.json', JSON.stringify(manifest, null, 2), 'utf-8');
console.log('Saved manifest: scripts/geography_0460_podcast_manifest.json');

// Safe two-phase rename
console.log('\n--- Renaming Vietnamese files in 2 phases ---');
// Phase 1: rename to temp
manifest.forEach(item => {
  const cur = path.join(viDir, item.viOldFile);
  const tmp = path.join(viDir, `__temp_${item.episode}__.mp3`);
  fs.renameSync(cur, tmp);
});
// Phase 2: rename from temp to final target
manifest.forEach(item => {
  const tmp = path.join(viDir, `__temp_${item.episode}__.mp3`);
  const fin = path.join(viDir, item.newViFile);
  fs.renameSync(tmp, fin);
  console.log(`[VI] ${item.viOldFile} -> ${item.newViFile}`);
});

console.log('\n--- Renaming English files in 2 phases ---');
manifest.forEach(item => {
  const cur = path.join(enDir, item.enOldFile);
  const tmp = path.join(enDir, `__temp_${item.episode}__.mp3`);
  fs.renameSync(cur, tmp);
});
manifest.forEach(item => {
  const tmp = path.join(enDir, `__temp_${item.episode}__.mp3`);
  const fin = path.join(enDir, item.newEnFile);
  fs.renameSync(tmp, fin);
  console.log(`[EN] ${item.enOldFile} -> ${item.newEnFile}`);
});

console.log('\n🎉 ALL 70 FILES RENAMED WITH STANDARDIZED PREFIXES 1.1- to 10.6-!');
