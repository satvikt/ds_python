# Python3 program to count
# occurrences of an element

# if x is present in arr[] then
# returns the count of occurrences
# of x, otherwise returns -1.
def count(arr, x, n):

    # get the index of first
    # occurrence of x
    i = first(arr, 0, n-1, x, n)

    # If x doesn't exist in
    # arr[] then return -1
    if i == -1:
        return i

    # Else get the index of last occurrence
    # of x. Note that we are only looking
    # in the subarray after first occurrence
    j = last(arr, i, n-1, x, n);

    # return count
    return j-i+1;

# if x is present in arr[] then return
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1
def first(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high)//2
        # Its the first element in the array
        #OR
        # Its less than mid-1 element, plus, it is the mid element
        if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid -1), x, n)
    return -1;

# if x is present in arr[] then return
# the index of LAST occurrence of x
# in arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if high >= low:

        # low + (high - low)/2
        mid = (low + high)//2;
        # Its the last element in the array
        #OR
        # Its less than mid+1 element, plus, it is the mid element
        if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid -1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)
    return -1


if __name__ == "__main__":
    # driver program to test above functions
    arr = [1, 2, 2, 3, 3, 3, 3, 4, 8, 9, 11, 33]
    x = 2 # Element to be counted in arr[]
    n = len(arr)
    c = count(arr, x, n)
    print ("%d occurs %d times "%(x, c))
