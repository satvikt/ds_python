def countWaysUtil(n, m):
    # this is not recursive code where we will return anything. This is iterative code.
    # to initialize here, we need to initialize the res itself.
    # if n <= 1:
    #     return n
    res = [0 for i in range(n)]
    res[0] = 1
    res[1] = 1


    for i in range(2, n):
        j = 1
        while j<=i and j<=m:
            res[i] += res[i-j]
            j += 1
    return res[n-1]

# Returns number of ways to reach s'th stair
def countWays(s, m):
    return countWaysUtil(s + 1, m)

if __name__ == '__main__':
    # Driver Program
    s, m = 4, 2
    print("Number of ways =", countWays(s, m))