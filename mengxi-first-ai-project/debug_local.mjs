import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  page.on('console', msg => console.log('LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  await page.goto('https://mengxi.space/', { waitUntil: 'load' });
  
  console.log("Page loaded");
  await new Promise(r => setTimeout(r, 1000));
  
  const hasBtn = await page.$('#explore-btn');
  console.log("Has button:", !!hasBtn);
  
  const gateClassBefore = await page.$eval('#poche-gate', e => e.className).catch(() => 'no-gate');
  console.log("Gate before:", gateClassBefore);
  
  const result = await page.evaluate(() => {
     if(typeof window.forceEnterGarden === 'function') {
         return 'function exists';
     } else {
         return 'function DOES NOT exist';
     }
  });
  console.log("forceEnterGarden status:", result);

  if(hasBtn) {
      await page.click('#explore-btn');
      console.log("Clicked button");
  }

  await new Promise(r => setTimeout(r, 1000));
  const gateClassAfter = await page.$eval('#poche-gate', e => e.className).catch(() => 'no-gate');
  const gateDisplay = await page.$eval('#poche-gate', e => window.getComputedStyle(e).display).catch(() => 'no-gate');
  console.log("Gate after classes:", gateClassAfter);
  console.log("Gate display:", gateDisplay);
  
  await browser.close();
})();
