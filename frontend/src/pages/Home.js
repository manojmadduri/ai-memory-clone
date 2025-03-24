// src/pages/Home.js
import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl font-bold mb-4">🧠 My AI Memory Clone</h1>
      <p className="text-lg mb-6 text-gray-600">
        Upload your memories, explore by person or timeline, and let your AI self recall the past.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-2xl mx-auto">
        <Link
          to="/upload"
          className="p-6 bg-blue-500 text-white rounded-xl shadow hover:bg-blue-600 transition"
        >
          📤 Upload a Memory
        </Link>

        <Link
          to="/people"
          className="p-6 bg-green-500 text-white rounded-xl shadow hover:bg-green-600 transition"
        >
          👥 View by People
        </Link>

        <Link
          to="/timeline"
          className="p-6 bg-purple-500 text-white rounded-xl shadow hover:bg-purple-600 transition"
        >
          🕒 View by Timeline
        </Link>

        <Link
          to="/memory/preview"
          className="p-6 bg-gray-800 text-white rounded-xl shadow hover:bg-gray-900 transition"
        >
          🔍 Memory Search (Coming Soon)
        </Link>
      </div>
    </div>
  );
};

export default Home;
