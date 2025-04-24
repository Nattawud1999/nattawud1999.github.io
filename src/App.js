import { useTranslation } from 'react-i18next';
import React, { useState, useEffect } from "react";
import Preloader from "../src/components/Pre";
import Navbar from "./components/Navbar";
import Home from "./components/Home/Home";
import About from "./components/About/About";
import Projects from "./components/Projects/Projects";
import Footer from "./components/Footer";
import Resume from "./components/Resume/ResumeNew";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate
} from "react-router-dom";
import ScrollToTop from "./components/ScrollToTop";
import "./style.css";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
// import CustomCursor from "./components/CustomCursor";

function App() {
  const [load, upadateLoad] = useState(true);
  const { i18n, t } = useTranslation();

  const changeLanguage = (lang) => {
    i18n.changeLanguage(lang);
    console.log("Current language:", i18n.language);
  };

  // ✅ ให้โหลดจนเสร็จจริง
  useEffect(() => {
    const handleWindowLoad = () => {
      upadateLoad(false);
    };
    window.addEventListener("load", handleWindowLoad);
    return () => window.removeEventListener("load", handleWindowLoad);
  }, []);

  // ✅ เอฟเฟกต์เม้าส์ฟรุ้งฟริ้ง
  useEffect(() => {
    const handleClick = (e) => {
      for (let i = 0; i < 10; i++) {
        const sparkle = document.createElement("span");
        sparkle.className = "click-star";
        
        // ตำแหน่งเริ่ม
        sparkle.style.left = `${e.clientX}px`;
        sparkle.style.top = `${e.clientY}px`;
    
        // สุ่มทิศทาง
        const angle = Math.random() * 2 * Math.PI;
        const distance = 40 + Math.random() * 20;
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;
    
        sparkle.style.setProperty("--x", `${x}px`);
        sparkle.style.setProperty("--y", `${y}px`);
    
        document.body.appendChild(sparkle);
        setTimeout(() => sparkle.remove(), 600);
      }
    };
    

    window.addEventListener("click", handleClick);
    return () => window.removeEventListener("click", handleClick);
  }, []);

  return (
    <Router>
      <Preloader load={load} />
      <div className="App" id={load ? "no-scroll" : "scroll"}>
        <div>
          {/* <CustomCursor /> */}

          {/* ปุ่มเปลี่ยนภาษา */}
          <div
            style={{
              position: "fixed",
              top: "15px",
              left: window.innerWidth <= 480 ? "50%" : "auto",
              right: window.innerWidth <= 480 ? "auto" : "15px",
              transform: window.innerWidth <= 480 ? "translateX(-50%)" : "none",
              zIndex: 9999,
            }}
          >
            <div
              style={{
                display: "flex",
                backgroundColor: "#2c2c2e",
                borderRadius: "999px",
                padding: "3px",
                width: "88px",
                justifyContent: "space-between",
                alignItems: "center",
                position: "relative",
                fontSize: "0.85rem",
                fontWeight: "bold",
                color: "#fff",
              }}
            >
              <div
                style={{
                  position: "absolute",
                  top: "3px",
                  left: i18n.language === "th" ? "3px" : "calc(100% - 43px)",
                  width: "40px",
                  height: "24px",
                  backgroundColor: "#00bfff",
                  borderRadius: "999px",
                  transition: "left 0.3s ease",
                  zIndex: 1,
                }}
              ></div>

              <div
                onClick={() => changeLanguage("th")}
                style={{
                  width: "40px",
                  height: "24px",
                  textAlign: "center",
                  lineHeight: "24px",
                  zIndex: 2,
                  cursor: "pointer",
                  userSelect: "none",
                }}
              >
                TH
              </div>

              <div
                onClick={() => changeLanguage("en")}
                style={{
                  width: "40px",
                  height: "24px",
                  textAlign: "center",
                  lineHeight: "24px",
                  zIndex: 2,
                  cursor: "pointer",
                  userSelect: "none",
                }}
              >
                EN
              </div>
            </div>
          </div>
        </div>

        <Navbar />
        <ScrollToTop />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/project" element={<Projects />} />
          <Route path="/about" element={<About />} />
          <Route path="/resume" element={<Resume />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
