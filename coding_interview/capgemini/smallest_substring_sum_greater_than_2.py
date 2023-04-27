import math


def smallestSubWithSum(arr1, n1, x):
    min_len = math.inf
    i, j = 0, 0
    curr_sum = 0
    while j < n1:
        while curr_sum <= x and j < n1:
            curr_sum += arr1[j]
            j += 1
        while curr_sum > x and i < n1:
            min_len = min(min_len, j-i)
            curr_sum -= arr1[i]

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