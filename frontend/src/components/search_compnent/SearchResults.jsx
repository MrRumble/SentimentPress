// src/components/search_component/SearchResults.jsx

import React from 'react';
import Speedometer from '../speedometer_component/Speedometer';
import ResultsInfo from './ResultsInfo';
import ArticleList from './ArticleList';

const SearchResults = ({ searchResults }) => {
    return (
        <div>
            <div className="speedometer-container">
                <Speedometer value={searchResults.query_info.mean_sentiment} />
            </div>

            <div className="results-container">
                <ResultsInfo queryInfo={searchResults.query_info} />

                <div className="articles-layout">
                    <ArticleList title="Top 3 Articles" articles={searchResults.top3} />
                    <ArticleList title="Bottom 3 Articles" articles={searchResults.bottom3} />
                </div>
            </div>
        </div>
    );
};

export default SearchResults;
