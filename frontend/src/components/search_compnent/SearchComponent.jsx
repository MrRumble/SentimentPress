import { useState } from 'react';
import './SearchComponent.css'; // Import the CSS file
import LoadingSpinner from '../loading_spinner_component/LoadingSpinner';

const SearchForm = () => {
    const [query, setQuery] = useState('');
    const [searchResults, setSearchResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true); // Set loading to true when starting the fetch

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': localStorage.getItem('token')
            },
            body: JSON.stringify({ query }),
        };

        try {
            const response = await fetch(`http://localhost:5002/query`, requestOptions);
            const data = await response.json();
            console.log('Received data from server:', data);

            setSearchResults(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false); // Set loading to false when fetch is complete
        }
    };

    return (
        <div className="search-container">
            <form onSubmit={handleSubmit} className="search-form">
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Enter your search query"
                    className="search-input"
                />
                <button type="submit" className="search-button">Search</button>
            </form>

            {loading && <LoadingSpinner />}

            {searchResults && !loading && (
                <div className="results-container">
                    <div className="search-info">
                        <h2>Search Info</h2>
                        <ul>
                            <li><strong>Total Articles:</strong> {searchResults.query_info.total_articles}</li>
                            <li><strong>Positive Count:</strong> {searchResults.query_info.positive_count}</li>
                            <li><strong>Negative Count:</strong> {searchResults.query_info.negative_count}</li>
                            <li><strong>Mean Sentiment:</strong> {searchResults.query_info.mean_sentiment}</li>
                            <li><strong>Summary:</strong> {searchResults.query_info.summary}</li>
                        </ul>
                    </div>

                    <div className="articles-container">
                        <h2>Top 3 Articles</h2>
                        <ul>
                            {searchResults.top3.map((article, index) => (
                                <li key={index} className="article-item">
                                    <h3>{article.title}</h3>
                                    <p>{article.description}</p>
                                    <p><strong>Source:</strong> {article.source}</p>
                                    <p><strong>Published Date:</strong> {new Date(article.published_date).toLocaleDateString()}</p>
                                    <p><strong>Sentiment Score:</strong> {article.sentiment}</p>
                                </li>
                            ))}
                        </ul>

                        <h2>Bottom 3 Articles</h2>
                        <ul>
                            {searchResults.bottom3.map((article, index) => (
                                <li key={index} className="article-item">
                                    <h3>{article.title}</h3>
                                    <p>{article.description}</p>
                                    <p><strong>Source:</strong> {article.source}</p>
                                    <p><strong>Published Date:</strong> {new Date(article.published_date).toLocaleDateString()}</p>
                                    <p><strong>Sentiment Score:</strong> {article.sentiment}</p>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </div>
    );
};

export default SearchForm;
