# Python 3 code to find Maximum difference
# between two elements such that larger 
# element appears after the smaller number

def maxDiff(arr, n):
    diff = [0] * (n - 1)
    for i in range (0, n-1):
        diff[i] = arr[i+1] - arr[i]

    # Now find the maximum sum
    # subarray in diff array
    max_diff = diff[0]
    for i in range(1, n-1):
        if (diff[i-1] > 0):
            diff[i] += diff[i-1]

        if (max_diff < diff[i]):
            max_diff = diff[i]

    return max_diff

# Driver program to test above function 
arr = [80, 2, 6, 3, 100]
size = len(arr)
print ("Maximum difference is",
       maxDiff(arr, size))

# This code is contributed by Swetank Modi
