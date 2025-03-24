// src/components/MemoryCard.js
import React from "react";
import { Link } from "react-router-dom";

const MemoryCard = ({ memory }) => (
  <div className="border p-4 rounded shadow">
    <p>{memory.content}</p>
    {memory.image_id && (
      <img
        className="mt-2 w-full object-cover"
        src={`https://your-project.supabase.co/storage/v1/object/public/memories/${memory.image_id}.jpg`}
        alt=""
      />
    )}
    <Link to={`/memory/${memory.id}`} className="text-blue-600 text-sm mt-2 block">
      View More
    </Link>
  </div>
);

export default MemoryCard;
