import codecs
import re

with codecs.open("index.html", "r", "utf-8") as f:
    text = f.read()

def clean_tag(match):
    # match.group(1) is the opening tag up to the class/data-i18n
    # match.group(2) is the content we want to clear
    # match.group(3) is the closing tag
    tag_start = match.group(1)
    tag_end = match.group(3)
    return tag_start + tag_end

# 1. Match simple tags not containing nested tags, just text inside
pattern_simple = re.compile(r'(<[a-zA-Z1-6]+[^>]*?data-i18n="[^"]*"[^>]*?>)([^<]*)(</[a-zA-Z1-6]+>)')
text = pattern_simple.sub(clean_tag, text)

# 2. Match specific tags with nested content like hero_cta_1, hero_cta_2, form_btn
btn1 = re.compile(r'(<a href="#projects" class="btn btn-primary" data-i18n="hero_cta_1">).*?(</a>)', re.DOTALL)
text = btn1.sub(r'\1\2', text)

btn2 = re.compile(r'(<a href="#contact" class="btn btn-outline" data-i18n="hero_cta_2">).*?(</a>)', re.DOTALL)
text = btn2.sub(r'\1\2', text)

btn_form = re.compile(r'(<button type="submit" class="btn btn-primary submit-btn".*?data-i18n="form_btn">).*?(</button>)', re.DOTALL)
text = btn_form.sub(r'\1\2', text)

with codecs.open("index.html", "w", "utf-8") as f:
    f.write(text)

print("HTML content inside data-i18n tags cleaned successfully!")
