// import React from 'react';
import './App.css';

import SpinningGlobe from './components/globe_component/GlobeComponent';
import SearchForm from './components/search_compnent/SearchComponent';
import Signup from "./components/signup/signupComponent.jsx";

const App = () => {
  return (
    <div className="app">
      <SpinningGlobe />
      <div className="content">
        
        <SearchForm />

        <Signup />

      </div>
    </div>
  );
};

export default App;
