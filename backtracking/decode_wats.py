def decode_ways(digits):
    # use numbers 1 to 26 to represent all alphabet letters
    prefixes = [str(i) for i in range(1, 27)]

    def dfs(i):
        if i == len(digits):
            return 1

        ways = 0
        remaining = digits[i:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                ways += dfs(i + len(prefix)) # add number of ways returned from child node

        return ways

    return dfs(0)

if __name__ == '__main__':
    print(decode_ways("123"))