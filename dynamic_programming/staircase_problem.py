def staircase_ways(n):
    if n == 0 or n == 1:
        return 1
    return staircase_ways(n-1) + staircase_ways(n-1)


def staircase_ways_X(n, possible_steps):
    pass


if __name__ == '__main__':
    n = 6
    print(f"Number of ways for {n} steps - {staircase_ways(n)}")
    possible_steps = [1,3,5]
    print(f"Number of ways for {n} steps - {staircase_ways_X(n,possible_steps)}")
