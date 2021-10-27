def eliminate_top_bottom(arr): 
    midpoint = len(arr)//2
    top = True
    while midpoint <= len(arr)-1: 
        print(arr)
        if top == True:
            arr = arr[0:midpoint+1] 
        else:
            arr = arr[len(arr)//2+1:] 
        top = not top     

    return arr[0]

print(eliminate_top_bottom([1, 2, 3, 6, 9, 10, 7]))
print("")
print(eliminate_top_bottom([2, 3, 6, 9, 10, 7]))
