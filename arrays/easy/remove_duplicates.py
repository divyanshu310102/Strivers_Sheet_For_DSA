#Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

#If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

def remove_duplicates(arr):
    i = 0
    for j  in range(1,len(arr)):
        if arr[i] != arr[j]:
            i = i + 1
            arr[i] = arr[j]
    return arr[:i+1]        

           

print(remove_duplicates([1,1,2,2,4,4,4,7,7,9,9,9]))