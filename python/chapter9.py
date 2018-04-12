# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------
#      Modules
# --------------------
'''
Modules are Python source files contains functions, classes or global variables. Modules can be imported by other program.

Here we created mymath.py as a module
'''

# --------------------
#      Namespace
# --------------------

'''
When we import a module the file we imported its name is called namespace. See the example below

'''

# --------------------
#      Import
# --------------------

## Import entire module
import mymath # mymath is a filename and namespace

print ( mymath.sum(10, 2) ) # using mymath namespace we can call its function
print ( mymath.subtract(10, 2) )


## Import specific functions
from mymath import subtract

print ( subtract(2, 1) )


## Import all functions
from mymath import *

print ( sum(2, 5) )
print ( subtract(29, 1) )

## Import class from modules
from mymath import MyMathClass

mmc = MyMathClass(4, 2)
print ( mmc.sum() )
print ( mmc.subtract() )

## Alias

from mymath import subtract as sb # sb alias

print ( sb(10, 5) )

# --------------------
#      Package
# --------------------

'''
Python package is simply a folder/directory contains modules. 
But a directory must need to have a file named __init__.py to treat the directory as package
__init__.py file must contains the modules import statements

We created a package named mspack contains 2 modules
mspack/msmath.py
mspack/msstring.py

'''
## import specific modules in a package
from mspack import msmath
from mspack import msstring

print ( msmath.sum(10, 2) )
print ( msmath.subtract(10, 2) )
print ( msmath.multiplication(2, 2))

msstring.print_chracters("BANGLADESH")

## import all modules in a package
from mspack import *

print ( msmath.sum(10, 2) )
print ( msmath.subtract(10, 2) )
print ( msmath.multiplication(2, 2))

msstring.print_chracters("BANGLADESH")

## import all functions from a package/module
from mspack.msmath import *

print ( sum(10, 2) )
print ( subtract(10, 2) )
print ( multiplication(2, 2))

# --------------------------------
#      Python Standard Library
# --------------------------------
'''
The modules which automatically included when Python installed 
https://docs.python.org/3/library/index.html
'''
from random import choice
list = [1, 2, 3, 4, 5]

for x in range(0, 3):
    print ( choice(list) )

