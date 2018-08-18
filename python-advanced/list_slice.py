# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#  List Slicing - Techniques
# --------------------------

# syntax: list[start:end:step] # returns a new list
# end always exclusive

mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

## print all
print(mlist[:])

print()
## natural sequence of getting 5 elements
print(mlist[0:5:1])

print()
## skip one element and print all
print(mlist[::2])

print()
## copy of original list in reverse order
print(mlist[::-1]) # check by -2

# mlist.reverse() # modify the original list
# print(mlist)

print()
## copy list
crlist = mlist 
print(f'mlist: {mlist}')
print(f'crlist: {crlist}')
mlist.reverse()
print(f'mlist: {mlist}')
print(f'crlist: {crlist}')

print()
## cloning list
clist = mlist[:]
mlist.reverse()
print(f'mlist: {mlist}')
print(f'clist: {clist}')

## clear all elements
del mlist[:]
print(mlist)

