def selection_sort(arr): 
    starting_index = 0
    while starting_index < len(arr)-1:
        low_value = arr[starting_index]
        low_index = starting_index
        for i in range(starting_index, len(arr)):
            if arr[i] < low_value:
                low_value = arr[i]
                low_index = i
        if low_index != starting_index:
            temp = arr[starting_index]
            arr[starting_index] = arr[low_index]
            arr[low_index] = temp 
        starting_index += 1
    return arr

arr = [15, 7, 11, 10, 7, 9]
print(arr)
arr = selection_sort(arr)
print(arr)


