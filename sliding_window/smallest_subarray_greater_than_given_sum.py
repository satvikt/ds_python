import math


def smallestSubWithSum(arr, n1, x):
    min_len = math.inf
    i, j = 0, 0
    curr_sum = 0
    while (j < n1):
        # A little different from the usual sliding window
        while curr_sum <= x and j < n1:
            # 1. instead of an if clause, we have a while, till we reach curr_sum>x
            # 2. Instead of having curr_sum outside, we have it inside this condition
            # this is because we only want to update curr_sum if < x, and not in every case
            # (which it shall be, if outside.
            # E.g. for arr = [1, 4, 45, 6, 10, 19], x=51 the first counting point is when
            # i=0, j=3, arr under consid = [1,4,45,6] and curr_sum = 56. Here min_len =4
            # A. If we allow the usual, i.e., j ++ and curr_sum outside, we will miss the case when
            # i=1, j=3, arr under consid = [4, 45, 6] and curr_sum = 55 where we have a
            # lower min_len = 3.
            # B. Instead, we shall have i=1, j=4 and subarr = [4, 45, 6, 10] curr_sum = 65
            # C. Also, this is the reason why we have the second cond in while loop as well, instead
            # of if. We want to keep incrementing i and subtracting, without incrementing j
            # till we have the condition curr_sum > x as valid.
            curr_sum += arr[j]
            j += 1
        while (curr_sum > x) and i < n1:
            min_len = min(min_len, j-i) # note that it is not (j-i+1) as j will already be 1
            # bigger than equired when it breaks out of previous while loop
            curr_sum -= arr[i]
            i += 1

    return min_len


if __name__ == "__main__":
    # Driver program to test above function */
    arr1 = [1, 4, 45, 6, 10, 19]
    x = 51
    n1 = len(arr1)
    res1 = smallestSubWithSum(arr1, n1, x);
    if res1 == n1+1:
        print("Not possible")
    else:
        print(res1)

    arr2 = [1, 10, 5, 2, 7]
    n2 = len(arr2)
    x = 9
    res2 = smallestSubWithSum(arr2, n2, x)
    print("Not possible") if (res2 == n2 + 1) else print(res2)

    arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    n3 = len(arr3)
    x = 280
    res3 = smallestSubWithSum(arr3, n3, x)
    print("Not possible") if (res3 == n3 + 1) else print(res3)