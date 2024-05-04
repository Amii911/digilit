import React from "react";
import Home from "./Home/Home";
import Signup from "./Home/Signup";
import Login from "./Home/Login";



function App() {
  return (
      <div className="App"> 
          <h1>Digilit.ai</h1>
          <Home />
          <Signup/>
          <Login/>
      </div>
  );
}

export default App;
