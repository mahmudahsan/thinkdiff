# Flutter

- [Background](#background)
- [Widget](#widget)
- [Layout in Flutter](https://flutter.dev/docs/development/ui/layout)
- [Animated Container](#animated-container)
- [Animated Opacity](#animated-opacity)
- [Navigation Drawer](#navigation-drawer)
- [States](#states)
- [States by Provider](#provider)

####  Background

Flutter is a cross-platform mobile app development framework by Google. It used Dart programming language. Flutter compiles to actual native code for (ARM) and is rendered using a library named skia.

- Flutter also supports hot reloading for faster development
- A flutter app is represented by a `widget tree` similar to the `DOM` on the browser.

-  Flutter app uses an `event loop`. Which is a background infinite loop periodically wake up and checks the `event queue` to see if there is any task assigned. If the **CPU is idle**, the event loop puts the task onto the `run stack`. 


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
  _MyHomePageState createState() => _MyHomePageState();   
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

### Animated Container

`ÀnimatedContainer` widget when change the properties it shows animation. It's similar like the `Container` widget. It's called implicit animation. [Code](https://github.com/mahmudahsan/thinkdiff/blob/master/flutter/small_demo/animation_container/lib/main.dart)

### Animated Opacity
If we need a widget to fade in and fade out, we can use `AnimatedOpacity` widget. Using `opacity` and `duration` properties we can change the opacity with animation.

```dart
       AnimatedOpacity(
          opacity: _isVisible ? 1 : 0,
          duration: Duration(milliseconds: 500),
          child: Container(
            height: 100,
            width: 100,
            color: Colors.green,
          ),
        ),
      ),

```
[Sample App](https://github.com/mahmudahsan/thinkdiff/blob/master/flutter/small_demo/fade_widget/lib/main.dart)

### Navigation Drawer

To show a navigation drawer within material app, `Scaffold` has a `drawer` property where we can initiate `Drawer()` widget. [Code](https://github.com/mahmudahsan/thinkdiff/blob/master/flutter/small_demo/drawer/lib/main.dart)

### States

There are two types of state:
1. Ephemeral (Widget Specific)
2. App (Global)

**How to do State Management**
1. Simple State (Stateful Widget)
2. InheritedWidget (low level)
3. Provider (Syntactic sugar of InheritedWidget, Recommended)
4. Scoped Model (No longer recommended)
5. Redux
6. BloC (Business Logic Component)

### Provider

It is a [3rd party library](https://pub.dev/packages/provider).

[My Sample Project of Provider](https://github.com/mahmudahsan/thinkdiff/tree/master/flutter/small_demo/states_provider)

There are 3 important class to use this library:
1. `ChangeNotifier` builtin class
2. `ChangeNotifierProvider`
3. `Consumer`

* `ChangeNotifier` is a simple class which provides notification to it's listeners. It's kind of `Observable` pattern. We can extends or use ChangeNotifier as a mixin to create our state model. We only need the `notifyListeners()` to notify the listeners.

```dart
import 'package:flutter/material.dart';

class UI with ChangeNotifier {
  double _fontSize = 0.5;

  set fontSize(newValue) {
    _fontSize = newValue;
    notifyListeners();
  }

  double get fontSize => _fontSize * 30;

  double get sliderFontSize => _fontSize;
}
```

* `ChangeNotifierProvider` is a widget that sends an instance of `ChangeNotifier` to it's descendent. I found it's better to put this widget at the top level of the widget tree.

```dart
import 'package:flutter/material.dart';
import 'package:states_provider/home.dart';
import 'package:states_provider/about.dart';
import 'package:states_provider/settings.dart';
import 'package:provider/provider.dart';
import 'package:states_provider/model/ui.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          builder: (_) => UI(),
        ),
      ],
      child: MaterialApp(
        initialRoute: '/',
        routes: {
          '/': (context) => Home(),
          '/about': (context) => About(),
          '/settings': (context) => Settings(),
        },
      ),
    );
  }
}
```

* `Consumer` widget it the widget where we need to consume the change. It's best practice to put `Consumer` as deep in the widget tree as possible.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_lorem/flutter_lorem.dart';
import 'package:states_provider/drawer_menu.dart';
import 'package:provider/provider.dart';
import 'package:states_provider/model/ui.dart';

class About extends StatelessWidget {
  String text = lorem(paragraphs: 3, words: 50);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('About'),
        backgroundColor: Colors.teal,
      ),
      drawer: DrawerMenu(),
      body: Container(
        margin: EdgeInsets.all(10.0),
        child: Consumer<UI>(
          builder: (context, ui, child) {
            return RichText(
              text: TextSpan(
                text: text,
                style:
                    TextStyle(fontSize: ui.fontSize, color: Colors.lightBlue),
              ),
            );
          },
        ),
      ),
    );
  }
}

```

If we do not need to update the widget based on the data  in the model but only need to access it. Then we can use `Provider.of()<T>(context, listen:false)` with listen parameter as `false` 

```dart
Provider.of<CartModel>(context, listen: false).methodName;
```