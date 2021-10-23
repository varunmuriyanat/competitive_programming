WEIGHT_LIMIT = 5
value  = [3, 9, 12, 8]
weight = [1, 3, 4, 2]

# pos: Index of the current item
# selected: list of indices of selected items
def knapsack(pos, selected):
    print("selected: " + str(selected))
    # Calculate totals
    totalValue = 0 
    totalWeight = 0
    for i in selected:
       totalValue += value[i]
       totalWeight += weight[i]
 
    # Base Case: Stop if Overweight
    if totalWeight > WEIGHT_LIMIT:
       return (0,0)
       
    # Base Case: No items left
    if pos >= len(weight):
       return (totalValue, totalWeight)
    
    # Recursive Case
    ans1 = knapsack(pos+1, selected+[pos])   # Switch On
    ans2 = knapsack(pos+1, list(selected))   # Switch Off
    
    if ans1[0] > ans2[0]:
       return ans1
    else:
       return ans2
       
ans = knapsack(0, [])
print(ans)

