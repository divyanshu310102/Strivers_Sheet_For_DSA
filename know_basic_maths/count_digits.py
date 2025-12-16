# Given an integer N, return the number of digits in N.

import math

n= int(input("Enter the no.: "))




# count = 0
# while n >= 10:
#     n = n // 10
#     count = count + 1
# print(count+1)    

print(int(math.log10(n) + 1))


