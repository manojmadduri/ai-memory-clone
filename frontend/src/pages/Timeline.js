// src/pages/Timeline.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import MemoryCard from "../components/MemoryCard";

const Timeline = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get("http://localhost:8000/memory/by-timeline?granularity=week")
      .then(res => setData(res.data));
  }, []);

  return (
    <div className="p-4">
      {Object.entries(data).map(([time, memories]) => (
        <div key={time}>
          <h2 className="text-lg font-bold">{time}</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {memories.map(mem => <MemoryCard key={mem.id} memory={mem} />)}
          </div>
        </div>
      ))}
    </div>
  );
};

export default Timeline;
