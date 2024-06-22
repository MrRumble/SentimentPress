//SERVICE FILES ARE FETCHING THE DATA FROM THE BACKEND
import axios from 'axios';

const ApiService = {
    fetchData: async () => {
        try {
            const response = await axios.get('http://localhost:5002/test');
            console.log(response.data); 
            return response.data;
        } catch (error) {
            console.error('Error fetching data:', error);
            throw new Error('Error fetching data:', error);
        }
    }
};

export default ApiService;
