MAX_WEIGHT = 5
NUM_ITEMS = 4

value  = [3, 9, 12, 8]
weight = [1, 3, 4, 2]

memo = [
    [0 for j in range(MAX_WEIGHT+1)]
    for i in range(NUM_ITEMS+1)
]

for i in range(NUM_ITEMS):
    val = value[i]
    wt = weight[i]
    
    for j in range(MAX_WEIGHT+1):
        if weight[i] > j:
            memo[i+1][j] = memo[i][j]
            
        else:
            biggestPossibleWeight = j - wt
            if biggestPossibleWeight < 0:
                biggestPossibleWeight = 0
        
            switchOff = memo[i][j]
            switchOn = memo[i][biggestPossibleWeight] + val
            memo[i+1][j] = max((switchOff, switchOn))
            
for row in memo:
    print(("{:4}"*(MAX_WEIGHT+1)).format(*row))

