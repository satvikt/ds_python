import math


def largest_subarray_with_given_sum(sum, arr):
    max_len = -math.inf
    win_sum = 0
    i, j = 0,0

    while j < len(arr):
        win_sum = win_sum + arr[j]

        if win_sum > sum:
            while win_sum > sum:
                win_sum -= arr[i]
                i += 1
        # Writing the below equality case, above the win_sum>k case + in an 'elif' statement will lead to missing out
        # on the case when subarray [5,2] and sum = 7, because we'll blindly take the add the
        # next element (8) without waiting and checking for the existing subarray [5,2] after the
        # previous element (1) has been removed

        # also, writing the following equals case above the greater than (>)) case would lead to the same mistake
        # as in coding_interview/capgemini/largest_subarray_given_sum.py
        if win_sum == sum:
            max_len = max(max_len, j-i+1)

        j += 1
    return max_len

def main():
    # print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()