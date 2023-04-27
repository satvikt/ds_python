# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
def binary_search(arr, low, high, ele):
    if len(arr) == 0:
        return -1

    if low <= high:
        mid = (high + low) // 2

        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            return binary_search(arr, low, mid-1, ele)
        else:
            return binary_search(arr, mid+1, high, ele)
    else:
        return -1

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")