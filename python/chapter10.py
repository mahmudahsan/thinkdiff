# author Mahmud Ahsan
# --------------------
#      Exception
# --------------------
'''
Exception are object in Python that arise runtime to handle error
'''

## Hello Exception
def div(x, y):
    return x / y
    
print ( div(4, 2) )
# print ( div(2, 0) ) # division by zero error

## try catch block
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("Can not divide by zero")
        return None
        
    return result 
    
print ( div(4, 2) )
print ( div(2, 0) )


## Catch all exceptions   
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("Can not divide by zero")
        return None
    except:
        print ("Error occurred")
        return None
        
    return result 
    
print ( div('5', '4') )
print ( div(2, 0) )
  
## Catch all exceptions 2  
def div(x, y):
    try:
        result = x / y
    except Exception as e:
        print ("Error happened: ", e)
        return None
    return result
    
print ( div('4', '2') )
print ( div(4, 0) )
    
## else block
try:
    div_result = div(8, 2)
    # div_result = div(2, 0)
except:
    print ("Division by zero not possible")
else:
    print ("Div result is: " + str(div_result))
    
## finally block for clean up actions
def div(x, y):
    try:
        result = x / y 
    except ZeroDivisionError:
        print ("Error Division by Zero")
    else:
        print ("Result is: ", result)
    finally:
        print ("Execute finally clause")
        
div (100, 10)
div (2, 0)
# div ('30', '5') # TypeError

### When finally is necessary
'''
# sample example for discussion
try:
    big_data = read_from_internet()
except:
    pass 
else:
    # do something on big_data
finally:
    big_data = None
'''
    
## Ignore exception by pass
try:
    div_result = div(2, 0)
except:
    pass # do nothing
else:
    print ("Div result is: " + str(div_result))
    
## Multiple exceptions 
try:
    disk_file = open('filename')
except (FileNotFoundError, PermissionError): # using tuple
    print ("Can not open the file")
    
try:
    disk_file = open('filename')
except FileNotFoundError:
    print ("File doesn't exist")
except PermissionError:
    print ("Permission denied to open the file")
    
## Creating custom exception
class VowelNotAccepted(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status  = status
        
def check_chars(word):
    for char in word:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            raise VowelNotAccepted("Vowel is not accepted", 101)
    return word
            
# print ( check_chars("love"))
            
try:
    print ( check_chars("love")) 
    # print ( check_chars('My') )
except Exception as e:
    print ("Error reason: " , e.message)
    

# Built-in exceptions
'''
https://docs.python.org/3/library/exceptions.html
'''    
