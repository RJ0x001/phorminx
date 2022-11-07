import React from "react";
import {useState} from 'react';
import ReactCountryFlag from "react-country-flag"

import { MDBCol, MDBContainer, MDBRow, MDBCard, MDBCardText, MDBCardBody, MDBCardImage, MDBBtn, MDBTypography, MDBNavbarBrand } from 'mdb-react-ui-kit';


class UserInfo extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
      username: null,
      userpic: null,
      contry: null,
    };
  };

  render() {
    const { isLoading, username, userpic, country } = this.state;
    const userInfoStyle = {
      width: "60px",
      marginTop: "10px",
    };
    return (
        <MDBRow>
          <MDBCol>
                <MDBCardImage
                  style={ userInfoStyle}
                  className="img-fluid rounded-circle"
                  src={ userpic }
                  alt=''
                  fluid />
          </MDBCol>
          <MDBCol style={{marginTop: "20px", color: "black"}}>
                  { username } <ReactCountryFlag countryCode={country} />
          </MDBCol>

        </MDBRow>
  );
  };

  getUserInfo = async () => {

    const res = await fetch('http://localhost:5000/user_info/');

    if (!res.ok) {
      const message = `An error has occured: ${res.status}`;
      throw new Error(message);
    }

    const userInfoJSON = await res.json();

    this.setState({
        ...this.state, ...{
            isLoading: false,
            username: userInfoJSON.username,
            userpic: userInfoJSON.userpic,
            country: userInfoJSON.country
        }
     });
   };

  async componentDidMount() {
    this.getUserInfo();
   };

}

export default UserInfo;
