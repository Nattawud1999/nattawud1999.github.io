import codecs

# 1. Update index.html
with codecs.open("index.html", "r", "utf-8") as f:
    html = f.read()

# Replace LinkedIn
html = html.replace('<a href="#" aria-label="LinkedIn">LinkedIn</a>', 
                    '<a href="#" id="line-popup-btn" aria-label="LINE">LINE</a>')

# Insert modal before closing body
modal_code = '''
    <!-- LINE QR Code Modal -->
    <div id="line-modal" class="modal">
        <div class="modal-content evidence-card">
            <span class="close-modal">&times;</span>
            <div class="stamp-confidential" style="top: 10px; right: 10px; font-size: 1.2rem; transform: rotate(5deg);">ติดต่อด่วน</div>
            <h3 class="mono-label" style="text-align: center; font-size: 1.5rem; margin-bottom: 20px;">สแกนเพื่อเพิ่มเพื่อน</h3>
            <img src="assets/img/Line.jpg" alt="LINE QR Code" style="width: 100%; max-width: 300px; display: block; margin: 0 auto; border: 2px solid var(--card-border); border-radius: 8px;">
            <p style="text-align: center; margin-top: 15px; font-size: 1.2rem; font-family: var(--font-mono);">
                <strong>LINE ID:</strong> <span class="highlight">1star_channel</span>
            </p>
        </div>
    </div>

</body>'''

html = html.replace('</body>', modal_code)

with codecs.open("index.html", "w", "utf-8") as f:
    f.write(html)

# 2. Update style.css
with codecs.open("assets/css/style.css", "r", "utf-8") as f:
    css = f.read()

modal_css = '''
/*--------------------------------------------------------------
# Modal Popup Styles (LINE QR)
--------------------------------------------------------------*/
.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(5px);
    align-items: center;
    justify-content: center;
}

.modal.show {
    display: flex;
}

.modal-content {
    background-color: var(--card-bg);
    margin: auto;
    padding: 30px;
    border: 1px solid var(--accent-gold);
    width: 90%;
    max-width: 450px;
    position: relative;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    animation: modalfadein 0.3s;
}

@keyframes modalfadein {
    from { opacity: 0; transform: translateY(-50px); }
    to { opacity: 1; transform: translateY(0); }
}

.close-modal {
    color: var(--text-muted);
    font-size: 32px;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    right: 20px;
    top: 10px;
    z-index: 20;
    line-height: 1;
}

.close-modal:hover,
.close-modal:focus {
    color: var(--accent-red);
    text-decoration: none;
    cursor: pointer;
}
'''
if '.modal {' not in css:
    css = css + '\\n' + modal_css

with codecs.open("assets/css/style.css", "w", "utf-8") as f:
    f.write(css)

# 3. Update main.js
with codecs.open("assets/js/main.js", "r", "utf-8") as f:
    js = f.read()

modal_js = '''
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
});'''

# Replace the final "});" with the new logic
if 'line-modal' not in js:
    if '});' in js:
        parts = js.rsplit('});', 1)
        js = parts[0] + modal_js

with codecs.open("assets/js/main.js", "w", "utf-8") as f:
    f.write(js)

print("LINE Modal updated successfully!")
