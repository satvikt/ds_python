import math


def smallest_subarray_with_given_sum(sum, arr):
    min_len = math.inf
    window_sum = 0
    length = len(arr)
    i, j = 0, 0

    while j < length:
        window_sum += arr[j]

        if window_sum == sum:
            min_len = min(min_len, j - i + 1)
        if window_sum > sum:
            while window_sum > sum:
                window_sum -= arr[i]
                i += 1

        j += 1

    return min_len

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()