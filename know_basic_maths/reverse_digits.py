# Given an integer N return the reverse of the given number


n = int(input("Enter the no.: "))

rev_no = 0

while n > 0:
    last_digit = n % 10
    rev_no = rev_no * 10 + last_digit
    n = n // 10

print(rev_no)    