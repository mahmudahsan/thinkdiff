### Python Language

- [Python Language](#python-language)
- [Variables](#variables)
- [Absent of Value](#absent-of-value)
- [Operators](#operators)
- [Statements Expression Comments](#statements-expression-comments)
- [String](#string)
- [Condition](#condition)
- [Iteration](#iteration)
- [List](#list)
- [Tuple](#tuple)
- [Dictionary](#dictionary)
- [Set](#set)
- [Function](#function)
- [Lambda](#lambda)
- [Class](#class)
- [Mixins](#mixins)
- [Map Filter Reduce](#map-filter-reduce)
- [Python 3.8 Features](#python-new-features)

### Variables

> Environment: Collection of bindings and their values that exist at a given time is called the environment

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

### Absent of Value

```python
name = None
print(name) # None
```

### Operators

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

### Statements Expression Comments

> The smallest part of codes that python interpreter can execute is called `statement`

> The combination of value, variable and operators are called `expression`

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

### String

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

### Condition

```python
num = 100
if num % 2 == 0:
    print ("Even Number")
    print ("Thank You")

# to run this part remove multipart comment
'''
num = input("Please enter a number: ")
num = int(num)
if num % 2 == 0:
    print ("Even Number")
    print ("Thank You")
else:
    print ("Odd Number")
    print ("Come Again")
'''

# to run this part remove multipart comment
# if-elif-else chained condition
'''
num = input("Please enter a number: ")
num = int(num)
if num == 50:
    print ("Half Century")
elif num == 100:
    print ("Century")
elif num > 100:
    print ("Century +")
else:
    print ("Unknown number")
    
'''

# Logical operators and or
num = 3
if num >= 3 and num < 5:
    print ('3 to 5')

num = 6
if num >= 3 and num < 5:
    print ('3 to 5')
else:
    print ("5 +")
    
num = -2
if num >= 3 or num == -2:
    print ('3 + or -2')

# Compare string
name1 = "Ahsan"
name2 = "ahsan"

if name1 == name2:
    print ("Same Name")
else:
    print ("Name doesn't match")
    
if name1.lower() == name2.lower():
    print ("Same Name by lower method")
    
# Not equals to
name = "Unknown Person"
if name != "Steve Jobs":
    print (name)
    
# nested condition
x = 5
if x < 2:
    print ("less than 2")
else:
    if x == 3:
        print ("x is 3")
    else:
        if x == 5:
            print ("x is 5")
```

# Iteration

```python
# while loop 
'''
while condition:
    body
'''

x = 1
print (x)
x += 1
print (x)
x += 1
print (x)
x += 1
print (x)
x += 1
print (x)

# 5 time repetition
x = 1
while x <= 5:
    print (x)
    x += 1
    
# infinite loop
x = 1
while True:
    print (x)
    x += 1
    if x > 10:
        break

# Omit even number 1 to 20
x = 0
while x < 20:
    x += 1
    if x % 2 == 0:
        continue 
    print (x)
    
# for loop
'''
for element in iterable:
    body
'''

# sum 1 to 10
sum = 0
for num in range(1, 11):
    print (num)
    sum += num
print ("Sum is {sum}".format(sum=sum))

# String characters by for loop
title = "Apple Inc."
for char in title:
    print (char)
```

### List

> List is a mutable ordered collection of items. 
- List item can be accessed by index number


`Python`
```python

# List
cars = ['honda', 'toyota', 'audi']
print(cars)
print (cars[0])
print (cars[2])

# Mixed List
mix_list = ['honda', 29, 4.4, False]
print (mix_list)

# Last element of list
print (mix_list[-1])

# empty list
cars = [] 
# print(cars[0]) will throw error

# 2D List or Matrix
'''
1 2 3 4 5 
4 5 6 7 8 
1 1 1 1 1 
0 0 0 0 0 
'''
# Nested list
matrix = [ [1, 2, 3, 4, 5],
           [4, 5, 6, 7, 8],
           [1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0]
          ]
                    
for x in matrix:
    for y in x:
        print (y, end=' ')
    print()


# list slicing
numbers_list = [1, 2, 3, 4, 5]
print ( numbers_list[0 : 2] )
print ( numbers_list[2 : -2])

# list iteration by for loop
cars = ['honda', 'toyota', 'audi']
for car in cars:
    print (car)
    if (car == 'toyota'):
        print ("I love toyota")
    
# sum of list numbers
list_of_number = [1, 2, 3, 4, 5]
sum = 0
for num in list_of_number:
    sum += num
print ("Sum is: {sum}".format(sum=sum))

list_of_number = [1, 2, 'Math', 4, 5.5, 5]
sum = 0
for num in list_of_number:
    if type(num) == int:
        sum += num
print ("Sum is: {sum}".format(sum=sum))

# List modification
mix_list = ['honda', 29, 4.4, False]
print(mix_list)
mix_list[0] = 'toyota'
print(mix_list)

# Adding item in list
mix_list.append('audi')
print(mix_list)

mix_list += ['mercedez'] # shortcut version for adding item
print(mix_list)

mix_list.insert(2, 'proton')
print(mix_list)

# Deleting item in list
cars = ['honda', 'toyota', 'audi']
del cars[0]
print( cars )

# Get and remove item using pop()
cars = ['honda', 'toyota', 'audi']
last_car = cars.pop() # last item
print(cars, "\n", last_car)

cars = ['honda', 'toyota', 'audi']
second_car = cars.pop(1) # second item
print(cars, "\n", second_car)

# Remove list item by value
numbers = [1, 2, 3, 4, 5, 6, 5]
numbers.remove(5) # remove the first value it finds in list
print(numbers)

# Splitting String into List items
import re
cars = "toyota, honda, bmw, audi"
# cars = ['toyota', 'honda', 'bmw', 'audi']
car_list = re.split(',', cars)
print(car_list)


# List's string item concatnation
quote = ['love', 'is', 'blind']
print(quote)
quote_str = ' '.join(quote)
print(quote_str)

# Sorting list
# list.sort(reverse=True|False, key=function)
cars = ['toyota', 'honda', 'audi', 'bmw']
print( cars )
cars.sort()
print( cars )
cars.sort(reverse=True)
print( cars )

cars = ['toyota', 'honda', 'audi', 'bmw']
print (sorted(cars)) # doesn't affect original list

# Reversing list
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# List length
numbers = [1, 2, 3, 4]
print (len(numbers))

# checking value exist in list
numbers = [1, 2, 3, 4]
if 2 in numbers:
    print ("2 is in number")

if 20 not in numbers:
    print ("20 does not exist")

# Empty list
list.clear()

# Joining two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list = list1 + list2

# Counting the occurrence of item
list = [1, 1, 2, 1, 3]
print(list.count(1)) # 3

# Extending list by list or any iterable object
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) # [1, 2, 3, 4, 5, 6]

```

### Tuple
> Tuple is an ordered immutable collection of items.

```python
# Syntax
tp = 1, 2, 'bill', 4.4, False
print (tp, type(tp))

# parentheses are optional
tp = (1, 2, 'bill', 4.4, False) 
print (tp)

# this is not tuple
a, b = 1, 2
print (a)
s = ('hi')
print (s, type(s))

# Access
tp = 1, 2, 'bill', 4.4, False
print (tp[0], tp[2], tp[-1], sep='|')

# Iteration 
tp = 1, 2, 'bill', 4.4, False
for t in tp:
    print (t)
    
# Comparing
t1 = 1, 2, 3
t2 = 1, 2, 3  # change order and discuss
if t1 == t2:
    print ("t1 and t2 values are equal")
    
# Immutable
t1 = 1, 2, 3
# t1[0] = 2 #'tuple' object does not support item assignment

# Unpacking or Multiple assignment
t1 = 5, 7, 11
x, y, z = t1
print (x, y, z, sep = ' | ')

# x, y = t1 # too many values to unpack
t1 = 5, 7, 11
x, y, _ = t1
print (x, y, sep = ' | ') # print (x, y, _, sep = ' | ')
```

### Dictionary
> Dictionary is an unordered, mutable collection of key:value pairs.

```python
# Syntax
'''
dict = {key : value}
'''

dict = {} # empty dictionary
dict['name'] = 'Swift'
dict['age']  = 55
print ( dict['name'], '|', dict['age'] )

dict = {'bill' : '01010101', 'steve' : '0404040'}
print (dict['bill'])
print (dict['steve'])
print (len(dict))

# Modification
shop_items_price_kg = {'rice' : 44, 'flour' : 33}
print ( shop_items_price_kg )

# Adding new item
shop_items_price_kg['oil'] = 39
print ( shop_items_price_kg )

# Deleting item 
del shop_items_price_kg['oil'] # removes key | value pair
print ( shop_items_price_kg )

# Editing item 
shop_items_price_kg['rice'] = 90
print ( shop_items_price_kg )

# Iteration 
# key and value
asci_dict = {'a':97, 'b':98, 'c':99, 'd':100}

for key, value in asci_dict.items(): 
    print (key, value, sep='->')
    
'''
# Error because it will search only keys
for key, value in asci_dict:
    print (key, value, sep='->')
'''

# Iterate key only
for key in asci_dict: # for key in asci_dict.keys() works same
    print (key)

# Iterate value only
for value in asci_dict.values():
    print (value)
    
# Sorted keys while iterate
shop_items_price_kg = {
    'rice' : 44, 
    'flour' : 33, 
    'oil': 32
}
print(shop_items_price_kg)
for key in sorted(shop_items_price_kg.keys()): # to remove confusion we used .keys()
    print (key, shop_items_price_kg[key])

```

### Set
> A set is an unordered and unindexed collection of values.
 
```python
fruites = {'mango', 'banana', 'pine-apple'}
print(fruites)
print(type(fruites))
```

### Function

```python
# Define
# sequence of statements can be defined as function
print ('Hello World')
for x in range(0,10):
    print ("HI", str(x))
    
def welcome():
    print ('Hello World')
    for x in range(0,10):
        print ("HI", str(x))
        
welcome()

# Built in function
'''
print('Something')
len('hello world')
max(2, 4)
'''

# Parameter
def welcome(name): # name is parameter
    print (f"Welcome {name}")
    
welcome('Bill') # 'Bill' is argument
welcome('Steve')

# Positional argument
def person_details(name, age, country):
    print (name, age, country, sep='|')
    
person_details('Bill', 55, 'US')
person_details('Swift', 40, 'Canada')

# Keyword argument
def person_details(name, age, country):
    print (name, age, country, sep='|')
    
## argument order doesn't matter
person_details(name='Bill', age=55, country='US')
person_details(age=40, country='Canada', name='Swift')

# Default value 
def person_details(name, age, country='Bangladesh'):
    print (name, age, country, sep='|')
    
person_details(name='Bill', age=55, country='US')
person_details(name='Swift', age=40) # default value keyword arg
person_details('Alam', 30) # default value positional arg

## non-default argument follows default argument
'''
def person_details(name='', age, country='Bangladesh'):
    print (name, age, country, sep='|')
'''

# Return value
def square (num):
    return num * num
    
print ( square(2), square(2.2), sep='|' )

def get_name(first_name, last_name):
    return first_name + " " + last_name

print ( get_name('Bill', 'Gates') )
print ( get_name('Steve', 'Jobs'))

# Optional argument
def get_name(first_name, last_name, middle_name=''):
    complete_name = first_name
    if middle_name:
        complete_name += ' ' + middle_name
    
    complete_name += ' ' + last_name
    return complete_name

print ( get_name('Bill', 'Gates') )
print ( get_name('Bill', 'Gates', 'S') )

print()
# Function are first-class object 
def str_upper(str):
    return str.upper()

print(str_upper("hello"))
stup = str_upper
print(stup("hello"))


## function can be passed as argument
def greetings(func):
    greet = func("Welcome, Nice to meet you")
    print(greet)
    
greetings(str_upper)

## Functional programming
up_list = list(map(str_upper, ["life", "is", "Cool"]))
print(up_list)

print()
## Nested Function
def hello_world(str):
    def print_upper(s):
        return s.upper()
        
    print(print_upper(str))

hello_world("mango")

print()
# Reference type parameter

## Value Type
num = 100
def change_num(n):
    n += 100 
    print ( f"Inner num: {n}")
change_num(num)
print ( 'Outside num: ' + str(num))

## List, Dictionary 
num_list = [1, 2, 3, 4, 5]
num_dict = {'one': 1, 'two': 2, 'three': 3}
def change_num_list(list, dict):
    del list[0]
    list[-1] = 50
    
    del dict['one']
    dict['three'] = 33
    print ("Inner List: ", list)
    print ("Inner Dict: ", dict)

print ( "Before" )
print ( "Outer List: ", num_list)
print ( "Outer Dict: ", num_dict)
change_num_list(list=num_list, dict=num_dict)
print ( "After" )
print ( "Outer List: ", num_list)
print ( "Outer Dict: ", num_dict)

# Arbitrary number of arguments
def students(*students_name):
    print (students_name, type(students_name))
    for student in students_name:
        print (student)
students('Bill', 'Steve', 'Jonathon', 'Jack', 'Bionic')
students()
students('Jack')

## Positional and Arbitrary arguments mixing
def students(captain, *other_students):
    print ('Captain ', captain)
    print ('Others ', other_students)
      
students('Mahmud', 'Fuad', 'Emon', 'Maruf', 'Arif')

# Arbitrary keyword arguments 
def students(captain, **other_students):
    print ('Captain ', captain)
    print ('Others ', other_students)
    
students(captain='Mahmud', second_captain='fuad', third_captain='emon')

## Arbitrary keyword arguments are optional
students(captain='Mahmud')
```

### Lambda

```python
# --------------------
#      Lambda
# --------------------

## Anonymous or Inline function
add_numbers = lambda x, y: x + y # auto return lambda expression
print( add_numbers(2, 3) )

bd_public = lambda name: "Bangladeshi Citizen: " + name
print ( bd_public('Mahmud') )

## Limitation of lambda expression
'''
single expression always returns a value
we can't include other if-else logic or iteration within it
'''
```

### Class
> Object-oriented programming or in short OOP is a computer programming paradigm where 
> data and related methods are encapsulated together using class.

```python
# Global varible
restaurant_name  = '7 Eleven'
restaurant_owner = 'Rahim'

def restaurant_details(): # function
    print (restaurant_name , restaurant_owner)
    
def another_restaurant():
    # Local variable
    restaurant_address = 'Bogra'
    print (restaurant_name , restaurant_owner)
    print (restaurant_address)

restaurant_details()
another_restaurant()
# print (restaurant_address) # shows error
# print (restaurant_name)

# Syntax 
'''
class ClassName (ParentClass):
    class variables
    instance methods
'''

class Restaurant: # () parentheses optional
    def details(self): # instance method
        print (self.name , self.owner)
        
    def details_with_address(self, address):
        # Local variable
        self.details()
        print (address)
        
## Instantiation
restaurant1 = Restaurant()
# creating instance variable
restaurant1.name  = '7 Eleven'
restaurant1.owner = 'Rahim'

# calling instance method will replacee self argument by
# instance object here restaurant1
restaurant1.details()  
restaurant1.details_with_address('Bogra')
# checking object type
print ( type(restaurant1) )

print()
## Second example 
class Person:
    def __init__(self, name="", age=0):
        # constructor when an instance created
        # if defined calls automatically during instantiation
        # used fo setting up initial configuration
        # self is required as first parameter
        # self.variable available all methods
        # variables called attributes in class
        # __init__ is called magic method or dunder method
        self.name = name 
        self.age  = age 
        
        # auto return instance of the class
        
    def details(self):
        print (self.name, self.age, sep=' | ')
        
bill1 = Person()
bill1.details()

bill2 = Person('Bill', 55) # self pass automatically
bill2.details()
print ( bill2.name, bill2.age)
'''
The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named self but anything else can also be used
'''

print()
## Third example
people_list = []
for x in range(0,3):
    person = Person("Person "+str(x), 30+x)
    people_list += [person]

for x in people_list:
    x.details()
    
print()
#-------------------------------------------
# Class variable and Instance variable Details
class Alien:
    legs = 5 # class variable
    
    def __init__(self, name):
        self.name = name # instance variable
        
## Instantiation
alien1 = Alien('Maven')
alien2 = Alien('Woven')

print(alien1.name, alien2.name) # accessing instance variable
print(alien1.legs, alien2.legs) # accessing class variable

## Updating class variable
Alien.legs = 10
print(alien1.legs, alien2.legs)


## Updating class variable by instance
alien1.legs = 1 # it creates a shadow instance variable
print(alien1.legs, alien2.legs) # alien1 now using instance variable

## removing shadow instance variable from instance
del alien1.legs
    
## Proper way to update class variable by instance
alien1.__class__.legs = 99
print(alien1.legs, alien2.legs)

#-------------------------------------------

print()
# Attribute value modification

class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age  = age 
        
    def change_name(self, name):
        self.name = name 
        
    def details(self):
        print (self.name, self.age, sep=' | ')
        
## Directly change
person_x = Person(name='Stone Cold', age=49)
person_x.details()

person_x.name = "Rock"
person_x.details()

## Indirectly change by instance's method
person_x.change_name('Triple X')
person_x.details()

# Lifecycle
class X:
    def __init__(self, name):
        self.name = name 
        print (self.name + " created")
    def __del__(self):
        print ( self.name + " is destoryed ")
  
# uncomment this to check lifecycle
# x = X('X') 
# y = X('Y')
print ("HELLO WORLD")

def hello():
    x = X('hello_X') 
    y = X('hello_Y')
hello()

##  Python garbage collection happens (by reference counting)

# Inheritence
class Math: # Parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def sum(self):
        return self.x + self.y 
        
class MathExtended1 (Math): # Child class
    def __init__(self, x, y):
        super().__init__(x, y) # super() func makes connection to parent class with child class
        
    def subtract(self):
        return self.x - self.y 
        
math_obj = Math(2, 4)
print ( math_obj.sum() )

math_ext_obj = MathExtended1(10, 2)
print ( math_ext_obj.subtract() )


## Multiple Inheritance
class MathExtra:
    def division(self, x, y):
        return x / y

class MathExtended2 (MathExtended1, MathExtra): # Child class
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def multiplication(self):
        return self.x * self.y 
        

math_ext2  = MathExtended2(10, 2)
print ( "Sum ", str(math_ext2.sum()) )
print ( "Subtract ", str(math_ext2.subtract()) )
print ( "Multiplication ", str(math_ext2.multiplication()) )
print ( "Division ", str(math_ext2.division(x=math_ext2.x,y=math_ext2.y)) )

# Method overriding
class Math: 
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def sum(self):
        return self.x + self.y 
        
class MathExtended1 (Math): # Child class
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def subtract(self):
        return self.x - self.y 
        
    def sum(self): # Override
        return self.x + self.y + 100
        
    def show_all(self):
        print ("Sum: " + str(self.sum()))
        print ("Subtract: " + str( self.subtract() ))
        # calling method from same class need self. at the front
'''
# Method overloading do not need in Python
    def sum(self, z):
        return self.x + self.y + self.z
'''
    
math_ext_obj = MathExtended1(10, 2)
math_ext_obj.show_all()

# Private and Public
'''
leading underscore before attributes and methods are
private by convention
'''
class Math: 
    def __init__(self, x, y):
        self._x = x 
        self._y = y 
    def sum(self):
        return self._x + self._y 

math = Math(2, 4)
print ( math._x )

print()
# Object comparison '==' vs 'is'
# == is used to check equality
# 'is' is used to check identity

x = [1, 2, 3]
xx = x

print(x == xx)
print(x is xx)

y = list(x)
print(x == y)
print(x is y)

print()
# String conversion of a class by __str__ method
l = [1, 2, 3]
print(l)

class Person:
    def __init__(self, name):
        self.name = name 
        
    def __str__(self):
        return f'{self.__class__.__name__} class, obj name:  {self.name}'
        
p1 = Person("Bill")
p2 = Person("Steve")

print(p1)
print(p2)
```

### Map Filter Reduce

```python
## syntax: map(func, iterable)
mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
slist = []
for x in mlist:
    slist.append(x * x)
'''

slist = list(map(lambda x: x * x, mlist))
print(slist)

## syntax: filter(func, iterable)
mlist = [1, 2, 3, -4, 5, 6, 7, -2, 9]

slist = list(filter(lambda x: x < 0, mlist))
print(slist)

## syntax: reduce(func, sequence)
from functools import reduce

product_price = [10, 20, 24.5, 50]

total_price = reduce(lambda x, y: x+y, product_price) 
print(total_price)
```

### Mixins
Mixins is a way to add extra methods or properties from other classes into a class. This creates a class in a compositional style.

In Python, class hierarchy is defined from right to left. So when we want to use mixins we have to be careful, in case there are same name method or property.


```python
# Mixins

class Base:
    def hello(self):
        print('Base')
        
class Mixin1:
    def hello(self):
        print('Mixin 1')
        
class Mixin2:
    def hello(self):
        print('Mixin 2')
        
class MyClass(Mixin2, Mixin1, Base):
    pass
        
if __name__ == '__main__':
    my_class = MyClass()
    my_class.hello()
    
```
Output
```
Mixin 2
```

#### Python New Features
### Python Version 3.8

Python version 3.8 introduced some new features. But in this section I will discuss, what features I think is important to know about.

#### Walrus Operator :=
Walrus operator assign a value in a variable as part of a larger expression.

```python
# Normal case
a = 100
print(a)

# Using Walrus Operator
print(b := 99)

# Another example
list = [1, 2, 3, 4, 5]

# Normal case
n = len(list)
if n > 4:
  print(f"List is oversized: {n}")

# Using Walrus Operator
if (n := len(list)) > 4:
  print(f"List is oversized: {n}")

```

#### Positional-Only Parameters

Normally if you use both positional and keyword arguments in a function call, you have to use positional arguments first and then keyword arguments.

```python
def output(a, b, c):
  print(a, b, c);

output(1, 2, c=4)

# It will show a syntax error
# output(a=1,b=2,3)
```

If you want, some function parameters only can be used as positionally not as keyword argument, you can mark those parameters by using `/` syntax. That means, you're basically forcing that some parameters can not be used as a keyword arguments.

```python
def showOutput(a, b, /, c, d):
  print(a, b, c, d)

showOutput(1, 2, c=3, d=4)

# TypeError 
# showOutput(a=1,b=2,c=3,d=4)
```

Basically to improve the readability of a function, the function writer intentional did that. 

For example `len()` function is intentionally designed as positional argument only. So if you call `len()` function like this it will not work:

```python
print(len(obj='hi'))
```

It will show a TypeError.
`TypeError: len() takes no keyword arguments`

You have to remove the 'obj' keyword. And you see, it basically improves the readability.

```python
print(len('hi'))
```

Another benefit of using parameter as positional-only is that, in future you can change the parameter name and it will not break the client code. 

But if the client used the positional argument as a keyword argument, it will break the client's code.

#### f-Strings Updated

f-Strings were introduced in Python 3.6 and in Python version 3.8 f-Strings are updated again.

Normally what we can do using f-String is, we can use literal, variable even expression within the string in curly braces. For example:

```python
num = 97.80
print(f'Num is: {num * 2:.2f}')
```
It will output:
```
Num is: 195.60
```
Here we used a format specifier by mentioning `:.2f` which means the output floating point number should not exceed 2 digit.

Now we can use walrus `:=` operator inside f-String to create a new variable as well. But you have to use surrounding parentheses in this kind of expression:

```python
num = 10
print(f'Sum: {(sum := num)}')
print(f'Sum + 2: {(sum := sum + 2)}')
```

Output:
```
Sum: 10
Sum + 2: 12
```

Another interesting f-String feature of Python 3.8 is, we can now use `=` at the end of the expression to see the output of the result and the expression:

```python
num = 100
print(f'{num=}')
print(f'{(sum := 2+2)=}')
```

output:

```
num=100
(sum := 2+2)=4
```

#### Improved Math functions
For multiplicative products, you can now use `math.prod` function.

```python
import math
result = math.prod((2, 3, 4, 5))
print(result)
```
Output
```
120
```
So basically if you have the factors stored in a list or set, using the `math.prod` function you can easily calculate the result.

Another function introduced is `math.isqrt` to find out the integer part of square roots.

```python
import math
num = 17
print(math.sqrt(num))
print(math.isqrt(num))
```
output:
```
4.123105625617661
4
```

If you use n-dimensional points and vectors you can now easily calculate the distance between two points using `math.dist` and the length of a vector using `math.hypot` function.

```python
import math
point_a = (24, 50, 40)
point_b = (12, 25, 30)

print(f'{math.dist(point_a, point_b)=}')
print(f'{math.hypot(*point_a)=}')
```
output
```
math.dist(point_a, point_b)=29.478805945967352
math.hypot(*point_a)=68.38128398911503
```

#### Improved Statistics functions

The statistics module also introduced some new functions.
- `statistics.fmean()`calculates the mean of floating point numbers
- `statistics.geometric_mean()` calculates the geometric mean of floating point numbers
- `statistics.multimode()` finds the most frequently occuring values in a sequence
- `statistics.quantiles()` calculates the cut points for dividing data into n continuous interval with equal probability


```python
import statistics

data = [10, 8, 5, 3, 1, 2, 1, 9, 10, 5]
print(f'{statistics.fmean(data)=}')

print(f'{statistics.geometric_mean(data)=}')

print(f'{statistics.multimode(data)=}')

print(f'{statistics.quantiles(data, n=3)=}')
```
output
```
statistics.fmean(data)=5.4
statistics.geometric_mean(data)=4.011828650378343
statistics.multimode(data)=[10, 5, 1]
statistics.quantiles(data, n=3)=[2.6666666666666665, 8.333333333333334]
```

There are some other features changed or improved in Python 3.8. For more information you can see the official what's new page:
[Python 3.8 What's New Official](https://docs.python.org/3/whatsnew/3.8.html)