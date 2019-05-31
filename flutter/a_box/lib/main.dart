import 'package:flutter/material.dart';

void main() {
  runApp(
      MyApp()
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Another Widget'),
          backgroundColor: Colors.green[800],
        ),
        body: SafeArea(
          child: Container(
            child: Text('Hello 1'),
            color: Colors.white,
            alignment: Alignment.center,
            margin: EdgeInsets.all(20),
            padding: EdgeInsets.all(10),
            height: 200,
          ),
        ),
        backgroundColor: Colors.teal[200],
      ),
    );
  }
}