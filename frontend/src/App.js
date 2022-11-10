import React from "react";
// import API from "./utils/API";
import Lyrics from "./lyrics/Lyrics";
import UserInfo from './user/UserInfo'
import Navbar from './navbar/Navbar'
import Login from './components/Login'
// import xtype from 'xtypejs'
import styles from "./style.css"
// import axios from "axios";

import { Routes, Route } from "react-router-dom";

class App extends React.Component {

  render() {
    return (
      <div className ="App">
        <Routes>
          <Route path="/login" element = {<Login/>}/>
          <Route path="/jaskier" element = {
              <React.Fragment>
                <Navbar/>
                <Lyrics/>
              </React.Fragment>}/>
        </Routes>
      </div>
    );
  };
}
export default App;
