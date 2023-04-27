


def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1

    mid = int(low + (high-low)/2)

    while low <= high:
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = mid = int(low + (high-low)/2)

    if low < len(arr) and arr[low] == key:
        return low
    return -1


def find_high_index(arr, low, key):
    high = len(arr) - 1
    mid = mid = int(low + (high-low)/2)

    while low <= high:
        # <= is the key here
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1

        mid = mid = int(low + (high-low)/2)

    if high == -1:
        return -1

    if high < len(arr) and arr[high] == key:
        return high

    return -1

array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
key = 5
low = find_low_index(array, key)
high = find_high_index(array, low, key)
print("Low Index of " + str(key) + ": " + str(low))
print("High Index of " + str(key) + ": " + str(high))

"""
Runtime complexity
Since we are using binary search, the runtime complexity is logarithmic, O(logn).
    
Memory complexity
The memory complexity is constant, O(1) since no extra storage is being used.


"""