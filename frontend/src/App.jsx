import React from 'react';
import './App.css';

import SpinningGlobe from './components/globe_component/GlobeComponent';
import SearchForm from './components/search_compnent/SearchComponent';

const App = () => {
  return (
    <div className="app">
      <SpinningGlobe />
      <div className="content">
        
        <SearchForm />
      </div>
    </div>
  );
};

export default App;
