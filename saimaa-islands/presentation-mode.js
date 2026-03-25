/**
 * Finland DMC — Presentation Mode v3.1
 * Updated: 2026-03-11 (Grok 4.20 review round 2)
 *
 * v3.1 fixes: proper fade (visibility+absolute, not display:none),
 *   overview as fixed container (not body class), focal-point defaults,
 *   adjacent slide preloading, reduced-motion support
 *
 * Keys:
 *   P / F5  — enter fullscreen presentation (420ms fade)
 *   Escape  — exit presentation
 *   Arrows / Space — navigate slides
 *   Home / End — first / last slide
 *   O — thumbnail overview (click to jump)
 *   Touch swipe left/right (mobile)
 *
 * HTML required:
 *   <div id="slide-counter" class="slide-counter"></div>
 *   <div id="overview-container" class="overview-container"></div>
 *   <script src="presentation-mode.js"></script>
 *
 * Requires template-styles-v3.css (v3.1+).
 */

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const counter = document.getElementById('slide-counter');
    const overviewEl = document.getElementById('overview-container');
    let current = 0;
    let touchStartX = 0;
    let overviewBuilt = false;

    // --- Focal Point Defaults by Slide Type ---
    const focalDefaults = {
        'slide-cover':      { x: '50%', y: '35%' },
        'slide-impact':     { x: '50%', y: '35%' },
        'slide-stats':      { x: '40%', y: '50%' },
        'slide-content-lr': { x: '65%', y: '45%' },
        'slide-content-rl': { x: '35%', y: '45%' },
        'slide-activities': { x: '50%', y: '50%' },
        'slide-testimonial':{ x: '50%', y: '50%' }
    };

    // Apply defaults to images without explicit --focal-x/y
    slides.forEach(slide => {
        const slideType = Array.from(slide.classList).find(c => c.startsWith('slide-'));
        const defaults = focalDefaults[slideType];
        if (!defaults) return;
        slide.querySelectorAll('img').forEach(img => {
            if (!img.style.getPropertyValue('--focal-x')) {
                img.style.setProperty('--focal-x', defaults.x);
                img.style.setProperty('--focal-y', defaults.y);
            }
        });
    });

    // --- Core Navigation ---

    function enterPresentation() {
        if (overviewEl) overviewEl.classList.remove('active');
        document.body.classList.add('presenting');
        slides.forEach((s, i) => s.classList.toggle('active', i === current));
        updateCounter();
        preloadAdjacent();
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        }
    }

    function exitPresentation() {
        document.body.classList.remove('presenting');
        if (overviewEl) overviewEl.classList.remove('active');
        slides.forEach(s => s.classList.remove('active'));
        if (document.fullscreenElement) {
            document.exitFullscreen();
        }
    }

    function goTo(n) {
        current = Math.max(0, Math.min(n, slides.length - 1));
        slides.forEach((s, i) => s.classList.toggle('active', i === current));
        updateCounter();
        preloadAdjacent();
    }

    function updateCounter() {
        if (counter) counter.textContent = (current + 1) + ' / ' + slides.length;
    }

    // --- Preload Adjacent Slides ---

    function preloadAdjacent() {
        [current - 1, current + 1].forEach(idx => {
            if (idx < 0 || idx >= slides.length) return;
            slides[idx].querySelectorAll('img[loading="lazy"]').forEach(img => {
                img.loading = 'eager';
            });
        });
    }

    // --- Thumbnail Overview (fixed container) ---

    function buildOverview() {
        if (!overviewEl || overviewBuilt) return;
        overviewBuilt = true;

        slides.forEach((slide, i) => {
            const thumb = document.createElement('div');
            thumb.className = 'slide-thumb' + (i === current ? ' current' : '');

            // Try to get a background image for the thumbnail
            const bgEl = slide.querySelector('[style*="background-image"]');
            const bgImg = slide.style.backgroundImage || (bgEl ? bgEl.style.backgroundImage : '');
            if (bgImg && bgImg !== 'none') {
                thumb.style.backgroundImage = bgImg;
            } else {
                thumb.style.background = '#F8F4ED';
            }

            // Label with slide title
            const label = document.createElement('div');
            label.className = 'thumb-label';
            const heading = slide.querySelector('h1, h2');
            label.textContent = (i + 1) + '. ' + (heading
                ? heading.textContent.replace(/\s+/g, ' ').trim().slice(0, 40)
                : 'Slide ' + (i + 1));
            thumb.appendChild(label);

            thumb.addEventListener('click', () => {
                current = i;
                overviewEl.classList.remove('active');
                enterPresentation();
            });

            overviewEl.appendChild(thumb);
        });
    }

    function toggleOverview() {
        if (!overviewEl) return;
        if (overviewEl.classList.contains('active')) {
            overviewEl.classList.remove('active');
            enterPresentation();
        } else {
            document.body.classList.remove('presenting');
            buildOverview();
            overviewEl.querySelectorAll('.slide-thumb').forEach((t, i) => {
                t.classList.toggle('current', i === current);
            });
            overviewEl.classList.add('active');
        }
    }

    // --- Keyboard ---

    document.addEventListener('keydown', (e) => {
        const inOverview = overviewEl && overviewEl.classList.contains('active');
        const inPresenting = document.body.classList.contains('presenting');

        // Enter presentation
        if (e.key === 'F5' || (e.key === 'p' && !e.ctrlKey && !e.metaKey && !inPresenting && !inOverview)) {
            e.preventDefault();
            enterPresentation();
            return;
        }

        // Toggle overview
        if (e.key === 'o' && !e.ctrlKey && !e.metaKey && (inPresenting || inOverview)) {
            e.preventDefault();
            toggleOverview();
            return;
        }

        // Exit
        if (e.key === 'Escape') {
            if (inOverview) {
                overviewEl.classList.remove('active');
                enterPresentation();
            } else {
                exitPresentation();
            }
            return;
        }

        // Navigate (only in presentation mode)
        if (!inPresenting) return;

        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'ArrowDown') {
            e.preventDefault();
            goTo(current + 1);
        }
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            e.preventDefault();
            goTo(current - 1);
        }
        if (e.key === 'Home') goTo(0);
        if (e.key === 'End') goTo(slides.length - 1);
    });

    // --- Click ---

    document.addEventListener('click', (e) => {
        if (overviewEl && overviewEl.contains(e.target)) return;
        if (document.body.classList.contains('presenting')) {
            goTo(current + 1);
        }
    });

    // --- Touch / Swipe ---

    document.addEventListener('touchstart', (e) => {
        if (!document.body.classList.contains('presenting')) return;
        touchStartX = e.touches[0].clientX;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
        if (!document.body.classList.contains('presenting')) return;
        const touchEndX = e.changedTouches[0].clientX;
        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) goTo(current + 1);
            else goTo(current - 1);
        }
    }, { passive: true });

    // --- beforeprint ---

    window.addEventListener('beforeprint', () => {
        const titleEl = document.querySelector('title');
        if (titleEl) document.title = titleEl.textContent;
    });
});
