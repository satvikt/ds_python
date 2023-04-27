
def knapsack_memoize(wt, val, W, n, t):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    if wt[n-1] <= W:
        chosen = val[n-1] + knapsack_memoize(wt, val, W - wt[n-1], n-1, t)
        not_chosen = knapsack_memoize(wt, val, W, n-1, t)
        t[n][W] = max(chosen, not_chosen)

    elif wt[n-1] > W:
        t[n][W] = knapsack_memoize(wt, val, W, n-1, t)

    return t[n][W]


def solve_knapsack(val, wt, W):
    size = len(wt)
    t = [[-1 for x in range(W+1)] for x in range(size+1)]
    # for i in range(size):
    #     t[]
    return knapsack_memoize(wt, val, W, size, t)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()