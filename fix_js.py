import codecs

en_projects = ""
th_projects = ""
for i in range(1, 21):
    en_projects += f'        proj_{i}_label: "FILE #{100+i}",\n'
    en_projects += f'        proj_{i}_title: "Evidence Photo {i}",\n'
    en_projects += f'        proj_{i}_desc: "Description or notes regarding the evidence piece number {i}.",\n'
    
    th_projects += f'        proj_{i}_label: "แฟ้ม #{100+i}",\n'
    th_projects += f'        proj_{i}_title: "รูปผลงานที่ {i}",\n'
    th_projects += f'        proj_{i}_desc: "คำอธิบายรายละเอียดผลงานชิ้นที่ {i} นี่คือที่สำหรับพิมพ์ข้อความบอกเล่าเรื่องราวการออกแบบหรือระบบที่คุณพัฒนาขึ้นมา",\n'

js_content = f'''/*==================================================================
  DETECTIVE OS / CLASSIFIED DOSSIER - MAIN JAVASCRIPT
===================================================================*/

/* Language Dictionary */
const i18n = {{
    en: {{
        title: "Investigator Portfolio | Classified Dossier",
        desc: "Confidential evidence files and project dossier of a Senior Front-end Developer.",
        nav_about: "Subject Profile",
        nav_projects: "Evidence Board",
        nav_history: "Case History",
        nav_contact: "Send Clue",
        status_active: "STATUS: ACTIVE",
        hero_title: "CLASSIFIED<br><span class='highlight'>DEVELOPER</span>",
        hero_subtitle: "I solve digital mysteries and architect high-performance front-end solutions.",
        hero_cta_1: "<span class='btn-text'>Examine Evidence</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><polyline points='9 18 15 12 9 6'></polyline></svg>",
        hero_cta_2: "Contact Operator",
        about_label: "// FILE #X-01",
        about_title: "Subject Profile",
        about_alias: "> <strong>ALIAS:</strong> [Your Name / Placeholder]<br>> <strong>ROLE:</strong> Senior Front-end Investigator<br>> <strong>BASE_OF_OPS:</strong> [Your City / Remote]<br>> <strong>CLEARANCE:</strong> Level 5 (Senior)",
        about_bio: "Suspect possesses highly advanced skills in crafting pixel-perfect web interfaces. Known to formulate robust UI architectures and investigate complex bugs deep within legacy systems. Approaches code like a crime scene—leaving no stone unturned and fully optimizing every performance bottleneck.",
        about_verified: "Verified by:",
        about_director: "Director of Engineering",
        stat_years: "Years of<br>Investigation",
        stat_cases: "Cases<br>Solved",
        projects_label: "// EXHIBIT A-T",
        projects_title: "Evidence Board",
        proj_confidential: "CONFIDENTIAL",
{en_projects.rstrip(',\\n')}
        hist_label: "// TIMELINE",
        hist_title: "Case History",
        hist_1_title: "Lead Front-End Investigator",
        hist_1_date: "2023 - Present",
        hist_1_comp: "Agency X (Tech Corp)",
        hist_1_desc1: "Headed a squad of junior detectives to refactor a massive monolith into performant micro-frontends.",
        hist_1_desc2: "Investigated and resolved critical UI rendering bottlenecks, improving load time by 40%.",
        hist_1_desc3: "Established continuous interrogation (CI/CD) pipelines for front-end assets.",
        hist_2_title: "UI/UX Specialist Agent",
        hist_2_date: "2020 - 2023",
        hist_2_comp: "Solving Bugs Inc.",
        hist_2_desc1: "Translated obscure design drafts into pixel-perfect responsive reality.",
        hist_2_desc2: "Integrated RESTful APIs, cracking the data communication barrier.",
        contact_label: "// SECURE COMM",
        contact_title: "Drop a Clue",
        contact_tab: "CONFIDENTIAL",
        contact_warn: "<strong>WARNING:</strong> This is a secure channel. Provide your informant details and Intel below.",
        form_name: "Alias (Name)",
        form_name_ph: "John/Jane Doe",
        form_email: "Comm Link (Email)",
        form_email_ph: "informant@agency.com",
        form_msg: "Intel (Message)",
        form_msg_ph: "I have a case for you...",
        form_btn: "<span class='btn-text'>Transmit Signal</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><line x1='22' y1='2' x2='11' y2='13'></line><polygon points='22 2 15 22 11 13 2 9 22 2'></polygon></svg>",
        footer_copy: "All rights reserved. Encrypted connection active."
    }},
    th: {{
        title: "แฟ้มลับ | แฟ้มสะสมผลงาน",
        desc: "แฟ้มหลักฐานผลงานสุดยอดของนักพัฒนา Web Front-end อาวุโส",
        nav_about: "ประวัติส่วนตัว",
        nav_projects: "ผลงาน",
        nav_history: "ประวัติการทำงาน",
        nav_contact: "ส่งเบาะแส",
        status_active: "สถานะ: ปฏิบัติการ",
        hero_title: "นักพัฒนา<br><span class='highlight'>ระดับลับสุดยอด</span>",
        hero_subtitle: "ผมไขปริศนาดิจิทัลและสร้างสรรค์ระบบแบบ Front-end ที่เปี่ยมประสิทธิภาพ",
        hero_cta_1: "<span class='btn-text'>ตรวจสอบผลงาน</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><polyline points='9 18 15 12 9 6'></polyline></svg>",
        hero_cta_2: "ติดต่อโอเปอเรเตอร์",
        about_label: "// แฟ้มส่วนตัว #X-01",
        about_title: "ประวัติส่วนกังขา",
        about_alias: "> <strong>นามแฝง (ชื่อ):</strong> [ชื่อของคุณ / ใส่ที่นี่]<br>> <strong>ตำแหน่ง:</strong> นักสืบ Front-end ระดับสูง<br>> <strong>ฐานปฏิบัติการ:</strong> [กรุงเทพ / ชลบุรี / Remote]<br>> <strong>ระดับการเข้าถึง:</strong> ระดับ 5 (Senior)",
        about_bio: "ผู้ต้องสงสัยมีทักษะขั้นสูงในการสร้างสรรค์ Web Interface ที่สมบูรณ์แบบระดับพิกเซล เป็นที่เลื่องลือในการวางโครงสร้าง UI ที่แข็งแกร่งและสืบสวนหาบั๊กที่ซับซ้อนในระบบรุ่นเก่า จัดการโค้ดราวกับรับเหมาเก็บกวาดสถานที่เกิดเหตุ—ไม่ปล่อยให้ร่องรอยใดหลุดรอด และแก้ปัญหาคอขวดของระบบอย่างหมดจด",
        about_verified: "รับรองรายงานโดย:",
        about_director: "ผู้อำนวยการฝ่ายวิศวกรรม",
        stat_years: "ปีแห่งการ<br>สร้างระบบ",
        stat_cases: "คดีโปรเจกต์<br>ปิดฉาก",
        projects_label: "// แฟ้มภาพหลักฐาน A-T",
        projects_title: "ผลงาน",
        proj_confidential: "ลับสุดยอด",
{th_projects.rstrip(',\\n')}
        hist_label: "// ลำดับเวลาปฏิบัติงาน",
        hist_title: "ประวัติการสืบสวนทำคดี",
        hist_1_title: "หัวหน้าทีมสายลับ Front-End",
        hist_1_date: "2023 - ปัจจุบัน",
        hist_1_comp: "องค์กรลับ Agency X (Tech Corp)",
        hist_1_desc1: "เป็นผู้นำทีมรุ่นเยาว์รื้อระบบใหญ่ (Monolith) ให้กลายเป็น Micro-frontends ที่ทำงานลื่นไหลรวดเร็ว",
        hist_1_desc2: "ค้นพบต้นตอปัญหาการเรนเดอร์ UI อืด ลดระยะเวลาโหลดเว็บได้เกินกว่า 40%",
        hist_1_desc3: "สร้างโครงข่ายจัดส่งงานสายฟ้าแลบ (CI/CD pipelines) เพื่อความเสถียร",
        hist_2_title: "เจ้าหน้าที่พิเศษด้านหน้าจอ UI/UX",
        hist_2_date: "2020 - 2023",
        hist_2_comp: "บริษัท Solving Bugs จำกัด",
        hist_2_desc1: "ปรับแปลแบบร่างบนกระดาษให้กลายเป็นระบบจริงที่ตอบสนองเข้ากับมือถือได้ทันตา",
        hist_2_desc2: "เชื่อมต่อกับ RESTful APIs ถอดรหัสลับและเจาะระบบดึงข้อมูลจาก Server ขึ้นมาวางบนหน้าเว็บได้อย่างหมดจด",
        contact_label: "// ช่องทางสื่อสารฉุกเฉิน",
        contact_title: "ส่งมอบเบาะแสให้ฉัน",
        contact_tab: "เอกสารลงยันต์ลับ",
        contact_warn: "<strong>คำเตือน:</strong> การสนทนานี้ถูกเข้ารหัสไว้ หากคุณมีบั๊กหรือโปรเจกต์ใหญ่ โปรดทิ้งชื่อนามแฝงและเบาะแสเรื่องราวไว้ได้เลย",
        form_name: "นามแฝง (ชือ)",
        form_name_ph: "สายลับ 007",
        form_email: "ลิงก์สื่อสาร (อีเมล)",
        form_email_ph: "informant@agency.com",
        form_msg: "เบาะแสข่าว (ข้อความ)",
        form_msg_ph: "ผมมีคดีโปรเจกต์ระบบเบ้อเริ่มให้คุณช่วย...",
        form_btn: "<span class='btn-text'>กดส่งสัญญาณลับ</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><line x1='22' y1='2' x2='11' y2='13'></line><polygon points='22 2 15 22 11 13 2 9 22 2'></polygon></svg>",
        footer_copy: "สงวนลิขสิทธิ์ทั้งหมด ระบบป้องกันสัญญาณเข้ารหัสทำงานอยู่"
    }}
}};

document.addEventListener('DOMContentLoaded', () => {{

    // 0. Language Toggle Logic
    const langToggleBtn = document.getElementById('lang-toggle');
    let currentLang = localStorage.getItem('dossier-lang') || 'th';
    const thSpan = document.querySelector('.th-lang');
    const enSpan = document.querySelector('.en-lang');

    const updateLanguage = (lang) => {{
        // Update document lang
        document.documentElement.lang = lang;
        
        // Update Title & Meta
        document.title = i18n[lang]['title'];
        const metaDesc = document.querySelector('meta[name="description"]');
        if(metaDesc) metaDesc.content = i18n[lang]['desc'];

        // Update all elements with data-i18n
        document.querySelectorAll('[data-i18n]').forEach(el => {{
            const key = el.getAttribute('data-i18n');
            if (i18n[lang] && i18n[lang][key]) {{
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {{
                    // Fallback
                }} else {{
                    el.innerHTML = i18n[lang][key];
                }}

                // If element has glitch effect, update data-text without HTML tags
                if (el.hasAttribute('data-text')) {{
                    const cleanText = i18n[lang][key].replace(/<[^>]*>?/gm, ' ').trim();
                    el.setAttribute('data-text', cleanText);
                }}
            }}
        }});
        
        // Update placeholders explicitly if present
        document.querySelectorAll('[data-i18n-ph]').forEach(el => {{
            const key = el.getAttribute('data-i18n-ph');
            if(i18n[lang] && i18n[lang][key]) {{
                 el.placeholder = i18n[lang][key];
            }}
        }});

        // Update Button Active state
        if(lang === 'th') {{
            thSpan.classList.add('lang-active');
            enSpan.classList.remove('lang-active');
        }} else {{
            enSpan.classList.add('lang-active');
            thSpan.classList.remove('lang-active');
        }}
    }};

    // Initialize lang
    updateLanguage(currentLang);

    langToggleBtn.addEventListener('click', () => {{
        currentLang = currentLang === 'th' ? 'en' : 'th';
        localStorage.setItem('dossier-lang', currentLang);
        
        // Subtle theme transition overlay
        document.body.classList.add('theme-transitioning');
        updateLanguage(currentLang);
        
        setTimeout(() => {{
            document.body.classList.remove('theme-transitioning');
        }}, 300);
    }});

    // 1. Initialize Year in Footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {{
        yearSpan.textContent = new Date().getFullYear();
    }}

    // 2. Theme Toggle (Dark/Light Mode)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    
    // Check local storage for theme preference
    const savedTheme = localStorage.getItem('dossier-theme');
    if (savedTheme) {{
        htmlElement.setAttribute('data-theme', savedTheme);
    }} else {{
        htmlElement.setAttribute('data-theme', 'dark');
    }}

    themeToggleBtn.addEventListener('click', () => {{
        const currentThm = htmlElement.getAttribute('data-theme');
        const newTheme = currentThm === 'dark' ? 'light' : 'dark';
        
        document.body.classList.add('theme-transitioning');
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('dossier-theme', newTheme);
        
        setTimeout(() => {{
            document.body.classList.remove('theme-transitioning');
        }}, 400); 
    }});

    // 3. Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    mobileMenuBtn.addEventListener('click', () => {{
        navLinks.classList.toggle('nav-active');
        mobileMenuBtn.classList.toggle('toggle');
    }});

    document.querySelectorAll('.nav-link').forEach(link => {{
        link.addEventListener('click', () => {{
            if (navLinks.classList.contains('nav-active')) {{
                navLinks.classList.remove('nav-active');
                mobileMenuBtn.classList.remove('toggle');
            }}
        }});
    }});

    // 4. Sticky Navbar Logic
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    setTimeout(() => {{
        navbar.classList.remove('hidden-onload');
    }}, 500);

    window.addEventListener('scroll', () => {{
        const currentScroll = window.pageYOffset;
        if (currentScroll > 50) {{
            navbar.classList.add('scrolled');
        }} else {{
            navbar.classList.remove('scrolled');
        }}
        lastScroll = currentScroll;
    }});

    // 5. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOptions = {{
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    }};

    const revealOnScroll = new IntersectionObserver((entries, observer) => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                entry.target.classList.add('active');
                
                // Counters
                const counters = entry.target.querySelectorAll('.counter');
                if(counters.length > 0) {{
                    animateCounters(counters);
                }}
            }}
        }});
    }}, revealOptions);

    revealElements.forEach(el => {{
        revealOnScroll.observe(el);
    }});

    // 6. Number Counter
    let countersAnimated = false;
    function animateCounters(counters) {{
        if (countersAnimated) return; 
        
        counters.forEach(counter => {{
            const target = +counter.getAttribute('data-target');
            const duration = 2000;
            const step = Math.ceil(target / (duration / 30)); 
            let current = 0;
            
            const updateCounter = () => {{
                current += step;
                if (current < target) {{
                    counter.innerText = current;
                    setTimeout(updateCounter, 30);
                }} else {{
                    counter.innerText = target;
                }}
            }};
            
            updateCounter();
        }});
        countersAnimated = true;
    }}

    // 7. Typewriter Effect
    const typewriterElement = document.querySelector('.hero-subtitle');
    if (typewriterElement) {{
        const text = typewriterElement.textContent;
        typewriterElement.textContent = '';
        typewriterElement.style.visibility = 'visible';
        
        let i = 0;
        function typeWriter() {{
            if (i < text.length) {{
                typewriterElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50 + Math.random() * 50);
            }}
        }}
        setTimeout(typeWriter, 1200);
    }}
    
    // 8. Contact Form
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');
    
    if (contactForm) {{
        contactForm.addEventListener('submit', (e) => {{
            e.preventDefault();
            
            const submitBtnText = contactForm.querySelector('.btn-text');
            const originalText = submitBtnText.textContent;
            
            submitBtnText.textContent = 'TRANSMITTING...';
            contactForm.classList.add('processing');
            
            setTimeout(() => {{
                contactForm.reset();
                submitBtnText.textContent = originalText;
                
                const lang = document.documentElement.lang || 'en';
                const successMsg = lang === 'th' ? '[ สถานะ: ได้รับข้อความเข้ารหัสแล้ว ]' : '[ STATUS: ENCRYPTED MESSAGE RECEIVED ]';
                
                formStatus.innerHTML = `<span style="color: var(--accent-red); font-family: var(--font-mono); font-weight: bold;">${{successMsg}}</span>`;
                
                setTimeout(() => {{
                    formStatus.innerHTML = '';
                }}, 5000);
                
            }}, 1500);
        }});
    }}

    // 9. Carousel Logic
    const carousel = document.querySelector('.projects-carousel');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if(carousel && prevBtn && nextBtn) {{
        prevBtn.addEventListener('click', () => {{
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({{ left: -cardWidth, behavior: 'smooth' }});
        }});
        nextBtn.addEventListener('click', () => {{
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({{ left: cardWidth, behavior: 'smooth' }});
        }});
    }}
}});
'''

with codecs.open('assets/js/main.js', 'w', 'utf-8') as f:
    f.write(js_content)
print("main.js fixed properly.")
