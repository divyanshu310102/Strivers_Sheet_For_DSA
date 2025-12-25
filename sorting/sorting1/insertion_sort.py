#Given an array of integers sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1 

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key  
    return arr    

arr = list(map(int, input("Enter the values separated with space: ").split()))
result = insertion_sort(arr)
print(result)          
    