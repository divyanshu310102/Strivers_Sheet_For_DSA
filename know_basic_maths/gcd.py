# Given two integers N1 and N2, find their greatest common divisor.


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a 

    if a == 0:
        return b
    return a           

n1 = int(input("Enter the first no.: "))
n2 = int(input("Enter the second no.: "))
print(f"GCD of {n1} and {n2} is: ", gcd(n1,n2))
