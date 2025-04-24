import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import myImg from "../../Assets/avatar.svg";
import Tilt from "react-parallax-tilt";
import { useTranslation } from 'react-i18next';
import {
  AiFillGithub,
  AiFillInstagram,
  AiFillFacebook,
} from "react-icons/ai";

function Home2() {
  const {  t } = useTranslation(); // ✅ เพิ่มฟังชั่นแปลภาษา ต้อง Import จากด้านบนมาก่อน
  return (
    <Container fluid className="home-about-section" id="about">
      <Container>
        <Row>
          <Col md={8} className="home-about-description">
            <h1 style={{ fontSize: "2.6em" }}>
              <span className="purple"> {t("ให้ผมPresen")} </span> {t("แบบสั้นๆ")}
            </h1>
            <p className="home-about-body">
            {t("ผมชื่นชอบในการแก้ไขปัญหาด้าน IT & Network")}
              <br />
              <br />{t("ผมมีความรู้ด้าน Hardware และ Firewall")}
              <i>
                <b className="purple"> Mangle TCP/IP </b>
              </i>
              <br />
              <br />
              {t("ผมสามารถซ่อมและแก้ไขปัญหาคอมพิวเตอร์ได้เกือบทุกรูปแบบ")} &nbsp;
              <i>
                <b className="purple">{t("รวมไปถึง Printer")} </b> {t("และ")}{" "}
                <b className="purple">{t("อุปกรณ์ต่อพ่วงอื่นๆ")}</b>
              </i>
              <br />
              <br />
              {t("และผมยังชื่นชอบการเขียน code")}{" "}
              <b className="purple">{t("ตอนนี้ผมยังไม่ค่อยมี Skill ในด้านนี้")}</b>{" "}
              {t("แต่ในอนาคต")}
              <i>
                <b className="purple">
                  {" "}
                  {t("ผมมั่นใจว่า ผมจะมี Project ใหญ่ๆเป็นของตัวเองและจะมาอัพเดตในเว็ปไซต์นี้")}
                </b>
              </i>
              &nbsp; 
              <i>
                <b className="purple"> </b>
              </i>
            </p>
          </Col>
          <Col md={4} className="myAvtar">
            <Tilt>
              <img src={myImg} className="img-fluid" alt="avatar" />
            </Tilt>
          </Col>
        </Row>
        <Row>
          <Col md={12} className="home-about-social">
            <h1>{t("ติดตามผมได้ทาง")}</h1>
            <p>
            {t("ช่องทางการติดต่อ")} <span className="purple">{t("ด้านล่างนี้")} </span>
            </p>
            <ul className="home-about-social-links">
              <li className="social-icons">
                <a
                  href="https://github.com/Nattawud1999"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillGithub />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://www.facebook.com/share/19o2jREnKF/"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillFacebook />
                </a>
              </li>

              <li className="social-icons">
                <a
                  href="https://www.instagram.com/firsttsanatong?igsh=MWQ5d3p3cGh1a2J3eg=="
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour home-social-icons"
                >
                  <AiFillInstagram />
                </a>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}

export default Home2;