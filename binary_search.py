def binary_search(arr, search_value):
    n = len(arr)
    midpoint = n // 2
    lower_bound = 0
    upper_bound = midpoint
    #print("n:{} lb:{} m:{} ub:{}".format(n, lower_bound, midpoint, upper_bound))

    while(lower_bound >= 0 and upper_bound <= n and lower_bound != upper_bound):
        if(arr[midpoint] == search_value):
            return midpoint
        elif(arr[midpoint] < search_value):
            lower_bound = midpoint + 1
            midpoint = (lower_bound + upper_bound) // 2
        elif(arr[midpoint] > search_value):
            upper_bound = midpoint - 1
            midpoint = (lower_bound + upper_bound) // 2

        if(arr[midpoint] == search_value):
            return midpoint

    return None


l = [1, 5, 6, 9, 14, 20, 70, 90, 88]
print(binary_search(l, 10))
print(binary_search(l, 14))


