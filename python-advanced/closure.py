# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#  Closures
# --------------------------

# Highter order function example
def make_total():
    arr = []
    
    def get_total(value):
        arr.append(value)
       
        return sum(arr)
    
    return get_total
    
sum1 = make_total()
print(sum1(10))
print(sum1(20))

# Another example
def make_total2():
    total = 0
    
    def get_total(value):
        nonlocal total
        
        total += value
        return total
    
    return get_total
    
sum2 = make_total2()
print(sum2(10))
print(sum2(20))
