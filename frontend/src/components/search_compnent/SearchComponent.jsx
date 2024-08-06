// src/components/search_component/SearchForm.jsx

import { useState } from 'react';
import './SearchComponent.css'; // Import the CSS file
import LoadingSpinner from '../loading_spinner_component/LoadingSpinner';
import SearchInput from './SearchInput';
import SearchResults from './SearchResults';

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
            <SearchInput query={query} setQuery={setQuery} handleSubmit={handleSubmit} />

            {loading && <LoadingSpinner />}

            {searchResults && !loading && (
                <SearchResults searchResults={searchResults} />
            )}
        </div>
    );
};

export default SearchForm;
