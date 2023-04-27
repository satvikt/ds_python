# Python3 program to Rearrange positive
# and negative numbers in an array

# Function to print an array
def printArray(A, size):

    for i in range(0, size):
        print(A[i], end = " ")
    print()

# Function to reverse an array. An array can
# be reversed in O(n) time and O(1) space.

def reverse(arr, l, r):
    if l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        reverse(arr, l, r)

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    while i <= mid and arr[i] < 0:
        i += 1

    while j <= right and arr[j] < 0:
        j += 1

    reverse(arr, i, mid)
    reverse(arr, mid +1, j -1)
    reverse(arr, i, j-1)


def RearrangePosNeg(arr, left, right):
    if left < right:
        mid = left + (right - left) //2

        RearrangePosNeg(arr, left, mid)
        RearrangePosNeg(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == "__main__":

    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)

    RearrangePosNeg(arr, 0, arr_size - 1)

    printArray(arr, arr_size)

    # This code is contributed by Rituraj Jain