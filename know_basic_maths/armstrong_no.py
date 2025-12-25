# Given an integer N, return true it is an Armstrong number otherwise return false
#An Amrstrong number is equal to the sum of its own digits each raised to the power of the number of digits.

import math

def armstrong_no(n):
    arm = 0
    while n > 0:
        last_digit = n % 10
        arm = arm + last_digit ** index
        n = n // 10
    return arm    

n = int(input("Enter the no.: "))
index = int(math.log10(n) + 1)



if n == armstrong_no(n):
    print(f"{n} is Armstrong number.")
else:
    print(f"{n} is not an Armstrong number."  )      


