# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Generator
# --------------------------

# Iterable 
str = "Hello World"
for i in str:
    print(i)
    
print("\nList Comprehension\n")

# List Comprehension
list = [x*x+2 for x in range(1, 5)]
for item in list:
    print(item)
    
# Everything we can use using for...in are iterable
# But for iteration all the values are stored in memory

print("\nGenerator\n")

# Generator
gen = (x*x+2 for x in range(1, 5)) # Generator comprehension
for item in gen:
    print(item)
    
# Nothing will print again, Gen is no longer available
for item in gen:
    print(item)
    
# Generator are kind of iterator which can only iterate once
# Generator do not store values in memory
# Generator generates value on fly
# List comprehension when iterator we use []
# Generator comprehension of List we use ()

print("\ngen123\n")
def gen123():
    yield 1 
    yield 2
    yield 3

print(gen123)    
print(gen123())
    
for i in gen123():
    print(i)

print("\ngen123 again\n")
gen_obj = gen123()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj)) # for loop catch the exception and terminate

# A function can not have both return and yield keywords
# yield is like return. The difference is when the function
# call again execution starts from the last call to yield statement