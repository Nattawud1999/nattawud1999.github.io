import codecs
import re

html_path = 'index.html'
css_path = 'assets/css/style.css'
js_path = 'assets/js/main.js'

def translate_file(path, translations):
    try:
        with codecs.open(path, 'r', 'utf-8') as f:
            content = f.read()
        
        for eng, thai in translations.items():
            content = content.replace(eng, thai)
            
        with codecs.open(path, 'w', 'utf-8') as f:
            f.write(content)
        print(f"Translated {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

html_translations = {
    '<!-- Custom CSS -->': '<!-- ไฟล์ CSS หลัักที่ใช้ปรับแต่งความสวยงามหน้าเว็บ -->',
    '<!-- Background Grid -->': '<!-- ตารางพื้นหลังลายๆ -->',
    '<!-- Mouse Follower -->': '<!-- เอฟเฟกต์จุดติดตามเมาส์ (ถ้ามี) -->',
    '<!-- Top Navbar -->': '<!-- แถบเมนูนำทาง (Navbar) ที่อยู่ด้านบนสุด -->',
    '<!-- Theme & Lang Toggle -->': '<!-- กลุ่มปุ่มสลับธีม (มืด/สว่าง) และปุ่มสลับภาษา -->',
    '<!-- Dark/Light theme icon via SVG -->': '<!-- ไอคอนพระอาทิตย์/พระจันทร์แบบ SVG -->',
    '<!-- Desktop Menu -->': '<!-- เมนูสำหรับหน้าจอคอมพิวเตอร์ -->',
    '<!-- Mobile Menu Button -->': '<!-- ปุ่มกดเมนูสำหรับหน้าจอมือถือ (แฮมเบอร์เกอร์) -->',
    '<!-- Hero Section -->': '<!-- ส่วนฮีโร่ (Hero Section) หน้าแรกสุดที่ดึงดูดสายตา -->',
    '<!-- Avatar รูปโปรไฟล์ -->': '<!-- รูปโปรไฟล์ของคุณ -->',
    '<!-- About Section (Classified Subject) -->': '<!-- ส่วนหน้าประวัติส่วนตัว (มาในธีม ข้อมูลผู้ต้องสงสัย) -->',
    '<!-- Projects / Evidence Board -->': '<!-- ส่วนของผลงานต่างๆ (มาในธีม กระดานหลักฐาน) -->',
    '<!-- Section Title -->': '<!-- หัวข้อย่อยของส่วนต่างๆ -->',
    '<!-- Experience / Timeline -->': '<!-- ส่วนประสบการณ์การทำงาน (เรียงตามลำดับเวลา) -->',
    '<!-- Contact Section -->': '<!-- ส่วนการติดต่องาน (ฟอร์มส่งเบาะแส) -->',
    '<!-- Footer -->': '<!-- ส่วนท้ายของเว็บไซต์ (Footer) -->',
    '<!-- Custom Scripts -->': '<!-- ไฟล์สคริปต์ JavaScript หลักของการทำงานเว็บ -->'
}

css_translations = {
    'DETECTIVE OS / CLASSIFIED DOSSIER - CSS STYLES': 'ระบบนักสืบ / แฟ้มลับสุดยอด - ไฟล์กำหนดสไตล์ CSS',
    '# Variables': '# ตัวแปรสีและฟอนต์ (Variables)',
    '/* Dark Theme (Default) */': '/* โหมดมืด (ค่าเริ่มต้น) */',
    '/* Light Theme (Paper/Dossier style) */': '/* โหมดสว่าง (สไตล์กระดาษแฟ้มคดี) */',
    '/* off-white paper tone */': '/* สีกระดาษขาวหม่นแบบเก่าๆ */',
    '/* Crimson red */': '/* สีแดงเลือดหมูสำหรับตราประทับ/เส้นเตือน */',
    '/* Gold/Yellow accent */': '/* สีทอง/เหลือง สำหรับเน้นข้อความ */',
    '/* red string */': '/* สีเส้นด้ายแดงโยงคดี */',
    '/* Typography */': '/* การตั้งค่าฟอนต์ */',
    '/* Layout */': '/* การตั้งค่าขนาดการจัดหน้า (Layout) */',
    '# Base Styles & Reset': '# สไตล์เริ่มต้นและการรีเซ็ตค่าของเบราว์เซอร์',
    '/* Background Grid Pattern */': '/* ลวดลายตารางตีกรอบพื้นหลัง */',
    '# Typography & Utilities': '# ตัวอักษรและคลาสสารพัดประโยชน์',
    '# Buttons': '# ปุ่มกดต่างๆ',
    '# Navbar': '# แถบเมนูนำทางด้านบนสุด (Navbar)',
    '# Evidence Card Styles (Shared Module)': '# โครงสร้างกล่องแฟ้มคดี (ใช้เป็นกล่องผลงาน)',
    '/* Paper texture overlay */': '/* แผ่นกระดาษที่มีพื้นผิวขรุขระ (Texture ใส) ซ้อนทับให้กล่องดูมีราคา */',
    '/* Pushpin */': '/* หมุดปักกระดานสีแดง */',
    '/* pin shadow */': '/* เงาที่ทอดลงมาจากตัวหมุด */',
    '/* Tape */': '/* สก๊อตเทปใสแปะขอบรูป */',
    '/* Stamps */': '/* ตรายางประทับ "ลับสุดยอด" */',
    '/* distressed effect using text shadow */': '/* เอฟเฟกต์สร้างความขรุขระของตรายางผ่านลูกเล่นเงา */',
    '# Hero Section': '# ส่วนอารัมภบทหน้าแรกสุด (Hero Section)',
    '/* offset navbar */': '/* เว้นระยะบนไว้เพื่อไม่ให้ชนกับเมนู Navbar */',
    '/* Space for typewriter */': '/* เว้นพื้นที่แนวตั้งเผื่อไว้ให้เอฟเฟกต์พิมพ์ดีดทำงาน */',
    '/* Glitch Effect */': '/* เอฟเฟกต์ภาพซ้อนวิบัติ (Glitch) สำหรับตัวหนังสือ */',
    '/* Avatar Visual */': '/* ส่วนกรอบรูปภาพโปรไฟล์ของคุณ */',
    '/* subtle rotation to look like a photo on a board */': '/* จับรูปเอียงองศาเล็กน้อยให้เหมือนรูปถ่ายที่ถูดแปะหมุดไว้บนบอร์ด */',
    '/* Fallback base styles for svg photo */': '/* สไตล์สำรองเผื่อรูปภาพไม่ขึ้น */',
    '/* Clean display for the normal color profile picture */': '/* ตัดสไตล์ย้อมสีขาวดำทิ้งไป เพื่อแสดงรูปถ่ายต้นฉบับปกติแบบคมชัด */',
    '# About Section': '# ส่วนแนะนำตัว (ประวัติ)',
    '# Projects / Evidence Section (Carousel)': '# ส่วนรวมผลงาน (แบบสไลด์ Carousel แนวนอน)',
    '# Experience / Timeline': '# ส่วนประวัติการศึกษาและการทำงาน (ลำดับเวลา)',
    '/* Creates the center vertical line */': '/* สร้างเส้นไทม์ไลน์ยาวแกนกลาง */',
    '# Contact Section': '# ส่วนฟอร์มข้อมูลติดต่อ (ส่งเบาะแสคดี)',
    '# Footer': '# ส่วนท้ายหน้าเว็บไซต์ (Footer)',
    '# Responsive Design / Media Queries': '# รองรับมือถือและหน้าจอแท็บเล็ต (Responsive CSS)',
    '/* hide full menu */': '/* ซ่อนเมนูเต็มแบบคอมพิวเตอร์ออกไป */',
    '/* show hamburger */': '/* แสดงปุ่มแฮมเบอร์เกอร์แทน */'
}

js_translations = {
    'DETECTIVE OS / CLASSIFIED DOSSIER - MAIN JAVASCRIPT': 'ระบบนักสืบ / แฟ้มลับสุดยอด - ไฟล์ทำงานโต้ตอบหลัก (JavaScript)',
    '/* Language Dictionary */': '/* พจนานุกรมคำแปลภาษาชุดเต็ม */',
    '// 0. Language Toggle Logic': '// 0. โลจิกปุ่มสลับภาษา (TH <-> EN)',
    '// Update document lang': '// อัปเดตคุณสมบัติ lang บนเว็บเบราว์เซอร์ให้รู้ว่าใช้ภาษาอะไร',
    '// Update Title & Meta': '// อัปเดตหัวข้อเว็บ (Title) และรายละเอียด (Meta) เอาไว้ให้ Google อ่าน',
    '// Update all elements with data-i18n': '// กวาดดึงข้อความจาก Object มาแสดงผลตามภาษาเป้าหมาย โดยหาจาก attribute: data-i18n',
    '// If element has glitch effect, update data-text without HTML tags': '// สำหรับตัวหนังสือที่มีเอฟเฟกต์ Glitch (ภาพซ้อน) ต้องคอยอัปเดตแกนข้อความด้วย',
    '// Update placeholders explicitly if present': '// อัปเดตข้อความลายน้ำ (Placeholder) ในช่องพวก Text Input ยิบย่อย',
    '// Update Button Active state': '// อัปเดตสีของปุ่มสลับภาษาเพื่อบอกว่าตอนนี้เลือกใช้ภาษาอะไรอยู่',
    '// Initialize lang': '// ดึงภาษามาแสดงตั้งแต่ตอนเปิดหน้าเว็บครั้งแรก',
    '// Subtle theme transition overlay': '// ใส่เอฟเฟกต์ซ้อนทับแปปหนึ่งเวลาสลับภาษาเพื่อความสมูทของสายตา',
    '// 1. Initialize Year in Footer': '// 1. ให้ปีใน Footer เป็นปีอัปเดตล่าสุดอัตโนมัติตามปฏิทินคอมพิวเตอร์ปัจจุบัน',
    '// 2. Theme Toggle (Dark/Light Mode)': '// 2. โลจิกปุ่มสลับธีมสี (โหมดกลางคืน / โหมดสว่าง(กระดาษ))',
    '// Check local storage for theme preference': '// เช็คความจำของเบราว์เซอร์ ว่ารอบที่แล้วเขาเลือกดาร์กโหมดค้างไว้หรือไม่',
    '// 3. Mobile Menu Toggle': '// 3. โลจิกปุ่มเปิด/ปิด เมนูด้านบนในมุมมองมือถือ (Hamburger menu)',
    '// 4. Sticky Navbar Logic': '// 4. โลจิกลูกเล่นของเมนูนำทาง (เมื่อจอด้านบนให้พื้นหลังโปร่ง เลื่อนลงมาให้ทึบ ฯลฯ)',
    '// 5. Scroll Reveal Animation': '// 5. แอนิเมชันสำหรับเผยไอเทมขึ้นมาแบบค่อยๆ ลอยขึ้น ตอนที่เราเลื่อนหน้าเว็บลงไปถึง',
    '// Counters': '// เช็คว่ามีกล่องนับเลขตัวเลขอ่านไหม ถ้ามีให้ทำงานแอนิเมชันวิ่งๆ ด้วย',
    '// 6. Number Counter': '// 6. แอนิเมชันวิ่งตัวเลข (จาก 0 ปรู๊ดขึ้นไปถึงเลขเป้าหมาย)',
    '// 7. Typewriter Effect': '// 7. เอฟเฟกต์รัวเครื่องพิมพ์ดีด',
    '// 8. Contact Form': '// 8. ระบบฟอร์มการส่งข้อความ / รับส่งเบาะแส',
    '// Fake API Simulation': '// สถานะส่งข้อมูลจำลอง (คุณสามารถต่อ API ไปยังบริการเช่น FormReek, EmailJS ภายหลังได้ที่ตรงนี้)',
    '// 9. Carousel Logic': '// 9. โลจิกระบบสไลด์เลื่อนผลงาน (Carousel) ซ้าย/ขวา'
}


translate_file(html_path, html_translations)
translate_file(css_path, css_translations)
translate_file(js_path, js_translations)

print("All comments translated successfully!")
