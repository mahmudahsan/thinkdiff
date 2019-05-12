import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default class App extends React.Component {
  render(){
    return (
      <View>
        <Text style={styles.stText} >
          Hello World
        </Text>
        <Text style={[styles.stText, styles.stTextName ]}>
          My name is Mahmud
        </Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  stText: {
    marginTop: 50, 
    marginLeft: 50
  },

  stTextName: {
    fontSize: 30
  }
});

