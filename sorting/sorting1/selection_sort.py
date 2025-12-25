#Given an array of N integers, write a program to implement the Selection sorting algorithm.

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] , arr[i]        
               
    return arr            


arr = list(map(int, input("Enter the values separated with space: ").split()))
result = selection_sort(arr)
print(result)


