def lcs(X, Y):
    n = len(X)
    m = len(Y)

    T = [[None]*(m+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                T[i][j] = 0
            elif X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i][j-1],T[i-1][j])

    return T[n][m]


if __name__ == "__main__":
    X = 'abcdgh'
    Y = 'abedfhr'

    print(lcs(X, Y))
