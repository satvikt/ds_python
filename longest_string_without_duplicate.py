import math
def longest(string):
    max_size = -math.inf
    n = len(string)
    word_count = {}
    i, j = 0, 0

    while j < n:
        if string[j] in word_count:
            word_count[string[j]] += 1
        else:
            word_count[string[j]] = 1

        if j-i + 1 > len(word_count):
            while j-i + 1 > len(word_count):
                word_count[string[i]] -= 1
                if word_count[string[i]] == 0:
                    word_count.pop(string[i])
                i += 1
        elif j-i+1 == len(word_count):
           max_size = max(max_size, len(word_count))

        j += 1
    return max_size


if __name__ == "__main__":
    string = "abccabcabcc"
    print(longest(string))