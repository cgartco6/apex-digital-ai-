import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between">
      <div className="font-bold">Apex Digital AI</div>
      <div className="space-x-4">
        <Link to="/">Home</Link>
        <Link to="/services">Services</Link>
        <Link to="/projects">Projects</Link>
        <Link to="/dashboard">Dashboard</Link>
      </div>
    </nav>
  );
}
