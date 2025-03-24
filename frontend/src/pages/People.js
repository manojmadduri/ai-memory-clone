// src/pages/People.js
import React, { useEffect, useState } from "react";
import axios from "axios";
import MemoryCard from "../components/MemoryCard";

const People = () => {
  const [clusters, setClusters] = useState({});

  useEffect(() => {
    axios.get("http://localhost:8000/memory/by-person")
      .then(res => setClusters(res.data));
  }, []);

  return (
    <div className="p-4">
      {Object.entries(clusters).map(([person, memories]) => (
        <div key={person}>
          <h2 className="text-lg font-bold">{person}</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {memories.map(mem => <MemoryCard key={mem.id} memory={mem} />)}
          </div>
        </div>
      ))}
    </div>
  );
};

export default People;
