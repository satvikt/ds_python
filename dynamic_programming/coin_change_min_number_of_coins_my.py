
infi = 1000000
def coin_change(coins, sum):

    n = len(coins)
    num = [[-1]*(sum + 1) for i in range(n+1)]


    for j in range(sum+1):
        num[0][j] = infi

    for i in range(n+1):
        num[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if coins[i-1] <= j:
                chosen = 1+ num[i][j - coins[i-1]]
                not_chosen = num[i-1][j]
                num[i][j] = min(chosen, not_chosen)

            else:
                num[i][j] = num[i-1][j]

    return num[n][sum]


if __name__ == '__main__':
    # coins = [9, 6, 5, 1]
    # coins = [6,5,3,9]
    # sum = 11
    coins = [1,2,3]
    sum = 3

    print(coin_change(coins, sum))
