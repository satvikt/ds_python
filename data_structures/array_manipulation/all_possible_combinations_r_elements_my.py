def combination_util(arr, n, r, data, index, i):
    if index == r:
        for i in data:
            print(i, end=" ")
        print()
        return

    if i >= n:
        return

    data[index] = arr[i]
    combination_util(arr, n, r, data, index + 1, i + 1)

    while i+1<n and arr[i] == arr[i+1]:
        # print(i)
        i += 1
        if i == n:
            break

    combination_util(arr, n, r, data, index, i + 1)


def printCombination(arr, n, r):
    data = [0 for x in range(r)]
    index = 0
    i = 0

    #for handling duplicates, sort the array
    arr.sort()

    combination_util(arr, n, r, data, index, i)

if __name__ == "__main__":
    arr = [1, 2, 1, 4, 5]
    r = 3
    n = len(arr)
    count = 0
    printCombination(arr, n, r)
