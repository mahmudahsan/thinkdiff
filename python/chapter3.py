# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# Statement
# The smallest part of codes that python interpreter can execute is called statement
# প্রোগ্রামিংয়োর ভাষায় কোডের ক্ষুদ্রতম অংশ যা পাইথন ইনটারপেটার এক্সকিউট করতে পারে সেটাই স্টেটমেন্ট

print ("Hello World")
x = 2
x = 2 + 1


# Expression
# The combination of value, variable and operators are called expression
# ভ‍্যালু, ভ‍্যারিয়েবল এবং অপারেটর এর কম্বিনেশন কেই এক্সপ্রেশন বলে
x = 17
y = x + 2 


# String

# Accessing string character
title = "Python Course"
print ( title[0], title[1], title[-1], title[-2])

# String operation
name = 'jonathon swift'
print ( name.title() )
print ( name.upper() )
print ( name.lower() )

# String Concatenation

first_name = "Steve"
last_name  = "Jobs"
name = first_name + ' ' + last_name
print ( name )

print ( first_name + ' ' + last_name )

# Newline
print (first_name + "\n" + last_name)

# Whitespace
name = "        Mr. X        "
print('_' + name + '_')
print('_' + name.lstrip() + '_')
print('_' + name.rstrip() + '_')
print('_' + name.strip() + '_')
print('_' + name.lstrip().rstrip() + '_')

# Printing Single and Double Quote
shop_name = "Rahim's Shop"
print(shop_name)

shop_name = 'Rahim"s Shop'
print(shop_name)

shop_name = 'Rahim\'s Shop'
print(shop_name)

# Matching text at start and at the end
filename = 'bigdata.txt'
print ( filename.endswith('.txt') )
print ( filename.startswith('bi') )

# Find word in sentence
sentence = "A quick brown fox jumps over the lazy dog"
print ( sentence.find('fox') )
print ( sentence.find('foxs') ) # -1 the value not found

# Replace text
sentence = "A quick brown fox jumps over the lazy dog"
sentence = sentence.replace('fox', 'tiger')
print ( sentence )

# Print separator
x = 'Dhaka'
y = 'Bogra'
z = 'Comilla'

print (x + '| ' + y + '| ' + z)
print (x, y, z, sep='| ')

# String interpolation
# Old style
person = '%s\'s age is %d'
print(person % ('Bill', 55) )

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bill', age=55))
print(person.format(name='Steve', age=50))

print()

# Formatted string literal Python 3.6+ 
name = 'Mark'
age  = 30
person = f'{name}\'s age is {age}'
print(person)

print()

# String slice
name = "Taylor Swift"
print (name[0: 6])
print (name[:6])
print (name[7:])
print (name[7:-1])
