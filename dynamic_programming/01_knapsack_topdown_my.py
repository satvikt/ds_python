val =[1, 6, 10, 16]
wt = [1, 2, 3, 5]
W = 7
n = len(val)


t = [[0 for j in range(W + 1)] for i in range(n + 1)]


def knapsack(wt, val, W, n):
    for i in range(0, n+1):
        for j in range(0, W +1):
            if wt[i-1] <= j:
                chosen = val[i-1] + t[i-1][j - wt[i-1]]
                not_chosen = t[i-1][j]

                # the row indices in matrix correspond to an index lower in wt/val array
                # not column index will always be j, corresponding to actual index of weight in W arr
                t[i][j] = max(chosen, not_chosen)
            else:
                t[i][j] = t[i-1][j]

    return t[n][W]



print(knapsack(wt, val, W, n))