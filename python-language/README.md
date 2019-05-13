### Python Language

- [Python Language](#python-language)
- [Variables](#variables)
- [Absent of Value](#absent-of-value)
- [Operators](#operators)
- [Statements Expression Comments](#statements-expression-comments)
- [String](#string)
- [List](#list)

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

`Python`
```python
lst = [1, 2, 3]
```
**Common Methods**

| List            |     `Python`      |
| --------------- | :---------------: |
| get first item  |   `lst.pop(0)`    |
| number of items |    `len(lst)`     |
| item existence  |   `item in lst`   |
| index of item   | `lst.index(item)` |

