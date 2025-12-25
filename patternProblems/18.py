# E
# DE
# CDE 
# BCDE
# ABCDE


n = int(input('Enter no.: '))
for i in range(1,n+1):
    for j in range(i, 0,-1):
        print(chr(64 + (n - j  + 1)), end = "")
    print()    
