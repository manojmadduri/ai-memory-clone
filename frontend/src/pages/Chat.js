import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [query, setQuery] = useState("");
  const [history, setHistory] = useState([]);

  const ask = async () => {
    const res = await axios.post("http://localhost:8000/chat", { query });
    setHistory([...history, { query, reply: res.data.reply }]);
    setQuery("");
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">🧠 Talk to Your Memories</h2>

      <div className="space-y-4">
        {history.map((chat, i) => (
          <div key={i}>
            <p className="font-semibold">🗨️ You: {chat.query}</p>
            <p className="text-gray-700">🤖 Clone: {chat.reply}</p>
          </div>
        ))}
      </div>

      <div className="mt-6 flex gap-2">
        <input
          className="flex-1 p-2 border rounded"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask anything..."
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={ask}>
          Ask
        </button>
      </div>
    </div>
  );
};

export default Chat;
