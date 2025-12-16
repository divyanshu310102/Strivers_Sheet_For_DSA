# A
# B B
# C C C
# D D D D
# E E E E E

n = int(input("Enter no.: "))

for i in range(1,n+1):
    print(i * f'{chr(64+i)}')
       
