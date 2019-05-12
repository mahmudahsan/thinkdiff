import React, { Component } from 'react';
import axios from 'axios'

const QUOTES_API = "http://127.0.0.1:8000/api/quotes/?format=json"

class App extends Component{
  state = {
    quotes: []
  }

  componentDidMount(){
    this.getCategories()
  }

  // loading data from a remote endpoint 
  getCategories(){
    axios.get(QUOTES_API)
    .then(res => {
      this.setState({quotes: res.data})
    })
    .catch(err => {
      console.log(err)
    })
  }

  render(){
    return(
      <div>
        {this.state.quotes.map(item => (
          <div>
            <h2>{item.quote}</h2>
            <em>{item.author}</em>
          </div>
        ))}
      </div>
    )
  }
}
export default App