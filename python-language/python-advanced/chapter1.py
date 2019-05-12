# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#      Files
# --------------------------

## Reading full contents of a text file 
'''
Encouraged way
with keyword close the file automatically
'''
try:
    with open('data/article.txt') as fobj:
        contents = fobj.read()
        print (contents)
except Exception as e:
    print ("File Error: " , e)
    
print()
### Another way
'''
In this way, file need to close manually
'''
try:
    fobj = open('data/article.txt')
except Exception as e:
    print ("File Error: " , e)
else:
    contents = fobj.read()
    print (contents)
finally:
    fobj.close()
    
print()
'''
MacOS and Linux
Relative path:
data/article.txt 

Absolute path:
/user/mahmud/python/data/article.txt
'''

# Windows:
# data\article.txt
# C:\Users\mahmud\python\data\article.txt
    
### Reading line by line and make uppercase
with open("data/article.txt") as fobj:
    for num, line in enumerate(fobj):
        print ( num+1, line.upper() )
        
print()
### Reading list of lines
with open("data/names.txt") as fobj:
    lines = fobj.readlines()
    
print (lines)

## Write text in a file
'''
w = write   # erase existing content if any
a = append
r = read # default
OR
wt = write
at = append
rt = read 
t is for text mode which is set by default
'''
with open ('data/number.txt', 'w') as fobj:
    fobj.write('1')
    fobj.write('\n')
    fobj.write('28484')

## Append text in an existing file
'''
# uncomment to run this program
with open ('data/message.txt', 'a') as fobj:
    fobj.write("life is good \n")
'''

## Encoding during writing file
# latin-1 other encoding
with open ('data/bangla.txt', 'w', encoding='UTF-8') as fobj:
    fobj.write('আমার দেশ বাংলাদেশ')
    fobj.write('\n')
    fobj.write('আমি আমার দেশকে ভালবাসি')
    
## Redirect print output to file 
with open ('data/print.txt', 'w') as fobj:
    print ("Nothing goes unpaid", file=fobj)
    
## Write a binary data to a file 
with open ('data/binary', 'wb') as fobj:
    fobj.write(b'Life is good')
    
## Read a binary data file 
with open ('data/binary', 'rb') as fobj:
    binary_data  = fobj.read()
    decoded_data = binary_data.decode('utf-8') 
    print ( decoded_data )
    
## File existence checking
import os 
if os.path.exists('data/article.txt'):
    print ("Yes, file exist")
    
## Temporary file 
'''
w+ = reading and writing same time
With auto destroyed when file closed
'''
from tempfile import TemporaryFile 

with TemporaryFile('w+') as fobj:
    fobj.write("Life is cool.\n")
    
    fobj.seek(0) # seek to the beginning
    data = fobj.read()
    print (data)
    
## pyserial serial port access library
'''
Controlling hardware device like robot, sensor
by using serial port
https://github.com/pyserial/pyserial
'''

## Serialize python object to a byte stream
import pickle

dict_data = {'name':'Ahsan', 'country':'Bangladesh'}
# serialize_data = pickle.dumps(dict_data)
with open ('data/serialize', 'wb') as fobj:
    pickle.dump(dict_data, fobj)
    
with open ('data/serialize', 'rb') as fobj:
    dict_data = pickle.load(fobj)
    print ( dict_data )
    
print()

## CSV file read

import csv 

with open('data/expense.csv', 'r') as fobj:
    fcsv = csv.reader(fobj)
    
    sum = 0
    for i, row in enumerate(fcsv):
        print (i, row[0], row[1])
        sum += int(row[1]) if i > 0 else 0
    print ("Total Cost: ", sum)
        
'''
https://docs.python.org/3/library/csv.html
http://pandas.pydata.org
Pandas has pandas.read_csv() function to load CSV data to a DataFrame object.
'''

## CSV file write
list_items   = [["name", 'age', 'country'],
                ['Bill Gates', 55, 'US'],
                ['Mark Zuckerberg', 34, 'US'],
                ['Swift', 35, 'Canada']
                ]

import csv

with open('data/people.csv', 'w') as fobj:
    fcsv = csv.writer(fobj)
    fcsv.writerows(list_items)
 
print()

## JSON Data Encode and Decode
'''
JSON (JavaScript Object Notation) is a common standard to exchange data between server and client in web application. 
'''
import json 

data = {
    'name' : 'Bill Gates',
    'age'  : 55,
    'country' : 'US',
    'is_retired': True 
}

json_encoded_str = json.dumps(data)
print(json_encoded_str)

json_decode = json.loads(json_encoded_str)
print(json_decode)

### Dumping data in file and load from file

with open('data/json_data.json', 'w') as fobj:
    json.dump(data, fobj)
    
with open('data/json_data.json', 'r') as fobj:
    json_data = json.load(fobj)
    print (json_data)
    
    

