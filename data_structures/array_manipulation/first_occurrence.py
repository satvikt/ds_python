def first_occurrence(arr, start, end, item):
    mid = start + (end-start)//2

    if item > arr[mid]:
        return first_occurrence(arr, mid+1,end, item)
    elif item < arr[mid]:
        return first_occurrence(arr, start, mid-1, item)
    # if item is the first element
    #OR
    # mid's the first occurrence of the item. We can confirm it by checking with mid-1, since it's a sorted array
    if (mid ==0 and arr[mid]==item) or (arr[mid-1] < item and arr[mid] == item):
        return mid
    elif item > arr[mid]:
        return first_occurrence(arr, mid+1,end, item)
    else: #we need to recur with modified end till the top condition becomes true
        # (we either)
        return first_occurrence(arr, start, mid-1, item)

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 3, 4, 8, 9, 11, 33]
    item = 3

    print(first_occurrence(arr, 0, len(arr)-1, item))