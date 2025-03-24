// src/App.js
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Upload from "./pages/Upload";
import People from "./pages/People";
import Timeline from "./pages/Timeline";
import MemoryView from "./pages/MemoryView";
import Chat from "./pages/Chat";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/people" element={<People />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/memory/:id" element={<MemoryView />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
