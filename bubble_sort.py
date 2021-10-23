def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            #print(i, j, j+1)
            if(arr[j+1] < arr[j]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

arr = [15, 7, 11, 10, 7, 9]

print(arr)
bubble_sort(arr)
print(arr)

