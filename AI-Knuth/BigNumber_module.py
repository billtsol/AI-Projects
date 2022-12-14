# How to use BigNimber Library in Python3.10

import BigNumber 
from BigNumber.BigNumber import factorial, sqrt


number = 500000 # 500.000

bigNumber = BigNumber.BigNumber.BigNumber(number) # Convert $number to BigNumber

newBigNumber = BigNumber.BigNumber.BigNumber(factorial(bigNumber)) # $newBigNumber get the factorial of $bigNumber

print("Number: ", number, " ",number.__class__)
print("BigNumber: ",bigNumber, " ", bigNumber.__class__)
print("Factorial of bigNumber: ", newBigNumber, " ", newBigNumber.__class__)


root = sqrt(bigNumber) # Root of bigNumber

print("Root: ",root, " ",root.__class__)

root = sqrt(newBigNumber) # Root of bigNumber factorial

print("Root of factorial: ",root, " ",root.__class__)

for i in range(17): # 17 times root of newBigNumber
    root = sqrt(root)

print("Root of factorial: ",root, " ",root.__class__)

# Floating point BigNumber
floatBigNumber = BigNumber.BigNumber.BigNumber("0.34")
print("Float: ", floatBigNumber, " ", floatBigNumber.__class__)

# Add in floating point bigNumber
newFloatBigNumber = BigNumber.BigNumber.BigNumber("3") + floatBigNumber
print("new Float: ", newFloatBigNumber, " ",newFloatBigNumber.__class__)
