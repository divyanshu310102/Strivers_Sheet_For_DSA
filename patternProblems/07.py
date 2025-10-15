 
#     *
#    ***
#   *****
#  *******
# *********

n = int(input('Enter no.: '))

# for i in range(n):
#     for j in range(n+i):
#         if i+j >= n-1:
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print()      
#
 #optimized version O(n)
for i in range(1,n+1):
    print((" " * (n - i)) + ('*' * (2*i-1)))