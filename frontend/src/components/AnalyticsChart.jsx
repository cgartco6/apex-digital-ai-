import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";

export default function AnalyticsChart() {
  const [data, setData] = useState({labels:[], datasets:[]});

  useEffect(() => {
    // Fetch analytics data from backend
    fetch("http://localhost:8000/analytics/report")
      .then(res => res.json())
      .then(json => {
        setData({
          labels: ["Revenue"],
          datasets: [{ label: "Total Revenue", data: [json.total_revenue], borderColor: "blue", fill: false }]
        });
      });
  }, []);

  return <Line data={data} />;
                                   }
