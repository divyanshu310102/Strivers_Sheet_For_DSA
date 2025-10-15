#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input('Enter no.: '))
mid = n//2
space = ' '
star = '*'
# for i in range(1,n+1):
    
#     if i <= mid:
#         print(space * (mid - i+1) + star * (2*i - 1))
#     else:
#         print(space * (i-mid-1) + star * (2*(n - i) + 1))    

for i in range(1,n+1):
    if n % 2 != 0:
    
        if i <= mid:
            print(space * (mid - i+1) + star * (2*i - 1))
        else:
            print(space * (i-mid-1) + star * (2*(n - i) + 1))
   
    else:
        if i <= mid:
            print(space * (mid - i+1) + star * (2*i - 1))
        else:
            print(space * (i-mid) + star * (2*(n - i) + 1))