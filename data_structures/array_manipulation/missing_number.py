# a represents the array
# n : Number of elements in array a
def getMissingNo(a, n):
    i, total = 0, 1

    for i in range(4, n + 4):
        total += i
        total -= a[i - 4]
    return total

# Driver Code
arr = [5,2,3,1]
print(getMissingNo(arr, len(arr)))

# This code is contributed by Mohit kumar
