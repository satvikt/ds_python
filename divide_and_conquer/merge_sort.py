
def mergesort(arr):
    # base case
    if len(arr) < 2:
        return arr
    mid = int(len(arr) / 2)
    # splitting array into two components, assume they are sorted recursively.
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    l, r, result = 0, 0, []
    # the merging (conquer) step, combining two cases to get the final result.
    while l < len(left) and r < len(right):
        if l >= len(left) or (r < len(right) and left[l] > right[r]) :
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    return result


if __name__ == "__main__":
    arr = [2,1,4,3]
    print(mergesort(arr))