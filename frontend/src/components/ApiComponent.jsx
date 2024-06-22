import React, { useState, useEffect } from 'react';
import ApiService from '../services/ApiService';

const MyComponent = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const fetchedData = await ApiService.fetchData();
                const parsedData = JSON.parse(fetchedData);
                setData(parsedData);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>Data from Backend</h1>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>
                        <h3>{item.Title}</h3>
                        <p>{item.Description}</p>
                        <p>Source: {item.Source}</p>
                        <p>Sentiment Score: {item['Sentiment Score']}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MyComponent;
