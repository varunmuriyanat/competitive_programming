def linear_search(arr, search_value):
    for i in range(len(arr)):
        if(arr[i] == search_value):
            return i
        elif arr[i] > search_value:
            break
    return None


l = [1, 5, 6, 9, 14, 20, 70, 90, 88]
print(linear_search(l, 10))
print(linear_search(l, 14))

