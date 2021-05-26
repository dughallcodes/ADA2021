import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

import Login from "./login";
import SignUp from "./signup";
import Home from "./home"
import { Component } from 'react';
import ActiveOrder from './activeOrder';
import OrderHistory from './orderHistory';

class DefaultNavBar extends Component{
 
  logoutOnClick = () => {
    this.props.logout();
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    localStorage.removeItem("userID");
  }
  render(){
  if(this.props.token){
    return (
      <ul className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link className="nav-link" >Welcome, {localStorage.getItem("username")}</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/order-history"}>Order history</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/active-order"}>Active order</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to={"/sign-in"} onClick={this.logoutOnClick} >Logout</Link>
            </li>
    </ul>
    );
  }
  else{
    return (
      <ul className="navbar-nav ml-auto">
      <li className="nav-item">
        <Link className="nav-link" to={"/sign-in"}>Login</Link>
      </li>
      <li className="nav-item">
        <Link className="nav-link" to={"/sign-up"}>Sign up</Link>
      </li>
    </ul>
    );
  }
  }
}

class App extends Component {

  state = {token:localStorage.getItem("token")};

  login = () => {
    this.setState({ token: localStorage.getItem("token")});
  }

  logout = () => {
    this.setState({ token:'' });
  }


  render(){

  return (<Router>
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <Link className="navbar-brand" to={{pathname: !this.state.token ? "/sign-in" : "/home"}}>Deliveroo</Link>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
            <DefaultNavBar token={this.state.token} logout={this.logout}></DefaultNavBar>
          </div>
        </div>
      </nav>

      <div className="outer">
          <Switch>
            <Route exact path='/' render={(props) => !this.state.token ? <Login login={this.login} /> : <Redirect to='/home'/>} />
            <Route path="/sign-in" render={(props) => !this.state.token ?  <Login login={this.login}/> : <Redirect to='/home'/> } />
            <Route path="/sign-up" render={(props) => !this.state.token ?  <SignUp/> : <Redirect to='/home'/> } />
            <Route path="/home" render={(props) => !this.state.token ? <Login login={this.login}/> : <Home></Home> } />
            <Route path="/active-order" render={(props) => !this.state.token ? <Login login={this.login}/> : <ActiveOrder></ActiveOrder> } />
            <Route path="/order-history" render={(props) => !this.state.token ? <Login login={this.login}/> : <OrderHistory></OrderHistory> } />
          </Switch>
      </div>
    </div>
    </Router>
  );
}
}

export default App;