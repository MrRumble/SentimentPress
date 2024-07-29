import React from 'react';
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
  return (
    <Router>
      <div className="app">
        <SpinningGlobe />
        <NavBar />
        <div className="content">
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/logout" element={<Logout />} />
            <Route path="/logged-in-as" element={<LoggedInAs />} />
            <Route path="/" element={<SearchForm />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
