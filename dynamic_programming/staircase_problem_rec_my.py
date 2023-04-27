def countWaysRecursive(n, m):
    if n<=1:
        return 1

    res = 0
    i = 1
    while i<=m and i<=n:
        res += countWaysRecursive(n-i, m)
        i += 1
    return res




def countWays(s, m):
    return countWaysRecursive(s+1, m)


if __name__ == '__main__':
    # Driver Program
    s, m = 4, 2
    print("Number of ways =", countWays(s, m))