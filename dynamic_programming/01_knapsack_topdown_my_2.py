def knapsack(wt, val, W):
    n = len(wt)
    t = [[0 for i in range(W+1)] for j in range(n + 1)]
    for i in range(1, n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            # i at line 9 must start with 1 so that wt[i-1] calculates to wt[0]
            # FIXME: WRONG ASSUMPTION ABOVE
            elif wt[i-1] <= j:
                chosen = val[i-1] + t[i-1][j-wt[i-1]]
                not_chosen = t[i-1][j]

                t[i][j] = max(chosen, not_chosen)
            else:
                t[i][j] = t[i-1][j]

    return t[n][W]


def main():
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()
