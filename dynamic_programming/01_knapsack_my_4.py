def knapsack_rec(wt, val, W, n):
    if n==0 or W==0:
        return 0
    elif wt[n-1] <= W:
        chosen = val[n-1] + knapsack_rec(wt, val, W - wt[n-1], n-1)
        not_chosen = knapsack_rec(wt, val, W, n-1)
        return max(chosen, not_chosen)
    else:
        return knapsack_rec(wt, val, W, n-1)


def solve_knapsack(profits, weights, capacity):
    size = len(weights)
    return knapsack_rec(weights, profits, capacity, size)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()