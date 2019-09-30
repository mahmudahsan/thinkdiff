/**
 * Fundamental code to understand how Redux works.
 */

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