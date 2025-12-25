# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****     
# **********



n = int(input("Enter the rows: "))
star = "*"
space = " "
mid = n//2
for i in range(1,n+1):
    if i <= mid:
        print((mid - i + 1) * star + (2*(i - 1)) * space +  (mid - i + 1) * star)
    else:
        print((i - mid) * star + (2 *(n - i)) * space + (i - mid) * star)    
