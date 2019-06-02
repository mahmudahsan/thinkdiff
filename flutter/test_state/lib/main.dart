import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(RandomWidget());

class RandomWidget extends StatefulWidget {
  @override
  _RandomWidgetState createState() => _RandomWidgetState();
}

class _RandomWidgetState extends State<RandomWidget> {
  int randomNum = 1;

  void makeRandomNumber() => setState(() {
    randomNum = Random().nextInt(100) + 1;
  });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Random Number'),
        ),
        body: SafeArea(
          child: Column(
            children: <Widget>[
              Expanded(
                child: Center(
                  child: Text(
                    'Random Number: $randomNum',
                    style: TextStyle(
                      fontSize: 30.0,
                      fontWeight: FontWeight.bold,
                      color: Colors.blue[700],
                    ),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(right: 16),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: <Widget>[
                    FloatingActionButton(
                      child: Icon(Icons.autorenew),
                      backgroundColor: Colors.red[500],
                      foregroundColor: Colors.white,
                      onPressed: () => makeRandomNumber(),
                    ),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
