def merge(arr1, arr2):
    print(arr1, arr2)

    new_arr = []

    ptr1 = 0
    ptr2 = 0
    steps = 0
    while (ptr1 < len(arr1)) or (ptr2 < len(arr2)): 
        if (ptr1 >= len(arr1)) and (ptr2 < len(arr2)):
            new_arr.append(arr2[ptr2])
            ptr2 += 1 
        elif (ptr2 >= len(arr2)) and (ptr1 < len(arr1)):
            new_arr.append(arr1[ptr1])
            ptr1 += 1 
        elif (ptr1 < len(arr1)) and (ptr2 < len(arr2)):
            if arr1[ptr1] < arr2[ptr2]: 
                new_arr.append(arr1[ptr1])
                ptr1 += 1
            else:
                new_arr.append(arr2[ptr2])
                ptr2 += 1
        steps += 1            

    print("steps:", steps)
    return new_arr     



arr1 = [1, 2, 3, 5, 7]
arr2 = [3, 4, 6, 8, 10]

print(merge(arr1, arr2))

