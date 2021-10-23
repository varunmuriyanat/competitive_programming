# | Item | Weight | Value |
# |------|--------|-------|
# | 1    | 2      | 1     |
# | 2    | 10     | 20    |
# | 3    | 3      | 3     |
# | 4    | 6      | 14    |
# | 5    | 18     | 100   |

# Put a placeholder 0 weight, 0 value item to max
# these line up better with the 1D memoization table K
item_weights = [0, 2, 10, 3, 6,   18]
item_values =  [0, 1, 20, 3, 14, 100]

n = len(item_weights)
W = 15 # total weight capacity
K = [[0 for w in range(W + 1)] for i in range(n)]

print("w" + "\t" + "i" + "\t"  + "i-1" + "\t" + "wi" + "\t" + "vi" + "\t" + "w-wi" + "\t" + "K[i-1][w-wi]" + "\t" + "K[i-1][w]" + "\t" + "K[i][w]")
# Recurrence
for i in range(1, n):
  for w in range(1, W + 1):
    wi = item_weights[i]
    vi = item_values[i]

    if wi <= w:
      K[i][w] = max([K[i - 1][w - wi] + vi, K[i - 1][w]])
    else:
      K[i][w] = K[i - 1][w]

    if wi <= w:
      print(str(w) + "\t" + str(i) + "\t" + str(i-1) + "\t" + str(wi) + "\t" + str(vi) + "\t" + str(w-wi) + "\t" + str(K[i-1][w-wi]) + "\t\t" + str(K[i-1][w]) + "\t\t" + str(K[i][w]))

# Results
print("Result: ", K[n - 1][W])

## Optional: Uncomment to view the 2D table
import pandas as pd
print("K table:")
print(pd.DataFrame(K))

#    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
# 0  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 1  0   0   1   1   1   1   1   1   1   1   1   1   1   1   1   1
# 2  0   0   1   1   1   1   1   1   1   1  20  20  21  21  21  21
# 3  0   0   1   3   3   4   4   4   4   4  20  20  21  23  23  24
# 4  0   0   1   3   3   4  14  14  15  17  20  20  21  23  23  24
# 5  0   0   1   3   3   4  14  14  15  17  20  20  21  23  23  24  
