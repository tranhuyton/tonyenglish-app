const puppeteer = require('puppeteer');
const { spawn } = require('child_process');

async function run() {
  const server = spawn('npm', ['run', 'dev'], { shell: true });
  
  server.stdout.on('data', (data) => {
    console.log(`Server: ${data}`);
  });

  server.stderr.on('data', (data) => {
    console.error(`Server Error: ${data}`);
  });

  console.log('Waiting 5 seconds for server to start...');
  await new Promise(r => setTimeout(r, 5000));

  console.log('Starting puppeteer...');
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log('BROWSER ERROR:', msg.text());
    } else {
      console.log('BROWSER LOG:', msg.text());
    }
  });

  page.on('pageerror', error => {
    console.log('PAGE ERROR:', error.message);
  });

  try {
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle2', timeout: 15000 });
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
