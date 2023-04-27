# Driver Code
def reverseWords(string):
    st = list()
    output = ""

    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])

        else:
            while st:
                output += st.pop()

            output += " "

    while st:
        output += st.pop()

    return output

if __name__ == "__main__":
    string = "Geeks . for Geeksasf@!"
    print(reverseWords(string))