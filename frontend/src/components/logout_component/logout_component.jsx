import React from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = ({ onLogout }) => {
  const navigate = useNavigate();

  const handleLogout = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:5002/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ jti: localStorage.getItem('token') }),
      });

      if (response.ok) {
        localStorage.clear(); // Clear localStorage after successful logout
        onLogout(); // Notify parent component of successful logout
        navigate('/login'); // Redirect to login page
      } else {
        console.error('Logout failed:', await response.text());
      }
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <button onClick={handleLogout}>
      Logout
    </button>
  );
};

export default Logout;
