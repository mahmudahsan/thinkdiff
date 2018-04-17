# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------
#      tuple
# --------------------

# Syntax
tp = 1, 2, 'bill', 4.4, False
print (tp, type(tp))

# parentheses are optional
tp = (1, 2, 'bill', 4.4, False) 
print (tp)

# this is not tuple
a, b = 1, 2
print (a)
s = ('hi')
print (s, type(s))

# Access
tp = 1, 2, 'bill', 4.4, False
print (tp[0], tp[2], tp[-1], sep='|')

# Iteration 
tp = 1, 2, 'bill', 4.4, False
for t in tp:
    print (t)
    
# Comparing
t1 = 1, 2, 3
t2 = 1, 2, 3  # change order and discuss
if t1 == t2:
    print ("t1 and t2 values are equal")
    
# Immutable
t1 = 1, 2, 3
# t1[0] = 2 #'tuple' object does not support item assignment

# Unpacking or Multiple assignment
t1 = 5, 7, 11
x, y, z = t1
print (x, y, z, sep = ' | ')

# x, y = t1 # too many values to unpack
t1 = 5, 7, 11
x, y, _ = t1
print (x, y, sep = ' | ') # print (x, y, _, sep = ' | ')

# --------------------
#      dictionary
# --------------------

# Syntax
'''
dict = {key : value}
'''

dict = {} # empty dictionary
dict['name'] = 'Swift'
dict['age']  = 55
print ( dict['name'], '|', dict['age'] )

dict = {'bill' : '01010101', 'steve' : '0404040'}
print (dict['bill'])
print (dict['steve'])
print (len(dict))

# Modification
shop_items_price_kg = {'rice' : 44, 'flour' : 33}
print ( shop_items_price_kg )

# Adding new item
shop_items_price_kg['oil'] = 39
print ( shop_items_price_kg )

# Deleting item 
del shop_items_price_kg['oil'] # removes key | value pair
print ( shop_items_price_kg )

# Editing item 
shop_items_price_kg['rice'] = 90
print ( shop_items_price_kg )

# Iteration 
# key and value
asci_dict = {'a':97, 'b':98, 'c':99, 'd':100}

for key, value in asci_dict.items(): 
    print (key, value, sep='->')
    
'''
# Error because it will search only keys
for key, value in asci_dict:
    print (key, value, sep='->')
'''

# Iterate key only
for key in asci_dict: # for key in asci_dict.keys() works same
    print (key)

# Iterate value only
for value in asci_dict.values():
    print (value)
    
# Sorted keys while iterate
shop_items_price_kg = {
    'rice' : 44, 
    'flour' : 33, 
    'oil': 32
}
print(shop_items_price_kg)
for key in sorted(shop_items_price_kg.keys()): # to remove confusion we used .keys()
    print (key, shop_items_price_kg[key])

