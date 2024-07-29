import React from 'react';
import './NavBar.css';

const NavBar = () => {
  return (
    <div className="nav-bar">
        <a href="/signup" className="nav-link">Sign Up</a>
        <a href="/login" className="nav-link">Log In</a>
        <a href="/logout" className="nav-link">Log Out</a>
    </div>
  );
};

export default NavBar;
