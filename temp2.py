#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

def searchSuggestions(repository, customerQuery):
    repository = [word.lower() for word in repository]
    repository = repository.sort()
    customerQuery = customerQuery.lower()
    length = len(customerQuery)

    if length < 2:
        return [[]]

    list1 = []
    output = []
    for i in range(2, length):
        searchQuery = customerQuery[0:i]

        for word in repository:
            #get the list of words starts with searchQuery
            if word.startswith(searchQuery):
                list1.append(word)
            output.append(list1[0:3])

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()
