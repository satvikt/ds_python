import copy

def to_string(array):
    return "".join(array)

def all_subsets_rec(input, output, lis):
    if len(input) == 0:
        lis.append(to_string(output))
        return

    op1 = copy.copy(output)
    op2 = copy.copy(output)

    op2.append(input[0])

    input = input[1:]

    all_subsets_rec(input, op1, lis)
    all_subsets_rec(input, op2, lis)

    return lis

if __name__ == "__main__":
    input = "ABC"
    output = []
    lis = []
    print(all_subsets_rec(list(input), output, lis))