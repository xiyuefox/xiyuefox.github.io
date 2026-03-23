import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  // Log all console messages
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

  await page.goto('http://127.0.0.1:8080', { waitUntil: 'load' });
  
  await new Promise(r => setTimeout(r, 2000));
  
  // Click explore button
  await page.click('#explore-btn');
  
  await new Promise(r => setTimeout(r, 1000));
  
  const gateClasses = await page.$eval('#poche-gate', el => el.className);
  
  console.log('--- STATUS ---');
  console.log('gate classes: ', gateClasses);

  await browser.close();
})();
