import { useState } from 'react'
import './App.css'
import ApiComponent from './components/ApiComponent'; 
import GlobeScene from './components/globe_component/script';

const App = () => {
  return (
    <div>
      <h1>SentimentPress</h1>
      
      <ApiComponent />
     
      {/* Insert other components here */}
    </div>
  );
};

export default App;
