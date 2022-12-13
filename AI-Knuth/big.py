# import sys
# import time
import mpmath

import math as m
import BigNumber
from BigNumber.BigNumber import factorial, sqrt


# a = 10000000
p = "4"

p = BigNumber.BigNumber.BigNumber(p)


p = BigNumber.BigNumber.BigNumber(factorial(p))
p = BigNumber.BigNumber.BigNumber(factorial(p))
p = BigNumber.BigNumber.BigNumber(factorial(p))


r = sqrt(p)
for i in range(80):
    r = sqrt(r)
    print(r)


# p = BigNumber.BigNumber.BigNumber(factorial(p))
print("Python BigNumebr Factorial ", p, "    ", p.__class__)
print("Python BigNumebr root ", r, "    ", p.__class__)

if (p < r):
    print(True)
