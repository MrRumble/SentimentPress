// src/components/search_component/ResultsInfo.jsx

import React from 'react';
import './SearchComponent.css'; // Import the CSS file

const ResultsInfo = ({ queryInfo }) => {
    return (
        <div className="info-container">
            <div className="info-item">
                <strong>Total Articles:</strong> {queryInfo.total_articles}
            </div>
            <div className="info-item">
                <strong>Positive Count:</strong> {queryInfo.positive_count}
            </div>
            <div className="info-item">
                <strong>Negative Count:</strong> {queryInfo.negative_count}
            </div>
            <div className="info-item">
                <strong>Summary:</strong> {queryInfo.summary}
            </div>
        </div>
    );
};

export default ResultsInfo;
