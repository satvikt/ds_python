def maxDiff(arr, size):
    diff_arr = [0]*size
    diff_arr[0] = arr[1] - arr[0]
    max_diff = diff_arr[0]
    for i in range(2, size):
        diff_arr[i-1] = arr[i] - arr[i-1]

    for i in range(1, size-1):
        if diff_arr[i-1] > 0:
            diff_arr[i] += diff_arr[i-1]

        if max_diff < diff_arr[i]:
            max_diff = diff_arr[i]

    return max_diff

def maxDiff2(arr, size):
    # diff_arr = [0]*size
    diff = arr[1] - arr[0]
    max_diff = diff
    # for i in range(2, size):
    #     diff_arr[i-1] = arr[i] - arr[i-1]

    for i in range(2, size):
        curr = arr[i] - arr[i-1]
        if curr > 0:
            diff += curr

        if max_diff < diff:
            max_diff = diff

    return max_diff

if __name__ == "__main__":
    arr = [80, 2, 6, 3, 100]
    size = len(arr)
    print ("Maximum difference is",
           maxDiff(arr, size))