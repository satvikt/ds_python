def combination_util(arr, n, r, data, index, i):
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    if i >= n:
        return

    data[index] = arr[i]
    combination_util(arr, n, r, data, index+1, i+1)

    while i < n-1 and arr[i+1] == arr[i]:
        i += 1

    combination_util(arr, n, r, data, index, i+1)



def printCombination(arr, n, r):
    data = [0] * r
    index = 0
    i = 0
    combination_util(arr, n, r, data, index, i)


if __name__ == "__main__":
    # Driver Code
    arr = [1, 2, 3, 4, 5];
    r = 3;
    n = len(arr);
    printCombination(arr, n, r);