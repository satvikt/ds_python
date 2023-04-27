def rearrange(arr, length):
    arr.sort()

    i, j = 1, 1
    while(arr[j] < 0):
        j += 1

    while arr[i] < 0 and j < length:
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1

    return arr


if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

    ans = rearrange(arr, len(arr))
    for num in ans:
        print(num, end = " ")