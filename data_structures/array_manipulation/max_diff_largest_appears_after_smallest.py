def maxDiff(arr, size):
    # if array is sorted
    #
    max_diff = 0
    min_element = arr[0]

    for i in range(1,size):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element

        if min_element > arr[i]:
            min_element = arr[i]

    return max_diff


if __name__ == "__main__":
    arr = [2, 1, 6, 80, 100, 85]
    size = len(arr)
    print ("Maximum difference is",
           maxDiff(arr, size))