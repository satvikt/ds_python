from math import inf


def smallest_subarray_with_given_sum(sum, arr):
    min_len = inf
    win_sum = 0
    length = len(arr)
    i, j = 0, 0

    while j < length:
        win_sum += arr[j]

        if win_sum > sum:
            while win_sum > sum:
                win_sum -= arr[i]
                i += 1
        if win_sum == sum:
            min_len = min(min_len, j-i+1)

        j += 1

    return min_len

def main():
    # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 3, 8, -1])))
    # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
