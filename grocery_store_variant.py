# | Item | Weight | Value |
# |------|--------|-------|
# | 1    | 2      | 1     |
# | 2    | 10     | 20    |
# | 3    | 3      | 3     |
# | 4    | 6      | 14    |
# | 5    | 18     | 100   |

# Put a placeholder 0 weight, 0 value item to max
# these line up better with the 1D memoization table K
item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]

n = len(item_weights)
W = 15 # total weight capacity
K = [0] * (W + 1)

# Base case redundant, but added for clarity
K[0] = 0

print("w" + "\t" + "i" + "\t" + "wi" + "\t" + "vi" + "\t" + "w-wi" + "\t" + "spv" + "\t" + "msr")
# Recurrence
for w in range(1, W + 1):
  max_sub_result = 0
  for i in range(1, n):
    wi = item_weights[i]
    vi = item_values[i]
    if wi <= w:
      subproblem_value = K[w - wi] + vi
      if subproblem_value > max_sub_result:
        max_sub_result = subproblem_value 
      print(str(w) + "\t" + str(i) + "\t" + str(wi) + "\t" + str(vi) + "\t" + str(w-wi) + "\t" + str(subproblem_value) + "\t" + str(max_sub_result))
  K[w] = max_sub_result

# Results
print("Result: ", K[W])

idx = 0
for i in K:
    print("{:3} ".format(idx), end='')
    idx += 1

print("")

for i in K:
    print("{:3} ".format(i), end='')


