def combination(arr, sum):
    lis = []
    arr = list(sorted(arr))
    def dfs(lis, temp, arr, remain, start):
        if remain < 0:
            return
        elif remain ==0:
            lis.append(temp[:])
        else:
            for i in range(start, len(arr)):
                temp.append(arr[i])
                dfs(lis, temp, arr, remain - arr[i], i) # not i+1 since repetitions allowd
                temp.pop()

    dfs(lis, [], arr, sum, 0)
    return lis

if __name__ == "__main__":
    arr = [1,2]
    sum = 4
    print(combination(arr, sum))