import React from "react";

export default function Services() {
    const services = [
        "AI Project Generation",
        "Marketing Campaigns",
        "Social Media Automation",
        "PDF Contracts & T&Cs",
        "Analytics & Revenue Tracking",
    ];

    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold">Our Services</h1>
            <ul className="mt-4 list-disc list-inside">
                {services.map((s, idx) => <li key={idx}>{s}</li>)}
            </ul>
        </div>
    );
}
