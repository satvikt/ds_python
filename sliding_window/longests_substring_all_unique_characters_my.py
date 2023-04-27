import math


def longest_substring_with_all_distinct(string):
    i, j= 0, 0
    max_len = -math.inf

    char_dict = {}

    while j < len(string):
        if string[j] in char_dict:
            char_dict[string[j]] += 1
        else:
            char_dict[string[j]] = 1

        if len(char_dict) < j-i+1:
            while len(char_dict) < j-i+1:
                char_dict[string[i]] -= 1
                if char_dict[string[i]] == 0:
                    char_dict.pop(string[i])
                i += 1
        elif len(char_dict) == j-i+1:
            max_len = max(max_len, j-i+1)
        # below condition: len(char_dict) > j-i+1, is not possible. as this tells  as the number of unique chars in the
        # dict is more than the total chars in the substring. LOL
        j += 1

    return max_len
def main():
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("araaci")))
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("arevali")))
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("cbbebi")))

main()