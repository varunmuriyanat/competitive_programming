def insertion_sort(arr): 
    for i in range(1, len(arr)):
        counter = 1
        temp_value = arr[i]
        while((i - counter) >= 0) and (arr[i - counter] > temp_value):
            arr[(i - counter) + 1] = arr[i - counter]
            arr[(i - counter)] = temp_value

            print("i:{} counter:{} i-counter:{} arr:{}".format(i, counter, i-counter, arr))
            counter += 1

    return arr

arr = [15, 7, 11, 10, 7, 9]
print(arr)
arr = insertion_sort(arr)
print(arr)


