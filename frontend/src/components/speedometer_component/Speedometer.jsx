// src/components/speedometer_component/Speedometer.jsx

import React from 'react';
import ReactSpeedometer from "react-d3-speedometer";
import './Speedometer.css';

const Speedometer = ({ value }) => {
  return (
    <div>
      <ReactSpeedometer
        minValue={-1}
        maxValue={1}
        value={value}
        segments={5}
        height={300}
        needleTransitionDuration={4000}
        needleTransition="easeElastic"
        customSegmentStops={[-1, -0.6, -0.2, 0.2, 0.6, 1]}
        segmentColors={["#d9534f", "#f0ad4e", "#f7f7f7", "#5bc0de", "#5cb85c"]}
        needleColor="black"
        currentValueText={`Sentiment Score: ${value.toFixed(2)}`}
        customSegmentLabels={[
          {
            text: "😞", // Very Bad
            position: "INSIDE",
            color: "#ffffff",
          },
          {
            text: "🙁", // Bad
            position: "INSIDE",
            color: "#ffffff",
          },
          {
            text: "😐", // Average
            position: "INSIDE",
            color: "#000000",
          },
          {
            text: "🙂", // Good
            position: "INSIDE",
            color: "#ffffff",
          },
          {
            text: "😃", // Very Good
            position: "INSIDE",
            color: "#ffffff",
          },
        ]}
      />
    </div>
  );
};

export default Speedometer;
