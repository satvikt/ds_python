def dfs(string, curr, used, res):
    if len(curr) == len(string):
        res.append(curr[:])
        return

    for i, letter in enumerate(string):
        if used[i]:
            continue

        curr.append(letter)
        used[i] = True

        dfs(string, curr, used, res)

        curr.pop()
        used[i] = False




def permutations(string):
    res = []
    used = [False] * len(string)
    curr = []
    dfs(string, curr, used, res)
    return res



if __name__ == "__main__":
    res = permutations(list(input()))
    print(' '.join(sorted(''.join(x) for x in res)))