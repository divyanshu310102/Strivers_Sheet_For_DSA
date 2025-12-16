# Given an integer N, check whether N is prime or not.
import math
n = int(input("Enter the no.: "))

is_prime = True

for i in range(1, math.isqrt(n) + 1):
    
        if i > 1 and n % i == 0:
            is_prime = False
            print(f"{n} is not a prime number.")
            break
        
if is_prime:
      print(f"{n} is a prime number.")              
   
