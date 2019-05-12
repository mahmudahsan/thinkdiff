# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------
#      function
# --------------------

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
