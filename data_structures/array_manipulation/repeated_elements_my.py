arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)


def printRepeating(arr, arr_size):
    print("The repeating elements are ")

    for i in range(arr_size):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")




printRepeating(arr, arr_size)