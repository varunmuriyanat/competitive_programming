def largest_product(arr):
    largest_product_so_far = arr[0] * arr[1] * arr[2]
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            k = j + 1
            while k < len(arr):
                if arr[i] * arr[j] * arr[k] > largest_product_so_far:
                    largest_product_so_far = arr[i] * arr[j] * arr[k]
                k += 1
            j += 1
        i += 1

    return largest_product_so_far


print(largest_product([1, 2, 3, 4, 5, 7, 8]))

