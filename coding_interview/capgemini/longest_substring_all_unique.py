import math


def longest_substring_with_all_distinct(string):
    max_len = -math.inf
    count = {}
    i, j = 0, 0
    n = len(string)
    curr_sum = 0
    while j < n:
        if string[j] in count:
            count[string[j]] += 1
        else:
            count[string[j]] = 1

        if len(count) < j-i + 1:
            while len(count) < j-i + 1:
                count[string[i]] -= 1
                if count[string[i]] == 0:
                    del count[string[i]]

                i += 1

        elif len(count) == j-i + 1:
            max_len = max(max_len, j-i+1)

        j += 1

    return max_len

def main():
    print("Length of the longest substring: " + str(longest_substring_with_all_distinct("araaci")))


main()