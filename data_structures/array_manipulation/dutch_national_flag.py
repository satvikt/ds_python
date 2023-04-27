def dutch_national_flag(arr):
    # i,j,k = 0,0,0
    low = 0
    i = 0
    high = len(arr) - 1

    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
            # Don't increment mid as we didn't process this element arr[high] which now resides at mid.           # Incrementing mid here will cause the arr[mid] to be skipped
            # mid += 1
    return arr

if __name__ == "__main__":
    arr = [0,1,1,0,1,1,1,0]
    arr1 = [0, 1, 2, 0, 1, 2]
    arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    arr3 = [2,2,1,1,0]
    print(dutch_national_flag(arr3))
    # print(arr)