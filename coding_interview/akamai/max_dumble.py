"""
Variation of knapsack. Given an array of non-negative integers and a max_capacity, select such combination from array, so as to
1. Maximize the sum
2. Should be less than or equal to max_capacity
"""


def solve_knapsack(weights, max_capacity):
    n = len(weights)

    if n == 0 or max_capacity == 0:
        return 0

    if weights[n-1] <= max_capacity:
        chosen = weights[n-1] + solve_knapsack(weights[:n-1], max_capacity - weights[n-1])
        not_chosen = solve_knapsack(weights[:n-1], max_capacity)

        return max(chosen, not_chosen)

    return solve_knapsack(weights[:n-1], max_capacity)




def main():
    print(solve_knapsack([1, 3, 5], 7))
    print(solve_knapsack([1, 4, 9], 11))


main()