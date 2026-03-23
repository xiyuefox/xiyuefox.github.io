import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  page.on('console', msg => console.log('LOG:', msg.text()));
  
  await page.goto('https://mengxi.space/', { waitUntil: 'load' });
  
  await new Promise(r => setTimeout(r, 1000));
  
  const box = await page.$eval('#explore-btn', el => {
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      return {
          x: rect.x, y: rect.y, width: rect.width, height: rect.height,
          pointerEvents: style.pointerEvents, zIndex: style.zIndex, display: style.display
      };
  });
  console.log("Button layout:", box);
  
  const gateBefore = await page.$eval('#poche-gate', e => e.className);
  console.log("Gate before:", gateBefore);

  await page.click('#explore-btn');
  
  await new Promise(r => setTimeout(r, 1000));
  const gateAfter = await page.$eval('#poche-gate', e => e.className);
  console.log("Gate after:", gateAfter);

  await browser.close();
})();
