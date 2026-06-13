const puppeteer = require('puppeteer');
const { spawn, execSync } = require('child_process');

async function run() {
  console.log('Building...');
  execSync('npm run build', { stdio: 'inherit' });

  console.log('Starting preview server...');
  const server = spawn('npm', ['run', 'preview'], { shell: true });
  
  server.stdout.on('data', (data) => console.log(`Preview: ${data}`));
  server.stderr.on('data', (data) => console.error(`Preview Error: ${data}`));

  await new Promise(r => setTimeout(r, 5000));

  console.log('Starting puppeteer on port 5000...');
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log('BROWSER ERROR:', msg.text());
    }
  });

  page.on('pageerror', error => {
    console.log('PAGE ERROR:', error.message);
  });

  try {
    await page.goto('http://localhost:5000', { waitUntil: 'networkidle2', timeout: 15000 });
    console.log('Page loaded');
    await new Promise(r => setTimeout(r, 5000));
  } catch (e) {
    console.log('Navigation Error:', e.message);
  }
  
  await browser.close();
  server.kill();
  process.exit(0);
}

run();
