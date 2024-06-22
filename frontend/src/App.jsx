import { useState } from 'react'
import './App.css'
import ApiComponent from './components/ApiComponent'; 


const App = () => {
  return (
    <div>
      <h1>MSentimentPress</h1>
      <ApiComponent />
      {/* Insert other components here */}
    </div>
  );
};

export default App;
