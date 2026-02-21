import codecs
import re

with codecs.open('assets/css/style.css', 'r', 'utf-8') as f:
    css = f.read()

# remove filter lines from .avatar-img and [data-theme='light'] .avatar-img
css = re.sub(r'\s*filter:\s*grayscale\(80%\)\s*contrast\(1\.2\);', '', css)
css = re.sub(r'\s*filter:\s*sepia\(40%\)\s*grayscale\(40%\)\s*contrast\(1\.1\);', '', css)

with codecs.open('assets/css/style.css', 'w', 'utf-8') as f:
    f.write(css)

print("Filters removed")
