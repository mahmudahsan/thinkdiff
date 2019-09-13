### Design Patterns

- [Redux Concept from Scratch](#redux-concept-from-scratch)
- [Redux Concept with Observer pattern](#redux-concept-with-observer-pattern)

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
