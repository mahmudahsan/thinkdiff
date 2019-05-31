# Dart Language

- [Setup](#setup) | [Official](https://dart.dev/get-dart)
- [Features](#features)
- [Complex Data Types](#complex-data-types)
- [Types in Function](#types-in-function)
- [Comments](#comments)
- [null object](#null-object)
- [Final and Const](#final-and-const)
- [Operators](#operators)
  - [Null Aware Operator](#null-aware-operator)
  - [Operator](#conditional-operator)
  - [Ternary Operator](#ternary-operator)
- [Loop](#loop)
- [Function](#function)

### Setup

Setup in Mac
```shell
brew tap dart-lang/dart
brew install dart
```

Upgrade in Mac
```shell
brew upgrade dart
```

#### Running Dart Code in Terminal

```dart
dart filename.dart
```

###  Features

Dart is a strictly typed programming language. It supports both AOT (Ahead of time) and JIT (Just In Time) compilation. It is a compiled programming language and can also transpile the code into JavaScript.

#### Code Samples

```dart
void main() {
  var firstName = 'Mahmud'; // String type inference
  String lastName = 'Ahsan'; // String type defined
  int number = 100; // integer type
  dynamic isOkay = true; // dynamic compiler decide

  print(firstName + ' ' + lastName);
  print(number);
  print(isOkay);
}
```

- `main()` is the entry point
- `dart` supports type inference and type defined

#### Importing package and take input from user

```dart
import 'dart:io';

void main() {
  stdout.writeln('What is your name: ?');
  String name = stdin.readLineSync();
  print('My name is: $name');
}
```

#### `Dart` Language Common Features:

- Object oriented programming language
- Everything is an object and derived from `object` class
- Static strongly typed language. Can not assign integer value to String type etc.
- ( ; ) Semicolon is mandatory to the end of statements

****Strongly Typed Language:**** The type of a variable is known at ***compile time***. For example: `C++`, `Java`, `Swift`

****Dynamic Typed Language:**** The type of a variable is known at ***run time.*** For example: `Python`, `Ruby`, `JavaScript`.

### Complex Data Types

We can define type when declare something or we can let it to the compiler to decide the type.

Here names is `String` type by type inference. 

And ages is `int` type as we defined it.

```dart
void main() {
  List names = ['Jack', 'Jill'];
  for (var n in names) {
    print(n);
  }

  List <int> ages = [18, 20, 33];
  for (var a in ages) {
    print(a);
  }
}
```

### Types in Function

Here we first defined a `square` function that take integer and return integer value after multiplication.

`doubleSquare` function takes `double` value and returns a `double` value type.

`dynamicSquare` function is dynamic and in this case best as we can pass both `int` and `double` value. And it returns result based on calculation. So if the result is integer it returns `int` and if result is `double` it returns `double`.

```dart
void main() {
  print(square(5));
  print(doubleSquare(5.5));

  print(dynamicSquare(5));
  print(dynamicSquare(5.5));
}

int square(int n) {
  return n * n;
}

double doubleSquare(double d) {
  return d * d;
}

dynamic dynamicSquare(dynamic val) {
  return val * val;
}
```
### Comments

```dart
// In-line comment
/*
Block comment
*/

/// Documentation
```

### null object

If a variable is declared but didn't assign with any value, it contains `null` object.

```dart
void main() {
  int num;
  print(num); // output: null
}
```
### Final and Const

`final` and `const` when used before defining any variable can not reassign. But `final` variable if declared in class without value must have to assigned in the `constructor()` method 

```dart
final String person1 = 'Jack';
const String person2 = 'Jill';

print(person1);
print(person2);

// can not reassign
// person1 = 'aa';
// person2 = 'bb';
```

### Operators

Same like JavaScript language. All the standard operators will work here.

```dart
void main() {
  int num = 10 + 22;
  num = num - 2;

  print(num);

  num = num % 5;
  print(num);

  // relational ==, !=, >=, <=
  if (num == 0) {
    print('Zero');
  }

  num = 100;
  num *= 2;
  print(num);

  // unary operator
  ++num;
  num++;
  num += 1;
  num -= 1;
  print(num);

  // logical && and logical ||
  if (num > 200 && num < 203) {
    print('200 to 202');
  }

  // != Not Equal
  if (num != 100) {
    print('num is not equal to 100');
  }
}
```

### Null Aware Operator

#### `(?.), (??), (??=)`

It is like `Swift` programming language's `optional (?:)` operator. It means, if the object is null then do nothing.

```dart
class Num {
  int num = 10;
}

void main () {
  var n = Num();
  int number;
  
  // we can check null by this
  if (n != null ){
    number = n.num;
  }
  print(number);
}
```

Or, we can use `Null Aware (?.)` operator to skip the `if..else` condition.

So in this case, if n object is `null` it will not crash.

```dart
void main () {
  var n = Num();
  int number;
  
  number = n?.num; // null aware
  print(number);
}
```

#### Code will Crash 

```dart
void main () {
  var n;
  int number;
  
  number = n.num; // no null checking
  print(number);
}
```

#### Safe Code if null comes (?.)

```dart
void main () {
  var n;
  int number;
  
  number = n?.num; // null checking
  print(number); // output: null
}
```
#### null aware variation two (??)

Suppose an object has few fields, but some field may be `null`. In this case if we want to provide a `default value` we can follow `??` operator.

```dart
class Num {
  int num;
}

void main () {
  var n = Num();
  int number;
  
  number = n.num ?? 18; // default value
  print(number);
}
```

#### null aware variation three (??=)

If the corresponding object is null, then it assigned the value to that object.

```dart
void main() {
  int number;
  number ??= 100;
  print(number);
}
```

### Conditional Operator

#### if..else if..else

Same like `JavaScript` language.

```dart
int number = 100;

if (number % 2 == 0) {
  print('Even');
}
else if (number % 3 == 0) {
  print('Odd');
}
else {
  print('Confused');
}
```
#### Switch statement
Same like `JavaScript` language.

```dart
int number = 1;

switch(number) {
  case 0:
    print('Even');
    break;
  case 1:
    print('Odd');
    break;
  default:
    print('Confused');
}
```

#### Ternary Operator

Same like `JavaScript` language `?:` 

```dart
int x = 100;
var result = x % 2 == 0 ? 'Even' :'Odd';
print(result);
```

### Loop

Same like `JavaScript` language

1. **Standard for loop**
```dart
for (var i = 0; i < 10; ++i) {
  print(i);
}
```

2. **for-in loop**
```dart
var numbers = [1, 2, 3];

for (var n in numbers) {
  print(n);
}
```

3. **forEach loop**

Here inside `forEach` method we provide a function. Thus `forEach` is a higher order function.

```dart
var numbers = [1, 2, 3];
  
numbers.forEach((num) => print(num));
```

we can rewrite this `forEach` by another way:

```dart
void main() {
  var numbers = [1, 2, 3];

  numbers.forEach(printNum);
}

void printNum(num) {
  print(num);
}
```

4. **While loop**

```dart
  int num = 5;

  while (num > 0){ 
    print(num);
    num -= 1;
  }
```

5. **do-while loop**

```dart
  int num = 5;

  do {
    print(num);
    num -= 1;
  } while(num > 0);
```

6. **Break and Continue**

```dart
void main() {
  for (var i = 0; i < 10; ++i) {
    if (i > 5) break;
    print(i);
  }

  for (var i = 0; i < 10; ++i) {
    if (i % 2 == 0) continue;
    print("Odd: $i");
  }
}
```

### Function

- Each `function` is an object of class `Function`
- Each `function` if returns something should have a `return type`. Otherwise it will return `void`

Some examples:
```dart
void main() {
  showOutput(square(2));
  showOutput(square(2.5));
}

void showOutput(var msg) {
  print(msg);
}

dynamic square(var num) {
  return num * num;
}
```

#### Fat Arrow Expression => or Arrow Function

For one expression within a function we can use the shorthand syntax called **Fat Arrow** `=>`. And it implicitly returns the value after `=>`. It's somewhat similar to `JavaScript Arrow Function`.

we can redefine the above `square` function by this:
```dart
dynamic square(var num) => num * num;
```

#### Positional and Named Parameter

Positional arguments works like other language starting from left.

```dart
void main() {
  print(sum(2, 2));
}

dynamic sum(var num1, var num2) => num1 + num2;

```

For Named parameter, whe have to use `{}` outside the named parameter within a function signature.

```dart
void main() {
  print(sumName(num1: 2, num2: 2));
}

dynamic sumName({var num1, var num2}) => num1 + num2;
```

We can also mix positional and named parameter.

By default, `named parameter` is optional. So we can use null aware operator to check this optional argument.

```dart
void main() {
  print(sum(2, num2: 2));
  print(sum(2));
}

dynamic sum(var num1, {var num2}) => num1 + ( num2 ?? 0 );
```

**Positional Optional Parameter**

We have to use square bracket around positional optional parameter. That's it.

So we use the above example redefined below:
```dart
void main() {
  print(sum(2, 2));
  print(sum(2));
}

dynamic sum(var num1, [var num2]) => num1 + ( num2 ?? 0 );
```

```dart

```

```dart

```