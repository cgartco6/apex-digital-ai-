import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Chatbot from "../components/Chatbot";

function Dashboard() {
    const userId = "user_123"; // dynamic per logged-in user
    return (
        <div>
            <h1>Dashboard</h1>
            <Chatbot userId={userId} />
        </div>
    );
}

export default function Dashboard() {
    const [tierData, setTierData] = useState({});
    const [projectData, setProjectData] = useState({name:"My Project"});

    useEffect(() => {
        axios.post("http://localhost:8000/recommend_tier", {
            monthly_projects: 12,
            design_complexity: 3,
            marketing_campaigns: 5
        }).then(res => setTierData(res.data));
    }, []);

    const schedulePosts = () => {
        axios.post("http://localhost:8000/schedule_posts", {
            project: projectData,
            platforms: ["TikTok","Instagram","YouTube","X"]
        }).then(res => console.log(res.data));
    }

    return (
        <div>
            <h2>Your Recommended Tier: {tierData.recommended_tier}</h2>
            <h3>Recommended Credits: {tierData.recommended_credits}</h3>
            <button onClick={schedulePosts}>Schedule Social Media Posts</button>
        </div>
    );
          }
