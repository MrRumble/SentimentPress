// NavBar.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import './NavBar.css'; // Optional: for styling

const NavBar = ({ isLoggedIn }) => {
  return (
    <div className="navbar">
      <Link to="/signup">Sign Up</Link>
      {isLoggedIn ? (
        <>
          <Link to="/logout">Log Out</Link>
          <Link to="/my-profile">My Profile</Link> {/* Added "My Profile" link */}
        </>
      ) : (
        <Link to="/login">Log In</Link>
      )}
      <Link to="/">Search</Link>
    </div>
  );
};

export default NavBar;
