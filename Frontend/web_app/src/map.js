import React, { Component } from 'react';
import { Map, GoogleApiWrapper, InfoWindow, Marker } from 'google-maps-react';
import { withRouter } from "react-router";

const mapStyles = {
  maxWidth: "750px",
  height: "600px",
};
const containerStyle = {
  width: "60%",
}

 class MapContainer extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  state = {
      currentMarker: 0,
      showingInfoWindows: [false, false],  // Hides or shows the InfoWindow
      activeMarkers: [{}, {}],          // Shows the active marker upon click
      selectedPlaces: [{}, {}],         // Shows the InfoWindow to the selected place upon a marker
      currentCenter: {
        lat: 45.755857,
        lng: 21.227904
      },
      destinationCenter: {
        lat: 45.755857,
        lng: 21.227904
      },
      info: '',
      description: ''
  }
  onMarkerClick = (props, marker, e) => {
    if (marker.name === "Pickup location") {
      this.setState({
        selectedPlaces: [props, this.state.selectedPlaces[1]],
        activeMarkers: [marker, this.state.activeMarkers[1]],
        showingInfoWindows: [true, this.state.showingInfoWindows[1]],
      });
    }
    else {
      this.setState({
        selectedPlaces: [this.state.selectedPlaces[0], props],
        activeMarkers: [this.state.activeMarkers[0], marker],
        showingInfoWindows: [this.state.showingInfoWindows[0], true],
      });
    }
  }

  onClose = (mark, props) => {
    //   let showingInfoWindows2 = this.state.showingInfoWindows;
    //   showingInfoWindows2[mark] = false;
    //   let activeMarkers2 = this.state.activeMarkers;
    //   activeMarkers2[mark] = null;
    //   this.setState({
    //     showingInfoWindows: showingInfoWindows2,
    //     activeMarkers: activeMarkers2,
    //   });
  };
  
  handleMapClick = (ref, map, ev) => {
    if (this.state.currentMarker === 0) {
      this.setState({ currentCenter: ev.latLng, currentMarker: 1 });
    }
    else {
      this.setState({ destinationCenter: ev.latLng, currentMarker: 0 });
    }
  };
  
  handleChange(event) {
    let name = event.target.name;
    this.setState({ [name]: event.target.value });
  }
  isFunction = (functionToCheck) => {
    return functionToCheck && {}.toString.call(functionToCheck) === '[object Function]';
   }
  handleSubmit(event) {
    event.preventDefault();
    const data = {
      order_txt: this.state.info,
      pick_up_description: this.state.description,
      pick_up_location: { lat:  this.isFunction(this.state.currentCenter.lat) ? this.state.currentCenter.lat() : this.state.currentCenter.lat,
                          lng:  this.isFunction(this.state.currentCenter.lng) ? this.state.currentCenter.lng() : this.state.currentCenter.lng,
      },
      delivery_location: {lat:  this.isFunction(this.state.destinationCenter.lat) ? this.state.destinationCenter.lat() : this.state.destinationCenter.lat,
                          lng:  this.isFunction(this.state.destinationCenter.lng) ? this.state.destinationCenter.lng() : this.state.destinationCenter.lng,
      },
    }
    console.log(data);
    fetch("http://localhost:8000/order/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        "Authorization": `Bearer ${localStorage.getItem("token")}`
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(jsonResponse => {
        console.log(jsonResponse);
        if (jsonResponse.id) {
          localStorage.setItem("orderID",jsonResponse.id);
          this.props.history.push('/active-order');
          console.log("ok");
        }
        else {
          console.log("nok");
        }

      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div className="container2">
        <div className="one">
          <Map
            google={this.props.google}
            zoom={14}
            style={mapStyles}
            containerStyle={containerStyle}
            onClick={this.handleMapClick}
            initialCenter={this.state.currentCenter}
          >

            <Marker position={this.state.currentCenter}
              name={'Pickup location'}
              onClick={this.onMarkerClick}
            />

            <Marker position={this.state.destinationCenter}
              name={'Destination location'}
              onClick={this.onMarkerClick}
            />

            <InfoWindow
              marker={this.state.activeMarkers[0]}
              visible={this.state.showingInfoWindows[0]}
              onClose={this.onClose(0)}
            >
              <div>
                <h4>{this.state.selectedPlaces[0].name}</h4>
              </div>
            </InfoWindow>

            <InfoWindow
              marker={this.state.activeMarkers[1]}
              visible={this.state.showingInfoWindows[1]}
              onClose={this.onClose(1)}
            >
              <div>
                <h4>{this.state.selectedPlaces[1].name}</h4>
              </div>
            </InfoWindow>

          </Map>
        </div>
        <div className="two">
          <h1 >Order Info</h1>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label>Info</label>
              <input type="text" className="form-control" placeholder="Enter order info" name='info' value={this.state.info} onChange={this.handleChange} />
            </div>
            <div className="form-group">
              <label>Description</label>
              <input type="text" className="form-control" placeholder="Enter order description" name='description' value={this.state.description} onChange={this.handleChange} />
            </div>

            <button type="submit" className="button btn btn-dark btn-lg btn-block">Submit order</button>

          </form>
        </div>
      </div>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: 'AIzaSyDUgig4c8icm60XLqrnKaX2WIg8trDoUnU'
})(withRouter(MapContainer));