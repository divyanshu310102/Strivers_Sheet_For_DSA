def rev_no(n):
    reverse_no = 0
    while n > 0:
        last_digit = n % 10
        reverse_no = reverse_no * 10 + last_digit
        n = n // 10
   
    return reverse_no


n = int(input("Enter the no.: "))
print(n == rev_no(n))    






