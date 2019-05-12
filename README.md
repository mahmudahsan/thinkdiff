<p align="center">
    <img src="cover.png" alt="Computer Programming" />
</p>
<p align="center">
    <a href="http://thinkdiff.net/">
        <img src="https://img.shields.io/badge/blog-thinkdiff.net-brightgreen.svg" alt="thinkdiff.net" />
    </a>
    <a href="https://www.youtube.com/channel/UCtHlgyUw0wLE5Ous9swfFlg">
        <img src="https://img.shields.io/badge/my-youtube channel-red.svg" alt="Youtube" />
    </a>
    <a href="https://pythonbangla.com">
        <img src="https://img.shields.io/badge/python-bangla.com-orange.svg" alt="pythonbangla.com" />
    </a>
    <a href="https://thinkdiff.net/about/">
        <img src="https://img.shields.io/badge/about-me-yellow.svg" alt="pythonbangla.com" />
    </a>
    <a href="https://twitter.com/mahmudahsan">
        <img src="https://img.shields.io/badge/contact%40-mahmudahsan-blue.svg" alt="Twitter: @mahmudahsan" />
    </a>
</p>

# Python, JavaScript and Computer Science

I created this repository to practice myself. Here I publish programming code for myself or for my tutorials published in my [Blog](https://thinkdiff.net) or my [Youtube Channel](https://www.youtube.com/channel/UCtHlgyUw0wLE5Ous9swfFlg). When I solve any programming problem I like to write solution in both `Python` and `JavaScript` languages. As these 2 languages currently I am mostly working on. Beside these 2 languages, I have extensive working knowledge of `Swift` and `Obj-C` programming langauges.

## My Programming Courses

- [Learn Python Programming Full Course FREE](https://youtu.be/llbgjR_tL2k)
- [Master Python Programming in 5 Hours](https://www.udemy.com/python-beginner-to-advanced-with-web-scraping-projects/)
- [Web Scraping in Python with BeautifulSoup & Scrapy Framework](https://www.udemy.com/web-scraping-in-python/)
- [বাংলায় পাইথন প্রোগ্রামিং](https://pythonbangla.com)


## Table of Contents

### Python and JavaScript

1. [Coding Problems](coding-problems/)
2. [Python and JavaScript Language Primer](#python-and-javascript) 
3. [Python Codes](python-language/)
4. [JavaScript Codes](javascript/)

### Django

1. [Django Codes](django-framework/)
2. [Django Rest Framework Codes](django-rest-framework/)

### React and React Native

1. [React Native Tutorials](react-native/)

### Open Source Projects

1. [Todos Mobile App- React-Native](https://github.com/mahmudahsan/todos-react-reactnative)
2. [Pythonbangla.com - React.js](https://github.com/mahmudahsan/python-bangla-react)
3. [Pythonbangla.com - Django](https://github.com/mahmudahsan/pythonbangla.com)
4. [Web Scraping - Python | Aljazzera | GoodReads](https://github.com/mahmudahsan/webscraping)
5. [Bank Rates - Python](https://github.com/mahmudahsan/bankrates)

### Python and JavaScript

1. [Variables](#variables)
2. [Absent of Value](#absent-of-value)
3. [Operators](#operators)
4. [Statements, Expression, comments](#statements-expression-comments)
5. [String](#string)
6. [List](#list)

### Variables

> Environment: Collection of bindings and their values that exist at a given time is called the environment

### `Python`

```python
name = "Grocery List"
detail = 'Buy from supershop'
number_of_items = 5
budget = 2500 # taka
amount_of_rice = 1.56 # kg
should_we_buy_today = True

print( name, type(name) )
print( detail, type(detail) )
print( number_of_items, type(number_of_items) )
print( amount_of_rice, type(amount_of_rice) )
print( should_we_buy_today,  type(should_we_buy_today) )

```

### `JavaScript`

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

### `Python`

```python
name = None
print(name) # None
```

### `JavaScript`

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

### `Python`

```python
number_of_items = number_of_items + 2
print( number_of_items )

number_of_items += 2
print( number_of_items )

amount_of_rice += 2.3
print ( amount_of_rice )

amount_of_rice -= 2
print ( amount_of_rice )

number_of_items *= 3
print (number_of_items)

number_of_items /= 3
print ( number_of_items, type(number_of_items) )
number_of_items = int(number_of_items)
print ( number_of_items, type(number_of_items) )

## Division

x = 10
y = 2
result = x / 2
print (result)

result = int (x / 2)
print (result)

y = 3
result = x / y
print (result)

## Remainder opertor
result = int (x / y)
print (result)

print (x, y, x % y)

x = 10.0
y = 3.0
print (x, y, x % y)

## Negative value 
x = 10
x = -x
print (x)

## Divmod
x = 10
y = 3
result = divmod(x, y)
print (result)

## Exponential

x = 2
result = x ** 4
print (result)

result = pow (2, 4)
print (result)
```

### `JavaScript`

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

> The smallest part of codes that python interpreter can execute is called `statement`

> The combination of value, variable and operators are called `expression`

### `Python`

```python
# This is a single line comment
"""
This is a
multiline comment or doc string
"""

'''
This is a
multiline comment
'''
```

### `JavaScript`

```javascript
// Single line comment
/* This is a
multiline comment */
```

### String

### `Python`

```python
# Accessing string character
title = "Python Course"
print ( title[0], title[1], title[-1], title[-2])

# String operation
name = 'jonathon swift'
print ( name.title() )
print ( name.upper() )
print ( name.lower() )

# String Concatenation

first_name = "Steve"
last_name  = "Jobs"
name = first_name + ' ' + last_name
print ( name )

print ( first_name + ' ' + last_name )

# Newline
print (first_name + "\n" + last_name)

# Whitespace
name = "        Mr. X        "
print('_' + name + '_')
print('_' + name.lstrip() + '_')
print('_' + name.rstrip() + '_')
print('_' + name.strip() + '_')
print('_' + name.lstrip().rstrip() + '_')

# Printing Single and Double Quote
shop_name = "Rahim's Shop"
print(shop_name)

shop_name = 'Rahim"s Shop'
print(shop_name)

shop_name = 'Rahim\'s Shop'
print(shop_name)

# Matching text at start and at the end
filename = 'bigdata.txt'
print ( filename.endswith('.txt') )
print ( filename.startswith('bi') )

# Find word in sentence
sentence = "A quick brown fox jumps over the lazy dog"
print ( sentence.find('fox') )
print ( sentence.find('foxs') ) # -1 the value not found

# Replace text
sentence = "A quick brown fox jumps over the lazy dog"
sentence = sentence.replace('fox', 'tiger')
print ( sentence )

# Print separator
x = 'Dhaka'
y = 'Bogra'
z = 'Comilla'

print (x + '| ' + y + '| ' + z)
print (x, y, z, sep='| ')

# String interpolation
# Old style
person = '%s\'s age is %d'
print(person % ('Bill', 55) )

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bill', age=55))
print(person.format(name='Steve', age=50))

print()

# Formatted string literal Python 3.6+ 
name = 'Mark'
age  = 30
person = f'{name}\'s age is {age}'
print(person)

print()

# String slice
name = "Taylor Swift"
print (name[0: 6])
print (name[:6])
print (name[7:])
print (name[7:-1])
```

### `JavaScript`

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

`Python`
```python
lst = [1, 2, 3]
```

`JavaScript`
```javascript
const lst = [1, 2, 3]
```

**Common Methods**

| List            |     `Python`      |         `JavaScript` |
| --------------- | :---------------: | -------------------: |
| get first item  |   `lst.pop(0)`    |        `lst.shift()` |
| number of items |    `len(lst)`     |         `lst.length` |
| item existence  |   `item in lst`   | `lst.includes(item)` |
| index of item   | `lst.index(item)` |  `lst.indexOf(item)` |


***Document Templates***

### Title

### `Python`

```python

```

### `JavaScript`

```javascript

```

| List | `Python` | `JavaScript` |
| ---- | :------: | -----------: |
|      |    ``    |           `` |
|      |    ``    |           `` |
|      |    ``    |           `` |

