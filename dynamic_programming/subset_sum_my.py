def subset_sum(arr, sum):
    n = len(arr)
    t = [[False for j in range(sum+1)] for i in range(n+1)]

    for j in range(sum+1):
        t[0][j] = False
    # Remember the True assignment has to be done AFTER the False assignment
    for i in range(n+1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            # NOTE: can't achieve initialization here as the ELSE part below when arrpi-1] > j,
            # will overwrite the initializatio

            # if i==0:
            #     t[i][j] = False
            # elif j==0:
            #     t[i][j] = True
            #     t[0][0] = True
            # Making the input shorter
            if arr[i-1] <= j:
                chosen = t[i-1][j-arr[i-1]]
                not_chosen = t[i-1][j]
                t[i][j] = chosen or not_chosen

            else:
                t[i][j] = t[i-1][j]

    return t[n][sum]


if __name__ == "__main__":
    print(subset_sum([1, 2, 3, 5], 7))
