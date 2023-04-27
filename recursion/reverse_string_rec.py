def reverseString(string):
    # Base Case
    if len(string) == 0:
        return string

    # Recursive Case
    else:
        return reverseString(string[1:]) + string[0]

# Driver Code
if __name__ == "__main__":

    targetVariable = "Educative"
    print(reverseString(targetVariable))