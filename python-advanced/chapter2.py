# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# youtube: https://www.youtube.com/c/mahmudahsanthinkdiff
# License: MIT License
# https://github.com/mahmudahsan/thinkdiff/blob/master/LICENSE 

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
