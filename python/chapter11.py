# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Script arguments
# --------------------------
import sys
from mspack import msmath

print (sys.argv)

def process_command(*args):
    command = args[0]
    x       = int(args[1])
    y       = int(args[2])

    if command == 'sum':
        print ('Sum is: ',             msmath.sum(x, y))
    if command == 'sub':
        print ('Subtraction is: ',     msmath.subtract(x, y))
    if command == 'mul':
        print ('Multiplication is: ',  msmath.multiplication(x, y))
    if command == 'div':
        print ('Division is: ',        msmath.division(x, y))
        
if len (sys.argv) >= 4:
    # valid commands: sum sub mul div
    command = sys.argv[1].lower()
    x       = sys.argv[2]
    y       = sys.argv[3]
    
    try:
        process_command(command, x, y)
    except Exception as e:
        print ("Error in process_command: ", e)
    
else:
    print ("Command and Paramters are not sufficient")
    
'''
Run the script: 
    python3 chapter11.py sum 2 4
    python3 chapter11.py sub 2 4
    python3 chapter11.py mul 2 4
    python3 chapter11.py div 4 2
    python3 chapter11.py div 4 0
'''

# ----------------------------------
#      Sets
# ----------------------------------
'''
An unordered collection with no duplicate elements.
'''

## Empty Set
num_set = set() # {} reserved for dictionary

## Add elements
num_set.add(1)
num_set.add(2)
num_set.add(3)
num_set.add(1)
print (num_set) # unique values 1 is shown only one time

## Set operations
set_a = {1, 2, 3, 4, 5, 1}
set_b = {6, 5, 4, 7, 8, 8}
print ("Set A: ", set_a)
print ("Set B: ", set_b)

print ( "A-B ", set_a - set_b ) # items in set_a but not in set_b
print ( "A|B ", set_a | set_b ) # items in set_a or set_b or both
print ( "A&B ", set_a & set_b ) # common items in set_a and set_b
print ( "A^B ", set_a ^ set_b ) # items in set_a or set_b but not both

## Check item exist or not
set_country = {'bangladesh', 'malaysia', 'singapore', 'usa'}
country = 'bangladesh'

if country in set_country:
    print ( country.title(), 'exists ')


# ----------------------------------
#      Conditional Expression
# ----------------------------------
'''
In Java, C++ there is ternary operator
    condition ? expression1 : expression2

In Python 3 the equivalent is called conditional expression
    expression1 if condition else expression2
    
single line statement assign value directly to the variable
'''
sum = 100
num = 10
sum += num if num % 2 == 0 else 0
print (sum)

'''
4 lines code ordinary way
if num % 2 == 0:
    sum += num 
else:
    sum += 0
'''

# ----------------------------------
#      Comprehension Syntax
# ----------------------------------
'''
It is produced one series of values based on processing of another series
Syntax List
[ expression for value in iterable if condition ]
'''

## List comprehension
num_squares = [v * v for v in range(1, 11)]
print (num_squares)

### normal way
num_squares = [] 
for v in range(1, 11):
    num_squares += [v * v]
print (num_squares)

### odd num only 
num_squares = [v * v for v in range(1, 11) if v%2 != 0]
print (num_squares)

## Dictionary expression
num_dict_sq = {v: v * v for v in range(1, 11) if v%2 != 0}
print (num_dict_sq)

## Set expression
num_set_sq = {v * v for v in range(1, 11) if v%2 != 0}
print (num_set_sq)