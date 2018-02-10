# author Mahmud Ahsan
# Comments

""" 
Multiline 
Comments
"""

# Variable

name = "Grocery List"
detail = 'Buy from supershop'
number_of_items = 5
budget = 2500 # taka
amount_of_rice = 1.56 # kg
should_we_buy_today = True

print( name, type(name) )
print( detail, type(detail) )
print( number_of_items, type(number_of_items) )
print( amount_of_rice, type(amount_of_rice) )
print( should_we_buy_today,  type(should_we_buy_today) )


# Operators

number_of_items = number_of_items + 2
print( number_of_items )

number_of_items += 2
print( number_of_items )

amount_of_rice += 2.3
print ( amount_of_rice )

amount_of_rice -= 2
print ( amount_of_rice )

number_of_items *= 3
print (number_of_items)

number_of_items /= 3
print ( number_of_items, type(number_of_items) )
number_of_items = int(number_of_items)
print ( number_of_items, type(number_of_items) )

## Division

x = 10
y = 2
result = x / 2
print (result)

result = int (x / 2)
print (result)

y = 3
result = x / y
print (result)

## Remainder opertor
result = int (x / y)
print (result)

print (x, y, x % y)

x = 10.0
y = 3.0
print (x, y, x % y)

## Negative value 
x = 10
x = -x
print (x)

## Divmod
x = 10
y = 3
result = divmod(x, y)
print (result)

## Exponential

x = 2
result = x ** 4
print (result)

result = pow (2, 4)
print (result)
