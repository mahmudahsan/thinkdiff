# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 
# Object-oriented programming or in short OOP is a computer programming paradigm where 
# data and related methods are encapsulated together.

# --------------------
#      class
# --------------------

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

