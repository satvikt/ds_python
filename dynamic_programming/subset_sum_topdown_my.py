def subset(arr, sum, n, t):
    for j in range(sum+1):
        t[0][j] = False
    for i in range(n+1):
        t[i][0] = True
    for i in range(n+1):
        for j in range(sum+1):
            # if i == 0:
            #     t[i][j] = False
            # if j == 0:
            #     t[i][j] = True
            if arr[i-1] <= j:
                chosen = t[i-1][j-arr[i-1]]
                not_chosen = t[i-1][j]
                t[i][j] = chosen or not_chosen
            else:
                t[i][j] = t[i-1][j]

    return t[n][sum]



def subset_sum(arr, sum):
    n = len(arr)
    t = [[False for x in range(sum+1)] for x in range(n+1)]
    return subset(arr, sum, n, t)


if __name__ == "__main__":
        print(subset_sum([1, 2, 3, 5], 7))
    # print(subset_sum([1, 2, 3], 5))
