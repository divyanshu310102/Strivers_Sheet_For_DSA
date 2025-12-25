#Given an array, we have to find the number of occurrences of each element in the array.

def frequency(arr):
    freq_dict = {}
    for element in arr:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict



# Example usage:arr = [1, 2, 2, 3, 4, 4, 4]
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
result = frequency(arr)
for key, value in result.items():
    print(f"Element {key} occurs {value} times.")   