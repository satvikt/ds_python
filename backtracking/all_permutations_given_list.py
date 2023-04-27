def permutations(l):
    def dfs(path, used, res):
        if len(path) == 2:
            res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
            return
        for i, letter in enumerate(l):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False
    res = []
    dfs([], [False] * len(l), res)
    return res
if __name__ == "__main__":
    # res = permutations(list(input()))
    # print(' '.join(sorted(''.join(x) for x in res)))
    #
    res = permutations([1 ,2, 3])
    print(res)
