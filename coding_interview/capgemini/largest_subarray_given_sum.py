import math


def largest_subarray_with_given_sum(sum, arr):
    n = len(arr)
    i, j = 0, 0
    curr_sum = 0
    max_len = -math.inf
    while j < n:
        curr_sum += arr[j]
        # if curr_sum < sum:
        #      pass
        if curr_sum == sum:
            max_len = max(max_len, j-i +1)
        elif curr_sum > sum:
            while curr_sum > sum:
                curr_sum -= arr[i]
                i +=1
        j += 1

    return max_len


def main():
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Largest subarray length: " + str(largest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    # print("Largest subarray length: " + str(largest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()