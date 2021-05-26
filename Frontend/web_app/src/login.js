import React, { Component } from "react";
import { withRouter } from "react-router";
import jwt_decode from "jwt-decode";
 class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fields:{},
            errors:{}
        };
      
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event) {   
        const name = event.target.name;
        let newFields = this.state.fields;
        newFields[name] = event.target.value;
        this.setState({
            fields : newFields
        });
    }
    handleSubmit(event) {
        event.preventDefault();
        if(this.handleValidation() === false){
            alert("Check fields");
            return;
        }
        let fields = this.state.fields;
           const data = {
                username: fields.username,
                password: fields.password,
            }
    
            fetch("http://localhost:8001/login/user/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(jsonResponse => {
                    console.log(jsonResponse);
                    if(jsonResponse.token){
                        var decoded = jwt_decode(jsonResponse.token);
                        localStorage.setItem("userID",decoded.user_id);
                        localStorage.setItem('token', jsonResponse.token);
                        localStorage.setItem('username',jsonResponse.username);
                        this.props.history.push('/home');
                        this.props.login();
                    }
                    else{
                        let errors = {};
                        errors["login"] = "Wrong username or password";
                        this.setState({errors: errors});
                    }
                    
                })
                .catch(error => console.log(error));
        }

    handleValidation(){
        let fields = this.state.fields;
        let errors = {};
        let formIsValid = true;
        if(!fields['username'] ){
            formIsValid = false;
            errors["username"] = "Cannot be empty";
        }
        if(!fields['password'] ){
            formIsValid = false;
            errors["password"] = "Cannot be empty";
        }
        this.setState({errors: errors});
        return formIsValid;
    }
    render() {
        return (
            <div className="inner">
            <form onSubmit={this.handleSubmit}>
                <h3>Log In</h3>

                <div className="form-group">
                    <label>Username</label>
                    <input type="text" className="form-control" placeholder="Enter username" name='username' value={this.state.fields.username} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["username"]}</span>
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" name='password' value={this.state.fields.password} onChange={this.handleChange}/>
                    <span style={{color: "red"}}>{this.state.errors["password"]}</span>
                </div>

                <button type="submit" className="button btn btn-dark btn-lg btn-block">Sign In</button>
            
            </form>
                <span style={{color: "red"}}>{this.state.errors["login"]}</span>
            </div>
        );
    }
}

export default withRouter(Login)