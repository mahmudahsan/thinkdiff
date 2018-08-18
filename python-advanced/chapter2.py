# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#      Unit Test
# --------------------------

'''
mspack.msmath and mspack.msstring modules are tested by 
chapter2_test.py file.
'''

from mspack import msmath
from mspack import msstring

print ( "Sum: ", msmath.sum(10, 20) )
print ( "Division: ", msmath.division(25, 5))
print ( "Full Name: ", msstring.MsName("Mahmud", "Ahsan").full_name())
