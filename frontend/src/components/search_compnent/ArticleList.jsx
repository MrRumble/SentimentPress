import React from 'react';
import './SearchComponent.css'; // Import the CSS file

const ArticleList = ({ title, articles }) => {
    return (
        <div className="articles-column">
            <h2>{title}</h2>
            <ul>
                {articles.map((article, index) => (
                    <li key={index} className="article-item">
                        <h3>{article.title}</h3>
                        <p>{article.description}</p>
                        <p><strong>Source:</strong> {article.source}</p>
                        <p><strong>Published Date:</strong> {new Date(article.published_date).toLocaleDateString()}</p>
                        <p><strong>Sentiment Score:</strong> {article.sentiment.toFixed(4)}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ArticleList;
