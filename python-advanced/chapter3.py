# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# Web: http://pythonbangla.com
# youtube: https://www.youtube.com/c/banglaprogramming
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Regular Expression
# --------------------------

'''
https://regex101.com
'''

## Text pattern matching
import re

date_data = '13/Feb/2019 I will go Canada'

if re.match(r'\d+/[a-zA-Z]+/\d{4}', date_data):
    print ("Matched")
else:
    print ("Mismatched")
    
## Compiling pattern for reuse
   
import re 
date_data    = '13/Feb/2019 I will go Canada'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

if date_pattern.match(date_data):
    print ("Matched")
else:
    print ("Mismatched")

## Matching all occurrences

import re 
date_data    = '13/Feb/2019 hmm 20/Mar/2038 ok 13/Feb/2019'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

result = date_pattern.findall(date_data)
print (result)

## Capture groups

import re 
date_data    = '13/Feb/2019 I will go Canada'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

result       = date_pattern.match(date_data)

for x in range(0, 4):
    print ( result.group(x) )

print (result.groups())

day, month, year = result.groups()
print ("Today's day is: ", day)

## Raw String

import re

date_data = '13/Feb/2019 I will go Canada'

# r'\d+/[a-zA-Z]+/\d{4}' RAW String doesn't interpret \n escape char
if re.match('\\d+/[a-zA-Z]+/\\d{4}', date_data):
    print ("Matched")
else:
    print ("Mismatched")
    
## Search and Replace
    
import re

date_data     = '13/Feb/2019 I will go Canada' # Convert to 2019-Feb-13
date_pattern  = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
print ("Before: ", date_data)

date_modify1 = date_pattern.sub(r'\3-\2-\1', date_data)
print ("After: ", date_modify1)

### Capital letter of month name
import re

date_data     = '13/Feb/2019 I will go Canada' 
date_pattern  = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

def to_upper(m):
    return '{} {} {}'.format(m.group(3), m.group(2).upper(), m.group(1))

date_modify2 = date_pattern.sub(to_upper, date_data)
print ("After: ", date_modify2)

## Case-insensitive search

import re 

text = "I am GOOD, but I am NOt very good"
list = re.findall('good', text, flags=re.IGNORECASE)
print (list)
text = re.sub('gOOd', 'bad', text, flags=re.IGNORECASE)
print (text)


## Unicode characters
import re 

num = re.compile(r'\d') # also show '\d+'
list = num.findall('১২৩৪ আমার দেশ বাংলাদেশ')
print (list)

## Strip unwanted middle space

import re 

text = "Life            is            Good"
txtre = re.compile(r'\s+')
text = txtre.sub(' ', text)
print (text)

