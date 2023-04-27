import unittest
from collections import Counter
from math import inf


# def printNonrepeated(string):
#     freq = Counter(string)
#
#     for i in string:
#         if freq[i] == 1:
#             print(i)
#             break

def firstNonRepeating(string):
    arr = [-1] * 256

    for i in range(len(string)):
        if arr[ord(string[i])] == -1:
            arr[ord(string[i])] = i
        else:
            arr[ord(string[i])] = -2

    min_index = inf
    for i in range(len(arr)):
        if arr[i] > 0:
            min_index = min(min_index, arr[i])

    return string[min_index]

if __name__ == "__main__":
    # Driver code
    string = "geeksforgeeks"

    # passing string to printNonrepeated function
    # printNonrepeated(string)
    print("First non-repeating character: ", firstNonRepeating(string))