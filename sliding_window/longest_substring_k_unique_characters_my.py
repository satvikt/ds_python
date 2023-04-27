from math import inf


def longest_substring_with_k_distinct(string, k):
    i, j = 0, 0
    max_len = -inf
    char_dict = dict()

    while j < len(string):
        if string[j] not in char_dict:
            char_dict[string[j]] = 1
        else:
            char_dict[string[j]] += 1

        if len(char_dict) > k:
            while len(char_dict) > k:
                char_dict[string[i]] -= 1
                # if will certainly turn to 0 before -1, and we immediately delete the char when the count becomes 0
                # so no need to check for -1 here
                if char_dict[string[i]] == 0:
                    char_dict.pop(string[i])
                i += 1
        if len(char_dict) == k:
            max_len = max(max_len, j-i+1)

        j += 1
    return max_len



def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()