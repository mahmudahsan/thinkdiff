import 'package:flutter/material.dart';

void main() => runApp(WarmUpApp());

class WarmUpApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Warm Up",
      home: SampleApp(),
    );
  }
}

class SampleApp extends StatefulWidget {
  @override
  _SampleAppState createState() => _SampleAppState();
}

class _SampleAppState extends State<SampleApp> {
  int counter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Warm Up'),
      ),
      body: Container(
        margin: EdgeInsets.all(10.0),
        child: Center(
          child: Text('Counter: $counter'),
        ),
      ),
      floatingActionButton: FloatingActionButton(
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
