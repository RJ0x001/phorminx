import React, { useState } from 'react';

import UserInfo from '../user/UserInfo'

import {
  MDBNavbar,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBNavbarToggler,
  MDBContainer,
  MDBIcon,
  MDBBtn,
  MDBCollapse,
  MDBNavbarBrand
} from 'mdb-react-ui-kit';

export default function Navbar() {
  const [showBasic, setShowBasic] = useState(false);

  return (
    <div>
        <MDBNavbar light>
            <MDBContainer>
                <MDBNavbarBrand>
                  <UserInfo/>
                </MDBNavbarBrand>
                <MDBNavbarBrand>Jaskier</MDBNavbarBrand>
                <MDBNavbarBrand>Phorminx</MDBNavbarBrand>
            </MDBContainer>
        </MDBNavbar>
    </div>
  );
}
