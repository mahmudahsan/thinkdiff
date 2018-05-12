# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Metaprogramming: Decorator
# --------------------------

# Decorator is a callable that takes function as argument.
# The function which is passed as argument is called decorated function.
# It can process, change the decorated function 
# It either returns the original function or replace it with another function
# A decorator usually replace a function with different one

# Example 1
def decor(decoratedFunc):
    def inner():
        print("Inner Function")
    return inner 
    
@decor
def testFunc():
    print("Test Func")
    
def testAnotherFunc():
    print("Test Another")
    
print(testFunc)
testFunc()

testAnotherFunc()
test_another = decor(testAnotherFunc)
test_another()

# Decorator is called syntactic sugar. It is convenient when doing metaprogramming the way to change a program behavior at runtime.
