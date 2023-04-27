def permutations(arr):
    def dfs(path, used, res):
        if len(arr) == len(path):
            res.append(path[:])
            return
        for i, char in enumerate(arr):
            if used[i]:
                continue

            path.append(char)
            used[i] = True

            dfs(path, used, res)

            path.pop()
            used[i] = False

    res = []
    dfs([], [False]*len(arr), res)
    return res

if __name__ == "__main__":
    res = permutations(list(input()))
    print(' '.join(sorted(''.join(x) for x in res)))