/**
 * Created by Mahmud Ahsan
 * https://github.com/mahmudahsan
 */
import "package:flutter/material.dart";
import 'package:flutter_warm_up/drawer_menu.dart';

class SimpleCounter extends StatefulWidget {
  @override
  _SimpleCounterState createState() => _SimpleCounterState();
}

class _SimpleCounterState extends State<SimpleCounter> {
  int counter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Simple Counter'),
        backgroundColor: Colors.teal,
      ),
      body: Container(
        margin: EdgeInsets.all(10.0),
        child: Center(
          child: Text(
            'Counter: $counter',
            style: TextStyle(fontSize: 20),
          ),
        ),
      ),
      drawer: DrawerMenu(),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.teal,
        child: Icon(Icons.add),
        onPressed: () {
          setState(() {
            counter++;
          });
        },
      ),
    );
  }
}
