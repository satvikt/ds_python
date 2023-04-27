import math


def smallest_substring_with_k_distinct(arr, k):
    i, j = 0, 0
    char_count = dict()
    min_size = math.inf

    while j < len(arr):
        if arr[j] in char_count:
            char_count[arr[j]] += 1
        else:
            char_count[arr[j]] = 1

        if len(char_count) < k:
            pass
        elif len(char_count) == k:
            min_size = min(min_size, j-i+1)
        elif len(char_count) > k:
            while len(char_count) > k:
                char_count[arr[i]] -= 1
                if char_count[arr[i]] == 0:
                    char_count.pop(arr[i])
                i += 1
        j += 1

    return min_size

def main():
    print("Length of thed longest substring: " + str(smallest_substring_with_k_distinct("araacc", 2)))
    # print("Length of the longest substring: " + str(smallest_substring_with_k_distinct("araaci", 1)))
    # print("Length of the longest substring: " + str(smallest_substring_with_k_distinct("cbbebi", 3)))


main()