import copy


def solve(input, output, lis):
    if len(input) == 0:
        lis.append(output)
        return

    op1 = copy.copy(output)
    op2 = copy.copy(output)

    op2.append(input[0])

    input = input[1:]

    solve(input, op1, lis)
    solve(input, op2, lis)

    return lis

if __name__ == "__main__":
    input = [0,1,2,23]
    output = []
    lis = []
    print(solve(input, output, lis))