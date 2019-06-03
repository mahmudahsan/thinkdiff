# Flutter

- [Background](#background)
- [Widget](#widget)

####  Background

Flutter is a cross-platform mobile app development framework by Google. It used Dart programming language. Flutter compiles to actual native code for (ARM) and is rendered using a library named skia.

Flutter also supports hot reloading for faster development.

### Widget

Flutter is a reactive library like ReactJS on Web. In flutter, ***everything is a widget*** and every widget is a dart class. Using widget we create view.

- Every widget must have a `build` method which must returns a `widget`


#### Widgets are 2 types:

1. Stateless
2. Statefull

#### Some common widgets are:

- Layout - `Row, Column, Scaffold, Stack`
- Structures - `Button, Toast, MenuDrawer`
- Styles - `TextStyle, Color`
- Animations - `FadeInPhoto, transformations`
- Position, Alignment - `Center, Padding`

##### Flutter favors composition over class inheritance

So this is wrong
```dart
class AddToCartButton extends Button {}
```

Correct Flutter widget composition

```dart
class AddToCartButton extends Widget {
  @override
  build() {
    return Center(
      child: Button(
        child: Text('Add to Cart'),
      )
    );
  }
}
```



