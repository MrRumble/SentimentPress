// src/components/search_component/SearchInput.jsx

import React from 'react';
import './SearchComponent.css'; // Import the CSS file

const SearchInput = ({ query, setQuery, handleSubmit }) => {
    return (
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
    );
};

export default SearchInput;
