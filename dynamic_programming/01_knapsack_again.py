val =[1, 6, 10, 16]
wt = [1, 2, 3, 5]
W = 7
n = len(wt)

def knapsack(wt, val, W):
    n = len(wt)

    t = [[-1 for j in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                chosen = val[i-1] + t[i-1][j - wt[i-1]]
                not_chosen = t[i-1][j]
                t[i][j] = max(chosen, not_chosen)
            else:
                t[i][j] = t[i-1][j]

    return t[n][W]

print(knapsack(wt, val, W))