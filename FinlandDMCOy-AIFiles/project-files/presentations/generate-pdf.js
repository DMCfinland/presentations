#!/usr/bin/env node
/**
 * Generate PDF from HTML presentation deck
 * Uses Playwright for reliable landscape A4 output
 *
 * Usage:
 *   node generate-pdf.js 04-Lakeland-Summer.html
 *   node generate-pdf.js 04-Lakeland-Summer.html "Finland DMC - Lakeland Summer.pdf"
 *
 * Install first:
 *   npm install playwright
 *   npx playwright install chromium
 */

const { chromium } = require('playwright');
const path = require('path');

const inputFile = process.argv[2];
if (!inputFile) {
    console.error('Usage: node generate-pdf.js <input.html> [output.pdf]');
    process.exit(1);
}

const inputPath = path.resolve(inputFile);
const defaultName = path.basename(inputFile, '.html') + '.pdf';
const outputFile = process.argv[3] || defaultName;
const outputPath = path.resolve(outputFile);

(async () => {
    console.log(`Generating PDF from: ${inputPath}`);
    console.log(`Output: ${outputPath}`);

    const browser = await chromium.launch();
    const page = await browser.newPage();

    await page.goto(`file://${inputPath}`, {
        waitUntil: 'networkidle',
        timeout: 30000
    });

    // Wait for fonts to load
    await page.waitForFunction(() => document.fonts.ready);

    // Wait for all images to load
    await page.waitForFunction(() => {
        const images = document.querySelectorAll('img');
        return Array.from(images).every(img => img.complete);
    });

    await page.pdf({
        path: outputPath,
        format: 'A4',
        landscape: true,
        printBackground: true,
        margin: { top: 0, bottom: 0, left: 0, right: 0 },
        preferCSSPageSize: true
    });

    await browser.close();
    console.log(`PDF generated: ${outputPath}`);
})();
