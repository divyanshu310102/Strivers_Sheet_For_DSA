#*        *
#**      **
#***    ***
#****  ****
#**********
#****  ****
#***    ***
#**      **
#*        *



n = int(input("Enter the rows: "))
star = "*"
space = " "
mid = n // 2
for i in range(1, n+1):
    if i <= mid+1:
        print(i * star + 2*(mid-i + 1) * space + i * star)
    else:
        print((n-i+1) * star + 2*(i - mid - 1)*space + (n-i+1) * star)    
