from array import array
from sys import stdout


def str_rev(string, start, end):
    while start < end:
        temp = string[start]
        string[start] = string[end]
        string[end] = temp

        start += 1
        end -= 1



def reverse_words(string):
    n = len(string)
    if n < 2:
        return string
    str_rev(string, 0, len(string) - 1)
    # print(string)
    start = 0
    end = 0

    while True:
        if start == n:
            break
        while start < n and string[start] == " ":
            start += 1


        end = start +1

        # need this end < n here to prevent infinite while True
        while end < n and string[end] != " ":
            end += 1

        str_rev(string, start, end - 1)
        start = end

# need this to manipulate the array as a list of indi. words
# list(string) would break into indi. characters, not words
def get_array(string):
    s = array('u', string)
    return s

def print_array(s):
    i = 0
    while i < len(s):
        stdout.write(s[i])
        i += 1
    print()

if __name__ == "__main__":
    string = "Satvik! is good."
    s = get_array(string)
    print_array(s)
    reverse_words(s)
    print_array(s)