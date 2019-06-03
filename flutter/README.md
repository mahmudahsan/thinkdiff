# Flutter

- [Background](#background)
- [Widget](#widget)

####  Background

Flutter is a cross-platform mobile app development framework by Google. It used Dart programming language. Flutter compiles to actual native code for (ARM) and is rendered using a library named skia.

- Flutter also supports hot reloading for faster development
- A flutter app is represented by a `widget tree` similar to the `DOM` on the browser.

### Widget

Flutter is a reactive library like ReactJS on Web. In flutter, ***everything is a widget*** and every widget is a dart class. Using widget we create view.

#### Widgets are 2 types:

1. Stateless - it's immutable
2. Statefull - tracks it's own internal state

#### Some common widgets are:

- Layout - `Container, Row, Column, Scaffold, Stack`
- Structures - `Button, Toast, MenuDrawer`
- Styles - `TextStyle, Color`
- Animations - `FadeInPhoto, transformations`
- Position, Alignment - `Center, Padding`

##### Flutter favors composition over class inheritance

- Every widget must have a `build` method which must returns `widget`
- `BuildContext` contains the reference of the widget location in the widget tree

##### Stateless widget example

```dart
class MyApp extends StatelessWidget {                      
  @override  
  Widget build(BuildContext context) {                     
    return MaterialApp(                                    
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),   
    );
  }
}
```

- Every `StatefulWidget` must have a `createState`method which returns a `State`object
- Every `StatefulWidget` has an associated `State` object, which have a `build`method
- Using `setState(() { })` method state object uses to manage internal state

##### Stateful widget example

```dart
class MyHomePage extends StatefulWidget {
@override
  _MyHomePageState createState() => new _MyHomePageState();   
}

class _MyHomePageState extends State<MyHomePage> { 
  int _counter = 0;
  
  @override
  Widget build(BuildContext context) { 
    return Container();
  }
  
  void increment() {
     setState(() {
      _counter += 1;
     });
  }
}
```

