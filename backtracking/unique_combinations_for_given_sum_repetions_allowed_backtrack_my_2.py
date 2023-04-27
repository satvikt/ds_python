def combination(arr, sum):
    output = []
    def dfs(temp, remain, start):
        if remain <0:
            return
        if remain == 0:
            output.append(temp[:])
            return
        else:
            for i in range(start, len(arr)):
                temp.append(arr[i])
                dfs(temp, remain - arr[i], i)
                temp.pop()
    dfs([], sum, 0)
    return output




if __name__ == "__main__":
    arr = [1,2,3]
    sum = 4
    print(combination(arr, sum))