import 'package:flutter/material.dart';
import 'package:flutter_warm_up/simple_counter.dart';

void main() => runApp(WarmUpApp());

class WarmUpApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Warm Up",
      initialRoute: '/',
      routes: {
        '/': (context) => SimpleCounter(),
      },
    );
  }
}
