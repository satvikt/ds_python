def knapsack_rec(val, wt, W, n):
    if n==0 or W==0:
        return 0

    if wt[n-1] <= W:
        chosen = val[n-1] + knapsack_rec(val, wt, W-wt[n-1], n-1)
        not_chosen = knapsack_rec(val, wt, W, n-1)

        return max(chosen, not_chosen)

    return knapsack_rec(val, wt, W, n-1)


def solve_knapsack(val, wt, W):
    n = len(val)
    return knapsack_rec(val, wt, W, n)


def main():
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()