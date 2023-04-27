def knapsack_memoize(val, wt, W, n, t):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # if wt[n-]


def solve_knapsack(val, wt, W):
    size = len(wt)
    t = [[-1 for j in range(W)] for i in range(size)]
    return knapsack_memoize(val, wt, W, size, t)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()