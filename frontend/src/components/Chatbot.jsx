import React, { useState } from "react";
import axios from "axios";

export default function Chatbot({ userId }) {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input) return;
        setMessages([...messages, { role: "user", content: input }]);
        const res = await axios.post("http://localhost:8000/chat/chat", {
            user_id: userId,
            message: input
        });
        setMessages([...messages, { role: "user", content: input }, { role: "assistant", content: res.data.response }]);
        setInput("");
    };

    return (
        <div className="chatbot p-4 border rounded w-96">
            <div className="messages h-64 overflow-auto mb-2">
                {messages.map((m, idx) => (
                    <div key={idx} className={m.role === "user" ? "text-right" : "text-left"}>
                        <span className={`px-2 py-1 rounded ${m.role==="user"?"bg-blue-500 text-white":"bg-gray-200"}`}>
                            {m.content}
                        </span>
                    </div>
                ))}
            </div>
            <div className="input flex">
                <input
                    className="flex-1 border px-2 py-1"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Ask Robyn..."
                />
                <button className="ml-2 px-4 bg-blue-600 text-white" onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
                                                                     }
