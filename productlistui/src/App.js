// Filename - src/App.js

import React from 'react';
import axios from 'axios';

class App extends React.Component {

    state = {
        products : [],
    }

    componentDidMount() {

        let data ;

        const config = {
          headers: {
            "Access-Control-Allow-Origin": "http://localhost:8000",
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
          }
        };

        axios.get('http://localhost:8000/api/products/',config)
        .then(res => {
            data = res.data;
            this.setState({
                products : data    
            });
        })
        .catch(err => {})
    }

  render() {
    return(
      <div>
            {this.state.products.map((product, id) =>  (
            <div key={id}>
            <div >
                  <div >
                        <h1>{product.apartmentName} </h1>
                        <footer >--- by
                        <cite title="city">
                        {product.city}</cite>
                        </footer>
                  </div>
            </div>
            </div>
            )
        )}
      </div>
      );
  }
}

export default App;