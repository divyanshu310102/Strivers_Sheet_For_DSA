#4 4 4 4 4 4 4
#4 3 3 3 3 3 4
#4 3 2 2 2 3 4
#4 3 2 1 2 3 4
#4 3 2 2 2 3 4
#4 3 3 3 3 3 4
#4 4 4 4 4 4 4 


n = 4  # outermost number

for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        top = i
        left = j
        right = (2 * n - 2) - j
        bottom = (2 * n - 2) - i
        min_dist = min(top, left, right, bottom)
        print(n - min_dist, end=" ")
    print()


