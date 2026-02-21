import codecs
import re
import os

# Create dummy resume.pdf
os.makedirs('assets', exist_ok=True)
with open('assets/resume.pdf', 'wb') as f:
    f.write(b"%PDF-1.4\n%Dummy PDF for Resume\n")

# 1. Update index.html
with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# Replace the contact nav link
html = re.sub(r'<li><a href="#contact".*?data-i18n="nav_contact".*?</a></li>',
              '<li><a href="#" id="download-resume-btn" class="nav-link resume-btn" data-i18n="nav_resume">ดาวน์โหลดประวัติ</a></li>', html)

boot_html = '''
    <!-- Terminal Boot Sequence -->
    <div id="boot-overlay" class="boot-overlay">
        <div class="boot-content">
            <button id="boot-start-btn" class="boot-btn">[ อนุมัติการเข้าถึงระบบ / INITIATE CONNECTION ]</button>
            <div id="boot-terminal" class="boot-terminal" style="display: none;"></div>
        </div>
    </div>
    
    <!-- BIG STAMP FOR RESUME -->
    <div id="stamp-approved" class="stamp-approved">อนุมัติ (APPROVED)</div>
'''

if 'id="boot-overlay"' not in html:
    html = html.replace('<body>', '<body>' + boot_html)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

# 2. Update style.css
with codecs.open('assets/css/style.css', 'r', 'utf-8') as f:
    css = f.read()

boot_css = '''
/*--------------------------------------------------------------
# Terminal Boot & Stamp Effects
--------------------------------------------------------------*/
.boot-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-color: #0b0f19;
    z-index: 9999;
    color: #4af626;
    font-family: var(--font-mono);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 1s ease-out;
}
.boot-btn {
    background: none;
    border: 1px dashed #4af626;
    color: #4af626;
    padding: 15px 30px;
    font-family: inherit;
    font-size: 1.2rem;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.3s ease;
}
.boot-btn:hover {
    background: rgba(74, 246, 38, 0.2);
    box-shadow: 0 0 15px #4af626;
    color: #fff;
}
.boot-terminal {
    width: 90vw;
    max-width: 800px;
    height: 60vh;
    text-align: left;
    font-size: 1.1rem;
    line-height: 1.6;
    overflow-y: hidden;
    text-shadow: 0 0 5px #4af626;
}
.boot-line {
    margin-bottom: 8px;
    word-break: break-word;
}
.cursor-blink {
    display: inline-block;
    width: 10px;
    height: 1.1rem;
    background-color: #4af626;
    animation: blink 1s step-end infinite;
    vertical-align: middle;
    margin-left: 5px;
}

/* Big Resume Stamp */
.stamp-approved {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(5);
    font-size: clamp(2rem, 5vw, 6rem);
    font-weight: 900;
    color: var(--accent-red);
    border: 8px solid var(--accent-red);
    padding: 20px 40px;
    font-family: var(--font-mono);
    text-transform: uppercase;
    z-index: 10000;
    opacity: 0;
    pointer-events: none;
    text-align: center;
    filter: drop-shadow(0 0 10px rgba(0,0,0,0.5));
}
.stamp-approved.animate {
    animation: stamp-bang 0.6s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes stamp-bang {
    0% { transform: translate(-50%, -50%) scale(3); opacity: 0; }
    40% { transform: translate(-50%, -50%) scale(0.9); opacity: 1; filter: drop-shadow(0 0 20px var(--accent-red)); }
    100% { transform: translate(-50%, -50%) scale(1) rotate(-15deg); opacity: 1; filter: drop-shadow(0 0 5px var(--accent-red)); }
}
'''
if '.boot-overlay {' not in css:
    css = css + '\n' + boot_css

with codecs.open('assets/css/style.css', 'w', 'utf-8') as f:
    f.write(css)

# 3. Update main.js
with codecs.open('assets/js/main.js', 'r', 'utf-8') as f:
    js = f.read()

if 'nav_resume: "Download Resume"' not in js:
    js = js.replace('nav_history: "Work Experience",', 'nav_history: "Work Experience",\n        nav_resume: "Download Resume",')
if 'nav_resume: "โหลดเรซูเม่ประวัติ"' not in js:
    js = js.replace('nav_history: "ประวัติการทำงาน",', 'nav_history: "ประวัติการทำงาน",\n        nav_resume: "โหลดเรซูเม่ประวัติ",')

boot_js = '''
    // ============================================
    // SOUND EFFECTS (Web Audio API)
    // ============================================
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playTone(freq, type, duration, vol=0.1) {
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

    function playType() { playTone(600 + Math.random()*400, 'square', 0.05, 0.02); }
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
                
                for(let i=0; i<text.length; i++) {
                    lineDiv.innerHTML = text.substring(0, i+1) + '<span class="cursor-blink"></span>';
                    playType();
                    await new Promise(r => setTimeout(r, 20 + Math.random() * 30));
                }
                lineDiv.innerHTML = text; 
            }

            for(let line of bootLines) {
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
    // RESUME DOWNLOAD ANIMATION
    // ============================================
    const resumeBtn = document.getElementById('download-resume-btn');
    const stampApproved = document.getElementById('stamp-approved');

    if (resumeBtn && stampApproved) {
        resumeBtn.addEventListener('click', (e) => {
            e.preventDefault(); 
            playStamp();
            
            stampApproved.classList.add('animate');
            
            setTimeout(() => {
                stampApproved.classList.remove('animate');
                
                const link = document.createElement('a');
                link.href = 'assets/resume.pdf';
                link.download = 'Nattawud-Resume.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }, 1500);
        });
    }
'''

if 'SOUND EFFECTS (Web Audio API)' not in js:
    js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + boot_js)

with codecs.open('assets/js/main.js', 'w', 'utf-8') as f:
    f.write(js)

print("Added Boot Sequence, SFX and Resume feature!")
