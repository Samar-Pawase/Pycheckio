# Given an integer return the number of digits in it

import math


def numberOfDigits(number):
    if (number == 0):
        return 1
    elif(number < 0):
        return int(math.log10(-1*number)+1)
    return int(math.log10(number)+1)


print(numberOfDigits(0))
print(numberOfDigits(000))
print(numberOfDigits(100))
print(numberOfDigits(-2332))
