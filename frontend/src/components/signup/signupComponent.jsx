import { useState } from "react";
import bcrypt from 'bcryptjs'
import Validator from "./Validator.js";

const Signup = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
      e.preventDefault();

      const saltRounds = 10;
      const hashedPassword = await bcrypt.hash(password, saltRounds);

      console.log("Valid email: " + Validator.validateEmail(email))
      console.log(firstName, lastName, email, hashedPassword);



      const requestOptions = {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({firstName, lastName, email, hashedPassword}),
      };

      try {
          const response = await fetch(`http://localhost:5002/signup`, requestOptions);
          const data = await response.json();
          console.log('Received data from server:', data);

      } catch (error) {
          console.error('Error fetching data:', error);
      }
  };

  return (
    <div>
      <h1>Signup</h1>
        <form onSubmit={handleSubmit}>
            <label htmlFor="firstName">First name:</label>
            <input
                type="text"
                id="firstName"
                value={firstName}
                required={true}
                onChange={(e) => setFirstName(e.target.value)}
            />

            <label htmlFor="lastName">Last name:</label>
            <input
                type="text"
                id="lastName"
                value={lastName}
                required={true}
                onChange={(e) => setLastName(e.target.value)}
            />

            <label htmlFor="email">Email:</label>
            <input
                type="email"
                id="email"
                value={email}
                required
                data-rules={['isEmail', 'required']}
                onChange={(e) => setEmail(e.target.value)}
            />

            <label htmlFor="password">Password:</label>
            <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit">Signup</button>
        </form>
    </div>
  );
};

export default Signup;