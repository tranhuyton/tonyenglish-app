const { createCanvas } = require('canvas');
const fs = require('fs');

function generateWordListImage(unitNum, listNum, words, title) {
  const width = 800;
  const rowHeight = 36;
  const headerHeight = 80;
  const height = headerHeight + words.length * rowHeight + 40;
  
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext('2d');

  // Background gradient
  const grad = ctx.createLinearGradient(0, 0, width, height);
  grad.addColorStop(0, '#f0fdf4');
  grad.addColorStop(1, '#ecfdf5');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, width, height);

  // Border
  ctx.strokeStyle = '#86efac';
  ctx.lineWidth = 3;
  ctx.strokeRect(1.5, 1.5, width - 3, height - 3);

  // Header
  ctx.fillStyle = '#166534';
  ctx.font = 'bold 28px Arial';
  ctx.fillText(`Unit ${unitNum} — Word List ${listNum}`, 30, 45);
  
  ctx.fillStyle = '#4ade80';
  ctx.fillRect(30, 60, width - 60, 3);

  // Words
  ctx.font = '18px Arial';
  words.forEach((w, i) => {
    const y = headerHeight + 10 + i * rowHeight;
    
    // Alternating background
    if (i % 2 === 0) {
      ctx.fillStyle = 'rgba(187, 247, 208, 0.3)';
      ctx.fillRect(20, y - 4, width - 40, rowHeight);
    }
    
    // Number
    ctx.fillStyle = '#6b7280';
    ctx.font = 'bold 16px Arial';
    ctx.fillText(`${i + 1}.`, 35, y + 20);
    
    // Word
    ctx.fillStyle = '#15803d';
    ctx.font = 'bold 18px Arial';
    ctx.fillText(w.word, 65, y + 20);
    
    // POS
    ctx.fillStyle = '#9ca3af';
    ctx.font = 'italic 14px Arial';
    const wordWidth = ctx.measureText(w.word).width;
    ctx.fillText(w.pos, 70 + wordWidth + 8, y + 20);
    
    // Short definition
    ctx.fillStyle = '#374151';
    ctx.font = '15px Arial';
    const defX = 250;
    const maxDefWidth = width - defX - 30;
    let defText = w.def;
    if (ctx.measureText(defText).width > maxDefWidth) {
      while (ctx.measureText(defText + '...').width > maxDefWidth && defText.length > 0) {
        defText = defText.slice(0, -1);
      }
      defText += '...';
    }
    ctx.fillText(defText, defX, y + 20);
  });

  return canvas.toBuffer('image/png');
}

function generateStoryImage(unitNum, storyTitle, subtitle) {
  const width = 800;
  const height = 400;
  
  const canvas = createCanvas(width, height);
  const ctx = canvas.getContext('2d');

  // Background gradient
  const grad = ctx.createLinearGradient(0, 0, width, height);
  grad.addColorStop(0, '#fef2f2');
  grad.addColorStop(0.5, '#fff7ed');
  grad.addColorStop(1, '#fefce8');
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, width, height);

  // Decorative border
  ctx.strokeStyle = '#f87171';
  ctx.lineWidth = 4;
  ctx.strokeRect(2, 2, width - 4, height - 4);
  
  ctx.strokeStyle = '#fbbf24';
  ctx.lineWidth = 2;
  ctx.strokeRect(10, 10, width - 20, height - 20);

  // Book icon / decoration
  ctx.fillStyle = '#dc2626';
  ctx.font = '60px Arial';
  ctx.fillText('📖', width / 2 - 35, 100);

  // Title
  ctx.fillStyle = '#991b1b';
  ctx.font = 'bold 36px Arial';
  const titleWidth = ctx.measureText(storyTitle).width;
  ctx.fillText(storyTitle, (width - titleWidth) / 2, 170);

  // Subtitle
  ctx.fillStyle = '#b45309';
  ctx.font = 'italic 22px Arial';
  const subWidth = ctx.measureText(subtitle).width;
  ctx.fillText(subtitle, (width - subWidth) / 2, 210);

  // Unit label
  ctx.fillStyle = '#6b7280';
  ctx.font = '18px Arial';
  const unitLabel = `Unit ${unitNum} — Comprehensive Reading`;
  const labelWidth = ctx.measureText(unitLabel).width;
  ctx.fillText(unitLabel, (width - labelWidth) / 2, 260);

  // Decorative line
  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(200, 280);
  ctx.lineTo(600, 280);
  ctx.stroke();

  // Bottom text
  ctx.fillStyle = '#9ca3af';
  ctx.font = '14px Arial';
  const bottomText = 'Expand Vocabulary Through Reading';
  const bottomWidth = ctx.measureText(bottomText).width;
  ctx.fillText(bottomText, (width - bottomWidth) / 2, 350);

  return canvas.toBuffer('image/png');
}

// Unit 8 words
const u8_words1 = [
  { word: "anniversary", pos: "n.", def: "A day that celebrates something from the past" },
  { word: "arithmetic", pos: "n.", def: "The branch of math dealing with numbers" },
  { word: "ashamed", pos: "adj.", def: "Feeling upset because you did something wrong" },
  { word: "burst", pos: "v.", def: "To suddenly break open or apart" },
  { word: "carpenter", pos: "n.", def: "A person who builds things with wood" },
  { word: "coal", pos: "n.", def: "A hard black rock burned for heat" },
  { word: "couch", pos: "n.", def: "A long, soft seat for many people" },
  { word: "drip", pos: "v.", def: "When liquid falls a little bit at a time" },
  { word: "elegant", pos: "adj.", def: "Very fancy and pleasing in appearance" },
  { word: "fabric", pos: "n.", def: "Cloth used to make clothes, furniture" },
];
const u8_words2 = [
  { word: "highlands", pos: "n.", def: "High areas of land with mountains" },
  { word: "ivory", pos: "n.", def: "White, hard substance from elephants" },
  { word: "mill", pos: "n.", def: "A building where flour is made" },
  { word: "needle", pos: "n.", def: "Small, sharp metal for sewing clothes" },
  { word: "polish", pos: "v.", def: "To rub something to make it shiny" },
  { word: "sew", pos: "v.", def: "To put cloth together using string" },
  { word: "shed", pos: "n.", def: "A small building for storing tools" },
  { word: "thread", pos: "n.", def: "A thin piece of string" },
  { word: "trim", pos: "v.", def: "To cut something a little bit" },
  { word: "upwards", pos: "adv.", def: "Moving vertically higher" },
];

// Unit 9 words
const u9_words1 = [
  { word: "admire", pos: "v.", def: "To like someone for what they do" },
  { word: "aid", pos: "v.", def: "To help someone when they need something" },
  { word: "attempt", pos: "v.", def: "To try to do something" },
  { word: "authority", pos: "n.", def: "Power from one's position" },
  { word: "capital", pos: "n.", def: "City where a country's leaders work" },
  { word: "cooperate", pos: "v.", def: "To work together to do something" },
  { word: "defend", pos: "v.", def: "To protect someone from attack" },
  { word: "destruction", pos: "n.", def: "Damage so bad it can't be fixed" },
  { word: "disorder", pos: "n.", def: "A lack of order, a complete mess" },
  { word: "division", pos: "n.", def: "Making smaller groups from a larger one" },
];
const u9_words2 = [
  { word: "enable", pos: "v.", def: "To make it possible to do something" },
  { word: "frustrate", pos: "v.", def: "To prevent fulfilling one's desire" },
  { word: "govern", pos: "v.", def: "To control public business of a country" },
  { word: "plenty", pos: "n.", def: "More of something than you need" },
  { word: "relieve", pos: "v.", def: "To make someone feel less pain" },
  { word: "reputation", pos: "n.", def: "The opinion people have about someone" },
  { word: "royal", pos: "adj.", def: "Belonging to a king or queen" },
  { word: "slave", pos: "n.", def: "A person not free, must work for others" },
  { word: "struggle", pos: "v.", def: "To fight against someone or something" },
  { word: "stupid", pos: "adj.", def: "Lacking intelligence" },
];

// Unit 10 words
const u10_words1 = [
  { word: "absence", pos: "n.", def: "The state of something being away" },
  { word: "aloud", pos: "adv.", def: "Saying so that others can hear" },
  { word: "bald", pos: "adj.", def: "Having no hair" },
  { word: "blanket", pos: "n.", def: "Cloth used to keep warm" },
  { word: "creep", pos: "v.", def: "To move quietly and slowly" },
  { word: "divorce", pos: "n.", def: "An event ending a marriage" },
  { word: "imitate", pos: "v.", def: "To do exactly what someone else does" },
  { word: "infant", pos: "n.", def: "A baby" },
  { word: "kidnap", pos: "v.", def: "To take someone illegally" },
  { word: "nap", pos: "n.", def: "A short sleep during the day" },
];
const u10_words2 = [
  { word: "nowhere", pos: "adv.", def: "A place that does not exist" },
  { word: "pat", pos: "v.", def: "To hit softly with your hand" },
  { word: "relief", pos: "n.", def: "Feeling when something bad ends" },
  { word: "reproduce", pos: "v.", def: "To make something exactly as before" },
  { word: "rhyme", pos: "n.", def: "Words with same sounds at the end" },
  { word: "suck", pos: "v.", def: "To put in mouth and get flavor" },
  { word: "urgent", pos: "adj.", def: "Important, needs to be done now" },
  { word: "vanish", pos: "v.", def: "To go away suddenly" },
  { word: "wagon", pos: "n.", def: "A cart to carry heavy things" },
  { word: "wrinkle", pos: "n.", def: "A line on face from aging" },
];

// Generate all images
const images = [
  { file: 'public/unit8_ielts_word_list_1.png', buf: generateWordListImage(8, 1, u8_words1, 'Unit 8 Word List 1') },
  { file: 'public/unit8_ielts_word_list_2.png', buf: generateWordListImage(8, 2, u8_words2, 'Unit 8 Word List 2') },
  { file: 'public/unit8_ielts_story.png', buf: generateStoryImage(8, 'The Anniversary Gift', 'A story of love, sacrifice, and surprising gifts') },
  { file: 'public/unit9_ielts_word_list_1.png', buf: generateWordListImage(9, 1, u9_words1, 'Unit 9 Word List 1') },
  { file: 'public/unit9_ielts_word_list_2.png', buf: generateWordListImage(9, 2, u9_words2, 'Unit 9 Word List 2') },
  { file: 'public/unit9_ielts_story.png', buf: generateStoryImage(9, 'The Tale of Bartelby O\'Boyle', 'A brave man who aided the poor') },
  { file: 'public/unit10_ielts_word_list_1.png', buf: generateWordListImage(10, 1, u10_words1, 'Unit 10 Word List 1') },
  { file: 'public/unit10_ielts_word_list_2.png', buf: generateWordListImage(10, 2, u10_words2, 'Unit 10 Word List 2') },
  { file: 'public/unit10_ielts_story.png', buf: generateStoryImage(10, 'Anna the Babysitter', 'A surprising afternoon with baby Grace') },
];

images.forEach(img => {
  fs.writeFileSync(img.file, img.buf);
  console.log(`✅ Created ${img.file}`);
});

console.log('\n🎉 All 9 images generated!');
