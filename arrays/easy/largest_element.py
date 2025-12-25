#Given an array, we have to find the largest element in the array.

def largest(arr):
    maximum = float('-inf')
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


arr = list(map(int, input("Enter the values separated with space: ").split()))
result = largest(arr)
print(result) 