from math import inf


def largest_subarray_with_given_sum(sum, arr):
    i, j = 0, 0
    max_len = -inf
    win_sum = 0

    while j < len(arr):
        win_sum += arr[j]

        if win_sum > sum:
            while win_sum > sum:
                win_sum -= arr[i]
                i += 1
        if win_sum == sum:
            max_len = max(max_len, j-i+1)

        j += 1
    return max_len



def main():
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()