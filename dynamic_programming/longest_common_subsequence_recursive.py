def lcs(X, Y, n, m):
    # Base condition
    if n == 0 or m == 0:
        return 0

    # Choice diagramN
    if X[n-1] == Y[n-1]:
        return 1 + lcs(X, Y, n-1, m-1)

    else:
        choice1 = lcs(X, Y, n, m-1)
        choice2 = lcs(X, Y, n-1, m)
        return max(choice1, choice2)


if __name__ == "__main__":
    X = 'abcdgh'
    Y = 'abedfhr'
    n = len(X)
    m = len(Y)

    print(lcs(X, Y, n, m))
