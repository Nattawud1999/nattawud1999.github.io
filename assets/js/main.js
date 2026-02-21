/*==================================================================
  ระบบนักสืบ / แฟ้มลับสุดยอด - ไฟล์ทำงานโต้ตอบหลัก (JavaScript)
===================================================================*/

/* พจนานุกรมคำแปลภาษาชุดเต็ม */
const i18n = {
    en: {
        title: "Dossier | Developer Portfolio",
        desc: "Confidential evidence files and project dossier of a IT Support / Network Engineer.",
        nav_about: "About Me",
        nav_projects: "Projects",
        nav_history: "Work Experience",
        nav_resume: "Download Resume",
        nav_contact: "Contact",
        status_active: "STATUS: ACTIVE",
        hero_title: "IT Support<br><span class='highlight'>Network Engineer</span>",
        hero_subtitle: "I am an IT Support professional with skills in troubleshooting Networks and Firewalls.",
        hero_cta_1: "<span class='btn-text'>View Projects</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><polyline points='9 18 15 12 9 6'></polyline></svg>",
        hero_cta_2: "Contact Me",
        about_label: "// FILE #X-01",
        about_title: "About Me",
        about_alias: "> <strong>NAME:</strong> [Nattawud Senathong]<br>> <strong>ROLE:</strong> IT Support & Network Engineer<br>> <strong>BASE_OF_OPS:</strong> [Bangkok / Laos / Remote]<br>> <strong>CLEARANCE:</strong> Level 3 (Middle)",
        about_bio: "Hello, my name is Nattawud Senathong, nickname Wut. I was born on August 1, 2003, in Nakhon Si Thammarat province. I am currently working in Vientiane, Laos as an IT Support and Network Engineer with experience in resolving Network and Firewall issues.",
        about_verified: "Signature:",
        about_director: "Nattawud Senathong",
        stat_years: "Years of<br>Experience",
        stat_cases: "Projects<br>Completed",
        projects_label: "// EXHIBIT A-T",
        projects_title: "Projects",
        proj_confidential: "CONFIDENTIAL",
        proj_1_label: "FILE #101",
        proj_1_title: "Network System Installation",
        proj_1_desc: "Installed equipment in Server Racks, including Core switches and Distribution switches, configured VLANs for different rooms, and installed Access Points for Wifi coverage.",
        proj_2_label: "FILE #102",
        proj_2_title: "Mikrotik Installation & 4 ISP Static IP Setup",
        proj_2_desc: "Installed and configured Mikrotik to manage 4 ISPs based on appropriate usage requirements.",
        proj_3_label: "FILE #103",
        proj_3_title: "Resolving UDP Flood Attack",
        proj_3_desc: "Detected abnormal outbound traffic causing bandwidth exhaustion due to a UDP flood attack on port 53. The root cause was the router's DNS exposing 'Allow Remote Requests'. Fixed by disabling this feature and dropping UDP/53 on WAN.",
        proj_4_label: "FILE #104",
        proj_4_title: "Applying Router for Static IP Management",
        proj_4_desc: "Due to the absence of a proper firewall box, I repurposed an existing router to receive the Static IP and distribute the connection efficiently to the switches.",
        proj_5_label: "FILE #105",
        proj_5_title: "CCTV System Setup",
        proj_5_desc: "Installed 150 CCTV cameras and an NVR connected to the Server room for centralized control and management.",
        proj_6_label: "FILE #106",
        proj_6_title: "Mikrotik Setup for Multi-WAN Management",
        proj_6_desc: "Connected 4 ISPs and configured Firewall, Load Balance, NAT, Mangle, QoS, and NAS Server routing.",
        proj_7_label: "FILE #107",
        proj_7_title: "Switch/NAS Optimization",
        proj_7_desc: "Configured SWA/SWB switches and NAS server systems to operate with high efficiency and data availability.",
        proj_8_label: "FILE #108",
        proj_8_title: "Mobile Signal Booster Installation",
        proj_8_desc: "Installed internal cellular signal boosters to expand coverage inside thick-wall office buildings.",
        proj_9_label: "FILE #109",
        proj_9_title: "Computer Repair & Assembly",
        proj_9_desc: "Upgraded, assembled, and troubleshooted various computer hardware components for users.",
        proj_10_label: "FILE #110",
        proj_10_title: "Wireless Point-to-Point Link",
        proj_10_desc: "Installed AirFiber AF-60-LR antennas bridging a high-speed link over a distance of 500 meters.",

        hist_label: "// TIMELINE",
        hist_title: "Work Experience",
        hist_1_title: "IT Staff in Laos",
        hist_1_date: "2024 - Present",
        hist_1_comp: "Hardware, Computer & Network Operations",
        hist_1_desc1: "Installed Network systems, Computers, CCTV, and other related IoT equipment.",
        hist_1_desc2: "Maintained systems and fixed incoming issues proactively, supporting over 500 active users.",
        hist_1_desc3: "Repaired and maintained other IT operational hardware.",
        hist_2_title: "Computer Technician",
        hist_2_date: "2022 - 2023",
        hist_2_comp: "Muang Thong Computer",
        hist_2_desc1: "Installed Windows, software programs, CCTV, and associated smart equipment.",
        hist_2_desc2: "Repaired computers and related corporate components such as office Printers.",
        contact_label: "// SECURE COMM",
        contact_title: "Contact Me",
        contact_tab: "CONFIDENTIAL",
        contact_warn: "<strong>WARNING:</strong> This is a secure channel. If you have big projects or job offers, leave your details below.",
        form_name: "Alias (Name)",
        form_name_ph: "John/Jane Doe",
        form_email: "Comm Link (Email)",
        form_email_ph: "informant@agency.com",
        form_msg: "Details (Message)",
        form_msg_ph: "I have a project for you...",
        form_btn: "<span class='btn-text'>Send Message</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><line x1='22' y1='2' x2='11' y2='13'></line><polygon points='22 2 15 22 11 13 2 9 22 2'></polygon></svg>",
        footer_copy: "All rights reserved. Encrypted connection active."
    },
    th: {
        title: "แฟ้มลับ | แฟ้มสะสมผลงาน",
        desc: "แฟ้มหลักฐานผลงานสุดยอดของนักพัฒนา Web Front-end อาวุโส",
        nav_about: "ประวัติส่วนตัว",
        nav_projects: "ผลงาน",
        nav_history: "ประวัติการทำงาน",
        nav_resume: "ดาวน์โหลดเรซูเม่",
        nav_contact: "ติดต่อ",
        status_active: "สถานะ: ปฏิบัติการ",
        hero_title: "IT Support<br><span class='highlight'>Network Engineer</span>",
        hero_subtitle: "ผมเป็น IT Support ที่มีสกิลในการแก้ไขปัญหา Network และ Firewall",
        hero_cta_1: "<span class='btn-text'>ตรวจสอบผลงาน</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><polyline points='9 18 15 12 9 6'></polyline></svg>",
        hero_cta_2: "ติดต่อผม",
        about_label: "// แฟ้มส่วนตัว #X-01",
        about_title: "ประวัติส่วนตัว",
        about_alias: "> <strong>นามแฝง (ชื่อ):</strong> [ณัฐวุฒิ เสนาทอง]<br>> <strong>ตำแหน่ง:</strong>IT Support & Network Engineer<br>> <strong>ฐานปฏิบัติการ:</strong> [กรุงเทพ / ประเทศลาว / Remote]<br>> <strong>ระดับการเข้าถึง:</strong> ระดับ 3 (middle)",
        about_bio: "สวัสดีครับ ผมชื่อ นาย ณัฐวุฒิ เสนาทอง ชื่อเล่น วุฒิ เกิดเมื่อวันที่ 1 สิงหาคม 2003 บ้านเกิดอยู่ที่ จังหวัด นครศรีธรรมราช ปัจจุบันทำงานอยู่ที่ ประเทศลาว เวียงจันทน์ เป็น IT Support และ Network Engineer ที่มีประสบการณ์ในการแก้ไขปัญหา Network และ Firewall",
        about_verified: "ลงชื่อ:",
        about_director: "ณัฐวุฒิ เสนาทอง",
        stat_years: "ปีแห่งการ<br>สร้างระบบ",
        stat_cases: "คดีโปรเจกต์<br>ปิดฉาก",
        projects_label: "// แฟ้มภาพหลักฐาน A-T",
        projects_title: "ผลงาน",
        proj_confidential: "ลับสุดยอด",
        proj_1_label: "แฟ้ม #101",
        proj_1_title: "ติดตั้งระบบ Network",
        proj_1_desc: "ติดตั้งอุปกรณ์ ใส่ตู้ Rack มี Core SW และ SW ย่อย แยก VLAN ไปยังห้องต่างๆ และติดตั้ง Access Point เพื่อกระจายสัญญาณ Wifi ",
        proj_2_label: "แฟ้ม #102",
        proj_2_title: "ติดตั้ง Mikrotik และรับ Static IP จำนวน 4 ISP",
        proj_2_desc: "ติดตั้งและจัดการ Internet 4 ISP ตามความเหมาะสมในการใช้งาน",
        proj_3_label: "แฟ้ม #103",
        proj_3_title: "แก้ไขปัญหาโดนยิง UDP",
        proj_3_desc: "ตรวจพบว่าอินเทอร์เน็ตเส้นหลักถูกยิง UDP เข้าที่พอร์ต 53 (DNS) ทำให้ทราฟฟิกขาออกสูงผิดปกติและแบนด์วิธเต็มชั่วคราวสาเหตุเกิดจาก DNS ของ Router เปิดรับจากภายนอก (Allow Remote Requests) จึงถูกใช้เป็นเป้าหมายโจมตีแก้ไข โดยปิด Allow Remote Requests บล็อก UDP/53 จากฝั่ง WAN",
        proj_4_label: "แฟ้ม #104",
        proj_4_title: "ประยุกต์ใช้ Router รับ Static IP ต่อเข้า SW เพื่อกระจายการใช้งาน",
        proj_4_desc: "เนื่องจากลูกค้าไม่มี Mikrotik จึงได้นำ Router ที่มีอยู่มาประยุกต์ใช้ในการรับ Static IP และกระจายการใช้งานไปยัง SW",
        proj_5_label: "แฟ้ม #105",
        proj_5_title: "ติดตั้งระบบCCTV",
        proj_5_desc: "ติดตั้งกล้องวงจรปิดจำนวน 150 ตัว และ NVR ต่อเข้าห้อง Server เพื่อควบคุมและจัดการ",
        proj_6_label: "แฟ้ม #106",
        proj_6_title: "ติดตั้ง Mikrotik ควบคุมและจัดการ Internet 4 ISP",
        proj_6_desc: "เชื่อมต่อกับ 4ISP จัดการ Firewall,Load NAT,Mangle,QoS,NAS Server",
        proj_7_label: "แฟ้ม #107",
        proj_7_title: "จัดระบบ SWA/SWB/NAS Server",
        proj_7_desc: "ตั้งค่าระบบ SWA/SWB และ NAS Server ให้สามารถทำงานได้อย่างมีประสิทธิภาพ",
        proj_8_label: "แฟ้ม #108",
        proj_8_title: "เครื่องขยายสัญญาณมือถือ",
        proj_8_desc: "ติดตั้งเครื่องขยายสัญญาณมือถือในสำนักงาน",
        proj_9_label: "แฟ้ม #109",
        proj_9_title: "ประกอบคอมพิวเตอร์/ซ่อมแซมคอมพิวเตอร์",
        proj_9_desc: "อัพเกรด/ประกอบคอมพิวเตอร์ และซ่อมแซมคอมพิวเตอร์",
        proj_10_label: "แฟ้ม #110",
        proj_10_title: "ตัวยิงสัญญาณ Internet",
        proj_10_desc: "ติดตั้งตัวยิงสัญญาณ AirFiber AF-60-LR ระยะทาง 500 เมตร",

        hist_label: "// ลำดับเวลาปฏิบัติงาน",
        hist_title: "ประวัติการทำงาน",
        hist_1_title: "พนักงาน IT ที่ประเทศลาว",
        hist_1_date: "2024 - ปัจจุบัน",
        hist_1_comp: "แก้ไขปัญหา Hardware computer Network",
        hist_1_desc1: "ติดตั้งระบบ Network Computer CCTV และอื่นๆที่เกี่ยวข้อง",
        hist_1_desc2: "ดูแลระบบ และ แก้ไขปัญหาที่เกิดขึ้น รองรับ500ผู้ใช้งาน",
        hist_1_desc3: "ซ่อมแซม บำรุงรักษาอุปกรณ์ IT อื่นๆที่เกี่ยวข้อง",
        hist_2_title: "ช่างคอมประจำร้าน",
        hist_2_date: "2022 - 2023",
        hist_2_comp: "เมืองทองคอวพิวเตอร์",
        hist_2_desc1: "ลง Windows และโปรแกรมต่างๆ ติดตั้ง CCTV และอื่นๆที่เกี่ยวข้อง",
        hist_2_desc2: "ซ่อมแซมคอมพิวเตอร์และอุปกรณ์ IT อื่นๆที่เกี่ยวข้อง เช่น Printer ",
        contact_label: "// ช่องทางสื่อสารฉุกเฉิน",
        contact_title: "ติดต่อผม",
        contact_tab: "เอกสารลับ",
        contact_warn: "<strong>คำเตือน:</strong> การสนทนานี้ถูกเข้ารหัสไว้ หากคุณมีงานหรือโปรเจกต์ใหญ่ โปรดทิ้งชื่อนามแฝงและเบาะแสเรื่องราวไว้ได้เลย",
        form_name: "นามแฝง (ชือ)",
        form_name_ph: "สายลับ 007",
        form_email: "ลิงก์สื่อสาร (อีเมล)",
        form_email_ph: "informant@agency.com",
        form_msg: "รายละเอียด (ข้อความ)",
        form_msg_ph: "ผมมีงานหรือโปรเจกต์ใหญ่ให้คุณช่วย...",
        form_btn: "<span class='btn-text'>กดส่งสัญญาณลับ</span> <svg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><line x1='22' y1='2' x2='11' y2='13'></line><polygon points='22 2 15 22 11 13 2 9 22 2'></polygon></svg>",
        footer_copy: "สงวนลิขสิทธิ์ทั้งหมด ระบบป้องกันสัญญาณเข้ารหัสทำงานอยู่"
    }
};

document.addEventListener('DOMContentLoaded', () => {

    // ============================================
    // SOUND EFFECTS (Web Audio API)
    // ============================================
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playTone(freq, type, duration, vol = 0.1) {
        if (audioCtx.state === 'suspended') return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(vol, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    }

    function playType() { playTone(600 + Math.random() * 400, 'square', 0.05, 0.02); }
    function playClick() { playTone(1200, 'sine', 0.1, 0.05); }
    function playStamp() { playTone(150, 'square', 0.4, 0.5); }
    function playGranted() {
        playTone(900, 'sine', 0.1, 0.1);
        setTimeout(() => playTone(1400, 'sine', 0.2, 0.1), 150);
    }

    // Play click on all buttons
    document.querySelectorAll('button, a').forEach(btn => {
        btn.addEventListener('click', () => {
            if (audioCtx.state !== 'suspended') playClick();
        });
    });

    // ============================================
    // TERMINAL BOOT SEQUENCE
    // ============================================
    const bootOverlay = document.getElementById('boot-overlay');
    const bootStartBtn = document.getElementById('boot-start-btn');
    const bootTerminal = document.getElementById('boot-terminal');

    if (bootOverlay && bootStartBtn && bootTerminal) {
        document.body.style.overflow = 'hidden';

        const bootLines = [
            "CONNECTING TO SECURE SERVER...",
            "ESTABLISHING ENCRYPTED PROTOCOL [AES-256]...",
            "BYPASSING FIREWALL... SUCCESS",
            "AUTHENTICATING AGENT: NATTAWUD...",
            "CLEARANCE LEVEL: 3 VERIFIED",
            "LOADING CLASSIFIED DOSSIER...",
            "DECRYPTING EVIDENCE FILES...",
            "ACCESS GRANTED."
        ];

        bootStartBtn.addEventListener('click', async () => {
            if (audioCtx.state === 'suspended') await audioCtx.resume();
            playClick();
            bootStartBtn.style.display = 'none';
            bootTerminal.style.display = 'block';

            let currentLine = 0;

            async function typeLine(text) {
                const lineDiv = document.createElement('div');
                lineDiv.className = 'boot-line';
                bootTerminal.appendChild(lineDiv);

                for (let i = 0; i < text.length; i++) {
                    lineDiv.innerHTML = text.substring(0, i + 1) + '<span class="cursor-blink"></span>';
                    playType();
                    await new Promise(r => setTimeout(r, 20 + Math.random() * 30));
                }
                lineDiv.innerHTML = text;
            }

            for (let line of bootLines) {
                await typeLine(line);
                await new Promise(r => setTimeout(r, 200 + Math.random() * 300));
            }

            playGranted();
            const grantedDiv = document.createElement('div');
            grantedDiv.className = 'boot-line';
            grantedDiv.innerHTML = '<br><span style="color:white; background:#4af626; padding:0 10px;">SYSTEM READY</span><span class="cursor-blink"></span>';
            bootTerminal.appendChild(grantedDiv);

            setTimeout(() => {
                bootOverlay.style.opacity = '0';
                setTimeout(() => {
                    bootOverlay.style.display = 'none';
                    document.body.style.overflow = '';
                }, 1000);
            }, 1000);
        });
    }

    // ============================================
    // RESUME DOWNLOAD ANIMATION & MODAL
    // ============================================
    const resumeBtn = document.getElementById('download-resume-btn');
    const stampApproved = document.getElementById('stamp-approved');
    const resumeModal = document.getElementById('resume-modal');
    const closeResumeModal = document.querySelector('.close-resume-modal');
    const resumeDlBtns = document.querySelectorAll('.resume-dl-btn');

    if (resumeBtn && stampApproved && resumeModal) {
        // 1. กดปุ่มแรก เปิด Popup ให้เลือกภาษา
        resumeBtn.addEventListener('click', (e) => {
            e.preventDefault();
            resumeModal.classList.add('show');
        });

        // 2. โลจิก ปิด Popup
        if (closeResumeModal) {
            closeResumeModal.addEventListener('click', () => {
                resumeModal.classList.remove('show');
            });
        }
        window.addEventListener('click', (e) => {
            if (e.target === resumeModal) {
                resumeModal.classList.remove('show');
            }
        });

        // 3. เมื่อกดปุ่มภาษาที่ต้องการ จะซ่อน Popup สับตรายาง แล้วดาวน์โหลดไฟล์
        resumeDlBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const langTarget = e.target.getAttribute('data-lang');
                const fileTarget = langTarget === 'th' ? 'resumeTH.pdf' : 'resumeEN.pdf';
                const dlName = langTarget === 'th' ? 'Nattawud-Resume-TH.pdf' : 'Nattawud-Resume-EN.pdf';

                // ปิด Popup
                resumeModal.classList.remove('show');

                // วิ่งแอนิเมชันตรายางอนุมัติ + เสียง
                playStamp();
                stampApproved.classList.add('animate');

                setTimeout(() => {
                    stampApproved.classList.remove('animate');

                    // สร้างการกดดาวน์โหลดจริง
                    const link = document.createElement('a');
                    link.href = 'assets/' + fileTarget;
                    link.download = dlName;
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                }, 1500);
            });
        });
    }


    // 0. โลจิกปุ่มสลับภาษา (TH <-> EN)
    const langToggleBtn = document.getElementById('lang-toggle');
    let currentLang = localStorage.getItem('dossier-lang') || 'th';
    const thSpan = document.querySelector('.th-lang');
    const enSpan = document.querySelector('.en-lang');

    const updateLanguage = (lang) => {
        // อัปเดตคุณสมบัติ lang บนเว็บเบราว์เซอร์ให้รู้ว่าใช้ภาษาอะไร
        document.documentElement.lang = lang;

        // อัปเดตหัวข้อเว็บ (Title) และรายละเอียด (Meta) เอาไว้ให้ Google อ่าน
        document.title = i18n[lang]['title'];
        const metaDesc = document.querySelector('meta[name="description"]');
        if (metaDesc) metaDesc.content = i18n[lang]['desc'];

        // กวาดดึงข้อความจาก Object มาแสดงผลตามภาษาเป้าหมาย โดยหาจาก attribute: data-i18n
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (i18n[lang] && i18n[lang][key]) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    // Fallback
                } else {
                    el.innerHTML = i18n[lang][key];
                }

                // สำหรับตัวหนังสือที่มีเอฟเฟกต์ Glitch (ภาพซ้อน) ต้องคอยอัปเดตแกนข้อความด้วย
                if (el.hasAttribute('data-text')) {
                    const cleanText = i18n[lang][key].replace(/<[^>]*>?/gm, ' ').trim();
                    el.setAttribute('data-text', cleanText);
                }
            }
        });

        // อัปเดตข้อความลายน้ำ (Placeholder) ในช่องพวก Text Input ยิบย่อย
        document.querySelectorAll('[data-i18n-ph]').forEach(el => {
            const key = el.getAttribute('data-i18n-ph');
            if (i18n[lang] && i18n[lang][key]) {
                el.placeholder = i18n[lang][key];
            }
        });

        // อัปเดตสีของปุ่มสลับภาษาเพื่อบอกว่าตอนนี้เลือกใช้ภาษาอะไรอยู่
        if (lang === 'th') {
            thSpan.classList.add('lang-active');
            enSpan.classList.remove('lang-active');
        } else {
            enSpan.classList.add('lang-active');
            thSpan.classList.remove('lang-active');
        }
    };

    // ดึงภาษามาแสดงตั้งแต่ตอนเปิดหน้าเว็บครั้งแรก
    updateLanguage(currentLang);

    langToggleBtn.addEventListener('click', () => {
        currentLang = currentLang === 'th' ? 'en' : 'th';
        localStorage.setItem('dossier-lang', currentLang);

        // ใส่เอฟเฟกต์ซ้อนทับแปปหนึ่งเวลาสลับภาษาเพื่อความสมูทของสายตา
        document.body.classList.add('theme-transitioning');
        updateLanguage(currentLang);

        setTimeout(() => {
            document.body.classList.remove('theme-transitioning');
        }, 300);
    });

    // 1. ให้ปีใน Footer เป็นปีอัปเดตล่าสุดอัตโนมัติตามปฏิทินคอมพิวเตอร์ปัจจุบัน
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 2. โลจิกปุ่มสลับธีมสี (โหมดกลางคืน / โหมดสว่าง(กระดาษ))
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // เช็คความจำของเบราว์เซอร์ ว่ารอบที่แล้วเขาเลือกดาร์กโหมดค้างไว้หรือไม่
    const savedTheme = localStorage.getItem('dossier-theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
    } else {
        htmlElement.setAttribute('data-theme', 'dark');
    }

    themeToggleBtn.addEventListener('click', () => {
        const currentThm = htmlElement.getAttribute('data-theme');
        const newTheme = currentThm === 'dark' ? 'light' : 'dark';

        document.body.classList.add('theme-transitioning');

        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('dossier-theme', newTheme);

        setTimeout(() => {
            document.body.classList.remove('theme-transitioning');
        }, 400);
    });

    // 3. โลจิกปุ่มเปิด/ปิด เมนูด้านบนในมุมมองมือถือ (Hamburger menu)
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    mobileMenuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('nav-active');
        mobileMenuBtn.classList.toggle('toggle');
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('nav-active')) {
                navLinks.classList.remove('nav-active');
                mobileMenuBtn.classList.remove('toggle');
            }
        });
    });

    // 4. โลจิกลูกเล่นของเมนูนำทาง (เมื่อจอด้านบนให้พื้นหลังโปร่ง เลื่อนลงมาให้ทึบ ฯลฯ)
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;

    setTimeout(() => {
        navbar.classList.remove('hidden-onload');
    }, 500);

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        lastScroll = currentScroll;
    });

    // 5. แอนิเมชันสำหรับเผยไอเทมขึ้นมาแบบค่อยๆ ลอยขึ้น ตอนที่เราเลื่อนหน้าเว็บลงไปถึง
    const revealElements = document.querySelectorAll('.reveal');

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');

                // เช็คว่ามีกล่องนับเลขตัวเลขอ่านไหม ถ้ามีให้ทำงานแอนิเมชันวิ่งๆ ด้วย
                const counters = entry.target.querySelectorAll('.counter');
                if (counters.length > 0) {
                    animateCounters(counters);
                }
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // 6. แอนิเมชันวิ่งตัวเลข (จาก 0 ปรู๊ดขึ้นไปถึงเลขเป้าหมาย)
    let countersAnimated = false;
    function animateCounters(counters) {
        if (countersAnimated) return;

        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000;
            const step = Math.ceil(target / (duration / 30));
            let current = 0;

            const updateCounter = () => {
                current += step;
                if (current < target) {
                    counter.innerText = current;
                    setTimeout(updateCounter, 30);
                } else {
                    counter.innerText = target;
                }
            };

            updateCounter();
        });
        countersAnimated = true;
    }

    // 7. เอฟเฟกต์รัวเครื่องพิมพ์ดีด
    const typewriterElement = document.querySelector('.hero-subtitle');
    if (typewriterElement) {
        const text = typewriterElement.textContent;
        typewriterElement.textContent = '';
        typewriterElement.style.visibility = 'visible';

        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                typewriterElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50 + Math.random() * 50);
            }
        }
        setTimeout(typeWriter, 1200);
    }

    // 8. ระบบฟอร์มการส่งข้อความ / รับส่งเบาะแส
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const submitBtnText = contactForm.querySelector('.btn-text');
            const originalText = submitBtnText.textContent;

            submitBtnText.textContent = 'TRANSMITTING...';
            contactForm.classList.add('processing');

            setTimeout(() => {
                contactForm.reset();
                submitBtnText.textContent = originalText;

                const lang = document.documentElement.lang || 'en';
                const successMsg = lang === 'th' ? '[ สถานะ: ได้รับข้อความเข้ารหัสแล้ว ]' : '[ STATUS: ENCRYPTED MESSAGE RECEIVED ]';

                formStatus.innerHTML = `<span style="color: var(--accent-red); font-family: var(--font-mono); font-weight: bold;">${successMsg}</span>`;

                setTimeout(() => {
                    formStatus.innerHTML = '';
                }, 5000);

            }, 1500);
        });
    }

    // 9. โลจิกระบบสไลด์เลื่อนผลงาน (Carousel) ซ้าย/ขวา
    const carousel = document.querySelector('.projects-carousel');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (carousel && prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({ left: -cardWidth, behavior: 'smooth' });
        });
        nextBtn.addEventListener('click', () => {
            const cardWidth = carousel.querySelector('.project-card').offsetWidth + 40; // width + gap
            carousel.scrollBy({ left: cardWidth, behavior: 'smooth' });
        });
    }

    // 10. ระบบ Popup LINE QR Code
    const lineBtn = document.getElementById('line-popup-btn');
    const lineModal = document.getElementById('line-modal');
    const closeBtn = document.querySelector('.close-modal');

    if (lineBtn && lineModal && closeBtn) {
        lineBtn.addEventListener('click', (e) => {
            e.preventDefault();
            lineModal.classList.add('show');
        });

        closeBtn.addEventListener('click', () => {
            lineModal.classList.remove('show');
        });

        window.addEventListener('click', (e) => {
            if (e.target === lineModal) {
                lineModal.classList.remove('show');
            }
        });
    }
});