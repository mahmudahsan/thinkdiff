# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#  Map, Filter, Reduce
# --------------------------

## syntax: map(func, iterable)
mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
slist = []
for x in mlist:
    slist.append(x * x)
'''

slist = list(map(lambda x: x * x, mlist))
print(slist)

## syntax: filter(func, iterable)
mlist = [1, 2, 3, -4, 5, 6, 7, -2, 9]

slist = list(filter(lambda x: x < 0, mlist))
print(slist)

## syntax: reduce(func, sequence)
from functools import reduce

product_price = [10, 20, 24.5, 50]

total_price = reduce(lambda x, y: x+y, product_price) 
print(total_price)
