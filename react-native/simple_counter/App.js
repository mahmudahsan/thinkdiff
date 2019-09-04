import React from 'react';
import { 
  StyleSheet, 
  Text, 
  View, 
  Navigator,
  TouchableHighlight,
  TouchableOpacity
} from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

const appName = 'Simple Counter';

class HomeScreen extends React.Component {
  state = {
    counter: 0,
  }

  render() {
    const counter = this.state.counter;

    return (
      <View style={styles.container}>
        <Text style={styles.counter}>Counter: {counter}</Text>
        <TouchableOpacity 
          style={styles.floatingButton}
          onPress={this.onIncrement}
        >
          <Icon name="plus" size={20} color="#900" />
        </TouchableOpacity>
      </View>
    );
  }

  onIncrement = () => {
    this.setState({
      counter: this.state.counter + 1,
    })
  };
}

const AppNavigator = createStackNavigator({
  Home: {
    screen: HomeScreen,
    navigationOptions: () => ({
      title: appName,
    }),
  },
});

const AppContainer = createAppContainer(AppNavigator);

export default function App() {
  return (
      <AppContainer />
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  floatingButton: {
    borderWidth: 1,
    borderColor: 'rgba(0,0,0,0.2)',
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    bottom: 15,
    right: 15,
    width: 60,
    height: 60,
    backgroundColor: '#fff',
    borderRadius: 100,
  },
  counter: {
    fontSize: 25,
  }
});