# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#      Metaprogramming: Decorator
# --------------------------

# Decorator is a callable that takes callable as argument and returns another callable
# The function which is passed as argument is called decorated function.
# It can process, change the decorated function 
# It either returns the original function or replace it with another function
# A decorator usually replace a function with different one which is part of metaprogramming

# Example 1
def decor(decoratedFunc):
    def inner():
        print("Inner Function")
    return inner 
    
def testFunc():
    print("Test Func")
    
decorated_func = decor(testFunc)
decorated_func()

print()
## syntactic sugar 
@decor
def testFunc1():
    print("Test Func1")
    
testFunc1()
    

print(testFunc)
print(testFunc1)

## Example 2 Uppercase
def uppercase(function):
    def decorated(*args):
        result = function(*args)
        result_upper = result.upper()
        return result_upper 
    return decorated
    
@uppercase 
def person_name(name):
    return name
    
upper_name = person_name("mahmud ahsan")
print(upper_name)

print(person_name("bill gates"))
