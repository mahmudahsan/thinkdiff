### Design Patterns

- [Redux Concept from Scratch](#redux-concept-from-scratch)
- [Redux Concept with Observer pattern](#redux-concept-with-observer-pattern)
- [React demo based on previous store](#react-demo-based-on-previous-store)

### Redux Concept from Scratch

Fundamental code to understand how Redux works. Here we are defining a reducer, a store and some action. In the store, we use clojure concept to store state value. 

```javascript
function reducer(state, action) {
  if (action.type === 'INCREMENT') {
    return state + action.payload;
  }
  else if (action.type === 'DECREMENT') {
    return state - action.payload;
  }
}

function createStore(reducer) {
  let state = 0;

  const getState = () => state;

  const dispatch = (action) => {
    state = reducer(state, action);
  }

  return {
    getState,
    dispatch,
  };
}

const store = createStore(reducer);

const incrementAction = {
  type: 'INCREMENT',
  payload: 1,
};

const decrementAction = {
  type: 'DECREMENT',
  payload: 1,
};

const commands = ['i', 'd', 'i', 'i', 'd', 'i', 'd'];

commands.forEach(cmd => {
  store.dispatch(cmd === 'i' ? incrementAction : decrementAction);
  console.log(store.getState());
});
```

Output
```
1
0
1
2
1
2
1
```

### Redux Concept with Observer pattern
```javascript
function createStore(reducer, intialState) {
  let state = initialState;
  const listeners = [];

  const getState = () => (state);

  const dispatch = (action) => {
    state = reducer(state, action);
    listeners.forEach(listener => listener());
  };

  // Observer Pattern
  const subscribe = (listener) => {
    listeners.push(listener);
  };

  return {
    subscribe,
    getState,
    dispatch,
  };
}

function reducer(state, action) {
  if (action.type === 'ADD_MESSAGE') {
    return {
      messages: state.messages.concat(action.message),
    };
  } else if (action.type === 'DELETE_MESSAGE') {
    return {
      messages: [
        ...state.messages.slice(0, action.index),
        ...state.messages.slice(action.index+1, state.messages.length),
      ]
    }
  }
  else {
    return state;
  }
}

const initialState = {
  messages: [],
};

// Store
const store = createStore(reducer, initialState);

// 
const listener = () => {
  console.log('Current State');
  console.log(store.getState());
}

store.subscribe(listener);

// Actions
const addMessageAction1 = {
  type: 'ADD_MESSAGE',
  message: 'Life is Cool',
};

const addMessageAction2 = {
  type: 'ADD_MESSAGE',
  message: 'You are doing too much',
};

const deleteMessageAction = {
  type: 'DELETE_MESSAGE',
  index: 0,
};

// Dispatching Actions
store.dispatch(addMessageAction1);
store.dispatch(addMessageAction2);
store.dispatch(deleteMessageAction);
```

Output
```
Current State
{ messages: [ 'Life is Cool' ] }
Current State
{ messages: [ 'Life is Cool', 'You are doing too much' ] }
Current State
{ messages: [ 'You are doing too much' ] }
```

### React demo based on previous store

> use create-react-app APP_NAME and use [Redux Concept with Observer pattern](#redux-concept-with-observer-pattern) code and the following code to see the demo

```javascript
// Store
const store = createStore(reducer, initialState);


class App extends React.Component {
  componentDidMount() {
    store.subscribe(() => this.forceUpdate());
  }
  render() {
    const messages = store.getState().messages;

    return (
      <div className='ui segment'>
        <MessageView messages={messages} />
        <MessageInput />
      </div>
    );
  }
}

class MessageInput extends React.Component {
  state = {
    value: '',
  };

  onChange = (e) => {
    this.setState({
      value: e.target.value,
    })
  };

  handleSubmit = () => {
    store.dispatch({
      type: 'ADD_MESSAGE',
      message: this.state.value,
    });
    this.setState({
      value: '',
    });
  };

  render() {
    return (
      <div className='ui input'>
        <input
          onChange={this.onChange}
          value={this.state.value}
          type='text'
        />
        <button
          onClick={this.handleSubmit}
          className='ui primary button'
          type='submit'
        >
          Submit
        </button>
       </div>
    );
  }
}

class MessageView extends React.Component {
  handleClick = (index) => {
    store.dispatch({
      type: 'DELETE_MESSAGE',
      index: index,
    });
  };

  render() {
    const messages = this.props.messages.map((message, index) => (
      <div
        className='ui comment'
        key={index}
        onClick={() => this.handleClick(index)}
      >
        {message}
      </div>
    ));

    return messages;
  }
}

export default App;
```
