# How to use BigNimber Library in Python 3.10
import mpmath as mp
import BigNumber
from BigNumber.BigNumber import factorial, sqrt


print("-----------------------BigNumber module-----------------------")
number = 500000  # 500.000

bigNumber = BigNumber.BigNumber.BigNumber(
    number)  # Convert $number to BigNumber

# $newBigNumber get the factorial of $bigNumber
newBigNumber = BigNumber.BigNumber.BigNumber(factorial(bigNumber))

print("Number: ", number, " ", number.__class__)
print("BigNumber: ", bigNumber, " ", bigNumber.__class__)
print("Factorial of bigNumber: ", newBigNumber, " ", newBigNumber.__class__)


root = sqrt(bigNumber)  # Root of bigNumber

print("Root: ", root, " ", root.__class__)

root = sqrt(newBigNumber)  # Root of bigNumber factorial

print("Root of factorial: ", root, " ", root.__class__)

for i in range(17):  # 17 times root of newBigNumber
    root = sqrt(root)

print("Root of factorial: ", root, " ", root.__class__)

# Floating point BigNumber
floatBigNumber = BigNumber.BigNumber.BigNumber("0.34")
print("Float: ", floatBigNumber, " ", floatBigNumber.__class__)

# Add in floating point bigNumber
newFloatBigNumber = BigNumber.BigNumber.BigNumber("3") + floatBigNumber
print("new Float: ", newFloatBigNumber, " ", newFloatBigNumber.__class__)


# How to use mpMath Library in Python 3.10
print("-----------------------mpMath module-----------------------")

bigNumber = 500000  # 500.000

# $newBigNumber get the factorial of $bigNumber
newBigNumber = mp.fac(bigNumber)

print("Number: ", bigNumber, " ", bigNumber.__class__)
print("Factorial of bigNumber: ", newBigNumber, " ", newBigNumber.__class__)


root = mp.sqrt(bigNumber)  # Root of bigNumber

print("Root: ", root, " ", root.__class__)

root = mp.sqrt(newBigNumber)  # Root of bigNumber factorial

print("Root of factorial: ", root, " ", root.__class__)

for i in range(17):  # 17 times root of newBigNumber
    root = mp.sqrt(root)

print("Root of factorial: ", root, " ", root.__class__)

# Floating point BigNumber
floatBigNumber = 0.34
print("Float: ", floatBigNumber, " ", floatBigNumber.__class__)

# Add in floating point bigNumber
newFloatBigNumber = mp.floor(floatBigNumber)
print("mpMath floor: ", newFloatBigNumber, " ", newFloatBigNumber.__class__)
