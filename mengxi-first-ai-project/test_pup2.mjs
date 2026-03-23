import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));

  await page.goto('http://127.0.0.1:8080', { waitUntil: 'load' });
  
  await new Promise(r => setTimeout(r, 1000));
  
  // click explore button
  try {
    console.log("clicking explore button");
    await page.click('#explore-btn');
    await new Promise(r => setTimeout(r, 1000));
    
    const gateDisplay = await page.$eval('#poche-gate', el => window.getComputedStyle(el).display);
    const gateTransform = await page.$eval('#poche-gate', el => window.getComputedStyle(el).transform);
    console.log('gate display: ', gateDisplay);
    console.log('gate transform: ', gateTransform);
  } catch(e) {
    console.log("error clicking: ", e.message);
  }

  await browser.close();
})();
