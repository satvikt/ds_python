import math

infi = 1000000
def coin_change(coins, sum):
    n = len(coins)

    t = [[-1 for i in range(sum+1)] for j in range(n+1)]
    t[0][0] = 0

    for i in range(sum+1):
        t[0][i] = infi

    for i in range(n+1):
        t[i][0] = 0
    # for i in range(1, sum+1):
    #     if i % coins[0] == 0:
    #         t[]

    for i in range(1, n+1):
        for j in range(1, sum+1):
            # if j % coins
            if coins[i-1] < j:
                chosen = 1 + t[i][j-coins[i-1]]
                not_chosen = t[i-1][j]
                t[i][j]= min(chosen, not_chosen)
            else:
                t[i][j] = t[i-1][j]

    return t[n][sum]

# coins = [9, 6, 5, 1]
coins = [6,5,3,9]
sum = 11

print(coin_change(coins, sum))
