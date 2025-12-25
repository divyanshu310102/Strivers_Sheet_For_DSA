#Given an integer N, return all divisors of N.
import math
n = int(input("Enter the no.: "))
divisors = []

#Brute Force approach

# for i in range(1,n+1):
#     if n % i == 0:
#         divisors.append(i)
# print(divisors)     
 

#   Optimized approach

for i in range(1, math.isqrt(n)+1):
    if n % i == 0:
        divisors.append(i)

        if i != n // i:
            divisors.append(n//i)
divisors.sort()            


print(divisors)



