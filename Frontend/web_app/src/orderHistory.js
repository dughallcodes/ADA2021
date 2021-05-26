import React, { Component } from "react";

export default class OrderHistory extends Component {
    state = {
        orders:[]
    };
    componentDidMount() {
        this.fetchOrders();
      }
    fetchOrders(){
        fetch("http://localhost:8000/order/get_order_by_user_id/?user_id=" + localStorage.getItem("userID"), {
            method: "GET",
            headers: {
              'Content-Type': 'application/json',
              "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
          })
            .then(response => response.json())
            .then(jsonResponse => {
              console.log(jsonResponse);
              this.setState({orders:jsonResponse});
      
            })
            .catch(error => console.log(error)); 
    }
    render() {
        return (
            <div className="order">
                <h1>History</h1>
                {this.state.orders.map((order, index) => (
                    <div className="">
                    <p className="thick">Order #{index+1}</p>
                    <p className="thick">Order status: {order.status}</p>
                    <p className="thick">Order date: {order.timestamp}</p>
                    <p className="thick">Order description: {order.pick_up_description}</p>
                    <p className="thick">Order info: {order.order_txt}</p>
                    <p className="thick">Pick-up location: {order.pick_up_location.lat}, {order.pick_up_location.lng}</p>
                    <p className="thick">Delivery location: {order.delivery_location.lat}, {order.delivery_location.lng}</p>
                    <hr></hr>
                    </div>
                    
                ))}
        </div>
        );
    }
}