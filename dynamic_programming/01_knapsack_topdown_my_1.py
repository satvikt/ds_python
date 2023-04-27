def knapsack(val, wt, W, n, t):
    for i in range(n+1):
        for j in range(W+1):
            if i ==0 or j ==0 :
                t[i][j] =0
            else:
                if wt[i-1] <= j:
                    chosen = val[i-1] + t[i-1][j - wt[i-1]]
                    not_chosen = t[i-1][j]
                    t[i][j] = max(chosen, not_chosen)
                else:
                    t[i][j] = t[i-1][j]

    return t[n][W]



def solve_knapsack(val, wt, W):
    n = len(wt)
    t = [[-1 for x in range(W+1)] for x in range(n+1)]
    return knapsack(val, wt, W, n, t)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()