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
import img7 from "../../Assets/project7.png";
import img8 from "../../Assets/project8.png";
import img9 from "../../Assets/project9.png";
import img10 from "../../Assets/project10.png";
import img11 from "../../Assets/project11.png";
import img12 from "../../Assets/project12.png";
import img13 from "../../Assets/project13.png";
import img14 from "../../Assets/project14.png";



const itemsPerPage = 3;

function Performance() {
  const { t } = useTranslation();
  
const performanceData = [
  {
    img: img1,
    title: t("รูป1"),
    desc: t("อธิบายรูป1")
  },
  {
    img: img2,
    title: t("รูป2"),
    desc: t("อธิบายรูป2")
  },
  {
    img: img3,
    title: t("รูป3"),
    desc: t("อธิบายรูป3")
  },
  {
    img: img4,
    title: t("รูป4"),
    desc: t("อธิบายรูป4")
  },
  {
    img: img5,
    title: t("รูป5"),
    desc: t("อธิบายรูป5")
  },
  {
    img: img6,
    title: t("รูป6"),
    desc: t("อธิบายรูป6")
  },
  {
    img: img7,
    title: t("รูป7"),
    desc: t("อธิบายรูป7")
  },
  {
    img: img8,
    title: t("รูป8"),
    desc: t("อธิบายรูป8")
  },
  {
    img: img9,
    title: t("รูป9"),
    desc: t("อธิบายรูป9")
  },
  {
    img: img10,
    title: t("รูป10"),
    desc: t("อธิบายรูป10")
  },
  {
    img: img11,
    title: t("รูป11"),
    desc: ""
  },
  {
    img: img12,
    title: t("รูป11"),
    desc: ""
  },
  {
    img: img13,
    title: t("รูป13"),
    desc: t("อธิบายรูป13")
  },
  {
    img: img14,
    title: t("รูป14"),
    desc: ""
  }


];

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
            ⬅️ {t("ย้อนกลับ")}
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
            {t("ถัดไป")} ➡️
          </Button>
        </div>
      </Container>
    </>
  );
}

export default Performance;
