const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://mengxi.space/');
  
  // wait 1 second to see the text
  await page.waitForTimeout(1000);
  const textBefore = await page.locator('.gate-title').innerText();
  console.log("Text at 1s:", textBefore);

  await page.waitForTimeout(1500);
  const gateDisplay = await page.locator('.poche-gate').evaluate(el => window.getComputedStyle(el).display);
  const gateTransform = await page.locator('.poche-gate').evaluate(el => window.getComputedStyle(el).transform);
  const gateClass = await page.locator('.poche-gate').getAttribute('class');
  
  console.log("Gate Display at 2.5s:", gateDisplay);
  console.log("Gate Transform at 2.5s:", gateTransform);
  console.log("Gate Class at 2.5s:", gateClass);

  await browser.close();
})();
