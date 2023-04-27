# driver code
val =[1, 6, 10, 16]
wt = [1, 2, 3, 5]
W = 7
n = len(val)

# We initialize the matrix with 0 at first.
# Note: DON'T INITIALIZE WITH -1
t = [[0 for i in range(W + 1)] for j in range(n + 1)]


def knapsack(wt, val, W, n):
    for i in range(0, n+1):
        for j in range(0, W+1):
            if i==0 or j==0:
                t[i][j] = 0
            if wt[i-1] <= j:
                chosen = val[i-1] + t[i-1][j - wt[i-1]]
                # since we didn't choose ith item, value at t[i][j] index will remain same
                # as that at t[i-1][j] and no weight to be deducted from `j` part
                not_chosen = t[i-1][j]
                t[i][j] = max(chosen, not_chosen)

            else:
                # since we didn't choose ith item, value at t[i][j] index will remain same
                # as that at t[i-1][j] and no weight to be deducted from `j` part
                t[i][j] = t[i-1][j]

    return t[n][W]


print(knapsack(wt, val, W, n))
