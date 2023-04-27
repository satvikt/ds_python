# Driver to test above code
def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """

    # Empty dictionary which holds subsets of all anagrams together
    dictionary = {}

    # traversing all the lst strings
    for string in lst:
        key = "".join(sorted(string))
        if key in dictionary:
            dictionary[key].append(string)
        else:
            dictionary[key] = []
            dictionary[key].append(string)

    final = []

    for value in dictionary.values():
        if len(value) > 1:
            final.append(value)

    return final


if __name__ == '__main__':
    lst = ['tom marvolo riddle ', 'abc', 'def', 'cab', 'fed', 'clint eastwood ', 'i am lord voldemort', 'elvis',
           'old west action', 'lives']
    print(anagrams(lst))


"""
Sorting one word takes O(klogk) time in the average case using quick sort (where k is the length of the longest word in the given list), so, sorting 
n  words would take O(n×klogk). The rest of the operations use hashing which is all in constant time and therefore, doesn’t count.
"""