import React, { useEffect, useState } from 'react';
import './CurrentlyLoggedInAs.css';

const LoggedInAs = () => {
  const [user, setUser] = useState({ firstName: '', lastName: '' });
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check for a token in local storage to determine if the user is logged in
    const token = localStorage.getItem('token'); // Or any other key you use for tracking login status
    if (token) {
      const firstName = localStorage.getItem('firstname') || 'First';
      const lastName = localStorage.getItem('lastname') || 'Last';
      setUser({ firstName, lastName });
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  if (!isLoggedIn) {
    return null; // Do not render anything if not logged in
  }

  return (
    <div className="loggedInAsWidget">
      Logged in as: {user.firstName} {user.lastName}
    </div>
  );
};

export default LoggedInAs;
