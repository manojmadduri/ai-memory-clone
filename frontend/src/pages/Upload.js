import React, { useState } from "react";
import axios from "axios";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const upload = async () => {
    if (!file) {
      setStatus("❗ No file selected");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    setStatus("Uploading...");

    try {
      await axios.post("http://127.0.0.1:8000/image/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setStatus("✅ Success! Memory processed.");
    } catch (error) {
      console.error("Upload failed:", error);
      setStatus("❌ Upload failed. Check backend & CORS settings.");
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">📤 Upload an Image</h2>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="block mb-4"
      />
      <button
        onClick={upload}
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded shadow"
      >
        Upload
      </button>
      <p className="mt-4 text-sm text-gray-700">{status}</p>
    </div>
  );
};

export default Upload;
