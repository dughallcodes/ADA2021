import React, { Component } from "react";
import { withRouter } from "react-router";

class SignUp extends Component {
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
            first_name: fields.firstName,
            last_name: fields.lastName,
            email: fields.email,
            username: fields.username,
            password: fields.password,
            phone_number: fields.phoneNumber,
        }

        fetch("http://localhost:8001/register/user/", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(success => {
                console.log(success);
                this.props.history.push('/sign-in');
            })
            .catch(error => console.log(error));
    }
    handleValidation(){
        let fields = this.state.fields;
        let errors = {};
        let formIsValid = true;
        if(!fields['firstName'] ){
            formIsValid = false;
            errors["firstName"] = "Cannot be empty";
        }
        if(!fields['lastName'] ){
            formIsValid = false;
            errors["lastName"] = "Cannot be empty";
        }
        if(!fields['email'] ){
            formIsValid = false;
            errors["email"] = "Cannot be empty";
        }
        if(!fields['username'] ){
            formIsValid = false;
            errors["username"] = "Cannot be empty";
        }
        if(!fields['phoneNumber'] ){
            formIsValid = false;
            errors["phoneNumber"] = "Cannot be empty";
        }
        if(!fields['password'] ){
            formIsValid = false;
            errors["password"] = "Cannot be empty";
        }
        if(!fields['password2'] ){
            formIsValid = false;
            errors["password2"] = "Cannot be empty";
        }
        if(!(fields["password"] === fields["password2"])){
            formIsValid = false;
            errors["password2"] = "Passwords do not match";
        }
 
        this.setState({errors: errors});
        return formIsValid;
    }
    render() {
        return (
            <div className="inner">
            <form onSubmit={this.handleSubmit}>
                <h3>Sign Up</h3>
                <div className="form-group">
                    <label>First name</label>
                    <input type="text" className="form-control" placeholder="First name" name='firstName' value={this.state.fields.firstName} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["firstName"]}</span>
                </div>
                <div className="form-group">
                    <label>Last name</label>
                    <input type="text" className="form-control" placeholder="Last name" name='lastName' value={this.state.fields.lastName} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["lastName"]}</span>
                </div>
                <div className="form-group">
                    <label>Email address</label>
                    <input type="email" className="form-control" placeholder="Enter email" name='email' value={this.state.fields.email} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["email"]}</span>
                </div>
                <div className="form-group">
                    <label>Username</label>
                    <input type="text" className="form-control" placeholder="Enter username" name='username' value={this.state.fields.username} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["username"]}</span>
                </div>
                <div className="form-group">
                    <label>Phone Number</label>
                    <input type="text" className="form-control" placeholder="Enter phone number" name='phoneNumber' value={this.state.fields.phoneNumber} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["phoneNumber"]}</span>
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" name='password' value={this.state.fields.password} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["password"]}</span>
                </div>
                <div className="form-group">
                    <label>Retype Password</label>
                    <input type="password" className="form-control" placeholder="Enter password again" name='password2' value={this.state.fields.password2} onChange={this.handleChange} />
                    <span style={{color: "red"}}>{this.state.errors["password2"]}</span>
                </div>
                <button type="submit" className="button btn btn-dark btn-lg btn-block">Register</button>
                <p className="forgot-password text-right">
                    Already registered <a href="/sign-in">sign in?</a>
                </p>
            </form>
            </div>
        );
    }
}

export default withRouter(SignUp);