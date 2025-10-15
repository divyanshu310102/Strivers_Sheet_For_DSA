# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = int(input('Enter no.: '))
mid = n//2
star = '*'
for i in range(1, n+1):
    if i <= mid:
        print(star*i)
    else:
        print(star * (n-i+1))    

    