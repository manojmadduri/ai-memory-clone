// src/components/Navbar.js
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <nav className="flex gap-4 p-4 bg-gray-800 text-white">
    <Link to="/">Home</Link>
    <Link to="/upload">Upload</Link>
    <Link to="/people">People</Link>
    <Link to="/timeline">Timeline</Link>
    <Link to="/chat">💬 Chat</Link>

  </nav>
);

export default Navbar;
