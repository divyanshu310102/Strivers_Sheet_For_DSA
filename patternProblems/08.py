# *********
#  *******
#   *****
#    ***
#     *


n = int(input('Enter no.: '))
# for i in range(n):
#     for j in range(2*n - i - 1):
#         if i > j:
#             print(" ", end=" ")
#         else:
#             print('*',end=" ")    
#     print()    

 #Optimized version O(n)
for i in range(n, 0, -1):
    print(" " * (n - i) + (('*') * (2*i - 1)))
