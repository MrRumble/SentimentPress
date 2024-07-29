// src/components/speedometer_component/Speedometer.jsx

import React from 'react';
import Speedometer from 'react-speedometer';

const SentimentSpeedometer = ({ sentimentScore }) => (
    <div className="speedometer-container">
        <Speedometer
            value={0.5}
            minValue={-1}  // Adjust according to your sentiment score range
            maxValue={1}
            needleColor="red"
            startColor="blue"
            endColor="green"
            textColor="black"
            segments={10}
            maxSegmentValue={0.5} // Customize according to your range
        />
    </div>
);

export default SentimentSpeedometer;
