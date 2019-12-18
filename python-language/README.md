### Python Language

- [Python Language](#python-language)
- [Variables](#variables)
- [Absent of Value](#absent-of-value)
- [Operators](#operators)
- [Statements Expression Comments](#statements-expression-comments)
- [String](#string)
- [List](#list)
- [Condition](#condition)
- [Iteration](#iteration)
- [Mixins](#mixins)
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