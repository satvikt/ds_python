# Python program to print all permutations with repetition
# of characters

def toString(List):
    return ''.join(List)

# The main function that recursively prints all repeated
# permutations of the given string. It uses data[] to store
# all permutations one by one
def allLexicographicRecur (string, data, last, index, lis):
    length = len(string)

    # One by one fix all characters at the given index and
    # recur for the subsequent indexes
    for i in range(length):

        # Fix the ith character at index and if this is not
        # the last index then recursively call for higher
        # indexes
        data[index] = string[i]

        # If this is the last index then print the string
        # stored in data[]
        if index==last:
            lis.append(toString(data))
        else:
            allLexicographicRecur(string, data, last, index+1, lis)

# This function sorts input string, allocate memory for data
# (needed for allLexicographicRecur()) and calls
# allLexicographicRecur() for printing all permutations
def allLexicographic(string):
    length = len(string)

    # Create a temp array that will be used by
    # allLexicographicRecur()
    data = [""] * (length+1)

    # Sort the input string so that we get all output strings in
    # lexicographically sorted order
    string = sorted(string)
    lis = []


    # Now print all permutations
    allLexicographicRecur(string, data, length-1, 0, lis)
    return lis

# Driver program to test the above functions
string = "AB"
print(allLexicographic(string))

# This code is contributed to Bhavya Jain
