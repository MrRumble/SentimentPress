// import React from 'react';
import './App.css';

import SpinningGlobe from './components/globe_component/GlobeComponent';
import SearchForm from './components/search_compnent/SearchComponent';
import Signup from "./components/signup/signupComponent.jsx";
import Login from "./components/login_component/loginComponent.jsx";
import Logout from "./components/logout_component/logout_component.jsx";
import LoggedInAs from './components/currently_logged_in_as_component/CurrentlyLoggedInAs.jsx';

const App = () => {
  return (
    <div className="app">
      <SpinningGlobe/>
      <div className="content">

        <SearchForm/>

        <Signup/>

        <Login/>

        <Logout />
        <LoggedInAs />

      </div>
    </div>
  );
};

export default App;
