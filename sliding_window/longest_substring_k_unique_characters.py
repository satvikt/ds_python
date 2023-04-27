import math


def longest_substring_with_k_distinct(string, k):
    max_size = -math.inf
    i, j = 0, 0
    char_count = dict()

    while j < len(string):
        if string[j] not in char_count:
            char_count[string[j]] = 1
        else:
            char_count[string[j]] += 1
        if len(char_count) < k:
            pass
        elif len(char_count) == k:
            max_size = max(max_size,j-i+1)
        else:
            while len(char_count) > k:
                char_count[string[i]] -= 1
                if char_count[string[i]] == 0:
                    char_count.pop(string[i])
                i += 1
        j += 1

    return max_size




def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()