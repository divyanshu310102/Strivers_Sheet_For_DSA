#Given an array of size N. Find the highest and lowest frequency element.

def frequency(arr):
    freq_dict = {}
    for element in arr:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    highest = -1
    lowest = 1000
    element_highest = None
    element_lowest = None
    for key, value in freq_dict.items():
        if value > highest:
            highest = value
            element_highest = key

        if value < lowest:
            lowest = value   
            element_lowest = key 
    return {element_highest:highest, element_lowest:lowest}



arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
result = frequency(arr)
print(result)  