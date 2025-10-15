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
space = " "
star = "*"
mid = n//2
for i in range(1, n+1):
    if i <= mid:
        print(space * (mid - i + 1) + star * (2*i - 1))
    else:
        print(space * (i - mid - 1) + star * (2*n - (2*i - 1)))       
    
