# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------
#      class
# --------------------

# Global varible
restaurant_name  = 'দই ঘর'
restaurant_owner = 'রহিম'

def restaurant_details(): # function
    print (restaurant_name , restaurant_owner)
    
def another_restaurant():
    # Local variable
    restaurant_address = 'বগুড়া'
    print (restaurant_name , restaurant_owner)
    print (restaurant_address)

restaurant_details()
another_restaurant()
# print (restaurant_address) # shows error
# print (restaurant_name)

# Syntax 
'''
class ClassName (ParentClass):
    variables
    methods
'''

class Restaurant: # () parentheses optional
    name  = ''
    owner = ''

    def details(self): # method
        print (self.name , self.owner)
        
    def details_with_address(self, address):
        # Local variable
        print (self.name , self.owner)
        print (address)
        
## Instantiation
restaurant1 = Restaurant()
restaurant1.name  = 'দই ঘর' # Value access
restaurant1.owner = 'রহিম'
restaurant1.details()  # method call
restaurant1.details_with_address('বগুড়া')
print ( type(restaurant1) )

## Another example 
class Person:
    def __init__(self, name, age):
        # constructor
        # self is required as first parameter
        # self.variable available all methods
        # variables called attributes in class
        # __init__ is called magic method
        self.name = name 
        self.age  = age 
        
        # auto return instance of the class
        
    def details(self):
        print (self.name, self.age, sep=' | ')
        
bill = Person('Bill', 55) # self pass automatically
bill.details()
print ( bill.name, bill.age)
'''
The first argument of every class method, including init, is always a reference to the current instance of the class. By convention, this argument is always named self
'''

## Another example
people_list = []
for x in range(0,3):
    person = Person("Person "+str(x), 30+x)
    people_list += [person]

for x in people_list:
    x.details()
    
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

##  Python garbage collection (by reference counting)

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