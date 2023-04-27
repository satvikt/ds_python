"""
Given an array of integers, find the 2nd largest number.
Constraints:

0. Positive integers
1. Unsorted array
2. Repetitions allowed -> (In case of array like [2,2,2], return -1 as we have a single element)
3. Complexity should be < O(nlogn) -> Can't sort it.

"""


def second_largest_my(arr):
    # largest = arr[0]
    second_highest = 0
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            # largest = max(arr[i-1], arr[i])
            second_highest = min(arr[i-1], arr[i])
    print(-1 if second_highest == 0 else second_highest)
    return -1 if second_highest == 0 else second_highest


def second_largest(arr):
    first = second = -1
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        # lies between first and second
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    print(second)
    return second


if __name__ == "__main__":
    second_largest([1,1,5,2,3,5,4]) # 2
    # second_largest([1,1,1]) # -1
    # second_largest_my([1,1,2,3,5,4]) # 2
    # second_largest_my([1,1,1]) # -1