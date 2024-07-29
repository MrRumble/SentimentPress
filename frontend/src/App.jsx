import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';

import SpinningGlobe from './components/globe_component/GlobeComponent';
import SearchForm from './components/search_compnent/SearchComponent';
import Signup from "./components/signup/signupComponent";
import Login from "./components/login_component/loginComponent";
import Logout from "./components/logout_component/logout_component";
import LoggedInAs from './components/currently_logged_in_as_component/CurrentlyLoggedInAs';
import NavBar from './components/navbar_component/NavBar';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check login status when the component mounts
  useEffect(() => {
    const token = localStorage.getItem('token');
    setIsLoggedIn(!!token);
  }, []);

  // Handle login status change
  const handleLoginStatusChange = (loggedIn) => {
    setIsLoggedIn(loggedIn);
  };

  return (
    <Router>
      <div className="app">
        <SpinningGlobe />
        <NavBar isLoggedIn={isLoggedIn} /> {/* Pass isLoggedIn prop */}
        <div className="content">
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login onLoginStatusChange={handleLoginStatusChange} />} />
            <Route path="/logout" element={<Logout onLogout={() => handleLoginStatusChange(false)} />} />
            <Route path="/logged-in-as" element={isLoggedIn ? <LoggedInAs /> : null} />
            <Route path="/" element={<SearchForm />} />
          </Routes>
        </div>
        {isLoggedIn && <LoggedInAs />}
      </div>
    </Router>
  );
};

export default App;
