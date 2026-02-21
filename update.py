import os
import re

html_path = 'index.html'
js_path = 'assets/js/main.js'
css_path = 'assets/css/style.css'

# 1. Update index.html
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove skills nav link
html = re.sub(r'<li><a href="#skills".*?</li>\s*', '', html)

# Remove skills section
html = re.sub(r'<!-- Skills Section -->[\s\S]*?<!-- Projects / Evidence Board -->', '<!-- Projects / Evidence Board -->', html)

# Replace projects grid with 20 items
import typing
cards: typing.List[str] = []
for i in range(1, 21):
    tilt = 'tilt-left' if i % 2 != 0 else 'tilt-right'
    delay = f' style="transition-delay: {0.2 * ((i-1)%3)}s;"' if i > 1 else ''
    card = f'''
                    <!-- Project {i} -->
                    <div class="project-card evidence-card reveal {tilt}"{delay}>
                        <div class="pushpin"></div>
                        <div class="project-img-container">
                            <img src="assets/img/project{i}.jpg" alt="Project {i}" class="evidence-photo" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <div class="project-img redacted-img" style="display: none;">
                                <span class="redacted-text" data-i18n="proj_confidential">ลับสุดยอด</span>
                            </div>
                        </div>
                        <div class="project-info">
                            <span class="mono-label" data-i18n="proj_{i}_label">แฟ้ม #{i}</span>
                            <h3 class="project-title" data-i18n="proj_{i}_title">ชื่อผลงานที่ {i}</h3>
                            <p class="project-desc" data-i18n="proj_{i}_desc">คำอธิบายภาพและผลงานที่ {i}</p>
                        </div>
                    </div>'''
    cards.append(card)

projects_html = f'''
                <div class="carousel-wrapper">
                    <button class="carousel-btn prev-btn" aria-label="Previous">❮</button>
                    <div class="projects-carousel">{''.join(cards)}
                    </div>
                    <button class="carousel-btn next-btn" aria-label="Next">❯</button>
                </div>
'''

html = re.sub(r'<div class="projects-grid">[\s\S]*?</div>\s*</div>\s*</section>', projects_html + '\n            </div>\n        </section>', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/*--------------------------------------------------------------
# Projects / Evidence Section (Carousel)
--------------------------------------------------------------*/
.carousel-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.projects-carousel {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    gap: 2.5rem;
    padding: 2rem 10px;
    width: 100%;
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
}
.projects-carousel::-webkit-scrollbar {
    display: none;
}

.project-card {
    flex: 0 0 calc(33.333% - 1.666rem);
    min-width: 320px;
    scroll-snap-align: start;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
}

.carousel-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: var(--card-bg);
    color: var(--accent-gold);
    border: 2px solid var(--accent-gold);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.carousel-btn:hover {
    background: var(--accent-gold);
    color: var(--bg-color);
    transform: translateY(-50%) scale(1.1);
}

.prev-btn { left: -25px; }
.next-btn { right: -25px; }

@media (max-width: 1200px) {
    .project-card {
        flex: 0 0 calc(50% - 1.25rem);
    }
}
@media (max-width: 768px) {
    .project-card {
        flex: 0 0 100%;
        min-width: unset;
    }
    .prev-btn { left: 5px; }
    .next-btn { right: 5px; }
    .projects-carousel { padding-left: 0; padding-right: 0; }
}
'''
css = re.sub(r'/\*--------------------------------------------------------------\n# Projects / Evidence Section[\s\S]*?(?=/\*--------------------------------------------------------------\n# Experience / Timeline)', new_css + '\n', css)

# remove skills css
css = re.sub(r'/\*--------------------------------------------------------------\n# Skills / Tools Section[\s\S]*?(?=/\*--------------------------------------------------------------\n# Projects)', '', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update main.js
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Add 20 translations
en_proj = ',\n'.join([f'        proj_{i}_label: "FILE #{100+i}",\n        proj_{i}_title: "Evidence Image {i}",\n        proj_{i}_desc: "Description or notes regarding the evidence piece number {i}."' for i in range(1, 21)])
th_proj = ',\n'.join([f'        proj_{i}_label: "แฟ้ม #{100+i}",\n        proj_{i}_title: "รูปผลงานที่ {i}",\n        proj_{i}_desc: "คำอธิบายรายละเอียดผลงานชิ้นที่ {i} นี่คือที่สำหรับพิมพ์ข้อความบอกเล่าเรื่องราวการออกแบบหรือระบบที่คุณพัฒนาขึ้นมา."' for i in range(1, 21)])

js = re.sub(r'proj_1_label[\s\S]*?btn_src: "Source Code",', en_proj + ',', js)
js = re.sub(r'proj_1_label[\s\S]*?btn_src: "ดูซอร์สโค้ด",', th_proj + ',', js)

# Add carousel JS
carousel_js = '''
    // 9. Carousel Logic
    const carousel = document.querySelector('.projects-carousel');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if(carousel && prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({ left: -cardWidth, behavior: 'smooth' });
        });
        nextBtn.addEventListener('click', () => {
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({ left: cardWidth, behavior: 'smooth' });
        });
    }
'''

js += carousel_js

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Update completed.")
