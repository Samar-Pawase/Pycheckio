# WAP to find number of zeros at the end of integer

from itertools import count

from numpy import zeros


def ending_zeros(num):
    zeros = 0
    if num == 0:
        return 1
    if(num%10 == 0):
        zeros+=1
    return zeros


num = int(input("Enter number - "))
print(ending_zeros(num))