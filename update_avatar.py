import re
import codecs

# Update index.html
with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# Pattern for the SVG avatar
svg_pattern = r'<svg class="avatar-svg".*?</svg>'
new_img = '''<img src="assets/img/profile.png" alt="Profile Vector/Photo" class="avatar-img" onerror="this.src='https://picsum.photos/seed/detective/400/400'">'''

html = re.sub(svg_pattern, new_img, html, flags=re.DOTALL)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

# Update style.css
with codecs.open('assets/css/style.css', 'r', 'utf-8') as f:
    css = f.read()

# Add styles for .avatar-img
css_img = '''
.avatar-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(80%) contrast(1.2);
    box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
    background-color: var(--card-bg);
}
[data-theme='light'] .avatar-img {
    filter: sepia(40%) grayscale(40%) contrast(1.1);
}
'''

# We can replace the `.avatar-svg` styles or just append it near it
if '.avatar-img' not in css:
    css = css.replace('.avatar-svg {', css_img + '\n\n.avatar-svg {')

with codecs.open('assets/css/style.css', 'w', 'utf-8') as f:
    f.write(css)

print("Update to profile image complete")
