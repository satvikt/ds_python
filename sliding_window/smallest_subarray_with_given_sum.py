import math


def smallest_subarray_with_given_sum(sum, arr):

    # Remember that irrespective of whether it's a variable window problem (smallest/largest subarray of sum k)
    # or fixed window problem (largest/smallest sum of window size k) the sub-optimal condition or while loop
    # will be placed at the top

    min_size = math.inf
    window_sum = 0
    i, j = 0, 0

    while j < len(arr):
        window_sum += arr[j]

        if window_sum > sum:
            while window_sum > sum:
                window_sum -= arr[i]

                i += 1
        if window_sum == sum:
            min_size = min(min_size, j-i+1)
        j += 1

    return min_size


def main():
    print("Largest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    # print("Largest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    # print("Largest subarray length: " + str(largest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()