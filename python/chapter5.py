# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# List
cars = ['honda', 'toyota', 'audi']
print(cars)
print (cars[0])
print (cars[2])

# Mixed List
mix_list = ['honda', 29, 4.4, False]
print (mix_list)

# Last element of list
print (mix_list[-1])

# empty list
cars = [] 
# print(cars[0]) will throw error

# 2D List or Matrix
'''
1 2 3 4 5 
4 5 6 7 8 
1 1 1 1 1 
0 0 0 0 0 
'''
# Nested list
matrix = [ [1, 2, 3, 4, 5],
           [4, 5, 6, 7, 8],
           [1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0]
          ]
                    
for x in matrix:
    for y in x:
        print (y, end=' ')
    print()


# list slicing
numbers_list = [1, 2, 3, 4, 5]
print ( numbers_list[0 : 2] )
print ( numbers_list[2 : -2])

# list iteration by for loop
cars = ['honda', 'toyota', 'audi']
for car in cars:
    print (car)
    if (car == 'toyota'):
        print ("I love toyota")
    
# sum of list numbers
list_of_number = [1, 2, 3, 4, 5]
sum = 0
for num in list_of_number:
    sum += num
print ("Sum is: {sum}".format(sum=sum))

list_of_number = [1, 2, 'Math', 4, 5.5, 5]
sum = 0
for num in list_of_number:
    if type(num) == int:
        sum += num
print ("Sum is: {sum}".format(sum=sum))

# List modification
mix_list = ['honda', 29, 4.4, False]
print(mix_list)
mix_list[0] = 'toyota'
print(mix_list)

# Adding item in list
mix_list.append('audi')
print(mix_list)

mix_list += ['mercedez'] # shortcut version for adding item
print(mix_list)

mix_list.insert(2, 'proton')
print(mix_list)

# Deleting item in list
cars = ['honda', 'toyota', 'audi']
del cars[0]
print( cars )

# Get and remove item using pop()
cars = ['honda', 'toyota', 'audi']
last_car = cars.pop() # last item
print(cars, "\n", last_car)

cars = ['honda', 'toyota', 'audi']
second_car = cars.pop(1) # second item
print(cars, "\n", second_car)

# Remove list item by value
numbers = [1, 2, 3, 4, 5, 6, 5]
numbers.remove(5) # remove the first value it finds in list
print(numbers)

# Splitting String into List items
import re
cars = "toyota, honda, bmw, audi"
# cars = ['toyota', 'honda', 'bmw', 'audi']
car_list = re.split(',', cars)
print(car_list)


# List's string item concatnation
quote = ['love', 'is', 'blind']
print(quote)
quote_str = ' '.join(quote)
print(quote_str)

# Sorting list
cars = ['toyota', 'honda', 'audi', 'bmw']
print( cars )
cars.sort()
print( cars )
cars.sort(reverse=True)
print( cars )

cars = ['toyota', 'honda', 'audi', 'bmw']
print (sorted(cars)) # doesn't affect original list

# Reversing list
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# List length
numbers = [1, 2, 3, 4]
print (len(numbers))

# checking value exist in list
numbers = [1, 2, 3, 4]
if 2 in numbers:
    print ("2 is in number")

if 20 not in numbers:
    print ("20 does not exist")


