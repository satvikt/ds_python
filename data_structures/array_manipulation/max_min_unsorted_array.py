def find_min_max(arr):
    start = 0
    end = len(arr)-1

    min = arr[start]
    max = arr[end]

    while start < end:
        if arr[start] < min:
            min = arr[start]
        start += 1
        if arr[end] > max:
            max = arr[end]



if __name__ == "__main__" :

    arr = [ 3, 5, 2, 4, 9, 3,
            1, 7, 3, 11, 12, 3, 5, 4]
    # x, k = 3, 3
    # n = len(arr)

    print(find_min_max(arr))