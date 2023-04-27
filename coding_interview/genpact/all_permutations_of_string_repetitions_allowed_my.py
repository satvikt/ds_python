def print_all_permutations_rec(string, data, index, last, output):

    length = len(string)

    for i in range(length):
        data[index] = string[i]

        if index == last:
            output.append("".join(data))
        else:
            print_all_permutations_rec(string, data, index+1, last, output)



def print_all_permutations(string):
    length = len(string)

    if length < 2:
        return string

    data = [""] * length

    output = []

    print_all_permutations_rec(string, data, 0, length-1, output)

    return output


if __name__ == "__main__":
    string = "ABC"
    print(print_all_permutations(string))