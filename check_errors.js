const puppeteer = require('puppeteer');

async function run() {
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
    await page.goto('http://localhost:5173', { waitUntil: 'networkidle2', timeout: 15000 });
    console.log('Page loaded');
    // Wait a bit to see if any runtime error happens
    await new Promise(r => setTimeout(r, 3000));
  } catch (e) {
    console.log('Error navigating:', e.message);
  }
  
  await browser.close();
}

run();
