// import React from 'react';
import './App.css';

import SpinningGlobe from './components/globe_component/GlobeComponent';
import SearchForm from './components/search_compnent/SearchComponent';
import Signup from "./components/signup/signupComponent.jsx";
import Login from "./components/login_component/loginComponent.jsx";

const App = () => {
  return (
    <div className="app">
      <SpinningGlobe/>
      <div className="content">

        <SearchForm/>

        <Signup/>

        <Login/>

      </div>
    </div>
  );
};

export default App;
