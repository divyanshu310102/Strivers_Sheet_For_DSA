#        **********
#        ****  ****
#        ***    ***
#        **      **
#        *        *
#        *        *
#        **      **
#        ***    ***
#        ****  ****
#        **********

n = int(input('Enter no.: '))
mid = n//2
star = '*'
space = " "
for i in range(1,n+1):
    if i <= mid:
        print(star * (mid - i + 1) + 2*(space * (i - 1)) + star * (mid - i + 1), end = "")
    else:
        print(star * (i-mid) + 2 * (space * (n - i)) + star * (i-mid), end="") 
    print()       
