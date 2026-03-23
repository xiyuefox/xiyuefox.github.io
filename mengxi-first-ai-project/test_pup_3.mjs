import puppeteer from 'puppeteer';
import http from 'http';
import fs from 'fs';
import path from 'path';

// simple server
const server = http.createServer((req, res) => {
  if (req.url === '/') req.url = '/index.html';
  const fp = path.join(process.cwd(), 'public', req.url);
  try {
    const data = fs.readFileSync(fp);
    res.end(data);
  } catch(e) {
    res.statusCode = 404;
    res.end();
  }
});
server.listen(8081, async () => {
  console.log("Server started");
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  page.on('console', msg => console.log('LOG:', msg.text()));
  page.on('pageerror', err => console.log('ERROR:', err.message));
  
  await page.goto('http://127.0.0.1:8081');
  await page.waitForSelector('#explore-btn');
  console.log("Ready to click");
  
  const gateClassBefore = await page.$eval('#poche-gate', e => e.className);
  console.log("before:", gateClassBefore);
  
  await page.click('#explore-btn');
  console.log("Clicked");
  
  await new Promise(r => setTimeout(r, 500));
  const gateClassAfter = await page.$eval('#poche-gate', e => e.className);
  console.log("after:", gateClassAfter);
  
  await browser.close();
  server.close();
});
