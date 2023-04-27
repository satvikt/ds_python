def smallest_subarray_with_given_sum(sum, arr):
    i, j = 0, 0
    min_len, window_sum = 0, 0

    while j < len(arr):
        window_sum += arr[j]

        if window_sum < sum:
            j += 1
        elif window_sum == sum:
            min_len = min(min_len, j-i+1)
        else:
            while window_sum > sum:
                window_sum -= arr[i]
                i += 1

    # where the fuck do I increase `j` which shall terminate the loop?
    return min_len


def main():
    # print("The Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    # print("The Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()