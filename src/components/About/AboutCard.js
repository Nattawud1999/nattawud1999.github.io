import React from "react";
import Card from "react-bootstrap/Card";
import { ImPointRight } from "react-icons/im";
import { useTranslation } from 'react-i18next';

function AboutCard() {
  const {  t } = useTranslation(); // ✅ เพิ่มฟังชั่นแปลภาษา ต้อง Import จากด้านบนมาก่อน
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{ textAlign: "justify" }}>
          {t("สวัสดีครับผมชื่อ")}<span className="purple">{t("ณัฐวุฒิ-เสนาทอง")}</span>
          {t("มาจาก")}<span className="purple">{t("จังหวัดนครศรีธรรมราช ประเทศ ไทย")}</span>
            <br />
            {t("ปัจจุบันผมทำงานเป็น IT-Support & Network")}
            <br />
            {t("อยู่ที่กรุงเทพมหานคร")}
            <br />
            <br />
            {t("นอกจากการเขียน Code ยังมีกิจกรรมอื่นๆที่ผมสนใจ")}
          </p>
          <ul>
            <li className="about-activity">
              <ImPointRight /> {t("เล่นเกมส์")}
            </li>
            <li className="about-activity">
              <ImPointRight /> {t("ดูหนัง")}
            </li>
            <li className="about-activity">
              <ImPointRight /> {t("และชอบเล่นฟุตบอล")}
            </li>
          </ul>

          <p style={{ color: "rgb(155 126 172)" }}>
          {t("ไม่หยุดที่จะเรียนรู้สิ่งใหม่ๆ")}{" "}
          </p>
          <footer className="blockquote-footer">Nattawut</footer>
        </blockquote>
      </Card.Body>
    </Card>
  );
}

export default AboutCard;
