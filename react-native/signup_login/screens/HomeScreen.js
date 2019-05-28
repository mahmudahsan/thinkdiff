/**
 * @author Mahmud Ahsan <https://github.com/mahmudahsan>
 */

import React from 'react';
import {
  SafeAreaView,
  Text,
  StyleSheet,
} from 'react-native';

class HomeScreen extends React.Component {
  render() {
    return (
      <SafeAreaView style={styles.container}>
        <Text style={styles.home}>Home Screen</Text>
      </SafeAreaView>
    );
  }
}


const styles = StyleSheet.create({
  home: {
    textAlign: 'center',
    fontSize: 20,
  }
});

export default HomeScreen;