def LIS_length(nums):
    length = len(nums)
    # we created a table here
    dp = [[-1] * (length + 2) for i in range(length + 1)]
    return LIS_length_rec(nums, 0, -1, dp)


def LIS_length_rec(nums, curr, prev, dp):
    # base case
    # if 'curr' reaches the end of the array, return 0
    if curr == len(nums):
        return 0

    # if subproblem has already been solved, use the stored result
    if dp[curr][prev + 1] != -1:
        return dp[curr][prev + 1]

    # solve the first subproblem
    length = LIS_length_rec(nums, curr + 1, prev, dp)

    # solve the second subproblem
    if prev < 0 or nums[prev] < nums[curr]:
        length = max(length, 1 + LIS_length_rec(nums, curr + 1, curr, dp))

    dp[curr][prev + 1] = length  # store the result of the current subproblem
    return dp[curr][prev + 1]


# driver code
def main():
    lists = [[1,3,2]]
    # lists = [[10, 9, 2, 5, 3, 7, 101, 18], [7, 7, 7, 7, 7, 7, 7], [0, 1, 0, 3, 2, 3],
    #          [3, 2], [6, 9, 8, 2, 3, 5, 1, 4, 7], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
    #          [9, 2, 5, 3, 6, 14, 11, 7, 9, 5, 13, 3, 15, 0, 8, 4, 1, 9, 5, 13, 3, 11, 7, 15, 0, 10, 6, 14, 9, 2, 5, 3,
    #           2, 10, 6, 10, 6, 5, 13, 3, 11, 7, 15, 3, 11, 7, 15]]

    # Let's uncomment this and check the effect of dynamic programming using memoization

    # lists.append([72, 56, 13, 33, 4, 5, 53, 14, 71, 42, 5, 74, 60, 15, 68, 42,
    # 56, 58, 67, 32, 65, 75, 47, 29, 86, 32, 77, 39, 19, 54, 54, 18, 49, 34,
    # 89, 85, 63, 86, 90, 53, 35, 2, 65, 63, 90, 26, 39, 41, 38, 32, 21, 35, 51,
    # 34, 50, 27, 51, 94, 70, 94, 18, 89, 45, 40, 13, 56, 25, 59, 51, 6, 59, 56,
    # 41, 44, 23, 26, 83, 8, 0, 33, 59, 43, 83, 40, 24, 86, 28, 2, 23, 87, 11,
    # 23, 13, 48, 20, 64, 21, 93, 8, 70, 33, 48, 10, 29, 24, 59, 92, 23, 67, 79,
    # 54, 7, 56, 5, 2, 63, 88, 58, 60, 95])

    for i, input_list in enumerate(lists):
        print(i + 1, ". Input array: ", input_list, sep="")
        print("Length of LIS is:", LIS_length(input_list))
        print("-" * 100)


if __name__ == '__main__':
    main()