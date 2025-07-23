import React, { useState } from "react";
import { Container, Row, Col, Card, Button } from "react-bootstrap";
import { useTranslation } from 'react-i18next';
import Particle from "../Particle";

import img1 from "../../Assets/project1.png";
import img2 from "../../Assets/project2.png";
import img3 from "../../Assets/project3.png";
import img4 from "../../Assets/project4.png";
import img5 from "../../Assets/project5.png";
import img6 from "../../Assets/project6.png";
import img7 from "../../Assets/project7.png"; // เปลี่ยนรูปตามจริงได้เลย

const performanceData = [
  {
    img: img1,
    title: "ติดตั้งระบบ CCTV",
    desc: "ติดตั้งระบบ CCTV จำนวน50ตัว ใช้ระบบ IP Address SW POE สามารถดูกล้องผ่าน IP/Phone ควบคุมและจัดการสะดวก"
  },
  {
    img: img2,
    title: "Setup และ Backup SW,Mikrotik",
    desc: "Setup ระบบ Mikrotik จำนวน 4 ISP ในประเทศกัมพูชา ทำระบบ QOS การใช้งานในแต่ละห้อง ทำระบบ Backup Internet สำรองกรณีฉุกเฉิน"
  },
  {
    img: img3,
    title: "ติดตั้ง SW,Mikrotik,NAS 4ISP",
    desc: "เชื่อมต่อกับ 4ISP จัดการระบบ IP-Address,NAS Server"
  },
  {
    img: img4,
    title: "ตั้งค่า CCTV",
    desc: "จัดการ IP-Address ด้วย SADP Tool (Search Active Device Protocol)"
  },
  {
    img: img5,
    title: "จัดระบบ SWA/SWB/NAS Server",
    desc: "ตั้งค่าระบบ SWA/SWB และ NAS Server ให้สามารถทำงานได้อย่างมีประสิทธิภาพ"
  },
  {
    img: img6,
    title: "CCTV Hikvision",
    desc: "ขั้นตอนการ Setup CCTV"
  },
  {
    img: img7,
    title: "ติดตั้ง ระบบ Wifi CA1",
    desc: "ใช้ ISP TODAY 100Mb ต่อเข้า Mikrotik-SwitchPOE-AP 2.4g/5g"
  }
];

const itemsPerPage = 3;

function Performance() {
  const { t } = useTranslation();
  const [currentPage, setCurrentPage] = useState(1);

  const totalPages = Math.ceil(performanceData.length / itemsPerPage);
  const startIdx = (currentPage - 1) * itemsPerPage;
  const currentItems = performanceData.slice(startIdx, startIdx + itemsPerPage);

  const handlePrev = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handleNext = () => {
  if (currentPage < totalPages) {
    setCurrentPage(currentPage + 1);
    console.log(">>> NEXT to page", currentPage + 1);
  }
};


  return (
    <>
      <Particle />

      <Container style={{ paddingTop: "140px" }}>
        <h2
          className="text-center mb-4"
          style={{
            color: "#b266ff",
            textShadow: "0 0 10px #b266ff, 0 0 20px #b266ff",
            fontWeight: "bold"
          }}
        >
          {t("ผลงาน")}
        </h2>

        <Row>
          {currentItems.map((item, idx) => (
            <Col md={4} sm={6} xs={12} key={idx} className="mb-4">
              <Card>
                <Card.Img variant="top" src={item.img} />
                <Card.Body>
                  <Card.Title>{item.title}</Card.Title>
                  <Card.Text>{item.desc}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>

        {/* ปุ่มถัดไป/ย้อนกลับ */}
        <div className="d-flex justify-content-center mt-4 gap-3">
          <Button
            variant="outline-light"
            style={{
              color: "#b266ff",
              borderColor: "#b266ff",
              textShadow: "0 0 5px #b266ff, 0 0 1px #b266ff",
              fontWeight: "bold"
            }}
            disabled={currentPage === 1}
            onClick={handlePrev}
          >
            ⬅️ ย้อนกลับ
          </Button>

          <Button
            variant="outline-light"
            style={{
              color: "#b266ff",
              borderColor: "#b266ff",
              textShadow: "0 0 5px #b266ff, 0 0 1px #b266ff",
              fontWeight: "bold"
            }}
            disabled={currentPage === totalPages}
            onClick={handleNext}
          >
            ถัดไป ➡️
          </Button>
        </div>
      </Container>
    </>
  );
}

export default Performance;
