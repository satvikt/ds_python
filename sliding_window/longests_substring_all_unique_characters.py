import math


def longest_substring_with_all_distinct(arr):
    max_size = -math.inf
    i,j = 0,0
    char_dict = dict()

    while j < len(arr):
        if arr[j] in char_dict:
            char_dict[arr[j]] += 1

        else:
            char_dict[arr[j]] = 1
        # this condition can only arrive if there are repeated characters in range j-i+1
        # OR, the frequency of a char in char_dict > 1
        if len(char_dict) < j-i+1:
            while len(char_dict) < j-i+1:
                char_dict[arr[i]] -= 1
                if char_dict[arr[i]] == 0:
                    char_dict.pop(arr[i])
                i += 1
        elif len(char_dict) == j-i+1:
            max_size = max(max_size, j-i+1)
        j += 1
    return len(char_dict)



def main():
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("araaci")))
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("arevali")))
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("cbbebi")))


main()