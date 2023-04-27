# Driver Code
def maxDiff(arr, n):
    diff = arr[1] - arr[0]
    curr_sum = diff
    max_sum = curr_sum

    for i in range(1, n-1):
        diff = arr[i+1] - arr[i]

        if curr_sum > 0:
            curr_sum += diff
        else:
            curr_sum = diff

        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    arr = [80, 2, 6, 3, 100]
    n = len(arr)

    # Function calling
    print("Maximum difference is",
          maxDiff(arr, n))
