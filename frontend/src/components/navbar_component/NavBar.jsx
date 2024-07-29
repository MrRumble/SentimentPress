// NavBar.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css'; // Optional: for styling

const NavBar = () => {
  return (
    <div className="navbar">
      <Link to="/signup">Sign Up</Link>
      <Link to="/login">Log In</Link>
      <Link to="/logout">Log Out</Link>
      <Link to="/">Search</Link>
    </div>
  );
};

export default NavBar;
