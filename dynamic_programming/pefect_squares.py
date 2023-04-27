from math import sqrt
def perfect_squares(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # set to arbitrarily high value, 10000 was chosen here but one only needs a sufficiently large value
    dp = [10000] * (n + 1)
    dp[0] = 0
    # we only need to loop up to the square root of the number so we don't exceed it
    for i in range (1, int(sqrt(n)) + 1):
        cur = i*i
        # loop forwards so we can count reusing a number multiple times
        for j in range (cur, n + 1):
            dp[j] = min(dp[j], dp[j - cur] + 1)
    return dp[n]
if __name__ == '__main__':
    n = 13
    res = perfect_squares(n)
    print(res)