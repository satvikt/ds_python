import math


def longest_substring_with_k_distinct(string, k):
    i, j= 0, 0
    max_len = -math.inf

    char_dict = {}

    while j < len(string):
        if string[j] in char_dict:
            char_dict[string[j]] += 1
        else:
            char_dict[string[j]] = 1

        if len(char_dict) < k:
            pass
        elif len(char_dict) == k:
            max_len = max(max_len, j-i+1)
        else:
            # no need to use a while here. len(char_dict) can exceed k by only 1, i.e., can reach k+1 max
            # as we are checking it at each char of given string
            char_dict[string[i]] -= 1
            if char_dict[string[i]] == 0:
                char_dict.pop(string[i])
            i += 1
        j += 1

    return max_len
def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()