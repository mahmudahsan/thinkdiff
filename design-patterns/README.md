### Design Patterns

- [Redux Concept from Scratch](#redux-concept-from-scratch)

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
