def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0

    arr1.sort()
    arr2.sort()
    while i < m and j < n:
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            return 0
        else:
            i += 1
    return 1 if j == n else 0

if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1,3]
    m = len(arr1)
    n = len(arr2)
    if isSubset(arr1, arr2, m, n) == True:
        print("arr2 is subset of arr1 ")
    else:
        print("arr2 is not a subset of arr1 ")
