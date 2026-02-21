import codecs

css_path = 'assets/css/style.css'

with codecs.open(css_path, 'r', 'utf-8') as f:
    css = f.read()

addon_css = """
/*--------------------------------------------------------------
# Custom NATIVE Cursor (Zero Delay)
--------------------------------------------------------------*/
body, html {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="%234af626" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>') 12 12, auto !important;
}

a, button, .project-card, input, textarea, select, .close-modal, .mobile-menu-btn, .lang-toggle, .theme-toggle {
    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="%23D32F2F" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="8"/><line x1="21" y1="21" x2="17.65" y2="17.65"/><circle cx="12" cy="12" r="2" fill="%23D32F2F"/></svg>') 16 16, pointer !important;
}

/*--------------------------------------------------------------
# Timeline Network Beam Effect
--------------------------------------------------------------*/
.timeline {
    overflow: hidden; /* Contains the beam */
}

.timeline-data-beam {
    position: absolute;
    top: -50px;
    left: 23px;
    width: 4px;
    height: 80px;
    background: linear-gradient(to bottom, transparent, #4af626, #ffffff);
    border-radius: 5px;
    box-shadow: 0 0 10px #4af626, 0 0 20px #4af626;
    z-index: 3;
    animation: dataTransfer 2.5s infinite ease-in;
}

@media (max-width: 768px) {
    .timeline-data-beam {
        left: 15px;
    }
}

@keyframes dataTransfer {
    0% { top: -100px; opacity: 0; }
    10% { opacity: 1; }
    80% { opacity: 1; }
    100% { top: 100%; opacity: 0; }
}
"""

if 'timeline-data-beam' not in css:
    css = css + '\n' + addon_css
    with codecs.open(css_path, 'w', 'utf-8') as f:
        f.write(css)

# Update HTML
html_path = 'index.html'
with codecs.open(html_path, 'r', 'utf-8') as f:
    html = f.read()

if '<div class="timeline-data-beam"></div>' not in html:
    html = html.replace('<div class="timeline">', '<div class="timeline">\n                    <!-- Data beam animation for network -->\n                    <div class="timeline-data-beam"></div>')
    with codecs.open(html_path, 'w', 'utf-8') as f:
        f.write(html)
        
print("Success!")
