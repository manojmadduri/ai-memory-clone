// src/pages/MemoryView.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const MemoryView = () => {
  const { id } = useParams();
  const [memory, setMemory] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/memory/query?query=id:${id}`)
      .then(res => setMemory(res.data.results[0]));
  }, [id]);

  return memory ? (
    <div className="p-4">
      <h1 className="text-2xl font-bold">{memory.content}</h1>
      {memory.image_id && (
        <img
          className="mt-4 w-full object-cover"
          src={`https://your-project.supabase.co/storage/v1/object/public/memories/${memory.image_id}.jpg`}
          alt=""
        />
      )}
    </div>
  ) : <p>Loading...</p>;
};

export default MemoryView;
