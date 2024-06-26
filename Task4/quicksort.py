def QuickSort(arr):
    elements = len(arr)
    
    # Base case
    if elements < 2:
        return arr
    
    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to its appropriate position
    
    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements])  # Sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together
    
    return arr

# Prompting user for input
user_input = input("Enter the elements of the array, separated by spaces: ")
array_to_be_sorted = list(map(int, user_input.split()))

print("Original Array:", array_to_be_sorted)
print("Sorted Array:", QuickSort(array_to_be_sorted))
