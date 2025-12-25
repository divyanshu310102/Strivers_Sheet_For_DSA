# Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorted(arr):
    sorted = False
    for i in range(1,len(arr)):
        if arr[i-1] <= arr[i]:
            sorted = True
        else:
            sorted = False
            break
    if sorted:
        return True
    else:
        return False    
    
print(check_sorted([0,1,2,3,4,5,9,6,8,7]) )

