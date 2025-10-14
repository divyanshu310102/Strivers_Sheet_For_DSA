# *********
#  *******
#   *****
#    ***
#     *


n = int(input('Enter no.: '))
for i in range(n):
    for j in range(2*n - i - 1):
        if i > j:
            print(" ", end=" ")
        else:
            print('*',end=" ")    
    print()    