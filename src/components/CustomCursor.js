import React, { useEffect } from "react";
const rocketCursor = "/rocket.gif"; // ใช้ path จาก public/

function CustomCursor() {
  useEffect(() => {
    console.log("🚀 CustomCursor Component Loaded!"); // ตรวจสอบว่าฟังก์ชันทำงาน

    const cursor = document.createElement("div");
    cursor.style.position = "fixed";
cursor.style.width = "50px"; // ปรับขนาดของ GIF
cursor.style.height = "50px";
cursor.style.pointerEvents = "none"; // ไม่ให้รบกวนการคลิก
cursor.style.backgroundImage = `url(/rocket.gif)`;
cursor.style.backgroundSize = "cover";
cursor.style.zIndex = "9999";
cursor.style.transform = "translate(-50%, -50%)"; // ให้ cursor อยู่ตรงกลาง

    document.body.appendChild(cursor);

    const moveCursor = (e) => {
      requestAnimationFrame(() => {
        cursor.style.left = `${e.clientX}px`;
        cursor.style.top = `${e.clientY}px`;
      });
    };    

    window.addEventListener("mousemove", moveCursor);

    return () => {
      console.log("🛑 CustomCursor Component Unmounted!");
      window.removeEventListener("mousemove", moveCursor);
      document.body.removeChild(cursor);
    };
  }, []);

  return null;
}

export default CustomCursor;
