### JavaScript Language

- [JavaScript Language](#javascript-language)
- [Variables](#variables)
- [Absent of Value](#absent-of-value)
- [Operators](#operators)
- [Statements Expression Comments](#statements-expression-comments)
- [Comment](#comment)
- [String](#string)
- [List](#list)
- [Set](#set)
- [Object](#object)
- [Destructuring](#destructuring)
- [Spread Operator](#spread-operator)
- [Function](#function)
- [Class](#class)
- [Promise](#promise)
- [Async / Await](#async-await)

### Variables

> Environment: Collection of bindings and their values that exist at a given time is called the environment

##### Primitive Types
There are 7 primitive types in JavaScript.
1. null
2. undefined
3. number
4. bigint (ES10)
5. string
6. boolean
7. symbol

```js
const num = 100n;
console.log(typof num); // bigint

const num2 = BigInt(100);
console.log(typeof num2); // bigint

const id1 = Symbol('id1');
console.log(typeof id1); // symbol
```

Some fundamentals:

```javascript
var number1 = 200; // number: integer
let number2 = 300.50; // number: floating-point
const name = "Aladin"; // string
const boolean = true; // true | false
const nothing = null; // absent of object
const undef = undefined; // absent of value

// const means constant. It can not be modifed once defined

console.log(number1, typeof number1);
console.log(number2, typeof number2);
console.log(name, typeof name);
console.log(boolean, typeof boolean);
console.log(nothing, typeof nothing);
console.log(undef, typeof undef);

console.log();
// var exist in function scope
{
  var str = "Hello World";
  console.log(str);
}
console.log(str); // Okay no error

console.log();
// let and const is in block scope
{
  let localStr1 = "Life is Cool";
  const localStr2 = "Nothing is impossible";

  console.log(localStr1);
  console.log(localStr2);
}

//console.log(localStr1); // ReferenceError: localStr1 is not defined
//console.log(localStr2); // ReferenceError: localStr2 is not defined
```

### Absent of Value

```javascript
/**
 * null vs undefined
 * you can use any to describe absent of value
 */

const absent1 = null;
const absent2 = undefined;
console.log(absent1 == absent2); // true
console.log(absent1 === absent2); // value and identity check false

console.log();
/**
 * Spcial Numbers
 */
const sp1 = Infinity;
const sp2 = -Infinity;
const sp3 = NaN; // Not a number
console.log(sp1, typeof sp1);
console.log(sp2, typeof sp2);
console.log(sp3, typeof sp3);
console.log((0/0)); // output: Nan
```

### Operators

```javascript
// Unary Operator
let uVal = 10;
console.log(-uVal); 

++uVal; // --uVal => pre-increment, pre-decrement
console.log(uVal); // 11

uVal++; // uVal-- => post-increment, post-decrement
console.log(uVal); // 12

// Difference between ++uVal and uVal++
uVal = 100;
console.log(++uVal);
console.log(uVal);
console.log(uVal++);
console.log(uVal);

console.log();
// Binary Operator
let bNum1 = 20;
let bNum2 = 40;
let resultBN = bNum1 + bNum2; // bNum1 - bNum2
console.log(`${bNum1}+${bNum2}=${bNum1 + bNum2}`);

resultBN = resultBN + 10;
console.log(resultBN);
resultBN += 1; // ++resultBN or resultBN++
console.log(resultBN);

console.log();
resultBN = 100;
console.log(resultBN); 
resultBN = resultBN - 10;
console.log(resultBN); 
resultBN = resultBN * 2;
console.log(resultBN);
resultBN = resultBN / 7;
console.log(resultBN); // 25.714285714285715
console.log(Math.floor(resultBN)); // 25

console.log();
// Remainder operator
let x = 10;
let y = 3;
console.log(x % y);

// Exponential function
let aNum = 2;
console.log("Exponential: " + Math.pow(aNum, 8));
```

### Statements Expression Comments

> The smallest part of codes that javascript interpreter can execute is called `statement`

> The combination of value, variable and operators are called `expression`

### Comment

```javascript
// Single line comment

/* This is a
multiline comment */
```

### String

```javascript
const strType1 = "Life is good"; // double quotes
const strType2 = 'Let\'s do it'; // single quotes
const strType3 = `Sum of 2+2=${2+2}`; // template literal

// Template literal ${} inside value computed and converted to string

console.log(strType1);
console.log(strType2);
console.log(strType3);

/**
 * Expression
 * In computer programming expression part of code that generates value
 */
console.log(2+2); // 2+2 is expression

const name = 'Mahmud';
const country = "Bangladesh";
const profession = 'Programmer';
const career = `Computer ${profession}`; // String interpolation

console.log(name); // Mahmud
console.log(country); // Bangladesh
console.log(career); // Computer Programmer

// String concatenation
const name = 'Mahmud' + ' ' + 'Ahsan';
console.log(name);

// Accessing characters in String
const name = "Mark Zuckerberg";
console.log(name.charAt(0));

// String Comparison
const name1 = "Mark Zuckerberg";
const name2 = "Bill Gates";

if (name1 < name2) {
  console.log(`${name1} is less than ${name2}`);
}
else if (name1 > name2) {
  console.log(`${name1} is greater than ${name2}`);
}
else {
  console.log(`${name1} is equal to ${name2}`);
}


// Converting Case
const name = "Mark Zuckerberg";
console.log(name.toLowerCase());
console.log(name.toUpperCase());

// Substring
console.log(name.substring(0, 5)); // Mark 

// Matching
console.log(name.startsWith('Mark')); // true
console.log(name.search('rk')); // 2
console.log(name.slice(5)); // Zuckerberg

const num = 100; // number type
console.log(num.toString(), typeof num.toString()); // 100 string
```

### List

```javascript
const lst = [1, 2, 3]
```

**Common Methods**

| List            |         `JavaScript` |
| --------------- | -------------------: |
| get first item  |        `lst.shift()` |
| number of items |         `lst.length` |
| item existence  | `lst.includes(item)` |
| index of item   |  `lst.indexOf(item)` |

### Set

##### Set object store unique values of any type

```js
const setNumbers = new Set([1, 2, 3, 4, 1]);
console.log(setNumbers);

setNumbers.add(3);
console.log(setNumbers);
```

### Object

A regular JavaScript object.
```js
const Person = {
    name: 'Ahsan',
    count: 'Bangladesh',
};

console.log(Person);
```

##### Shorthand property name in object
When object property name and initializing variable name are same we can use shorthand syntax

```js
// ES5
var person = {
  name: name
};
console.log(person.name);

// ES6
const personSame = {
  name,
};
console.log(personSame.name);
```

##### Concise Method name in object

```js
// ES5
var person = {
  name: 'Mahmud',
  getName: function(){
    return this.name;
  }
};

console.log(person.getName());

// ES6
const personAgain = {
  name: 'Mahmud Ahsan',
  getName(){
    return this.name;
  }
};

console.log(personAgain.getName());
```

##### Computed property name

```js
const key = 'key' + 1;
const obj = {
  [key]: 'data',
};

console.log(obj[key]);
```

### Destructuring

##### Destructuring is an easier way to access properties in objects and arrays

Object destructuring
```js
const person = {
  name: "Mahmud",
  country: "Bangladesh",
};

// individual variable
// const { name } = person;
// console.log(name);

// be careful to use actual property name
// here if i use nameAgain it will not work
// const { nameAgain, country } = person;
// console.log(nameAgain, " " + country);

// Correct Solution
const { name, country } = person;
console.log(name, " " + country);

// in function call common destructuring scenario
const personName = ( {name} ) => {
  console.log(name.toUpperCase());
};

personName(person);
```

#####  Destructuring array. In this case use [] square brackets instead of {}

```js
const arrNumbers = [1, 2, 3, 4, 5];

const [ one, two, three ] = arrNumbers;
console.log(one, two, three);
```

### Spread Operator

##### Spread operator (...Name) allows an iterable to spread or expand individually inside a receiver. Iterables can be  strings, arrays, sets, etc.

```js
// arr1 and arr2 are same this is not the right way
const arr1 = [1, 2, 3, 4];
const arr2 = arr1;
console.log(arr1 === arr2);

arr2.push(5);
console.log(arr1);

// ...array return each element of an array
// here arr3 is completely new array and has no relation with arr1
const arr3 = [...arr1, 6];
console.log(arr3);
console.log(arr1 === arr3);
```

##### Spread operator for object is proposal feature but it works with babel transpiler

```js
const obj1 = {
  name: 'rice',
  price: 20
};

const type = 'groceries';

const obj2 = {...obj1, type}
console.log(obj2);
```

### Function

##### A regular function
```javascript
function sum(items) {
    return items.reduce((total, item) => total + item );
}

console.log(sum([1, 2, 3]));
```

##### Function binding with a variable name
```javascript
const sum = function(items) {
    return items.reduce((total, item) => total + item );
}

console.log(sum([1, 2, 3]));
```

##### Default value in function parameter
```js
const personDetails = (name, country='Bangladesh') => {
  console.log(name + " " + country);
}

personDetails("mahmud");
personDetails('mark', 'Malaysia');
```

#### Regular function vs Function binding with variable

- We can not call the function binded with a variable before defining the function.
- The following will throw an error

```js
callX(10);
const callX = function (x) {
    console.log(x);
}
```

**Correct Solution**
```js
const callX = function (x) {
    console.log(x);
}
callX(10);
```

**BUT** we can call a regular function anywhere in the context

```js
// It works perfectly fine
callX(10);
function callX (x) {
    console.log(x);
}
```

#### Arrow Function

An arrow function is shorter than a regular function expression

```javascript
// Arrow function 1
const squareArrow1 = (n) => {
  return n * n;
};
console.log("Arrow1: " + squareArrow1(7));

// Arrow function 2
// When there is one parameter, () is optional
const squareArrow2 = n => {
  return n * n;
};
console.log("Arrow2: " + squareArrow1(9));

// Arrow function 3
// When no curly braces provided after arrow, that means implicit returns
const squareArrow3 = n => n * n;
console.log("Arrow3: " + squareArrow1(11));

// Invalid 
// Must have to pass () beside parameters before arrow 
//const addArrow = a, b => a + b; // ERROR

// Valid
const addArrow = (a, b) => a + b; 

// Empty parameter
// Must have to provid ()
const helloWorld = () => {
  console.log("Hello World");
}
helloWorld();

```

### Class

##### JavaScript classes are syntactic sugar over existing prototype based inheritance.

##### constructor is a special method to initialize class object while initiating.

```js
class Address {
  constructor(city, country){
    this.city = city;
    this.country = country;
  }

  print(){
    console.log(this.city);
    console.log(this.country);
  }
}

// initiating instance of class
const myAddress = new Address('dhaka', 'bangladesh');
myAddress.print();
```

##### static method can be called with the class name

```js
class Point {
  constructor(x, y){
    this.x = x;
    this.y = y;
  }

  static distance(pointA, pointB){
    const ptX = Math.pow((pointB.x - pointA.x), 2);
    const ptY = Math.pow((pointB.y - pointA.y), 2);
    const dt  = Math.sqrt(ptX + ptY);
    return dt;
  }
}

const pt1 = new Point(5, 2);
const pt2 = new Point(10, 3);
const distanceOfPt = Point.distance(pt1, pt2);
console.log(distanceOfPt);
```

##### Subclass
```js
class Car {
  constructor(brand, type){
    this.brand = brand;
    this.type = type;
  }

  print(){
    console.log('Brand: ' + this.brand);
    console.log('Type: ' + this.type);
  }
}

// if subclass has constructor it needs to call
// super before using this
class Honda extends Car {
  constructor(brand, type, model){
    super(brand, type);
    this.model = model;
  }

  print(){
    super.print();
    console.log('Model: ' + this.model);
  }
}

const honda = new Honda('honda', 'sedan', 'accord');
honda.print();
```

### Promise

##### A promise object represents an eventual completion or failure for an asynchronous operation.

##### Promise has 3 states:
1. Pending
2. Fulfilled
3. Rejected

When a pending promise either fulfilled or rejected and if a corresponding handler is attached by 'then' method, the handler will be called. If it is rejected, the corresponding catch method if attached will be called.

```js
 const getData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve('data received');
    }, 1000);

    // reject example 
    setTimeout(()=>{
      reject('network disconnected');
    }, 500);
  });
 };

 const dataFromServer = getData();
 
 dataFromServer.then(
    (value)=>{
      console.log(value);
    }, 
    (error)=>{ // implicit catch within then
      console.log(error);
    }
 ); 

  /*
  // explicit catch to detect rejection
   dataFromServer.then(
    (value)=>{
      console.log(value);
    })
    .catch((error)=>{
      console.log(error);
    }  
 );
 */
```

### Async Await

##### `async/await` functions are built onto promise. A function starts with async keyword means, it will must return a `promise` either implicitly or explicitly.

##### The keyword `await` makes JavaScript wait until the `promise` settled and return the result

***Example 1:***

```js
 const sum = async (a, b) => {
   return a + b;
 };
 console.log(sum); // [AsyncFunction: sum]
 console.log(sum(1, 2)); // Promise { 3 }
 const result = sum(100, 200);
 result.then(value => {
  console.log(value);
 });
 ```

 ***Example 2:***

```js
const pow = async (num, pow) => {
  return new Promise((resolve, reject)=>{
    const r = Math.pow(num, pow);
    resolve(r);
  });
 };

 pow(2, 2).then(val => {console.log(val)});
```

 ***Example 3:***

```js
 const getData = async () => {
    const data = new Promise((resolve, reject) => {
      setTimeout(()=>{
        resolve("data received");
      }, 2000);
    });

    console.log('test 1');
    let result = await data;
    console.log('test 2');
    return result;
 };

 getData().then(result => {
   console.log(result);
 });
```

 ***Example 4:***
 
> `async / await` with synchronous fashion without using `then` of `promise` object

```javascript
function task1() {
  console.log('Task 1');
}

function task2() {
  console.log('Task 2');
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve('Task 2'), 2000);
  });
}

function task3(data) {
  console.log(`Task 3 with ${data}`);
}

async function main() {
  task1();
  const data = await task2();
  task3(data);
}

main();
```

We can also redefine the `main()` function like this. In this case we use `then` method of `promise` object for the asynchronous operation.

```javascript
function main() {
  task1();
  task2().then(data => task3(data));
}
```