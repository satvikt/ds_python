def printCombinationUtil(arr, res, temp, n, left, k):
    if k == 0:
        res.append(temp[:])
        return

    for i in range(left, n):
        temp.append(arr[i])
        printCombinationUtil(arr, res, temp, n, i+1, k-1)
        temp.pop()



def printCombination(arr, k):
    res = []
    temp = []
    n = len(arr)

    printCombinationUtil(arr, res, temp, n,0, k)

    return res
    


if __name__ == "__main__":
    arr = [1, 2, 1, 4, 5]
    r = 3
    n = len(arr)
    count = 0
    print(printCombination(arr, r))
