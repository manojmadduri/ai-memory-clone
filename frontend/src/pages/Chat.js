import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [query, setQuery] = useState("");
  const [history, setHistory] = useState([]);

  const ask = async () => {
    try {
      const res = await axios.post("http://localhost:8000/chat", { query });
      const { reply, memories_used } = res.data;
      console.log("🚀 Backend response:", res.data);


      setHistory([
        ...history,
        {
          query,
          reply,
          memories: memories_used || [],
        },
      ]);

      setQuery("");
    } catch (err) {
      console.error("Failed to fetch chat:", err);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-4">🧠 Talk to Your Memories</h2>

      <div className="space-y-6">
        {history.map((chat, i) => (
          <div key={i} className="bg-gray-100 p-3 rounded">
            <p className="font-semibold">🗨️ You: {chat.query}</p>
            <p className="text-gray-800">🤖 Clone: {chat.reply}</p>

            {/* {chat.memories.length > 0 && (
              <div className="mt-2">
                <p className="text-sm font-medium text-gray-600">📚 Memories used:</p>
                <ul className="list-disc list-inside text-sm text-gray-700">
                  {chat.memories.map((mem, idx) => (
                    <li key={idx}>{mem}</li>
                  ))}
                </ul>
              </div>
            )} */}
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
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded"
          onClick={ask}
        >
          Ask
        </button>
      </div>
    </div>
  );
};

export default Chat;
