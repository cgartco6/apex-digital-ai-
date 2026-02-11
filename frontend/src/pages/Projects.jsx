import React from "react";

export default function Projects() {
    const sampleProjects = ["Brand Design", "Social Media Campaign", "Website UI Mockup"];
    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold">Your Projects</h1>
            <ul className="mt-4 list-disc list-inside">
                {sampleProjects.map((p, idx) => <li key={idx}>{p}</li>)}
            </ul>
        </div>
    );
}
