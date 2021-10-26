def selection_sort(array):
    for i in range(len(array) - 1):
        lowestNumberIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j
        if lowestNumberIndex != i:
            temp = array[i]
            array[i] = array[lowestNumberIndex]
            array[lowestNumberIndex] = temp
    return array

arr = [15, 7, 11, 10, 7, 9]
print(arr)
arr = selection_sort(arr)
print(arr)


