def knapsack_memoize(wt, val, W, n, matrix):
    if n == 0 or W == 0:
        return 0
    if matrix[n][W] != -1:
        return matrix[n][W]

    if wt[n-1] > W:
        matrix[n][W] = knapsack_memoize(wt, val, W, n-1, matrix)
    else:
        chosen = val[n-1] + knapsack_memoize(wt, val,  W - wt[n-1], n-1, matrix)
        not_chosen = knapsack_memoize(wt, val, W, n-1, matrix)

        matrix[n][W] = max(chosen, not_chosen)

    return matrix[n][W]




def solve_knapsack(profits, weights, capacity):
    size = len(weights)
    matrix = [[-1 for i in range(capacity+1)] for j in range(size+1)]

    return knapsack_memoize(weights, profits, capacity, size, matrix)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

main()