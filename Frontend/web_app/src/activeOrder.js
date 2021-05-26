import React, { Component } from "react";


export default class ActiveOrder extends Component {
    state ={
        pick_up_location:{lat:'',lng:''},
        delivery_location:{lat:'', lng:''},
        timestamp:'',
        status:'',
        order_txt:'',
        pick_up_description:'',
        courier_fetched:false,
        courier_email:'',
        courier_phone:'',
        courier_first:'',
        courier_last:'',
    }
    componentDidMount() {
        this.fetchOrder();
        this.timer = setInterval(()=> this.fetchOrder(), 3000);
      }
      
      componentWillUnmount() {
        clearInterval(this.timer);
      }
    

    fetchCourier(courier_id){
      fetch("http://localhost:8001/register/courier/" + courier_id, {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => response.json())
        .then(jsonResponse => {
          console.log(jsonResponse);
          this.setState({courier_email:jsonResponse.email, courier_phone:jsonResponse.phone_number, courier_first:jsonResponse.first_name, courier_last:jsonResponse.last_name});
        })
        .catch(error => console.log(error));
  }
    
    fetchOrder(){
        fetch("http://localhost:8000/order/" + localStorage.getItem("orderID"), {
            method: "GET",
            headers: {
              'Content-Type': 'application/json',
              "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
          })
            .then(response => response.json())
            .then(jsonResponse => {
              console.log(jsonResponse);
              if(!jsonResponse.status){
                console.log("nok");
              }
              else if(jsonResponse.status === "completed"){
                  localStorage.removeItem("orderId");
                  this.setState({});
              }
              else{
                this.setState({
                    pick_up_location:{lat:jsonResponse.pick_up_location.lat, lng: jsonResponse.pick_up_location.lng},
                    delivery_location:{lat:jsonResponse.delivery_location.lat, lng:jsonResponse.delivery_location.lng},
                    timestamp:jsonResponse.timestamp,
                    status: jsonResponse.status,
                    order_txt: jsonResponse.order_txt,
                    pick_up_description: jsonResponse.pick_up_description,
                })

                if(this.state.courier_fetched == false && jsonResponse.courier_id != ''){
                    this.setState({courier_fetched:true});
                    this.fetchCourier(jsonResponse.courier_id);
                }
              }
            })
            .catch(error => console.log(error));
    }
    render() {
        if(localStorage.getItem("orderID")){
        return (
            <div>
                <h1 className="order">Active order</h1>
                <h3>Status : {this.state.status}</h3>
                <h3>Pick up location : {this.state.pick_up_location.lat}, {this.state.pick_up_location.lng}</h3>
                <h3>Delivery location : {this.state.delivery_location.lat}, {this.state.delivery_location.lng}</h3>
                <h3>Order date : {this.state.timestamp}</h3>
                <h3>Order info : {this.state.order_txt}</h3>
                <h3>Order description : {this.state.pick_up_description}</h3>
                <div className="order">
                <h5>Picked up by:</h5>
                  <p>Courier name: {this.state.courier_first} {this.state.courier_last}</p>
                  <p>Phone number: {this.state.courier_phone}</p>
                  <p>Email: {this.state.courier_email}</p>
                </div>
            </div>
        )
        }
        else{
            return(
                <h1>No active orders</h1>
            )
        }
    
    };
}