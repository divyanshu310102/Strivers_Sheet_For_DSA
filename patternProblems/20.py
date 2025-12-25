#*        *
#**      **
#***    ***
#****  ****
#**********
#****  ****
#***    ***
#**      **
#*        *

n = int(input('Enter no.: '))
star = '*'
space = " "
mid = n//2
for i in range(1, n+1):
    if i <= mid:
        print(star * i + space * (2*(mid - i )) + star * i)
    else:
        print(star * (n - i) + space * (2*i - n) + star * (n - i))    

